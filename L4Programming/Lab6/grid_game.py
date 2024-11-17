import random
# game bascially creates a 2D list of random integers 1-10
# then finds the row and column indices of the max number in the list
# then determines if the user has won based on the sum of the row and column indices
# if the sum is less than or equal to 3, the user has won
# otherwise, the user has lost

def create_2d_list(n):
    # receives an integer n

    # list_2d is a 2D list of random integers 1-10
    list_2d = []
    # iterate through the range of n
    for i in range(n):
        row =[]
        # append a random integer 1-10 to the row
        for i in range(n):
            row.append(random.randint(1,10))
        list_2d.append(row)
    return list_2d

def row_col_max(list_2d):
    # receives a 2D list

    # variables to store the max number, row index, and column index
    max_num = 0
    row_index = 0
    col_index = 0
    
    # iterate through the 2D list
    for i, row in enumerate(list_2d):
        # iterate through the row
        for j, value in enumerate(row):
            # if the value is greater than the max number
            # set the max number to the value
            if value > max_num:
                max_num = value
                row_index = i
                col_index = j
                # set the row index and column index to the current indices
    return row_index, col_index

def is_win(row, column):
    # receives the row and column indices of the max number
    if row + column <= 3:
        return True
    else:
        return False

def main():
    # propt user for size of 2D list
    n = int(input("Enter a number greater than 5: "))
    # use the create_2d_list function to create the 2D list
    list_2d = create_2d_list(n)
    # use the row_col_max function to get the row and column indices of the max number
    row, column = row_col_max(list_2d)
    # use the is_win function to determine if the user has won
    win = is_win(row, column)
    # display message to user if they have won
    if win:
        print("Congratulations, you have won!")
    else:
        print("Sorry, you have lost.")




if __name__ == "__main__":
    main()
