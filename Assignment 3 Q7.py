class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Error: Negative numbers are not allowed.")

# Example usage
try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)