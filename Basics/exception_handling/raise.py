def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive")
        return a + b
    except ValueError as e:
        # print(f"Got error - {e}") # returns None
        return f"Got error - {e}"

print(add_positive_numbers(-1, 4))