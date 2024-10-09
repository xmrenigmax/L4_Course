
'''
@author: Riley
@date: 2024-10-08
'''


def pyramid_loop():
    # program that takes an integer as input and prints in a pyramid

    # @param: rows: int: the amount of rows the user wants
    # @return: None

    # get the number of rows from the user
    rows = int(input("Enter amount of rows you would like: "))
    # a loop that goes through to the users amount of rows
    for i in range(1, rows + 1):
        # i = the row number,, rows + 1 = the amount of rows the user wants
        print((str(i) + " ") * i)


def first_digit():
    # takes integer from user, returns the first number of number
    number = int(input("Enter a number: "))
    # Ensure the number is not a single digit
    while abs(number) < 10:
        number = int(input("Enter a number with more than one digit: "))
    # Find the first digit
    first_digit = str(number)[0]
    print("The first digit is:", first_digit)
        


def selection_sort():
    # takes a list of numbers from user and sorts them into ascending order
    sorting_list = []
    # get the amount of numbers and the numbers from the user
    amount = int(input("Enter the amount of numbers you would like to sort: "))
    # get the list of numbers from the user
    for i in range(amount):
        number = int(input("Enter a number: "))
        sorting_list.append(number)
    # sort the list
    sorting_list.sort()
    print("The sorted list is:", sorting_list)

selection_sort()