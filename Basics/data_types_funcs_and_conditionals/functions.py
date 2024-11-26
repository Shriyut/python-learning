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