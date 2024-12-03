import copy

# Exercise 1
def add_two_numbers(a, b):
    return a + b

def product_two_numbers(a, b):
    return a * b

def sorted_alphabetically(a):
    # creating a custom sorting key
    # uppercase Letter followed by lowercase
    # alphabetically
    def custom_sort_key(x):
        x = x.join([x.lower(), x])
        return x
    # sorting the string
    a = sorted(a, key=custom_sort_key)
    return a

def commons_of_lists(a,b):
    # return common element out between both lists
    a = set(a)
    b = set(b)
    if a.intersection(b):
        return list(a.intersection(b))
    else:
        return []
    
def palindrome(a):
    # check if the string is a palindrome by 
    # comparing the string to its reverse, 
        # [::-1] is a slicing technique that reverses the string
    return a == a[::-1]


def movie_ticket_price(child, adult, senior, time):
    # ticket prices
    adult_ticket_prices = 15
    child_ticket_prices = 5
    senior_ticket_prices = 12

    # consumer discount prices
    if (adult == 2 and child >= 2):
        #2 children get in free with 2 adults
        child = child - 2


    if (adult == 1 and senior == 1):
        # 1 chid goes free
        child = child - 1
        # calculate the total ticket prices
        adult_ticket_prices = adult_ticket_prices * adult
        child_ticket_prices = child_ticket_prices * child
        senior_ticket_prices = senior_ticket_prices * senior

    if (adult == 2 and senior == 1):
        # half price for senior
        senior_ticket_prices = senior_ticket_prices * 0.5
        # calculate the total ticket prices
        adult_ticket_prices = adult_ticket_prices * adult
        child_ticket_prices = child_ticket_prices * child
        senior_ticket_prices = senior_ticket_prices * senior

    if (adult == 3 and senior == 2):
        # every adult and senior gets a discount
        adult_ticket_prices = adult_ticket_prices * 0.75
        senior_ticket_prices = senior_ticket_prices * 0.75
        # if two children are present, they get in free
        if child >= 2:
            child = child - 2
        
        child_ticket_prices = child_ticket_prices * 0.5

        # calculate the total ticket prices
        adult_ticket_prices = adult_ticket_prices * adult
        child_ticket_prices = child_ticket_prices * child
        senior_ticket_prices = senior_ticket_prices * senior

    # time based discounts
    if time <= 15:
        # discount of 5%
        adult_ticket_prices = adult_ticket_prices * 0.95
        child_ticket_prices = child_ticket_prices * 0.95
        senior_ticket_prices = senior_ticket_prices * 0.95

        # calculate the total ticket prices
        adult_ticket_prices = adult_ticket_prices * adult
        child_ticket_prices = child_ticket_prices * child
        senior_ticket_prices = senior_ticket_prices * senior


def divisible_by_2_3_5(n):
    x = []
    for i in range(1, n):
        x.append(i*30)
    return x

# Exercise 2
def fix_code(year):
    if year <= 2023:
        year = "That's the past!"
    elif year >= 2024 and year < 2025:
        year = "That's the present!"
    else:
        year = "That's the future!"
    return year

def total_sum(lst):
    total = 0
    for x in lst:
        total = total + x
    return total

def count_n(n):
    i = 0
    n = n + 1
    while i < n:
        i = i + 1

def sort_list(original_list):
    sorted_list = sorted(original_list)
    return sorted_list

def power(a, b):
    return a ** b

def even_in_list(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
        
def copied_list(original_list):
    copied_list = copy.deepcopy(original_list)
    copied_list[1][0] = "changed"
    print("Original list: ", original_list)
    print("Copied list: ", copied_list)

    ' or u can just remove [0] '


# Exercise 3
def error_handling():
    try:
        with open("file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")

    try:
        with open("file.txt", "w") as file:
            file.write("The Result of" + str(1/0) + "is undefined")
    except ZeroDivisionError:
        print("Cannot divide by zero")

    try:
        with open("file.txt", "w") as file:
            file.write("\nAlso, the result of " + 5 + str(5) + "is" + str(10))
    except TypeError:
        print("Cannot do string and integer")


def between_values():
    Bool = True
    while Bool:
        try:
            x = float(input("Enter a number between 13.1 and 13.9 >>> "))
            if x > 13.1 and x < 13.9:
                Bool = False
                print(f"Correct: ", x)
            elif x == 13.1 or x == 13.9:
                print(f"equal to 13.1 or 13.9: ",x)
            else:
                print(f"Wrong: ", x)
        except ValueError:
            print("Invalid input") 

def password_guesser():
    conditional = True

    predefined_password = "oiesf"
    steps = 0
    print("Welcome to the password guesser game!")
    print("\n Try to guess the password. You will receive hints upon each guess")
    while conditional:
        steps = steps + 1
        try:
            password = input("Enter a password: ")
            if password == predefined_password:
                print("Correct Password on step: ", steps)
                conditional = False
            elif len(password) < len(predefined_password):
                print("Password is too short\n Steps: ", steps)
            elif len(password) > len(predefined_password):
                print("Password is too long\n Steps: ", steps)
            else:
                list1 = []
                print("password length is correct")
                for i in range(len(predefined_password)):
                    if password[i] != predefined_password[i]:
                        list1.append(i)
                print(f"Wrong character at position {list1}\nSteps:", steps)
        except ValueError:
            print("Invalid input")

def first(x):
    print("starting first")
    try:
        second(x)
    except:
        print("First An error occurred")
    print("ending first")

def second(x):
    print("starting second")
    try:
        third(x)
    except ValueError:
        print("Second An error occurred")
    print("ending second")

def third(x):
    print("starting third")
    if x < 0:
        x = 1/0
    elif x > 0:
        n = n + 1
    print("ending third")
# first(1)
                
# Exercise 4
'''
def prompt_equations():
    Conditional = True
    while Conditional:
        try:
            x = input("Enter an equation: ")
            x = x.split()
            new_list = []
            for i in x:
                if i == "(" or i == ")":
                    new_list.append(i)
                elif i.isdigit() or (i.replace('.', '', 1).isdigit() and i.count('.') < 2):
                    new_list.append(float(i) if '.' in i else int(i))
                elif i in ["+", "-", "*", "/"]:
                    new_list.append(i)
            print(new_list)
        except ValueError:
            print("Invalid input")

prompt_equations()
# retrying the function with a different approach
'''
def prompt_equations2():
    conditional = True
    while conditional:
        try:
            x = input("Enter an Equation (type 'Exit' to leave): ")
            print(x)
            if x.lower() == "exit":
                conditional = False
                print("Exiting...")
                continue
            result = eval(x)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except Exception as e:
            print(f"Invalid input: {e}")

prompt_equations2()
        