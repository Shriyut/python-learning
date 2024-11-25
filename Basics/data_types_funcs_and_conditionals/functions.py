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