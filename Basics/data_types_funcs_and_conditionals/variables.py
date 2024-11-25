# Variable is a name that refers to the object (not the actual object)

name = "sunny"

# python follows snakecasing variable_name

variable_name_is = True

fact_or_fiction = 6 < 10
print(fact_or_fiction) # returns false

#Python is dynamically typed i.e. a variable can be reassigned to diff value (can be diff data type)
# no need to mention the data type of the variable
c = 5
print(c)
c = "string"
print(c)

a = b = 5 #python compiler interprets this as whatever value is assigned to the variable b, same value should be assigned to variable a

a, b = 6, 9 # a = 6, b = 9

a = a + 2

#above statement using augumented assignment operator
a += 2

#collecting user input

input("Enter some text ") #input is taken as string