"""
Lightweight Return Transaction Matcher - Test Version
======================================================
Generates test data within pipeline and prints results to console.
No CSV files or GCS required - perfect for testing the stateful DoFn concept.

Usage:
    python lightweight_return_matcher.py
"""

import apache_beam as beam
from apache_beam import TimeDomain
from apache_beam.transforms.userstate import (
    BagStateSpec,
    TimerSpec,
    on_timer
)
from apache_beam.transforms.window import GlobalWindows
from apache_beam.options.pipeline_options import PipelineOptions
from typing import Dict, Tuple
import json


class ReturnTransactionMatcherDoFn(beam.DoFn):
    """Lightweight stateful DoFn for matching return transactions"""

    TRANSACTIONS_STATE = BagStateSpec('transactions', beam.coders.registry.get_coder(dict))
    RETURN_REF_STATE = BagStateSpec('return_refs', beam.coders.registry.get_coder(dict))
    RETURN_FINAL_STATE = BagStateSpec('return_finals', beam.coders.registry.get_coder(dict))
    EOW_TIMER = TimerSpec('end_of_window', TimeDomain.WATERMARK)

    OUTPUT_COMPLETE_3TX = 'complete_return_3tx'
    OUTPUT_COMPLETE_2TX = 'complete_return_2tx'
    OUTPUT_NORMAL_TX = 'normal_transaction'
    OUTPUT_ORPHAN_REF = 'orphan_return_ref'
    OUTPUT_ORPHAN_FINAL = 'orphan_return_final'

    def process(self, element,
                transactions=beam.DoFn.StateParam(TRANSACTIONS_STATE),
                return_refs=beam.DoFn.StateParam(RETURN_REF_STATE),
                return_finals=beam.DoFn.StateParam(RETURN_FINAL_STATE),
                eow_timer=beam.DoFn.TimerParam(EOW_TIMER),
                window=beam.DoFn.WindowParam):

        key, (record, return_metadata) = element
        eow_timer.set(window.max_timestamp())
        tx_type = self._classify_transaction(return_metadata)

        if tx_type == 'initial':
            yield from self._process_initial(key, record, return_metadata,
                                             transactions, return_refs, return_finals)
        elif tx_type == 'return_ref':
            yield from self._process_return_ref(key, record, return_metadata,
                                                transactions, return_refs, return_finals)
        elif tx_type == 'return_final':
            yield from self._process_return_final(key, record, return_metadata,
                                                  transactions, return_refs, return_finals)

    def _classify_transaction(self, return_metadata: Dict) -> str:
        has_return_ref = bool(return_metadata.get('returnreference'))
        has_return_code = bool(return_metadata.get('returncode'))

        if has_return_code:
            return 'return_final'
        elif has_return_ref:
            return 'return_ref'
        else:
            return 'initial'

    def _process_initial(self, key, record, return_metadata,
                         transactions, return_refs, return_finals):
        tx_id = record.get('transaction_id')
        to_ref = return_metadata.get('to_ref')

        matched_return_ref = None
        for ref_tx in return_refs.read():
            if ref_tx['return_metadata'].get('returnreference') == to_ref:
                matched_return_ref = ref_tx
                break

        matched_return_final = None
        if matched_return_ref:
            ref_return_ref = matched_return_ref['return_metadata'].get('returnreference')
            for final_tx in return_finals.read():
                if final_tx['return_metadata'].get('from_ref') == ref_return_ref:
                    matched_return_final = final_tx
                    break

        if matched_return_ref and matched_return_final:
            output = {
                'initial': record,
                'return_ref': matched_return_ref['record'],
                'return_final': matched_return_final['record']
            }
            yield beam.pvalue.TaggedOutput(self.OUTPUT_COMPLETE_3TX, (key, output))
        else:
            transactions.add({
                'record': record,
                'return_metadata': return_metadata,
                'tx_id': tx_id,
                'to_ref': to_ref
            })

    def _process_return_ref(self, key, record, return_metadata,
                            transactions, return_refs, return_finals):
        return_ref = return_metadata.get('returnreference')

        matched_initial = None
        for tx in transactions.read():
            if tx.get('to_ref') == return_ref:
                matched_initial = tx
                break

        matched_final = None
        for final_tx in return_finals.read():
            if final_tx['return_metadata'].get('from_ref') == return_ref:
                matched_final = final_tx
                break

        if matched_initial and matched_final:
            output = {
                'initial': matched_initial['record'],
                'return_ref': record,
                'return_final': matched_final['record']
            }
            yield beam.pvalue.TaggedOutput(self.OUTPUT_COMPLETE_3TX, (key, output))
        elif matched_final:
            output = {
                'return_ref': record,
                'return_final': matched_final['record']
            }
            yield beam.pvalue.TaggedOutput(self.OUTPUT_COMPLETE_2TX, (key, output))
        else:
            return_refs.add({
                'record': record,
                'return_metadata': return_metadata
            })

    def _process_return_final(self, key, record, return_metadata,
                              transactions, return_refs, return_finals):
        from_ref = return_metadata.get('from_ref')

        matched_return_ref = None
        for ref_tx in return_refs.read():
            if ref_tx['return_metadata'].get('returnreference') == from_ref:
                matched_return_ref = ref_tx
                break

        if matched_return_ref:
            ref_return_ref = matched_return_ref['return_metadata'].get('returnreference')

            matched_initial = None
            for tx in transactions.read():
                if tx.get('to_ref') == ref_return_ref:
                    matched_initial = tx
                    break

            if matched_initial:
                output = {
                    'initial': matched_initial['record'],
                    'return_ref': matched_return_ref['record'],
                    'return_final': record
                }
                yield beam.pvalue.TaggedOutput(self.OUTPUT_COMPLETE_3TX, (key, output))
            else:
                output = {
                    'return_ref': matched_return_ref['record'],
                    'return_final': record
                }
                yield beam.pvalue.TaggedOutput(self.OUTPUT_COMPLETE_2TX, (key, output))
        else:
            return_finals.add({
                'record': record,
                'return_metadata': return_metadata
            })

    @on_timer(EOW_TIMER)
    def on_end_of_window(self, key=beam.DoFn.KeyParam,
                         transactions=beam.DoFn.StateParam(TRANSACTIONS_STATE),
                         return_refs=beam.DoFn.StateParam(RETURN_REF_STATE),
                         return_finals=beam.DoFn.StateParam(RETURN_FINAL_STATE)):

        for tx in transactions.read():
            yield beam.pvalue.TaggedOutput(self.OUTPUT_NORMAL_TX,
                                           (key, {'transaction': tx['record']}))

        for ref_tx in return_refs.read():
            yield beam.pvalue.TaggedOutput(self.OUTPUT_ORPHAN_REF,
                                           (key, {'transaction': ref_tx['record']}))

        for final_tx in return_finals.read():
            yield beam.pvalue.TaggedOutput(self.OUTPUT_ORPHAN_FINAL,
                                           (key, {'transaction': final_tx['record']}))

        transactions.clear()
        return_refs.clear()
        return_finals.clear()


def generate_test_data():
    """Generate synthetic test data covering all scenarios"""
    test_data = []

    # Scenario 1: Complete 3-transaction return
    test_data.append(({
                          'transaction_id': 'TX001',
                          'period_reference': '2025-10',
                          'amount': 100.0
                      }, {
                          'to_ref': 'REF001',
                          'from_ref': 'REF002',
                          'returnreference': '',
                          'returncode': ''
                      }))

    test_data.append(({
                          'transaction_id': 'TX002',
                          'period_reference': '2025-10',
                          'amount': 100.0
                      }, {
                          'to_ref': 'REF003',
                          'from_ref': 'REF004',
                          'returnreference': 'REF001',
                          'returncode': ''
                      }))

    test_data.append(({
                          'transaction_id': 'TX003',
                          'period_reference': '2025-10',
                          'amount': 100.0
                      }, {
                          'to_ref': 'REF005',
                          'from_ref': 'REF001',
                          'returnreference': '',
                          'returncode': 'R01'
                      }))

    # Scenario 2: Normal transactions
    test_data.append(({
                          'transaction_id': 'TX004',
                          'period_reference': '2025-10',
                          'amount': 200.0
                      }, {
                          'to_ref': 'REF010',
                          'from_ref': 'REF011',
                          'returnreference': '',
                          'returncode': ''
                      }))

    test_data.append(({
                          'transaction_id': 'TX005',
                          'period_reference': '2025-10',
                          'amount': 300.0
                      }, {
                          'to_ref': 'REF012',
                          'from_ref': 'REF013',
                          'returnreference': '',
                          'returncode': ''
                      }))

    # Scenario 3: 2-transaction return (no initial)
    test_data.append(({
                          'transaction_id': 'TX006',
                          'period_reference': '2025-10',
                          'amount': 150.0
                      }, {
                          'to_ref': 'REF020',
                          'from_ref': 'REF021',
                          'returnreference': 'REF099',
                          'returncode': ''
                      }))

    test_data.append(({
                          'transaction_id': 'TX007',
                          'period_reference': '2025-10',
                          'amount': 150.0
                      }, {
                          'to_ref': 'REF022',
                          'from_ref': 'REF099',
                          'returnreference': '',
                          'returncode': 'R02'
                      }))

    # Scenario 4: Orphan return ref
    test_data.append(({
                          'transaction_id': 'TX008',
                          'period_reference': '2025-10',
                          'amount': 50.0
                      }, {
                          'to_ref': 'REF030',
                          'from_ref': 'REF031',
                          'returnreference': 'REF999',
                          'returncode': ''
                      }))

    # Scenario 5: Orphan return final
    test_data.append(({
                          'transaction_id': 'TX009',
                          'period_reference': '2025-10',
                          'amount': 75.0
                      }, {
                          'to_ref': 'REF040',
                          'from_ref': 'REF888',
                          'returnreference': '',
                          'returncode': 'R03'
                      }))

    # Scenario 6: Complete 3-transaction return (out of order)
    test_data.append(({
                          'transaction_id': 'TX012',
                          'period_reference': '2025-10',
                          'amount': 500.0
                      }, {
                          'to_ref': 'REF055',
                          'from_ref': 'REF051',
                          'returnreference': '',
                          'returncode': 'R04'
                      }))

    test_data.append(({
                          'transaction_id': 'TX011',
                          'period_reference': '2025-10',
                          'amount': 500.0
                      }, {
                          'to_ref': 'REF053',
                          'from_ref': 'REF054',
                          'returnreference': 'REF051',
                          'returncode': ''
                      }))

    test_data.append(({
                          'transaction_id': 'TX010',
                          'period_reference': '2025-10',
                          'amount': 500.0
                      }, {
                          'to_ref': 'REF051',
                          'from_ref': 'REF052',
                          'returnreference': '',
                          'returncode': ''
                      }))

    return test_data


def extract_key(element):
    """Extract key for stateful processing"""
    record, return_metadata = element
    key = record.get('period_reference', 'unknown')
    return (key, element)


def format_output(element, output_type):
    """Format output for printing"""
    key, data = element
    return f"[{output_type}] Key={key}, Data={json.dumps(data, indent=2)}"


def run_lightweight_test():
    """Run the lightweight test pipeline"""

    print("\n" + "="*80)
    print("LIGHTWEIGHT RETURN TRANSACTION MATCHER - TEST RUN")
    print("="*80)

    test_data = generate_test_data()

    print(f"\nGenerated {len(test_data)} test transactions")
    print("\nScenarios covered:")
    print("  1. Complete 3-transaction return (2 instances)")
    print("  2. Normal transactions (2 instances)")
    print("  3. 2-transaction return (1 instance)")
    print("  4. Orphan return ref (1 instance)")
    print("  5. Orphan return final (1 instance)")
    print("\n" + "-"*80)
    print("PIPELINE OUTPUTS:")
    print("-"*80 + "\n")

    with beam.Pipeline(options=PipelineOptions()) as p:

        results = (
                p
                | 'CreateData' >> beam.Create(test_data)
                | 'AddKeys' >> beam.Map(extract_key)
                | 'Window' >> beam.WindowInto(GlobalWindows())
                | 'MatchReturns' >> beam.ParDo(ReturnTransactionMatcherDoFn()).with_outputs(
            ReturnTransactionMatcherDoFn.OUTPUT_COMPLETE_3TX,
            ReturnTransactionMatcherDoFn.OUTPUT_COMPLETE_2TX,
            ReturnTransactionMatcherDoFn.OUTPUT_NORMAL_TX,
            ReturnTransactionMatcherDoFn.OUTPUT_ORPHAN_REF,
            ReturnTransactionMatcherDoFn.OUTPUT_ORPHAN_FINAL
        )
        )

        # Print complete 3-transaction returns
        (results[ReturnTransactionMatcherDoFn.OUTPUT_COMPLETE_3TX]
         | 'Format3TX' >> beam.Map(lambda x: format_output(x, 'COMPLETE 3TX RETURN'))
         | 'Print3TX' >> beam.Map(print))

        # Print complete 2-transaction returns
        (results[ReturnTransactionMatcherDoFn.OUTPUT_COMPLETE_2TX]
         | 'Format2TX' >> beam.Map(lambda x: format_output(x, 'COMPLETE 2TX RETURN'))
         | 'Print2TX' >> beam.Map(print))

        # Print normal transactions
        (results[ReturnTransactionMatcherDoFn.OUTPUT_NORMAL_TX]
         | 'FormatNormal' >> beam.Map(lambda x: format_output(x, 'NORMAL TRANSACTION'))
         | 'PrintNormal' >> beam.Map(print))

        # Print orphan return refs
        (results[ReturnTransactionMatcherDoFn.OUTPUT_ORPHAN_REF]
         | 'FormatOrphanRef' >> beam.Map(lambda x: format_output(x, 'ORPHAN RETURN REF'))
         | 'PrintOrphanRef' >> beam.Map(print))

        # Print orphan return finals
        (results[ReturnTransactionMatcherDoFn.OUTPUT_ORPHAN_FINAL]
         | 'FormatOrphanFinal' >> beam.Map(lambda x: format_output(x, 'ORPHAN RETURN FINAL'))
         | 'PrintOrphanFinal' >> beam.Map(print))

    print("\n" + "="*80)
    print("EXPECTED RESULTS:")
    print("="*80)
    print("Complete 3TX Returns: 2 (TX001-TX003 and TX010-TX012)")
    print("Complete 2TX Returns: 1 (TX006-TX007)")
    print("Normal Transactions: 2 (TX004 and TX005)")
    print("Orphan Return Refs: 1 (TX008)")
    print("Orphan Return Finals: 1 (TX009)")
    print("="*80 + "\n")


if __name__ == '__main__':
    run_lightweight_test()