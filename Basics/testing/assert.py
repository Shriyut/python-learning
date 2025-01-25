# a regression is when a feature that used to work no longer does
# testing prevents regression
# a test suite is a collection of tests that target related functionality
# code coverage refers to the percentage of codebase that is tested by tests

def add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "Both arguments must be integers"
    # if both are true then returns None
    return x + y

print(add(3,4))
print(add(3, "5")) # type error changes to assertion error