import numpy as np
import matplotlib.pyplot as plt
array = []
def sum_of_random_integers():
    for i in range(6):
        integer_random = np.random.randint(50)
        print(integer_random)
        # Add random number to the list
        array.append(integer_random)
        # Calculate the sum of the list
        total_sum = sum(array)
        print(total_sum)
sum_of_random_integers()

