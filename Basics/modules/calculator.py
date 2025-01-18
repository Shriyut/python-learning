creator = "sunny"
PI = 2.14
_year = 2025
# prefixing _ tells python not to export this variable outside the module

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def area(radius):
    return  PI * radius * radius

if __name__ == "__main__":
    print("Calculator file called as a script")
else:
    print("Calculator file called as a module")