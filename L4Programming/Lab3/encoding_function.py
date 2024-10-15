def encoding_function(message_in_number):
    """
    2. **Part B (Encoding the message)**:
       - The function takes a string of numbers (e.g., "2 0 5 4"), splits it into individual numbers, and converts each number into its corresponding letter using the dictionary created in Part A.
       - If a number is not found in the dictionary, the function prints an error message.
       - The encoded message is then printed and returned.

    Parameters:
    ----------
    message_in_number : str
        A string of space-separated numbers that represent the message to be encoded. Each number should correspond to a letter as per the mapping defined in Part A.

    Returns:
    -------
    str:
        The encoded message constructed by mapping each number to its corresponding letter.

    Example:
    --------
    encoded_message = encoding_function(" 1 2 3 4")
    print(encoded_message)
    
    
    Note:
    -----
    - The function expects the `my_dict` variable to be properly set up in Part A by the user.
    - If a number is not found in the `my_dict`, the function will print an error message and skip that number.
    """
    '''************************************************PART A************************************************************************'''
    # Complete the function implementation in Part A only.
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    
    my_dict = dict(zip(num_list, alphabet_list))

    '''************************************************PART B************************************************************************'''
    numbers = message_in_number.split()
    result = ""
    for number in numbers:
        num = int(number)
        if num in my_dict:
            result += my_dict[num]
        else:
            print("The numbers/alphabets are not in the range")

    print(f"The encoded message is: {result}")

    return result
# # Example usage:
#encoding_function("2 0 5 4")  # Uncomment to test the function
