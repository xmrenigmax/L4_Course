def exercise_list():
    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    print(my_list[-1])
    print(my_list[1:3])
    # add a new item at the end of the list with a number at the start of the list
    result = my_list[0]+my_list[-1]
    my_list.append(result)

def lists_tuples_sets():
    #create a list of 5 items with different data types
    my_list = [1, 2.0, "three", [4, 5], 1+2, 2]
    #prints list
    print(my_list)
    #adds an extra element to the end of the list
    my_list.append("six")
    #adds an element to the start of the list
    my_list.insert(0, "zero")
    #removes the last element of the list
    my_list.pop(-1)
    #finds the length of list
    print(len(my_list))
    #prints the value of the first item of your list
    print(my_list[0])
    #change the second element in list 
    my_list[1] = 2.5
    #verify data type of sequence
    print(type(my_list))
    #convert datatype to a tuple
    my_tuple = tuple(my_list)
    #verify data type of sequence
    print(type(my_tuple))
    #access the first value of tuple
    print(my_tuple[0])
    #find length of the tuple
    print(len(my_tuple))
    #change the value of the first item in tuple
    my_tuple[0] = 1000
    # create another tuple
    another_tuple = (1, 2, 3, 4, 5)
    #add both tuples together
    combined_tuple = my_tuple + another_tuple
    #print joined tuple
    print(combined_tuple)
    #convert the joined tuple into a list
    combined_list = list(combined_tuple)
    #verify data type of sequence
    print(type(combined_list))
    #convert your list to set
    my_set = set(combined_list)
    #find length of set
    print(len(my_set))
    #adds an element to set
    my_set.add(1000)
    #prints the set
    print(my_set)
    #adds another pre-existing element to set
    my_set.add(1)
    #prints the set (duplication is not allowed)
    print(my_set)
    #create another set
    another_set = {1, 2, 3, 4, 5}
    #find common elements between the two sets
    common_set = my_set.intersection(another_set)
    print(common_set)

def dictionary_exercise():
    #dictionary with key-value pairs for a car
    car_details = {"Car_make":"Toyota",
                "Car_model":"Corolla",
                "Car_year":2018,
                "Car_price":10000}
    #prints the dictionary
    print(car_details)
    #retrieves and prints the value associated with a specifc key
    make = car_details["car_make"]
    print(make)
    #modify the value associated with a key
    car_details["Car_price"] = 15000
    print(car_details)
    #adds a new key-value pair to the dictionary
    car_details["car_color"] = "red"
    print(car_details)
    #removes a key-value pair from the dictionary
    del car_details["color"]
    
