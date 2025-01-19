# getters and setters are instance methods that get/set attribute values on the objects
# property can thought of as a mix of attributes and instance methods
# behind the scenes properties secretly invoke instance methods for us

class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

    feet = property(_get_feet, _set_feet)

h = Height(5)
print(h.feet) # feet is a property of the Height class
# above statement will invoke _get_feet and _set_feet methods

h.feet = 6
print(h.feet)

h.feet = -10
print(h.feet) # prints 6 (because of if condition)
# looks like attributes but behind the scenes its invoking methods
# property and attributes cant have same names in the class

# defining property as a decorator

class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100

bank_account = Currency(50000)
print(bank_account.dollars)
bank_account.dollars = 1
print(bank_account.dollars)

# getattr and setattr which allow us to get/set the value of an object on the object without using . syntax

stats = {
    # these key value pairs will serve as attributes and their respective values
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["Chicken", "Onion", "BBQ sauce"]
}

class Pizza():
    def __init__(self, stats):
        for k, v in stats.items():
            setattr(self, k, v)

bbq = Pizza(stats)
print(bbq.ingredients)

for attr in ["price", "name", "diameter", "discount"]:
    print(getattr(bbq, attr, "Not_Available"))

# dir function returns a list of all attributes associated with the object

# hasattr ad deleteattr as the name suggests check/delete attribute for an object

stats_to_delete = ["size", "diameter", "spice_level", "ingredients"]

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)

# print(bbq.size) # results in an error