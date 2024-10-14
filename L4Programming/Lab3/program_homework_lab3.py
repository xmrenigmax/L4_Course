import math
import random

def herons_formula():
    # gets the length of the sides of a triangle 
    # {a, b, c} is with input from the user
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    side_c = float(input("Enter the length of side c: "))
    # checks if the sides form a valid triangle using the triangle inequality theorem
    if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
        # calculates the area of the triangle
        surface = ((side_a + side_b + side_c) / 2)
        # calculates the area of the triangle using Heron's formula
        herons_equation = (surface * (surface - side_a) * (surface - side_b) * (surface - side_c))
        area = math.sqrt(herons_equation)
        # prints the area of the triangle
        print("The area of the triangle is:", area)
    else:
        print("Error: The provided sides do not form a valid triangle.")
    
#herons_formula()

def odometer_checker():
    # variable to store the number of kilometers driven
    distance = 160648
    # if a digit in distance is above 5 change it to one lower on that digit
    # convert to string to allow for manipulation
    distance = str(distance)
    # convert to list to seperate the digits
    distance = list(distance)
    # loop through the list and check if the digit is above 5
    for i in range(len(distance)):
        # if the digit is above 5, subtract 1 from the digit
        if int(distance[i]) > 5:
            # convert the digit back to a string then interger and subtract 1
            distance[i] = str(int(distance[i]) - 1)
    # convert the list back to a string by joining the elements
    calculate_distance = "".join(distance)
    print("The new distance is:", calculate_distance)
#odometer_checker()

def coin_flip_betting():
    #100 rounds bet on either heads or tails each round
    #winnings are £1 for a win
    
    # variable to store the amount of money won
    winnings_by_random = 0
    winnings_by_heads = 0
    # loop through 100 rounds
    for i in range(100):
        # generate a number between 0 and 1
        flip = random.randint(0, 1)
        # randomly select heads or tails
        random_bet = random.randint(0, 1)
        heads_bet = 1
        # if the flip is equal to the bet, the player wins
        if flip == random_bet:
            winnings_by_random += 1
        elif flip == heads_bet:
            winnings_by_heads += 1
    # print the amount of money won
    print("The amount of money won by random betting is:", winnings_by_random)
    print("The amount of money won by betting on heads is:", winnings_by_heads)
# coin_flip_betting()

def longest_string_recuring():
    # gets variable to store string of 0 and 1
    binary_string = input("Enter a string of 0s and 1s: ")
    # variable to store the longest recurring substring
    longest_recurring = ""
    # variable to store the current recurring substring
    current_recurring = ""
    # loop through the string
    for i in range(len(binary_string)):
    # if character is the samee as the previous character, add it to the current recurring substring
        if binary_string[i] == binary_string[i-1]:
            current_recurring += binary_string[i]
        else:
            # if the current recurring substring is longer than the longest recuring substring
            # update the longest recurring substring
            if len(current_recurring) > len(longest_recurring):
                longest_recurring = current_recurring
            # reset the current recurring substring
            current_recurring = ""
    # print the longest recurring substring
    print("The longest recurring substring is:", longest_recurring)
    length_of_longest_recurring = len(longest_recurring)
    print("The length of the longest recurring substring is:", length_of_longest_recurring)
longest_string_recuring()