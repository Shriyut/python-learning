def sum_of_list(numbers):
    """REturns sum of all numbers in a list, test driven development (writing tests first)
    >>> sum_of_list([1,2,3])
    6
    >>> sum_of_list([3,4,5])
    12
    if wrong output is returned then line 5 returns an error when program is executed
    """

    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()
