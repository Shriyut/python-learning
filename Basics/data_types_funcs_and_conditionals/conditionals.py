if 2 != 1:
    print("Success condition")

if 3:
    # 0 is treated as false value and any other number (including negative numbers) is taken as true value
    # empty string is treated as false but others as true
    print("another success condition")

if 10 > 15:
    print("will never be printed")
elif 10 < 15:
    print("will be printed")
else:
    print("else criteria")

# ternary operator ( can only be used with if - else conditions )
check = "Valid" if len("12345") == 5 else "Invalid"

if 10 > 14 or 14 > 10:
    print("yes")

if 10 == 10 and 14 > 1:
    print("yes")

if "z" not in "hello":
    print("yes")

i = 0
while i < 5:
    print("low", str(i))
    i += 1

print(i)

for number in range(5):
    print(number)  # starts with 0

for number in range(1, 11):
    print(number)  # starts with 1, 11 not included

for number in range(10, 101, 8):
    print(number)  # iterates over 8 places

print(3 in [1, 2, 3, 4, 5])


def contains(values, target):
    found = False
    for value in values:
        if value == target:
            found = True
            break
    return found


def sum_of_positive_numbers(values):
    total = 0
    for value in values:
        if value < 0:
            continue
        total += value
    return total

