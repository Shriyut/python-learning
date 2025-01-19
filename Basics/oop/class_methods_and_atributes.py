class SushiPlatter():
    origin = "Japan" # class attribute
    def __init__(self, **kwargs):
        self.salmon = kwargs.get("salmon", "NA")
        self.tuna = kwargs.get("tuna", "NA")
        self.shrimp = kwargs.get("shrimp", "NA")
        self.squid = kwargs.get("squid", "NA")

    @classmethod
    def lunch_special_a(cls):
        # python will feed the class to this method
        # all attributes defined in constructor will be available to this method
        # return SushiPlatter() # can be done
        return cls(salmon = 2, tuna = 5, shrimp = 8, squid = 1)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon=0, tuna=10, shrimp=0, squid = 1)

sunny = SushiPlatter(salmon=8, tuna=4, shrimp=3, squid=7)
print(sunny.squid)

lunch = SushiPlatter.lunch_special_a()
print(lunch.squid)

tuna_fan = SushiPlatter.tuna_lover()
print(tuna_fan.tuna)

print(tuna_fan.origin)

# working with class attributes

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"New number of counter objects created: {cls.count}")
        return two_counters

print(Counter.count) # 0
c1 = Counter()
print(Counter.count) # 1

c2, c3 = Counter.create_two()
print(Counter.count) # 3

print(c1.count) # 3
print(c2.count) # 3
print(c3.count) # 3

# attribute lookup order
# python will look for instance attribute first and then class attribute for a referenced object


# static methods

# static methods are used for utility operations that affect neither the class nor its objects

class WeatherForecast:
    def __init__(self, temperatures):
        self.temperatures = temperatures

    @staticmethod
    def convert_from_fahrenheit_to_Celsius(fahr):
        # static methods dont rely on self or cls they just perform a utility
        # STATIC METHODS ARE ALSO AVAILABLE AS A CLASS METHOD
        calculation = (5/9) * (fahr - 32)
        return round(calculation, 2)

    def in_celsius(self):
        # instance method
        return [self.convert_from_fahrenheit_to_Celsius(temp) for temp in self.temperatures]


wf = WeatherForecast([100, 90, 877, 240])
print(wf.in_celsius())

print(WeatherForecast.convert_from_fahrenheit_to_Celsius(100))