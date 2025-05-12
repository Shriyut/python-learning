# Function to perform lexicographical sorting
def lexicographical_sort(values):
    return sorted(values)

# Example usage
values = ["apple", "apple#2025-05-12#1", "apple#2025-05-13", "date", "01", "1", "2", "1.1", "3", "20", "03"]
sorted_values = lexicographical_sort(values)

print("Original list:", values)
print("Lexicographically sorted list:", sorted_values)