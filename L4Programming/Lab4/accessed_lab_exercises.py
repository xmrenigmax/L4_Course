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
    maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    return maximum
'''
maximum = max_of_three(10, 20, 30)
print(maximum, "is the maximum")
'''

def calculator(num1, num2, operator):
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