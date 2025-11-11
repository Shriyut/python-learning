import logging
from typing import TextIO

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions, SetupOptions
from google.cloud import dlp_v2
from google.cloud import bigtable
from google.cloud.bigtable import row
from google.cloud.bigtable.row import DirectRow
import json
import datetime
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.io.gcp.bigtableio import WriteToBigTable


def get_audit_record(message, metadata, row_key):
    return {
        'message_body': str(message),
        'insert_timestamp': datetime.datetime.now().isoformat(),
        'metadata': metadata,
        'row_key': row_key
    }


def convert_msg_to_bigtable_row(message):
    row_key = f"{message.get("originator")["party_id"]}#{message.get("payment_type")}#{message.get("created_at")[0:10]}#{message.get("status")}"
    # row_key = f{}
    row_bigtable = row.DirectRow(row_key.encode('utf-8'))
    # TODO: Implement schema mapping for bigtable in dynamic manner
    bigtable_timestamp = datetime.datetime.now()

    # amount_info column family
    row_bigtable.set_cell("amount_info", b"currency", message.get("amount")["currency"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("amount_info", b"value", message.get("amount")["value"].encode('utf-8'),
                          timestamp=bigtable_timestamp)

    # metadata column family
    row_bigtable.set_cell("metadata", b"status", message.get("status").encode('utf-8'), timestamp=bigtable_timestamp)
    row_bigtable.set_cell("metadata", b"version", message.get("version").encode('utf-8'), timestamp=bigtable_timestamp)
    row_bigtable.set_cell("metadata", b"customer_id", message.get("originator")["party_id"].encode('utf-8'),
                          timestamp=bigtable_timestamp)

    # party_info column family
    row_bigtable.set_cell("party_info", b"beneficiary_account_id",
                          message.get("beneficiary").get("account_info")["account_id"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"beneficiary_account_type",
                          message.get("beneficiary").get("account_info")["account_type"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"beneficiary_id",
                          message.get("beneficiary")["party_id"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"beneficiary_name",
                          message.get("beneficiary")["name"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"beneficiary_type",
                          message.get("beneficiary")["party_type"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"beneficiary_routing_type",
                          message.get("beneficiary").get("account_info").get("routing_info")["type"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"beneficiary_routing_value",
                          message.get("beneficiary").get("account_info").get("routing_info")["value"].encode('utf-8'),
                          timestamp=bigtable_timestamp)

    row_bigtable.set_cell("party_info", b"originator_account_id",
                          message.get("originator").get("account_info")["account_id"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"originator_account_type",
                          message.get("originator").get("account_info")["account_type"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"originator_id",
                          message.get("originator")["party_id"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"originator_name",
                          message.get("originator")["name"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"originator_routing_type",
                          message.get("originator").get("account_info").get("routing_info")["type"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"originator_routing_value",
                          message.get("originator").get("account_info").get("routing_info")["type"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("party_info", b"originator_type",
                          message.get("originator")["party_type"].encode('utf-8'),
                          timestamp=bigtable_timestamp)

    # payment_info column family
    row_bigtable.set_cell("payment_info", b"payment_type", message.get("payment_type").encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("payment_info", b"payment_id", message.get("payment_id").encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("payment_info", b"direction", message.get("direction").encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("payment_info", b"created_at", message.get("created_at").encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("payment_info", b"status", message.get("status").encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("payment_info", b"updated_at", message.get("updated_at").encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("payment_info", b"version", message.get("version").encode('utf-8'),
                          timestamp=bigtable_timestamp)

    # processing_info column family
    row_bigtable.set_cell("processing_info", b"effective_date",
                          message.get("processing")["effective_date"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("processing_info", b"priority", message.get("processing")["priority"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("processing_info", b"processing_window",
                          message.get("processing")["processing_window"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("processing_info", b"settlement_date",
                          message.get("processing")["settlement_date"].encode('utf-8'),
                          timestamp=bigtable_timestamp)
    row_bigtable.set_cell("processing_info", b"submission_date",
                          message.get("processing")["submission_date"].encode('utf-8'),
                          timestamp=bigtable_timestamp)

    # status_info column family
    row_bigtable.set_cell("status_info", b"status_tracking",
                          str(message.get("processing").get("status_tracking")).encode('utf-8'),
                          timestamp=bigtable_timestamp)

    # type specific column family
    row_bigtable.set_cell("type_specific", b"type_specific_data",
                          str(message.get("type_specific_data")).encode('utf-8'),
                          timestamp=bigtable_timestamp)

    return row_bigtable


class TransformDataToBigTable(beam.DoFn):
    OUTPUT_TAG_VALID_MESSAGES = 'tag_valid_messages'
    OUTPUT_TAG_INVALID_MESSAGES = 'tag_invalid_messages'

    def process(self, element):
        row_key = None
        try:
            message = element
            row_key = f"{message.get("originator")["party_id"]}#{message.get("payment_type")}#{message.get("created_at")[0:10]}#{message.get("status")}"
            bigtable_row = convert_msg_to_bigtable_row(message)
            yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_VALID_MESSAGES, bigtable_row)
        except Exception as e:
            tb = e.__traceback__
            logging.error(f"Error processing message: {e}")
            logging.debug(str(e.with_traceback(tb)))
            audit_record = {
                'message_body': str(element),
                'insert_timestamp': datetime.datetime.now().isoformat(),
                'metadata': f"Exception raised during bigtable row conversion {e}",
                'row_key': row_key
            }
            yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_INVALID_MESSAGES, audit_record)


class ReconcileData(beam.DoFn):
    OUTPUT_TAG_VALID_MESSAGES = 'tag_valid_messages'
    OUTPUT_TAG_INVALID_MESSAGES = 'tag_invalid_messages'

    def __init__(self, project, instance_id, table_id, *unused_args, **unused_kwargs):
        # super().__init__(*unused_args, **unused_kwargs)
        self.table = None
        self.instance = None
        self.bigtable_client = None
        self.project = project
        self.instance_id = instance_id
        self.table_id = table_id

    def setup(self):
        self.bigtable_client = bigtable.Client(project=self.project, admin=True)
        self.instance = self.bigtable_client.instance(self.instance_id)
        self.table = self.instance.table(self.table_id)

    def teardown(self):
        self.bigtable_client.close()

    def process(self, element):

        # perform reconciliation
        # read data from bigtable
        row_key = element.row_key.decode('utf-8')
        try:
            logging.info(f"Row key is {row_key}")
            bigtable_record = read_row_from_bigtable(self.project, self.instance_id, self.table_id,
                                                     row_key)
            if bigtable_record is not None:

                # check for duplication and perform lookup
                input_msg_list = element.__dict__["_pb_mutations"]
                bigtable_record_list = bigtable_record.__dict__["_pb_mutations"]

                input_msg_mutation_dict = extract_families(input_msg_list)
                bigtable_record_mutation_dict = extract_families(bigtable_record_list)

                final_check = input_msg_mutation_dict == bigtable_record_mutation_dict

                if final_check:
                    logging.info("Records are totally duplicate")
                    # yield invalid tag for totally duplicate record
                    yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_INVALID_MESSAGES, get_audit_record(
                        str(element.__dict__), "Totally duplicate record received from Pub/Sub", row_key
                    ))
                else:
                    # ignoring situations where families can be different since mutation object is built in the pipeline
                    differences = check_for_differences(input_msg_mutation_dict, bigtable_record_mutation_dict)
                    logging.info("There are some changes in the record")
                    logging.info(differences.__repr__())

                    current_timestamp = datetime.datetime.now()

                    for family, qualifiers in differences.items():

                        for qualifier, (new_value, _) in qualifiers.items():
                            # Update record read from bigtable here
                            bigtable_record.set_cell(
                                family,
                                qualifier,
                                new_value,
                                timestamp=current_timestamp
                            )

                    yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_VALID_MESSAGES, bigtable_record)
            else:
                # process new record - yield input element
                # perform order validation here

                from google.cloud.bigtable.row_set import RowSet

                prefix = row_key.rpartition('#')[0]
                message_status = row_key.rpartition('#')[2]

                initiated_key = f"{prefix}#INITIATED"
                processing_key = f"{prefix}#PROCESSING"
                received_key = f"{prefix}#RECEIVED"

                row_set = RowSet()

                row_set.add_row_key(initiated_key.encode('utf-8'))
                row_set.add_row_key(processing_key.encode('utf-8'))
                row_set.add_row_key(received_key.encode('utf-8'))

                try:
                    status_values = []
                    rows = self.table.read_rows(row_set=row_set)
                    for record_row in rows:
                        status_values.append(record_row.row_key.decode('utf-8').rpartition('#')[2])
                    logging.info(status_values.__repr__())

                    if "RECEIVED" == message_status and "PROCESSING" in status_values and "INITIATED" in status_values and len(
                            status_values) == 2:
                        yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_VALID_MESSAGES, element)
                    elif "PROCESSING" == message_status and "INITIATED" in status_values and len(status_values) == 1:
                        yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_VALID_MESSAGES, element)
                    elif "INITIATED" == message_status and len(status_values) == 0:
                        yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_VALID_MESSAGES, element)
                    else:
                        yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_INVALID_MESSAGES, get_audit_record(
                            str(element.__dict__), "Pub/Sub message received out of order", row_key
                        ))

                except Exception as e:
                    logging.error(f"Error reading rows from bigtable {e}")
                    # abc audit
                    audit_record = {
                        'message_body': str(element.__dict__),
                        'insert_timestamp': datetime.datetime.now().isoformat(),
                        'metadata': f"Error during order validation {e}",
                        'row_key': row_key
                    }
                    yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_INVALID_MESSAGES, audit_record)


        except Exception as e:
            logging.error(f"Error reading row from bigtable {e}")
            audit_record = {
                'message_body': str(element.__dict__),
                'insert_timestamp': datetime.datetime.now().isoformat(),
                'metadata': f"Error reading row from bigtable {e}",
                'row_key': row_key
            }
            yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_INVALID_MESSAGES, audit_record)

class DLPDeidentify(beam.DoFn):
    def __init__(self, project, key_name, wrapped_key):
        self.project = project
        self.key_name = key_name
        self.wrapped_key = wrapped_key

    def start_bundle(self):
        self.dlp_client = dlp_v2.DlpServiceClient()

    def process(self, element, dlp_config_file_si):
        item = {"value": element}
        parent = f"projects/{self.project}"

        inspect_config = json.loads(dlp_config_file_si[0])

        # inspect_config = {
        #     "info_types": [
        #         {"name": "EMAIL_ADDRESS"},
        #         {"name": "PHONE_NUMBER"},
        #         {"name": "CREDIT_CARD_NUMBER"},
        #         {"name": "US_BANK_ROUTING_MICR"},
        #     ],
        #     "include_quote": True
        # }

        crypto_replace_config = {
            "crypto_key": {
                "kms_wrapped": {
                    "wrapped_key": self.wrapped_key,
                    "crypto_key_name": self.key_name,
                }
            },
            "surrogate_info_type": {"name": "SURROGATE_TYPE"},
        }

        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "info_types": inspect_config["info_types"],
                        "primitive_transformation": {
                            "crypto_deterministic_config": crypto_replace_config
                        },
                    }
                ]
            }
        }

        response = self.dlp_client.deidentify_content(
            request={
                "parent": parent,
                "inspect_config": inspect_config,
                "deidentify_config": deidentify_config,
                "item": item
            }
        )

        yield response.item.value

def extract_families(mutations):
    families = {}

    for mutation in mutations:

        set_cell = mutation.set_cell
        family_name = set_cell.family_name
        column_qualifier = set_cell.column_qualifier
        value = set_cell.value

        if family_name not in families:
            families[family_name] = {}

        families[family_name][column_qualifier] = value

    return families


def check_for_differences(input_msg_dict, bigtable_record_dict):
    differences = {}

    for family in input_msg_dict.keys() | bigtable_record_dict.keys():

        for column_qualifier in input_msg_dict[family].keys() | bigtable_record_dict[family].keys():

            if input_msg_dict[family][column_qualifier] != bigtable_record_dict[family][column_qualifier]:
                if family not in differences:
                    differences[family] = {}

                differences[family][column_qualifier] = (
                    input_msg_dict[family][column_qualifier], bigtable_record_dict[family][column_qualifier])

    return differences


def read_row_from_bigtable(project_id, instance_id, table_id, row_key):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    total_versions = None
    latest_cell = None
    direct_row = None
    row = table.read_row(row_key.encode('utf-8'))

    if row:

        direct_row = DirectRow(row_key.encode('utf-8'))

        for column_family_id, columns in row.cells.items():

            for column, cells in columns.items():
                latest_cell = cells[0]  # only considering the latest values for reconciliation
                direct_row.set_cell(
                    column_family_id,
                    column.decode('utf-8'),
                    latest_cell.value.decode('utf-8'),
                    timestamp=latest_cell.timestamp
                )
    else:
        #  i.e a new record -  handle during order validation step in dofn
        logging.info(f"Not found: {row_key}")

    return direct_row


class ValidatePubSubMessages(beam.DoFn):
    # These tags will be used to tag the outputs of this DoFn.
    OUTPUT_TAG_VALID_MESSAGES = 'tag_valid_messages'
    OUTPUT_TAG_INVALID_MESSAGES = 'tag_invalid_messages'

    def process(self, element):
        try:
            if isinstance(element, bytes):
                message = json.loads(element.decode("utf-8"))
            if isinstance(element, (str, bytearray)):
                message = json.loads(element)
            else:
                raise ValueError(f"Invalid pub/sub message format: {type(element)} received")
            # complete below validations
            # validate payment types
            # check if amount > 0, required keys are present, created_at is before updated_at

            required_keys = ["payment_type", "payment_id", "created_at", "updated_at", "amount", "originator",
                             "beneficiary", "processing"]
            valid_payment_types = ["ACH", "CARD", "WIRE", "SEPA", "SWIFT", "RTP"]

            required_keys_check = all(key in message.keys() for key in required_keys)

            timestamp_check = datetime.datetime.fromisoformat(
                message.get("created_at")) <= datetime.datetime.fromisoformat(message.get("updated_at"))

            type_check = message.get("payment_type") in valid_payment_types

            amount_check = float(message.get("amount")["value"]) >= 0

            message.keys()
            if required_keys_check and timestamp_check and amount_check and type_check:
                # return python object generated from input pubsub msg ( in json format )
                yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_VALID_MESSAGES, message)
            else:
                #  returns tablerow (python dictionary) object to load abc record in bigquery
                yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_INVALID_MESSAGES,
                                               get_audit_record(element, "Pub/Sub message validation failed",
                                                                "Rowkey not generated"))
        except Exception as e:
            logging.error(f"Error processing message: {e}")
            audit_record = {
                'message_body': str(element),
                'insert_timestamp': datetime.datetime.now().isoformat(),
                'metadata': f"Exception raised while processing pubsub message {e}",
                'row_key': "Row key not generated for the record"
            }
            yield beam.pvalue.TaggedOutput(self.OUTPUT_TAG_INVALID_MESSAGES, audit_record)


class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            '--sub1',
            help='Subscription for source1')
        parser.add_argument(
            '--sub2',
            help='Subscription for source2')
        parser.add_argument(
            '--sub3',
            help='Subscription for source3')
        parser.add_argument(
            '--projectId',
            help='GCP Project ID where BigTable is present')
        parser.add_argument(
            '--instanceId',
            help='BigTable Instance ID')
        parser.add_argument(
            '--tableId',
            help='BigTable Table ID')
        parser.add_argument(
            '--auditTableId',
            help='BigQuery Audit Table Id')
        parser.add_argument(
            '--keyName',
            help='DLP key name')
        parser.add_argument(
            '--wrappedKey',
            help='DLP wrapped key')
        # parser.add_argument(
        #     '--dlpConfigFile',
        #     help='DLP Inspect Config File')


def run(argv=None, save_main_session=True):

    pipeline_options = PipelineOptions()
    dataflow_options = pipeline_options.view_as(MyOptions)

    pipeline_options.view_as(StandardOptions).runner = 'DataflowRunner'
    pipeline_options.view_as(StandardOptions).streaming = True  # Enable streaming mode
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session

    pipeline_object = beam.Pipeline(options=pipeline_options)

    dlp_config_file = pipeline_object | "Read DLP configuration File" >> beam.io.ReadFromText(r"gs://us-gcp-ame-con-ff12d-npd-1-dataflow-stage/configurations/dlp_inspect_config")
    dlp_config_file_si = beam.pvalue.AsList(dlp_config_file)

    filter_messages_source1 = (pipeline_object | "Read from Pub/Sub for source1"
                               >> beam.io.ReadFromPubSub(subscription=dataflow_options.sub1).with_output_types(bytes)
                               | "Apply Windowing" >> beam.WindowInto(beam.window.FixedWindows(1))
                               | "DLP De-identification for source1" >> beam.ParDo(DLPDeidentify(dataflow_options.projectId,
                                                                                                 dataflow_options.keyName,
                                                                                                 dataflow_options.wrappedKey),dlp_config_file_si)
                               | "Validate PubSub Messages for source1" >> beam.ParDo(
                ValidatePubSubMessages()).with_outputs(
                ValidatePubSubMessages.OUTPUT_TAG_INVALID_MESSAGES, ValidatePubSubMessages.OUTPUT_TAG_VALID_MESSAGES))

    filter_messages_source2 = (pipeline_object | "Read from Pub/Sub for source2"
                               >> beam.io.ReadFromPubSub(subscription=dataflow_options.sub2).with_output_types(bytes)
                               | "Apply Windowing 2" >> beam.WindowInto(beam.window.FixedWindows(1))
                               | "DLP De-identification for source2" >> beam.ParDo(DLPDeidentify(dataflow_options.projectId,
                                                                                                 dataflow_options.keyName,
                                                                                                 dataflow_options.wrappedKey),dlp_config_file_si)
                               | "Validate PubSub Messages for source2" >> beam.ParDo(
                ValidatePubSubMessages()).with_outputs(
                ValidatePubSubMessages.OUTPUT_TAG_INVALID_MESSAGES, ValidatePubSubMessages.OUTPUT_TAG_VALID_MESSAGES))

    filter_messages_source3 = (pipeline_object | "Read from Pub/Sub for source3"
                               >> beam.io.ReadFromPubSub(subscription=dataflow_options.sub3).with_output_types(bytes)
                               | "Apply Windowing 3" >> beam.WindowInto(beam.window.FixedWindows(1))
                               | "DLP De-identification for source3" >> beam.ParDo(DLPDeidentify(dataflow_options.projectId,
                                                                                                 dataflow_options.keyName,
                                                                                                 dataflow_options.wrappedKey),dlp_config_file_si)
                               | "Validate PubSub Messages for source3" >> beam.ParDo(
                ValidatePubSubMessages()).with_outputs(
                ValidatePubSubMessages.OUTPUT_TAG_INVALID_MESSAGES, ValidatePubSubMessages.OUTPUT_TAG_VALID_MESSAGES))

    # Flattern all valid and invalid data into corresponding PCollection
    valid_messages_from_all_sources = ((filter_messages_source1[ValidatePubSubMessages.OUTPUT_TAG_VALID_MESSAGES],
                                        filter_messages_source2[ValidatePubSubMessages.OUTPUT_TAG_VALID_MESSAGES],
                                        filter_messages_source3[ValidatePubSubMessages.OUTPUT_TAG_VALID_MESSAGES])
                                       | 'Flatten valid messages PCollections' >> beam.Flatten())


    # using dofn instead of map to generate bigtable rows
    converted_bigtable_rows = (
            valid_messages_from_all_sources | "Convert to BigTable Row" >> beam.ParDo(
        TransformDataToBigTable()).with_outputs(
        TransformDataToBigTable.OUTPUT_TAG_VALID_MESSAGES, TransformDataToBigTable.OUTPUT_TAG_INVALID_MESSAGES))

    # only valid bigtable records should be sent for reconciliation
    reconciled_bigtable_records = (converted_bigtable_rows[TransformDataToBigTable.OUTPUT_TAG_VALID_MESSAGES]
                                   | "Reconciliation" >> beam.ParDo(
                ReconcileData(dataflow_options.projectId, dataflow_options.instanceId, dataflow_options.tableId))
                                   .with_outputs(ReconcileData.OUTPUT_TAG_VALID_MESSAGES,
                                                 ReconcileData.OUTPUT_TAG_INVALID_MESSAGES))

    (reconciled_bigtable_records[ReconcileData.OUTPUT_TAG_VALID_MESSAGES]
     | "Write to BigTable" >> WriteToBigTable(
                project_id=dataflow_options.projectId,
                instance_id=dataflow_options.instanceId,
                table_id=dataflow_options.tableId))

    invalid_messages_from_all_sources = ((filter_messages_source1[ValidatePubSubMessages.OUTPUT_TAG_INVALID_MESSAGES],
                                          filter_messages_source2[ValidatePubSubMessages.OUTPUT_TAG_INVALID_MESSAGES],
                                          filter_messages_source3[ValidatePubSubMessages.OUTPUT_TAG_INVALID_MESSAGES],
                                          converted_bigtable_rows[TransformDataToBigTable.OUTPUT_TAG_INVALID_MESSAGES],
                                          reconciled_bigtable_records[ReconcileData.OUTPUT_TAG_INVALID_MESSAGES])
                                         | 'Flatten invalid messages PCollections' >> beam.Flatten())

    (invalid_messages_from_all_sources
     | "Dummy PCollection" >> beam.Map(lambda x: x)
     | "Write to BigQuery" >> WriteToBigQuery(project=dataflow_options.projectId,
                table=dataflow_options.auditTableId,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER))

    result = pipeline_object.run()


if __name__ == "__main__":
    run()