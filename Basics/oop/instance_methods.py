# instance method is a function that belongs to an object (bounded to an object, need to be referenced from an object)

class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        # all instance methods take self as the first parameter
        print(f"Pokemon {self.name} roar")

    def take_damage(self, amount):
        self.health -= amount


squirtle = Pokemon("Squirtle", "Water")
squirtle.roar()
squirtle.take_damage(20)
print(squirtle.health) # 80