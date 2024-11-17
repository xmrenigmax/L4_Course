
# restaurant order taking program
def restaurant():
    # menu dictionary with items and prices
    menu ={"burger": 5.00, "fries": 2.00, "soda": 1.50
           ,"salad": 3.00, "chicken": 6.00, "steak": 8.00
           ,"ice cream": 2.50, "cake": 3.00, "pie": 3.50}
    # variables for order and total
    order = []
    total = 0.0

    # welcome message
    print("Welcome to the restaurant!")

    # ask user if they would like to see the menu
    print("would you like to see the menu?")
    # user input for seeing the menu
    see_menu = input("yes or no: ")
    if see_menu == "yes":
        print(menu)
    else:
        print("okay, let's get started")

    # while loop for ordering items
    while True:
        print("what would you like to order?")
        item = input()
    
        # if item is in menu, add to order and total
        if item in menu:
            order.append(item)
            total = total + menu[item]
            # print current total and ask if user wants to order more
            print("your current total is: $", total)
            # user input for ordering more
            print("is there anything else you would like to order?")
            more = input("yes or no: ")
            if more == "":
                break
            if more == "no":
                break
        else:
            print("sorry, we don't have that item")
            
    # print order and total
    print("your order is: ")
    print(order)
    print("your total is: $", total)
    print("thank you for dining with us!")

def main():
    restaurant()

if __name__ == "__main__":
    main()


    