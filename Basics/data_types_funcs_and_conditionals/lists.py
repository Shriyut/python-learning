"""A list is a mutable, iterable data structure that stores an ordered sequence of objects"""
# literal for list - []

empty = []
# empty = list()

drinks = ["Beer",
          "Rum",
          "Whiskey",
          "Tonic",
          "Water"]
print(len(drinks))
if "Gin" in drinks:
    print("Found new drink")
elif "Gin" not in empty:
    print("Nothing")
else:
    print("Gin is not a drink")

test_scores = [99.0, 87.5, 67]

if 99 in test_scores:
    print("Python automatically converts the value")

# index position of list elements starts with 0, -1 denotes the last element

print(drinks[0])
print(drinks[0][3])  # returns r
print(drinks[1:3])  # slicing a list
print(drinks[-4:-2])
print(drinks[:-1])

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * num)

reversed_drinks = drinks[::-1]
print(reversed_drinks)
print(reversed(drinks))

for elem in reversed_drinks:
    print(f"{elem} has length {len(elem)}")

if reversed_drinks == reversed(drinks):
    print("Will not be printed, since both are different type of objects")

# for massive collection of data, generators (reversed) are more useful because they dont store the data in memory,
# processes one element at a time while keeping track of the next one


chores = ["gym", "cleaning", "cooking", "sleeping"]
print(enumerate(chores))  # returns a generator object so that it can be iterated over a for loop

for index, chore in enumerate(chores):
    print(f"{chore} is at position {index + 1}")
# is same as
for index, chore in enumerate(chores, 1):
    print(f"{chore} is at position {index}")

# to update an element in the list
numbers[1] = 23
print(numbers)

chores[1:3] = ["decoration", "building"] # replacing elements in a range of index
print(chores)
chores[1:3] = ["nothing"]
print(chores) #drops one element from the list since we are slicing for 2 places and assigning just one value


countries = ["USA", "Germany", "India", "Canada", "Australia"]
countries.append("Japan") # returns None and adds element to the list at the end of list
print(countries)

countries.extend(["Singapore", "Thailand"])
print(countries)
countries.insert(3, "Kenya")
print(countries)

countries.pop() # removes last element of the list and returns the element
print(countries)
countries.pop(0) # removing element based on an index, -2 - removes second element from the end
print(countries)
# del function behaves in the same way as pop but doesn't return the element - del list_name[1]

del countries[1:3]
print(countries)

# remove method removes a value from the list based on its value not position
countries.remove("Germany")
print(countries)

countries.reverse() # returns None
print(countries)
print(countries.sort())
numbers.sort()
print(numbers)


#clear method removes all elements from the list
countries.clear()
print(countries)

test_list = ["Techno", "Techno", "RnB", "Punk Rock"]
print(test_list.count("Techno"))
print(test_list.index("Techno")) # returns first occurrence of the value -. value error if value doesnt exist, case sensitive

dinner = "chicken and wine"
items = dinner.split(" ") # returns a list
print(items)

joined_dinner = ",".join(items) # returns comma separated string of elements from items list
print(joined_dinner)

breakfasts = ["eggs", "oats"]
lunches = ["rice", "daal"]
dinner = ["bhujiya", "roti"]

print(zip(breakfasts, lunches, dinner)) # zip function returns an iterator
print(list(zip(breakfasts, lunches, dinner)))

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinner):
    print(f"{breakfast} {lunch} {dinner}") # iterates based on index in each list


nested_list = [[1,2,3], ["a","b"]]
print(nested_list[1][1])

numbers = [3, 4, 5, 6, 7, 8]
squares = [num ** 2 for num in numbers] # list comprehension - always generates a new list
print(squares)

#list comprehensions can be used for filtering
print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "katakuri"])
print("abcdefghijklmnopqrstuvwxyz".index(char) for char in "katakuri") # returns generator object above one returns list

print([number / 2 for number in numbers])