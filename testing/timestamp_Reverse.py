def reverse_nanos(nanos):
    # Calculate the reversed timestamp in nanoseconds
    max_nanos = (2 ** 63) - 1
    reversed_nanos = max_nanos - nanos
    return reversed_nanos

# Input timestamps in nanoseconds
start_timestamp = 1746521635599247872
end_timestamp = 1747304376781824000

# Convert to reversed timestamps
reversed_start = reverse_nanos(start_timestamp)
reversed_end = reverse_nanos(end_timestamp)

# Print the results
print(f"Reversed Start Timestamp: {reversed_start}")
print(f"Reversed End Timestamp: {reversed_end}")


test="{accountId}#{transactionType}#{transactionTimestamp}"

print(test.format(
    accountId="1",
    transactionType="2",
    transactionTimestamp=3,test=4))