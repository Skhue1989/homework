while True:
    user_input = input("Please enter a number: ")
    try:
        number = float(user_input)  # Convert input to a float (handles integers and decimals)
        print(f"Valid number entered: {number}")
        break  # Exit the loop after valid input
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
