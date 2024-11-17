import math
def area(r):
    # receives radius as input and calculates the area of a circle
    output = math.pi * r ** 2
    return output

def sum_of_sequence(n):
    # sn = n/n+1
    while n > 1: 
        for i in range(n):
            n = n/(n+1)
    return n

            

print(sum_of_sequence(3))
