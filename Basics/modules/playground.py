# __name__ is a special variable that tells python compiler whether the file is used as a script or a module

import math, calculator

print(math.__name__) # math
print(calculator.__name__) # calculator
print(__name__) # __main__ - suggests the file is the primary file i.e. launching point - executed as a script

print(calculator.area(5))
#print(year) # results in error even print(_year) will result in error
# aliases
import calculator as calc
print(calc.subtract(5, 4))