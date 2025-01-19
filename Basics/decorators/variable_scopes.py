# scope refers to the locations in the python program in which a name(variable/function i.e. something with an identifier) can be used

#constant values can be declared here
age = 28 # scoped to this file, needs to be imported to use in other scripts

# within a module(any python file) a variable assigned outside of a function or code block is globally scoped in the current file
# variables defined in a code block are locally scoped to the execution of the file

def fancy_func():
    nonsense = 10
    print(age) # age is globally scoped so it can be used here

# a shallow variable is a local variable that shares the same name as a global variable
# within the code block  where shallow variable is defined the local variable will be used instead of global

fancy_func()
#print(nonsense) # will result in an error since nonsense is locally scoped

# legb rule is how python searches for a name within the program

# local > enclosing functions > global > built-in
# this is how python searches to resolve a name, if name is not found starting from local and till built-in
# python throws an error
