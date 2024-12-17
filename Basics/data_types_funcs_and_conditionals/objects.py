# a variable is an identifier for an object

# the objects that dont have any references (variables) are garbage collected (thrown out of computer's memory)

#shared references for immutable types
a = 3
b = a

a = 5
print(a)
print(b) # doesnt get reassigned to 5

#shared refs for mutable types
c = [1, 2, 3, 4]
d = c
c.append(5)
print(c)
print(d) # both values are same since list is mutable

students = ["a", "b", "c"]
athletes = students
nerds = ["a", "b", "c"]

print(students == athletes)
print(students == nerds)

# both return true since they evaluate equality
print(students is athletes)
print(students is nerds) # returns false since is checks for object ref in memory i.e. checks for identity

# identical refs to mutable objects can lead to issues

# shallow copy - creates new list and inserts all elements
a = [1,2,3]
b = a[:] # equivalent t using copy method

print(a==b) #returns true
print(a is b) # returns false

numbers = [23, 34, 45]
a1 = [1, numbers, 5]
b1 = a1.copy()

print(a1[1] is b1[1]) # returns true since it is a ref to numbers list
a1[1].append(100)
print(b1) # shows the 100 value added to numbers list by default

