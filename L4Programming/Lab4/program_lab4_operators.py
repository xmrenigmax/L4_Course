def number_classified():
    # This function takes an integer as input and classifies it as even, odd, or a multiple of 4.
    # @Param number (int): The number to classify.
    # @Return None: The function does not return a value.

    # Prompt the user to enter a number.
    number = int(input("Enter a number: "))
    # modulus operator shows the remainder of the division
    if number % 2 == 0:
        print("The number is even.")
    if number % 4 == 0:
        print("The number is a multiple of 4.")
    if number % 5 == 0:
        print("The number is a multiple of 5.")
    else:
        print("The number is odd.")

def count_digits():
    # This function takes an integer as input and counts the number of digits in the integer.
    # @Param number (int): The number to count the digits of.
    # @Return None: The function does not return a value.

    # Prompt the user to enter a number.
    number = int(input("Enter a number: "))
    # Convert the number to a string and count the number of characters in the string.
    print("The number has", len(str(number)), "digits.")

def nested_condition():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    if x > 5:
        if y > 5:
            print("Both numbers are greater than 5.")
        elif y == 5:
            print("x is greater than 5 and y is 5.")
        else:
            print("x is greater than 5 and y is less than 5.")

def tower_of_hanoi():
    # This function solves the Tower of Hanoi puzzle.
    # @param disks (int): The number of disks.
    # @param source (str): The source tower. 
    # @param target (str): The target tower.
    # @param auxiliary (str): The auxiliary tower.

    def hanoi(disks, source, target, auxiliary):
        # Base case: only one disk to move.
        if disks == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        
        # Move n-1 disks from source to auxiliary, so they are out of the way.
        hanoi(disks - 1, source, auxiliary, target)
        # Move the nth disk from source to target.
        print(f"Move disk {disks} from {source} to {target}")
        # Move the n-1 disks from auxiliary to target.
        hanoi(disks - 1, auxiliary, target, source)

    disks = int(input("Enter the number of disks: "))
    hanoi(disks, 'A', 'C', 'B')
    print("The disks have been moved.")
    number_of_moves = (2 ** disks) - 1
    print(f"It took {number_of_moves} moves to move {disks} disks.")

def main():
    # Uncomment the function you want to run.
    # number_classified()
    # count_digits()
    # nested_condition()
    tower_of_hanoi()

if __name__ == "__main__":
    main()
