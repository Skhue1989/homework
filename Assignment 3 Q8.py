import random

def generate_random_numbers(count, lower_bound, upper_bound):
    """Generate a list of random integers."""
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    # Generate 10 random integers between 1 and 100
    random_numbers = generate_random_numbers(10, 1, 100)
    print("Random Numbers:", random_numbers)

    # Calculate and print the average
    average = calculate_average(random_numbers)
    print("Average:", average)

if __name__ == "__main__":
    main()