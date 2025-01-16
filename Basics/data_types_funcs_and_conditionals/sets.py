# Set is a mutable, unordered data structure that prohibits duplicate values

# literal for set - {}

empty_set = set()
# empty_set = {}  # this is a dictionary


stocks = {"AAPL", "GOOGL", "TSLA", "AAPL"}
print(stocks)  # {'AAPL', 'GOOGL', 'TSLA'} - removes duplicates
print(len(stocks))  # 3

# sets are unordered, so indexing is not possible
# print(stocks[0])  # TypeError

lottery_numbers = { (1,2,3), (4,5,6), (1,2,3) }
print(lottery_numbers)  # {(1, 2, 3), (4, 5, 6)} - removes duplicates

print(1 in lottery_numbers)  # False - since it is a tuple
print("AAPL" in stocks)  # True

squares = { number ** 2 for number in [-5, -4, -3, 3, 4, 5] }
print(squares)  # {16, 9, 25}

# set methods
# add
stocks.add("AMZN")
print(stocks)  # {'AAPL', 'GOOGL', 'TSLA', 'AMZN'}

# remove
stocks.remove("AAPL")
print(stocks)  # {'GOOGL', 'TSLA', 'AMZN'}

# discard - removes the element if it exists, else does nothing
stocks.discard("AAPL")
print(stocks)  # {'GOOGL', 'TSLA', 'AMZN'}

# pop - removes and returns an arbitrary element from the set
print(stocks.pop())  # GOOGL
print(stocks)  # {'TSLA', 'AMZN'}

# clear - removes all elements from the set
stocks.clear()
print(stocks)  # set()

# union - returns a new set with all elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}

# intersection - returns a new set with elements that are common to both sets
print(set1.intersection(set2))  # {3}

# difference - returns a new set with elements in the first set but not in the second
print(set1.difference(set2))  # {1, 2}

# symmetric_difference - returns a new set with elements in either set but not in both
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}

# issubset - returns True if all elements of the set are present in the other set
print(set1.issubset(set2))  # False

# issuperset - returns True if all elements of the other set are present in the set
print(set1.issuperset(set2))  # False

# isdisjoint - returns True if the sets have no elements in common
print(set1.isdisjoint(set2))  # False

# copy - returns a shallow copy of the set
set1_copy = set1.copy()
print(set1_copy)  # {1, 2, 3}

# set comprehension - similar to list comprehension
numbers = { number for number in range(1, 6) }
print(numbers)  # {1, 2, 3, 4, 5}

# set comprehension with condition
odd_numbers = { number for number in range(1, 11) if number % 2 != 0 }
print(odd_numbers)  # {1, 3, 5, 7, 9}

# set comprehension with nested loop
squares = { outer ** 2 for outer in range(1, 4) for inner in range(1, 3) }
print(squares)  # {1, 4, 9}

# set comprehension with nested loop and condition
squares = { outer ** 2 for outer in range(1, 4) for inner in range(1, 3) if outer % 2 == 0 }
print(squares)  # {4}

philosophers = ["Neitzsche", "Plato", "Aristotle", "Socrates", "Plato"]
philosopher_set = set(philosophers)
print(philosopher_set)  # {'Neitzsche', 'Plato', 'Socrates', 'Aristotle'}

# update - adds elements from another set to the current set
philosopher_set.update({"Kant", "Hume"})
print(philosopher_set)  # {'Neitzsche', 'Plato', 'Socrates', 'Aristotle', 'Kant', 'Hume'}



