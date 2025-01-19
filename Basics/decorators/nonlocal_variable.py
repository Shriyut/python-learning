def outer():
    coffee_type = "Black"

    def inner():
        nonlocal coffee_type
        # nonlocal keyword suggests  where it is used the value
        # of the variable should be what is mentioned in the code block not the global value
        coffee_type = "Cappacino"
        print("Coffee type in inner function "+coffee_type)

    inner() # if inner function is not called then the value remains black

    return coffee_type

print(outer()) # cappacino