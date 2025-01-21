# x = 10

try:
    print(x + 5)
except NameError:
    print("Variable not declared")
else:
    print("THis will be printed when there are no errors in try block")
finally:
    print("THis block will execute regardless of what happens")
