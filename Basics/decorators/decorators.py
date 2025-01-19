# a decorator is a higher order function that accepts a function as an input and returns another function
import functools


def be_nice(fn):
    # def inner()
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        # *args is optional, **kwargs can also be used or it can be left as empty
        print("Starting execution")
        print(args)
        print(kwargs)
        # fn()
        # fn(*args, **kwargs)
        result = fn(*args, **kwargs)
        return result
        # above 2 lines were added to resolve the issue where complex_busines_sum function output was printed as None

        print("Executed")

    return inner
# Above approach can be used to get the time taken by the function to execute

def sample_function():
    print("THis is a sample function")

result = be_nice(sample_function)
result()

# decorators can also be declared using the @ symbol - syntactic sugar for decorators

@be_nice
def another_sample_function(sample):
    print("THis is the other sample function")

another_sample_function("test")
another_sample_function(sample = "test1")

@be_nice
def complex_business_sum(a, b):
    "Complex business logic executed here"
    return a + b

print(complex_business_sum(9,8)) # prints none

# help(len) # returns documentation for len function

def fn_with_docstring():
    "THis is how you define docstrings in python"
    print("docstring function")

help(fn_with_docstring)
# help(complex_business_sum) # prints inner(*args, **kwargs) - function was used with a decorator
# functools can help resolve the above issue
help(complex_business_sum)

