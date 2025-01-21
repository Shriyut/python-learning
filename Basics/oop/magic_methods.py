# magic methods allow to customize the complexity of the classes
# magic methods are used to behave similarly to python built in classes

# magic methods begin and end with dunder (__)
# dunder methods act as hooks for our classes
# a hook is a procedure that intercepts a process at some point in its execution
# magic method is a hook which is called by python
# behind the scenes at the right moment

print(3.3 + 4.4) # python invokes a dunder method to add behind the scenes
print(3.3.__add__(4.4)) # 7.7

# len also calls a dunder method to calculate the length
print([1, 2, 3].__len__())
print("hello".__contains__("h"))
print(["a", "b", "c"].__getitem__(2))


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # dunder string  customize the string representation of an object when its printed
        # name should be same as this method
        # goal is to give an user friendly string to represent the object
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        # dunder representation method is used to reflect how an object should be represented
        # to be used for a more technical representation of an object
        return f'Card("{self.rank}", "{self.suit}")'

c = Card("Ace", "Spades")
print(c)
print(repr(c)) # Card("Ace", "Spades")
print(c.__str__())
print(c.__repr__())

# a docstring is a regular python string that creates technical documentation for a piece of program
class Student:
    """
    Sample class to showcase how to use dunder methods
    There are more dunder methods than that are used in this class
    GO through python documentation to understand them
    docstring can be used in the beginning of file for documentation of module
    or like here for documentation of class
    or for a method
    """
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        # since grades is a property it can be referred as an attribute
        return self.math + self.history + self.writing

    def __eq__(self, other_students):
        # used to specify how object equality should be treated
        # must always return a boolean
        return self.grades == other_students.grades

    def __gt__(self, other):
        # dunder method for greater than
        return self.grades > other.grades

    def __le__(self, other):
        # dunder method for less than equal to
        return self.grades <= other.grades

    def __add__(self, other):
        # dunder method to add
        return self.grades + other.grades

    def __bool__(self):
        return self.grades > 250

bob = Student(math = 90, history = 90, writing = 90)
sunny = Student(math = 90, history = 90, writing = 90)
shanu = Student(math = 70, history = 40, writing = 20)

print(bob == sunny)   # true since grades for both objects are equal
print(sunny == shanu) # false since grades are not equal

print (sunny > shanu) # true
print(sunny + shanu)

if shanu:
    print("THis will not be printed")
elif sunny:
    print("THis will be printed because it satisfies the condition in __bool__ method")

print(Student.__doc__)

# named tuples can be used to create  basic classes

import collections

Book = collections.namedtuple("Book", ["title", "author"]) # returns a class

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title = "THe GReat GAtsby", author="F. Scott Fitzgerald")
print(animal_farm[1])
print(animal_farm.title)

class Library:
    def __init__(self, *books):
        # allows for any number of books objects
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library(animal_farm)
l2 = Library(animal_farm, gatsby)
print(l1.__len__())
print(len(l2))


pillows = {
    "soft": 7.99,
    "hard": 99.99
}

print(pillows["soft"])
print(pillows.__getitem__("soft")) # this function is executed behind the scenes for above lines

class Crayon:
    def __init__(self):
        self.crayons = []

    def add(self, crayon):
        self.crayons.append(crayon)

    def __getitem__(self, index):
        return self.crayons[index]

    def __setitem__(self, index, value):
        self.crayons[index] = value

    def __del__(self):
        # the below line will be printed every time the class obejct is created
        # refers to the behaviour at garbage collection moment
        print("Deleting the object aka garbage collection")

cb = Crayon()
cb.add("Blue")
cb.add("Red")

print(cb[0]) # without __getitem__ defined in the class this will result in an error
cb[0] = "Yellow"
print(cb[0])

# having getitem dunder method makes the object iterable
for crayon in cb:
    print(crayon)


