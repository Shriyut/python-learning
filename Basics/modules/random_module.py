import copy
import random

print(random.random()) # generates random floating point number between 0.0 and 1.0
print(random.random() * 100)

print(random.randint(1, 5)) # both bounds are inclusive

print(random.randrange(0, 50, 10)) # gives random number between 0 10 20 30 40, upperbound is not inclusive here

# choice function returns a random element from an iterable sequence
# hence set and dictionary can not be used since they are not iterable

print(random.choice(["BOb", "ALice", "Chekov"]))
print(random.choice((1,2,3,4)))
print(random.choice("elephant")) # returns a random character


lottery_numbers = [random.randint(1, 50) for value in range(50)]

print(random.sample(lottery_numbers, 1)) # number is for how many elements to return
print(random.sample(lottery_numbers, 6))

# shuffle function accepts a list as an argument and shuffles it
# list will be mutated in place, does not return new list object

characters = ["Warrior", "Druid", "Hunter", "Rogue", "Mage"]
print(random.shuffle(characters))
print(characters)

clone = characters[:]
clone = characters.copy()
clone = copy.copy(characters) # creates a shallow copy

print(characters)
print(clone)