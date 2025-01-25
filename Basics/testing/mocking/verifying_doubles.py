from unittest.mock import MagicMock

class BurritoBowl:
    restaurant_name = "Bobo's Burrito"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "WHite", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1

# lunch = BurritoBowl.steak_special()
# print(lunch.guacamole_portions)
# lunch.add_guac()
# print(lunch.guacamole_portions)

class_mock = MagicMock(spec = BurritoBowl)
# if we try to access attributes/methods that are not present in BurritoBowl class then python will raise an error
print(class_mock.restaurant_name) # returns object not the value of attribute
# print(class_mock.chicken()) # throws AttributeError

instance_mock = MagicMock(spec = BurritoBowl.steak_special())
print(instance_mock.protein) # returns object
instance_mock.beans = True
print(instance_mock.beans) # TRue

# spec_set does not allow to set new attributes on the class object
instance_mock_1 = MagicMock(spec_set = BurritoBowl.steak_special())
print(instance_mock_1.rice)