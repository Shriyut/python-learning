# protected attributes are semi private to the object
# their values should only be modified by instance methods

# encapsulation suggests data should be bundled together with the methods that work on that data
# i.e. objects data should be hidden and only way to modify it should be through instance methods

class SmartPhone():
    def __init__(self):
        self.company = "Apple"
        self.firmware = 16.0

iphone = SmartPhone()
print(iphone.company)
print(iphone.firmware)

iphone.company = "Samsung"
iphone.firmware = 17.0
print(iphone.company)
print(iphone.firmware)
# object attributes were modified
# all object attributes are public in python by default


class NewSmartPhone():
    def __init__(self):
        # prefixed _ suggests these attributes are not meant to
        # be modified not hardbound
        # _ prefix also works for instance methods suggesting
        # it should not be used by developers to call that function
        # it should only be called by other instance methods
        self._company = "Google"
        self._firmware = 14

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Updating firmware version")
        self._firmware += 1

phone = NewSmartPhone()
print(phone._company)
phone.update_firmware()
print(phone._firmware)