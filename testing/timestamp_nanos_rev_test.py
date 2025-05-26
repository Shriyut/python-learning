import datetime


def nanos_to_datetime(nanos):
    """Convert nanoseconds to datetime object."""
    seconds = nanos / 1e9
    return datetime.datetime.fromtimestamp(seconds)


def reverse_nanos(nanos):
    """Calculate the reversed timestamp in nanoseconds."""
    max_nanos = (2 ** 63) - 1
    reversed_nanos = max_nanos - nanos
    return reversed_nanos


def reversed_nanos_to_datetime(reversed_nanos):
    """Convert reversed nanoseconds to datetime object."""
    max_nanos = (2 ** 63) - 1
    original_nanos = max_nanos - reversed_nanos
    return nanos_to_datetime(original_nanos)


# Example usage:
nanos_timestamp = 1746521635599247872
reversed_nanos_timestamp = 981251866694263647

# Convert nanoseconds to datetime
datetime_from_nanos = nanos_to_datetime(nanos_timestamp)

# Convert reversed nanoseconds to datetime
datetime_from_reversed_nanos = reversed_nanos_to_datetime(reversed_nanos_timestamp)

print(f"Datetime from nanoseconds: {datetime_from_nanos}")
print(f"Datetime from reversed nanoseconds: {datetime_from_reversed_nanos}")
