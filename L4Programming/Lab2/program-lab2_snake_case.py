"""
@Author: Riley
@Date: 2024-10-08
"""

def snake_case():
    # @param: user_name - the name of the user
    # @param: user_age - the age of the user
    # @param: user_hobby - the hobby of the user
    # @param: user_units - the number of units the user is enrolled in

    # assign name to a variable
    user_name = "Riley"
    # assign age to a variable
    user_age = 20
    # assign hobby to a varaible
    user_hobby = "programming"
    # assign number of units enrolled in
    user_units = 6
    #display the name, age, hobby and units enrolled in
    print(user_name + " is " + str(user_age) + " years old and enjoys " + user_hobby + ". " + user_name + " is enrolled in " + str(user_units) + " units.")

def string_exercise():
    # @param: my_text - string to be converted

    # convert string to uppercase
    my_text = "Hello, World!"
    my_text = my_text.upper() 
    print(my_text)

    # replace string
    my_text = my_text.replace(my_text, "     i have an apple     ")
    print(my_text)

    # strip string - remove leading and trailing whitespaces
    my_text = my_text.strip()
    print(my_text)

    # split string - split the string seperated by spaces
    my_text = my_text.split()
    print(my_text)

    # count string - count the number of times a string appears in a string
    my_text = my_text.count('a')
    print(my_text)

    
def storage_space():
    snake_case()
    string_exercise()

storage_space()