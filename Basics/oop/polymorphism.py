# polymorphism
import random


class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __len__(self):
        return self.height

values = [
    "Boris",
    [1, 2, 3],
    (4,5,6,7,8),
    {"a":"b"},
    Person(name = "sunny", height = 6)
]

# len is used as an example of polymorphism
for v in values:
    print(len(v))

class Player:
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.games_played

class HumanPlayer(Player):
    def make_move(self):
        print("PLayer move")

class ComputerPlayer(Player):
    def make_move(self):
        print("COmputer move")

hp = HumanPlayer(games_played=30, victories=20)
cp = ComputerPlayer(games_played=1000, victories=999)
print(hp.win_ratio)
print(cp.win_ratio)

game_players = [hp, cp]
starting_players = random.choice(game_players)
starting_players.make_move()

# name mangling in python
# intentionally twisting attributes/method names around so that subclasses or after import method with same name is not created
# an attribute is mangled if it begins with __
# can be used when there is a probability for subclass to will accidently overwrite something in your superclass

class Nonsense:
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("THis is some method")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense() # n = Nonsense doesnt instantiate the object so () is required
sn = SpecialNonsense()
# print(n.__some_attribute) # results in attribute error saying 'Nonsense' object has no attribute '__some_attribute'
# print(sn.__some_attribute) # same error
# n.__some_method() # same attribute error

print(n._Nonsense__some_attribute) # hello
print(sn._Nonsense__some_method)
# this is how python mangles the name of attribute and method
