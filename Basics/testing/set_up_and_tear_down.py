"""A test fixture is a piece of code that constructs and configures an object or system under test"""


import unittest

class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Restaurant:
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age

    def summary(self):
        return f"Restaurant owned by {self.owner.name} and is located in {self.address.city}"


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        # This function will run before each test is executed, gets executed for each testcase
        address = Address(city = "Blr", state = "Karnataka")
        owner = Owner(name = "sunny", age = 28)
        self.golden_palace = Restaurant(address, owner) # adding self allows the object ot be used in test case


    def tearDown(self):
        #  similar to setup runs after each testcase is executed
        print("THis will run after every test case")

    def test_owner_Age(self):
        self.assertEqual(self.golden_palace.owner_age, 28)

    def test_summary(self):
        self.assertNotEqual(
            self.golden_palace.summary(),
            "sdasdasdasdasdasda"
        )

if __name__ == "__main__":
    unittest.main()