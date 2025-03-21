def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input types. Please provide numbers.")

# Example usage
print(divide_numbers(24, 6))  # Should print 4.0
print(divide_numbers(10, 0))  # Should print an error message
print(divide_numbers(10, 'a'))  # Should print an error message
