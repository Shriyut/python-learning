# an exception is a special object that python uses to manage errors during program execution
# a traceback is a report of the exception that was raised

def divide_five_by_number(n):
    try:
        result = 5 / n
    #  except (ZeroDivisionError, TypeError) as e: # this will also work
    except ZeroDivisionError:
        # result = 0 # runs for all  exceptions
        # pass  # can also be added
        return "You can't divide by 0"
    except TypeError as err:
        return f"Pass a numeric value {err}"

    return result

print(divide_five_by_number(0))

