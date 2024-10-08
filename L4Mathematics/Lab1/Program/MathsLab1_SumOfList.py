values = [2,3,4,5,6,7]
def display_List():  
  #a for loop. plotting the list and there data
    # gets the values in the list
    for value in values:
    # prints the values in the list
        print(values)
    # gets the values in the list
    for i,value in enumerate(values):
        print(i,value)

    #another example of a for loop getting data
    for i in range(len(values)):
        # prints length of list, and then the values of item 
        print(f"{i} + {values[i]}")
display_List()

def sum_Of_List():
    # Using a for loop to sum the values
    sum_List = 0
    for value in values:
        sum_List += value
    print(f"Sum using for loop: {sum_List}")

    # Using the built-in sum function to sum the values
    sum_List= sum(values)
    print(f"Sum using built-in sum function: {sum_List}")
sum_Of_List()
