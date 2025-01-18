# Everything in python is an object

import calculator # similar to from calculator import *
# this module in python contains the best practices
# import this will show all the design patterns suggested in python
# whenever a module is imported python will execute all of the code present in the module
# if there were a print statement in calculator.py just the running this file
# with import calculator would print that statement
# python will import a module only once even if its imported multiple times

print(calculator.creator)
print(calculator.add(1, 3))


