# Tuples can be thought of as a fixed length immutable list with same or different data types
# Tuples are optimal when structured ordered data needs to be preserved without any chance of it being accidently altered
# useful when data needs to be passed around multiple times in a program

foods = ("daal", "sushi", "roll")
foods_new_tuple = "daal", "sushi", "roll"
empty_tuple = ()
single_elem_tuple = 1,  # also (1, )
# commas are required to create tuples not parenthesis

print(tuple("abcdef"))  # takes every element of a string as tuple
print(foods[0])
print(foods_new_tuple[-1])
# list stored inside a tuple can be modified

addresses = (
    ['Bommanahalli', "Bengaluru", "Karnataka"],
    ['Ashiana Nagar', 'Patna', 'BIhar']
)

addresses[0][0] = "HSR"
addresses[1].append("TEst")
print(addresses)  # a tuple of 2 lists needs to remain a tuple of 2 lists that can't be changed

# a tuple object can be unpacked i.e. its ordered elements can be assigned to multiple variables in a program

employee = ("Sunny", "J", "DE", "27")
first_name = employee[0]
last_name = employee[1]
role = employee[2]
age = employee[3]

# details will have the role and age stored as a list because of * (without * error)
fn, ln, *details = employee
print(fn)
print(ln)
print(details)

*names, role2, age2 = employee  # first 2 values of tuple get stored in list
# only 1 variable can have *
fn1, *details1, age1 = employee
print(details1)
print(names)
