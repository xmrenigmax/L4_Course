# finds all numbers divisiible by 6 between 0 and 100
def divisible_by_six():
    number_list = []
    for number in range(0,101):
        if number % 6 == 0:
            number_list.append(number)
    print(number_list)
# divisible_by_six()

# prints squares up to given User input number
def squared():
    user_number = int(input("Enter a number: "))
    # loop until squared number is greater than user input
    for number in range(0, user_number):
        if number**2 <= user_number:
            print(number**2)
#squared()

# loops between num1 and num2 and prints all numbers divisible by 13
def divisible_by_13():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num1 > num2:
        num1, num2 = num2, num1
    number_list = []
    for number in range(num1, num2):
        if number % 13 == 0:
            number_list.append(number)
    print(number_list)
#divisible_by_13()

# loop between 0 - 100. sum of all even numbers that are not divisible by 3
def even_not_three():
    sum = 0
    for number in range(0, 101):
        if number % 3 == 0:
            continue
        if number % 2 == 0:
            sum += number
    print(sum)
even_not_three()