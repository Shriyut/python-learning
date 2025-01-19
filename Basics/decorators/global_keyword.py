x = 10
y = 10

def change_stuff():
    x = 15 # since x is globally scoped and this is a shallow variable
    # x will be 15 only in this function not outside the function
    global y
    y = 15
    global z # global variables can be declared from anywhere
    z = 20   #  will only be created after function change_stuff() has been called - not a best practice

print("X is "+str(x)) # 10
print("Y is "+str(y)) # 10
change_stuff()
print("X after "+str(x)) # 10
print("Y after "+str(y)) # 15

print("Z is "+str(z))