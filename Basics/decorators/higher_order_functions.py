# a higher order function either accepts a function as an value arguments
# or returns a function as a return value

def one():
    return 1

print(type(one)) # sample usage of higher order functions

def add(a,b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(func, a, b):
    return func(a, b)


print(calculate(add, 3, 4))

# returning a function from another function

def calculator(operation):
    def add(a, b):
        return a + b


    def subtract(a, b):
        return a - b

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract


print(calculator("add")(10, 5))
print(calculator("subtract")(9,8))

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def times10(num):
    return num * 10

operations = [square, cube, times10]

for func in operations:
    print(f"OPeration {func} has value "+str(func(5)))

