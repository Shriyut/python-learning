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