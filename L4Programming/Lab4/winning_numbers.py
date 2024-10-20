def winning_numbers(user_numbers, winning_numbers):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_numbers (list): A list of three integers representing the user's chosen numbers.
    winning_numbers (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_numbers = [5, 14, 17]
    user_numbers = [3, 5, 10]
    result = winning_numbers(user_numbers, winning_numbers)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_numbers = [14, 5, 10]
    result = winning_numbers(user_numbers, winning_numbers)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...

    # Print the result
    print(f"Congratulations, you won {prize} prize!")

    return prize