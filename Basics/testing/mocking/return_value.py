from unittest.mock import Mock

mock = Mock()

print(mock()) # just returns a mock object

print(mock.return_value) # returns same object as above

mock.return_value = 25

print(mock()) # 25
# mock = Mock(return_value = 25) - also a valid declaration

stuntman = Mock()
stuntman.jump_off_building.return_value = "my legggg"
stuntman.light_on_fire.return_value = "burrnnnnnn"

print(stuntman.jump_off_building())
print(stuntman.light_on_fire())
print(stuntman.light_on_fire) # this will return the object not the burn string