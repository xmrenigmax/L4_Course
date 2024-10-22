'''
@Author: Riley Jordan
@Date: 20/10/2024
@Version: 1.0
'''

def max_of_three(num1, num2, num3):
    # This function takes three integers as input and returns the maximum of the three given numbers.
    # @Param maximum (int): The number of comparison.
    # @Param num1 (int): The first number.
    # @Param num2 (int): The second number.
    # @Param num3 (int): The third number.
    # @Return int: The maximum of the three numbers.

    # Initialize the maximum to the first number
    maximum = num1
    # Compare the second and third numbers to the current maximum
    if num2 > maximum:
        maximum = num2
    # Compare the third number to the current maximum
    if num3 > maximum:
        maximum = num3
    # Return the maximum number
    return maximum
'''
maximum = max_of_three(10, 20, 30)
print(maximum, "is the maximum")
'''

def calculator(num1, num2, operator):
    # Inform the user of the available operations they can perform.
    print("Available operations: +, -, /, *, %, >, >=, <, <=")

    # This function performs basic arithmetic and comparison operations on two numbers.
    # @Param num1 (int or float): The first number.
    # @Param num2 (int or float): The second number.
    # @Param operator (str): A string representing the operation to perform. The valid operators are: "+", "-", "/", "*", "%", ">", ">=", "<", "<=".

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        # If the numbers are not integers or floats, the function prints an error message and does not return a result.
        return "Invalid numbers."

    if operator == "/" and num2 == 0:
        # If the second number is 0 and the operator is division, the function prints an error message and does not return a result.
        return "Cannot divide by zero"
    
    # Perform the operation based on the operator provided
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "%":
        result = num1 % num2
    elif operator == ">":
        result = num1 > num2
    elif operator == ">=":
        result = num1 >= num2
    elif operator == "<":
        result = num1 < num2
    elif operator == "<=":
        result = num1 <= num2
    else:
        # If an invalid operator is provided, the function prints an error message and does not return a result.
        return "Invalid operator."
    return result

# Example usage:
## please use 2 numbers and an operator to perform an operation
## operators: +, -, /, *, %, >, >=, <, <=
'''
print(calculator(10, 5, "+"))  # Output: 15
print(calculator(10, 5, "-"))  # Output: 5
print(calculator(10, 5, "/"))  # Output: 2.0
print(calculator(10, 5, "*"))  # Output: 50
print(calculator(10, 5, "%"))  # Output: 0
print(calculator(10, 5, ">"))  # Output: True
print(calculator(10, 5, ">=")) # Output: True
print(calculator(10, 5, "<"))  # Output: False
print(calculator(10, 5, "<=")) # Output: False
print(calculator(10, 0, "/"))  # Output: cannot divide by zero
print(calculator(10, 5, "x"))  # Output: invalid operator
print(calculator("10", 5, "+")) # Output: invalid numbers
'''

def winning_numbers(user_numbers, winning_numbers):
    # This function checks if the user's numbers match the predefined winning numbers.
    # @Param user_numbers (list): A list of three integers representing the user's chosen numbers.
    # @Param winning_numbers (list): A list of predetermined integers representing the winning numbers.
    # @Return str: A string indicating the prize won: "First", "Second", "Third", "No".

    # makes sure the lists are 3 numbers long
    if len(user_numbers) != 3 or len(winning_numbers) != 3:
        return "Invalid input. Please enter three numbers."

    # Check how many numbers match the winning numbers using set intersection
    # using sets because they are unordered and do not contain duplicates
    ## set() creates a set from the list of numbers
    match_count = len(set(user_numbers) & set(winning_numbers))

    # Determine the prize based on the number of matches
    if match_count == 3:
        prize = "First"
    elif match_count == 2:
        prize = "Second"
    elif match_count == 1:
        prize = "Third"
    else:
        prize = "No"
    # Return the prize won
    return prize

# Example usage:
## please use 3 numbers in each list to find if you have won a prize
'''
print(winning_numbers([3, 5, 10], [5, 14, 17]))  # Output: Third
print(winning_numbers([14, 5, 17], [5, 14, 6]))  # Output: Second
print(winning_numbers([5, 14, 17], [5, 14, 17]))  # Output: First
print(winning_numbers([1, 2, 3], [5, 14, 17]))  # Output: No
print(winning_numbers([1, 2], [5, 14, 17]))  # Output: Invalid input. Please enter three numbers.
'''