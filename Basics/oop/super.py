class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return f"{self.name} is enjoying {food}"

class Dog(Animal):
    # pass
    def __init__(self, name, breed):
        super().__init__(name) # equivalent to Animal.__init__(name)
        self.breed = breed


# zoey = Dog() # will result in error with empty Dog class since dunder init method is also inherited and name isnt supplied
# zoey = Dog("Zoey") # will result in error since breed isnt provided
zoey = Dog("Zoey", "Labrador")
print(zoey.eat("chicken"))
print(zoey.name)
print(zoey.breed)

