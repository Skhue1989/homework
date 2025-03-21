def calculate_average(*args):
    """Calculate the average of a variable number of numeric arguments.

    Returns:
        float: The average of the provided numbers. If no arguments are provided, returns 0.0.
    """
    if not args:
        return 0.0
    return sum(args) / len(args)