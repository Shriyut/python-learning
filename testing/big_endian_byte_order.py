# Python script to convert strings to big-endian byte order and sort them

strings = ["apple", "banana", "cherry", "date"]

# Convert each string to big-endian byte order (UTF-8 encoding)
big_endian_bytes = {s: s.encode("utf-8") for s in strings}

# Sort the byte values in dictionary order
sorted_big_endian = sorted(big_endian_bytes.items(), key=lambda x: x[1])

# Create a dictionary mapping string to its big-endian byte order (hex)
big_endian_hex_dict = {s: b.hex() for s, b in big_endian_bytes.items()}

print("Sorted (string, big-endian bytes):")
for s, b in sorted_big_endian:
    print(f"{s}: {b.hex()}")

print("\nDictionary mapping:")
print(big_endian_hex_dict)