from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10) # returns anything between 1 and 9 including both


call_me_maybe = Mock()
# call_me_maybe = Mock(side_effect = generate_number)
# if both return_value and side_Effect are mentioned while declaring side_effect will get the preference

print(call_me_maybe.side_effect) # returns None

#  side effect can be used to assign a function. iterable, or even an exception

call_me_maybe.side_effect = generate_number
print(call_me_maybe()) # gives a random number

three_item_list = Mock()
three_item_list.pop.side_effect = [3, 2, 1, IndexError("pop from empty list")]

print(three_item_list.pop())
print(three_item_list.pop())
print(three_item_list.pop())
# print(three_item_list.pop()) # gives the index error

mock = Mock(side_effect = NameError("SOme error msg"))
mock() # throws NAme Error