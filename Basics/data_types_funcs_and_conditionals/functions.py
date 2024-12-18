# fn(*args) suggests the function can take any number of input parameters

def output_text():
    pass #does nothing

def output():
    print("Sample output")

output_text()
output()

def p(text):
    print(text)

p(1)

def add(a, b):
    print(a + b)

add(a=4,b=9)    # keyword arguments
add(4, 9) # positional arguments

def add(a, b = 0):
    # when mentioning default value to a function argument, add argument with default at the end otherwise all arguments are expected to have a default value
    return a+b

result = add(2, 3)

a = None # represents the absence of value

def word_multiplier(word: str, times: int) -> str:
    return word * times


# functions can be annotated


def count_down_from(number):
    start = number
    while start > 0:
        print(start)
        start -= 1

count_down_from(5)

def recursive_count_down(num):
    if num == 0:
        return
    else:
        print(num)
        recursive_count_down(num - 1)


recursive_count_down(6)


def reverse_string(string):
    if len(string) == 1:
        return string
    return string[-1] + reverse_string(string[0:-1])

print(reverse_string("strawhat"))


#to get details about a function
help(print) # class names can also be supplied to the help function


# alternative for list comprehensions is map function
numbers = [4, 8, 15, 16, 23, 42]
def cube(num):
    return num ** 3

print(map(cube, numbers)) # returns map iterator object
print(list(map(cube, numbers))) # returns a list

print(map(len, numbers))

# filter function

animals = ["elephant", "horse", "cat", "giraffe", "dog"]
# filtering using list comprehension
long_words = [animal for animal in animals if len(animal) > 5]

def is_long_animal(animal):
    return len(animal) > 5 # returns naimals with name length > 5 i.e. returns true

print(list(filter(is_long_animal, animals))) # function used with filter must return a boolean

# lambda functions - anonymous function
metals = ["gold", "silver", "bronze", "tin"]
print(filter(lambda metal: len(metal) > 5, metals))
print(map(lambda val: val.repalce("s", "$"), metals))

# these function calls return true
print(all([True]))
print(all([]))
print(all([True, True]))
print(all(["a", "b"]))
print(any([True, False]))

# these function results are false
print(all([True, True, False]))
print(any([False, False]))
print(any(["a"]))

num = [1, 2, 3, 4]
print(max(num))
print(min(num))
print(sum(num))


print(dir([])) # returns all methods available to the input of dir function


float_number = 0.123456789
print(format(float_number, ".2f")) # format function returns a string and takes a number for formatting

# variable number of arguments
def accept_stuff(*args):
    # * allows python to collect any number of positional arguments to teh function and they are stored as a tuple(named args as per this example)
    print(type(args))
    print(args)

accept_stuff(1)
accept_stuff(1,2,3,4,5)

def my_max(nonsense, *args):
    greatest = args[0]
    for num in args:
        if num > greatest:
            greatest = num

    return greatest

print(my_max(1,3,6,9))
# print(my_max(1, nonsense="asdasdfa"))

def product(a, b):
    return a * b

numbers = (3,5)
print(product(*numbers)) # reverse of above approach, along with tuple list can also be used this way


#  provide ** to accept keyword arguments even if the function doesn't have any arguments
def accept_stuff(**kwargs):
    # ** allows python to collect any number of keyword arguments to teh function and they are stored as a dictionary(named kwargs as per this example)
    print(type(kwargs))
    print(kwargs)

accept_stuff(a=1, b=2, c=3)
accept_stuff(a=1, b=2, c=3, d=4, e=5)

def collect_keyword_args(**kwargs):
    print(kwargs)
    return kwargs  # returns a dictionary

def collect_kwargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

collect_kwargs(a=1, b=2,c=3)


def args_and_kwargs(a, b, *args, **kwargs):
    # python bundles positional arguments into a tuple and keyword arguments into a dictionary
    print("args below")
    print(args)
    print("kwargs below")
    print(kwargs)
    print(a+b)
    for value in args:
        print(value)
    for value in kwargs:
        print(value)

args_and_kwargs(1, 2, 3, 4, 5, c=6, d=7, e=8)