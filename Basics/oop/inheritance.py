# inheritance is a design pattern in which a class inherits(or receives) attributes and methods from one or more classes
# class inherited from is super class and class that inherits is called the subclass
# public and protected (that begin with single underscore) attributes
# and dunder methods are inherited by the subclass
# private (name mangled attributes that begin with dunder (__) are not inherited
# by subclass
# subclass can be described as TYPE OF superclass
from Basics.oop.polymorphism import Person


class Store:
    def __init__(self):
        self.owner = "sunny"

    def exclaim(self):
        print("Welcome to the store")

class CoffeeShop(Store):
    # coffeshop (subclass) inherits from store(superclass)
    # functionality of parent class can be extended here
    # functions declared here will not be available to objects of super class
    pass

starbucks = CoffeeShop()

print(starbucks.owner)
print(starbucks.exclaim())

class Employee:
    def do_work(self):
        print("WOrk work work")

class Manager(Employee):
    def waste_time(self):
        print("Chill")

class Director(Manager):
    def fire_employee(self):
        print("You're fired")

d = Director()
d.do_work()
d.waste_time()
d.fire_employee()

# method resolution order

class FrozenFood:
    def thaw(self, minutes):
        print(f"Thawing for {minutes}")

    def store(self):
        print("Put in freezer")

class Dessert:
    def add_weight(self):
        print("Putting on weight eh")

    def store(self):
        print("Put in refrigerator")

class IceCream(FrozenFood, Dessert):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)
ic.store() # store method from FRozenFood class will be invoked
# since its defined first while inheriting
# if ice cream has a store method then that will be invoked instead of
# same method from other two

print(IceCream.mro()) # function to give method resolution order for the class used

# bfs dfs

class Restaurant:
    def make_reservation(self, party_size):
        print(f"Booked for {party_size}")

class SteakHouse(Restaurant):
    pass

class Bar:
    def make_reservation(self, party_size):
        print(f"Booked lounge for {party_size}")

class BarAndGrill(SteakHouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservation(2)
# where will python search first for the function REstaurant which is inherited by SteakHOuse or Bar
# breadth first search - check at each level
# depth first search - search till the end of one arm and then more to next node
# BY DEFAULT PYTHON Uses depth first search - so here method from Restaurant class is used
# use mro method to understand how python would refer
print(BarAndGrill.mro())

# diamond shaped inheritance

class FilmMaker:
    def give_interview(self):
        print("Edgy interview")

class Director(FilmMaker):
    pass

class Screenwriter(FilmMaker):
    def give_interview(self):
        print("Serious interview")

class JackOfAllTrades(Director, Screenwriter):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()

# if the same class (FIlmMaker) occurs multiple times in the
# method resolution order of inheritance tree
# python will remove all earlier occurences of the class and
# keep only the last occurence of the class
# so here give_interview method will be used from ScreenWriter class
# regardless of order while inheriting

print(JackOfAllTrades.mro())

# built in function isinstance and issubclass

print(isinstance(1, int))
print(isinstance(stallone, Restaurant)) # False
print(isinstance(stallone, Screenwriter)) # True

print(isinstance([], (list, dict, int)))
print(issubclass(JackOfAllTrades, Screenwriter)) # true
print(issubclass(JackOfAllTrades, Restaurant)) # False
print(issubclass(JackOfAllTrades, object)) # true