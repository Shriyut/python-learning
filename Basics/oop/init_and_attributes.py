# __init__ method and similar methods are called magic methods because they work behind the scenes
# declared within the body of a class


class Guitar():
    def __init__(self): # constructor
        # dunder init method should be the first method defined in the class
        # will be executed where an object is instantiated for this class
        # the dunder (__) init method should not return any value
        # must include atleast a single parameter (self in this case)
        # self refers to the object being instantiated
        print(f"New guitar object being created {self}")

electric = Guitar()
print(electric) # same object reference will be printed twice, once from init and other from this print


# an attribute is a piece of data stored on an object
acoustic = Guitar()

#below is an anti-pattern of defining attributes but is possible in python

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

print(acoustic.wood)

class NewGuitarClass:
    def __init__(self, wood, year = 1990):
        # self.wood = "Mahogany" # constant value for each object of this class
        self.wood = wood
        self.strings = 6 # constant value for all objects
        self.year = year # default value set in dunder init declaration

baritone = NewGuitarClass("Alder") # if value not given then type error
print(baritone.wood)
print(baritone.strings)
print(baritone.year)
