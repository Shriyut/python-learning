import datetime

java_lang_long_max = 2 ** 63 - 1
timestamp_value = datetime.datetime.now().timestamp()


def reverse_timestamp(timestamp_ns):
    timestamp_ms = timestamp_ns // 1_000_000  # Convert nanoseconds to milliseconds
    reversed_timestamp = java_lang_long_max - timestamp_ms
    return reversed_timestamp


def nanos_to_datetime(nanos):
    """Convert nanoseconds to datetime object."""
    seconds = nanos / 1e9
    return datetime.datetime.fromtimestamp(seconds)


def reversed_nanos_to_datetime(reversed_nanos):
    max_nanos = (2 ** 63) - 1
    original_nanos = max_nanos - reversed_nanos
    return nanos_to_datetime(original_nanos)


nanos_value = int(timestamp_value * 1e9)
reversed_nanos_value = reverse_timestamp(nanos_value)

print("Checking reversed timestamp with naosecond values")
print("Max long integer value is :", java_lang_long_max)
print("Checking if sum of timestamps in nanoseconds is the same as max long value",
      nanos_value + reversed_nanos_value == java_lang_long_max)
print("Current time is :", timestamp_value)
print("Original timestamp in nanoseconds:", nanos_value)
print("Reversed timestamp:", reversed_nanos_value)
print("Timestamp from reversed nanoseconds:", reversed_nanos_to_datetime(reversed_nanos_value))

# Number of milliseconds in a second
milliseconds_in_second = 1_000  # int

# Number of microseconds in a second
microseconds_in_second = 1_000_000  # int

# Number of nanoseconds in a second
nanoseconds_in_second = 1_000_000_000  # int

print("Checking reversed timestamp in microsecond values")


def timestamp_to_microseconds(timestamp):
    return int(timestamp * 1e6)


current_timestamp_in_microseconds = timestamp_to_microseconds(timestamp_value)
reversed_timestamp_in_microseconds = java_lang_long_max - current_timestamp_in_microseconds


def reversed_microseconds_to_datetime(reversed_microseconds):
    max_microseconds = (2 ** 63) - 1
    original_microseconds = max_microseconds - reversed_microseconds
    return datetime.datetime.fromtimestamp(original_microseconds / 1e6)


print("Current time in microseconds:", current_timestamp_in_microseconds)
print("Reversed timestamp in microseconds:", reversed_timestamp_in_microseconds)
print("Max long integer value is :", java_lang_long_max)
print("Checking if sum of reversed and normal timestamp is equal to max long integer value:",
      current_timestamp_in_microseconds + reversed_timestamp_in_microseconds == java_lang_long_max)
print("Timestamp from reversed microseconds:", reversed_microseconds_to_datetime(reversed_timestamp_in_microseconds))

print("Microsecond representaiton of a timestamp should be used for reversed timestamp values in rowkey")
