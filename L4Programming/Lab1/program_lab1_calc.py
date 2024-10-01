def Greetings():
    
    """"
    Methods:
    1. Using the built-in print() function.
    2. Using a function to encapsulate the print statement.
    3. Using variable names to store the message.
    4. Using a lambda function to print the message.
    5. Using end= at the end of the print statement.
    6. Seperating intergers from strings
    """
        # Method 1: Using the built-in print() function
    print("Hello, World! x1 ")

        # Method 2: Using a function to encapsulate the print statement
    def print_hello():
        print("Hello, World!")
    print_hello()

        # Method 3: using variable names to store the message
    name = "User"
    age = 20
        #without using f-string
    print("Hello, " + name + "! You are " + str(age) + " years old.")
        #using f-string
    print(f"Hello, {name}! You are {age} years old.")
        #using format()
    print("Hello, {}! You are {} years old.".format(name, age))

        # Method 4: Using a lambda function to print the message
    hello_lambda = lambda: print("Hello, World!")
    hello_lambda()

        # Method 5: using end= at the end of the print statement
    print("Hello, ", end="")
    print("World!")

        # Method 6: seperating intergers from strings
    print("Hello", "World", 2024)

def calculator():
    def operatorExplainedd():
        # addition (adding two numbers using the + operator)
        print(265+5924)
        # subtraction (subtracting two numbers using the - operator)
        print(5022-901)
        # multiplication (multiplying two numbers using the * operator)
        print(5*10)
        # division (dividing two numbers using the / operator)
        print(604/4)
        # modulus (getting the remainder of the division of two numbers using the % operator)
        print(3%2)
        # exponentiation (raising a number to a power using the ** operator)
        print(4**3)
        print(5**2)
        # floor division (getting the quotant of the division of two numbers using the // operator)
        print(9//3)
        print(8//3)
    operatorExplainedd()

    #assigning values to variables
    x = 5
    y = 123
    result = x + y
    print(x, "+", y, "=", result)

    #variable assignment for mathematical operations
    a = 6
    b = 4
    c = 5
    d = 2
    e = 3
    print((a * b)+(c**d)-(b%e))


Greetings()
calculator()