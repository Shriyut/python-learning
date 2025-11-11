# Function to perform lexicographical sorting
def lexicographical_sort(values):
    return sorted(values)


# Example usage
values = ["apple", "apple#2025-05-12#1", "apple#2025-05-13", "date", "01", "1", "2", "1.1", "3", "20", "03", "01#1",
          "01#2", "011#", "apple#1", "apple#", "apple#2025", "apple#20251", "apple#2025#", "02", "3000", "00003000"]
sorted_values = lexicographical_sort(values)

print("Original list:", values)
print("Lexicographically sorted list:", sorted_values)
# ['01', '01#1', '01#2', '011#', '03', '1', '1.1', '2', '20', '3', 'apple', 'apple#', 'apple#1', 'apple#2025', 'apple#2025#', 'apple#2025-05-12#1', 'apple#2025-05-13', 'apple#20251', 'date']
