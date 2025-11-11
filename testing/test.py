from datetime import datetime


def convert_to_nanos(date_str):
    # Parse the date string into a datetime object
    dt = datetime.strptime(date_str, "%m/%d/%Y %I %p")

    # Convert the datetime object to nanoseconds since the epoch
    nanos = int(dt.timestamp() * 1e9)
    return nanos


# Input timestamps
timestamp1 = "05/14/2025 12 am"
timestamp2 = "05/16/2025 12 am"

# Convert to nanoseconds
nanos1 = convert_to_nanos(timestamp1)
nanos2 = convert_to_nanos(timestamp2)

# Print the results
print(f"Nanoseconds for {timestamp1}: {nanos1}")
print(f"Nanoseconds for {timestamp2}: {nanos2}")