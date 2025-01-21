# all exception classes are organized in an inheritance hierarchy
# when creating a module that can raise several distinct errors best practice is to
# create a base class for exceptions defined by the module
# and then subclasses for specific error conditions

class NegativeNumberError(Exception):
    """WHen one or more index are negative"""
    pass

def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumberError
    except NegativeNumberError:
        return "SHame"

print(add_positive_numbers(-8, 0))

class Mistake(Exception):
    pass

class SillyMistake(Mistake):
    pass

class SeriousMistake(Mistake):
    pass

try:
    raise SillyMistake("Extra stupid mistake")
except SillyMistake as e:
    print(f"Caught error: {e}")

# below block results in an error
# try:
#     raise SeriousMistake("Extra stupid mistake")
# except SillyMistake as e:
#     print(f"Caught error: {e}")

try:
    raise SillyMistake("Extra nice mistake")
except Mistake as e:
    print(f"Caught mistake error: {e}")