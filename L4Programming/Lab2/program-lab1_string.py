
"""
This program is to demonstrate the use of string in Python
@Author: Riley
@Date: 2024-10-08
"""

# @param: unit_name - the name of the unit
unit_name = "Level 4 programming"
#prints the unit name and the character at index
print(unit_name)
print(unit_name[0])
print(unit_name[0:5])
print(unit_name[8:])

# @param: greeting_string - greeting message
greeting_string = "Welcome to programming unit"
# prints the greeting message and the character at index
print(greeting_string)
# prints the first character of the string
print(greeting_string[0])
print(greeting_string[4])
# prints the first 5 characters of the string
print(greeting_string[0:5])
# prints the characters from index 4 to the end of the string
print(greeting_string[-4:])

def typeofvariable():
   # @param: a - float
   # @param: b - integer
   # @param: c - string
   # @param: d - boolean
   a = 11.0
   print(type(a)) 
   b = 11+11
   print(type(b)) 
   c = "c"
   print(type(c))
   d = True
   print(type(d))

typeofvariable()

def typeconversion():
   # @param: x - float
   x = 10.5
   # prints the type of the variable
   print(type(x))
   # converts the float to an integer
   print(int(x))
   # converts the float to a string
   print(str(x))
   # converts the float to a boolean
   print(float(x))

typeconversion()
def typelogic():
   x = "Look i will become the best python programmer"
   y = 10
   z = 5.5

   # data type of x
   print(type(x))
   # data type of y
   print(type(y))
   # data type of z
   print(type(z))
   #result and the data type of y+z
   print(y + z) 
   print(type(y + z))
   #result and the data type of y + int(z)
   print(y + int(z))
   print(type(y + int(z)))
   #result of z + float(y)
   print(z + float(y))
   print(type(z + float(y)))
   #data type of str(z)
   print(type(str(z)))
   #result and data type of x + str(y) + str(z)
   print(x + str(y) + str(z))
   print(type(x + str(y) + str(z)))
   #adding string to a number
   print(x + str(y))

typelogic()