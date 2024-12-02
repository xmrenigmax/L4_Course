# receives filename and number from user
# creates a reverse triangle shape using *

# function
def create_triangle(filename, length):
    with open(filename, 'w') as file:
        for i in range(length):
            file.write("*" * (length - i) + "\n")

# Test the function
print(create_triangle("triangle.txt", 5))