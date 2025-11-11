# Windowing concepts

## WIndows

Windows define how the data is grouped over time or element count

Beam provides fixed windows, sliding windows, and session windows

Windowing allows for partitioning unbounded data into manageable chunks for aggregation (like sum, count)

Default accumulation mode is DISCARDING( other being ACCUMULATING) i.e. that every time a trigger fires, the output contains only new data accumulated since last firing.
Panes donot accumulate previous data; only changes since last firing are emitted
THis can cause repeated keys to appear multiple times separately.

Fixed Windows have fixed length.
A sliding window of 1 hour with a slide of 10 minutes assigns each event time into six distinct windows, each shifted by 10 minutes.
Neither tumbling nor sliding windows depend on the data itself – each data element is assigned to a window (or several windows) based solely on the element's timestamp. 

The boundary of all the windows in the stream is exactly aligned for all the data. This is not the case for session windows.

Session windows split the stream into independent sub-streams based on a user-provided key for each element in the stream.

A session gap duration is a timeout (in the event time) that has to elapse between the timestamps of two successive elements with the same key in order to prevent assigning them in the same window.
 That is to say, as long as elements for a key arrive with a frequency higher than the gap duration, all are placed in the same window. 
Once there is a delay of at least the gap duration, the window is closed, and another window will be created when a new element arrives. 
This type of window is frequently used when analyzing user sessions in web clickstreams (which is where the name session window came from).

There is one more special window type called a global window. 
This very special type of window assigns all data elements into a single window, regardless of their timestamp. 
Therefore, the window spans a complete time interval from –infinity to +infinity. 
This window is used as a default window before any other window is applied.

A state is associated with each window, we cannot keep the window open forver since it has non-zero memory footprint, delelting the state early would cause loss of late data.
To resolve this dilemma, stream processing engines introduce an additional concept called allowed lateness. This defines a timeout (in the event time) after which the state in a window can be cleared and all remaining data can be cleared. This option gives us the possibility to achieve the following:
- Enable the watermark heuristic to advance sufficiently quickly to not incur unnecessary latency.
- Enable an independent measure of how many states are to be kept around, even after their maximal timestamp has already passed.

When a trigger fires and causes data to be output from the current window(s) to downstream processing, there are several options that can be used with both the state associated with the window and with the resulting value itself.
After a trigger fires and data is output downstream, we have essentially two options:
- Reset the state to an empty (initial) state (discard).
- Keep the state intact (accumulate).

Why this matters

- Using discarding mode with triggers means partial results are emitted incrementally but without accumulating previous results, affecting final aggregation.
- To get combined (accumulated) results across trigger firings, use AccumulationMode.ACCUMULATING, which accumulates across panes.
1. Discarding (default):

- Emitted panes contain only new data since last firing.
- Previous results are discarded.
- Useful when only incremental updates matter or deduplication is handled downstream.

2. Accumulating:

- Emitted panes accumulate (add) data from previous firings.
- Results grow over time for the window.
- Useful when you want growing aggregates and full window view on each pane firing.

To sum this up, we can see that we can derive batch semantics from streaming semantics by performing the following:
- Assigning a fixed timestamp to all input key-value pairs.
- Assigning all input key-value pairs to the global window.
- Moving the watermark from –inf to +inf in one hop once all the data is processed
So, the unified approach of Beam comes from the following logic:
Code your pipeline as a streaming pipeline then run it in both a batch and streaming fashion.


## Panes

Panes are subset of data within a window, produced based on trigger firing policies.
Each time a trigger fires, it produces a pane ( a partial or complete view of the window's data)

First pane contains data received so far, subsequent panes include late or future data based on trigger rules

## Triggers

Triggers determine when a pane is emitted, they control the timing of output, including early, regular, and late results.
TRiggers can be based on
- Event Time: When the system watermark passes the window end
- Processing Time: Wallclock time during processing
- Data count: after N elements are received
- Custom or composite conditions combining multipl triggers

Options would be to output the current value in the following ways:
- In fixed periods of processing time (for instance, every 5 seconds)
- When the watermark reaches a certain time (for instance, the output count when our watermark signals that we have processed all data up to 5 P.M.)
- When a specific condition is met in the data

These emitting conditions are called triggers

Each of these possibilities represents one option: a processing time trigger, an event time trigger, and a data-driven trigger. 
Beam provides full support for processing and event time triggers and supports one data-driven trigger, which is a trigger that outputs after a specific number of elements (for example, after every 10 elements).


| Trigger Type          | Description                                       | Use Case Example                                 |
| --------------------- | ------------------------------------------------- | ------------------------------------------------ |
| AfterWatermark        | Fires when event-time watermark passes window end | Producing results once most or all data expected |
| AfterProcessingTime   | Fires after processing time delay                 | Low-latency periodic updates                     |
| AfterCount            | Fires after N elements have arrived               | Batch-like chunk processing                      |
| Repeatedly            | Repeats firing of an embedded trigger             | Continuous early updates                         |
| AfterPane             | Fires based on pane properties (empty/non-empty)  | Control based on element availability            |
| AfterFirst            | Fires when first condition met (OR)               | Get earliest trigger of multiple                 |
| AfterAll              | Fires when all conditions met (AND)               | Synchronize multiple trigger conditions          |
| OrFinally (Java only) | Repeat until finally condition fires              | Combine early repeated firing with a final timer |

Apache Beam also supports allowed lateness and window closing behavior to control late data handling in conjunction with triggers.

Windowing + Triggering + Panes = Controlled Data Emission

## Watermarks

A watermark is an estimate of how far along event time the pipeline has processed.

A watermark is a (heuristic) algorithm that gives us an estimation of how far we have got in the event time domain. A perfect watermark gives the highest possible time (T) that guarantees no further data arrives with an event time < T.

It represents a point in event time before which the pipeline assumes it has received all or most of the data.

- Watermark is a timestamp that signals "we do not expect any earlier events that this"
- Data sources or runners produce watermarks and propogate them throough the pipeline
- When the watermark advances past the end of a window, Beam triggers final computations for that window.
- Late data arriving after the watermark has passed can be handled differently based on configuration (allowed lateness, dropping, or side inputs).

### Examples:

- Fixed windows of 10s with AfterWatermark trigger produce one pane at the end
- Fixed windows with early triggers ( eg. after 5 elements or 5 seconds) emit partial results before the window closes


## Processing time vs Event time

The time at which data originated and the time at which data is processed.

### Summary:

- Windows group data.
- Triggers decide when to output each group (each pane).
- Paned outputs allow incremental or final results depending on trigger configuration.
- Proper use of AccumulationMode and triggers enables fine control of latency and completeness.