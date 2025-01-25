"""A mock is an object that takes the place of another object in a test"""

from unittest.mock import Mock

pizza = Mock() # dynamic object to which we can assign the attributes/methods we want without worrying about implementation

print(pizza)
print(type(pizza))

# pizza.size = "Large"
# pizza.price = 19.99
# pizza.toppings = ["BBQ", "Chilli"]

pizza.configure_mock(
    size = "Large",
    price = 19.99,
    toppings = ["BBQ", "Chilli"]
)

print(pizza.size)

print(pizza.anything) # will not throw an error
print(pizza.anything) # returns the same object as above

print(pizza.anything.we.want)

print(pizza.cover_with_cheese()) # returns mock object

