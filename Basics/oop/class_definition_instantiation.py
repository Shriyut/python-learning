class Person():
    pass # indicates code block has no content for python to not throw an error
    # variables declared here will be limited to scope of the class

class DatabaseConnection():
    x = 5

# instantiation of classes

Person() # creates a new person object
sunny = Person() # another object of same class with name assigned
shanu = Person()

# print statement gives the location of the object in memory
print(sunny)
print(shanu)