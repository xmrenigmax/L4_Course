
def reverse_list(my_list):
    """
    Reverse the values in a list containing exactly two numbers.

    Input:
    lst (list): A list containing exactly two numbers.

    Returns:
    list: The list with its two values swapped.
    
    Example:
    --------
    >>> reverse_list([5, 10])
    [10, 5]

    """
   
    # Reverse the values in the list
    # Complete your code here...
    my_list[0], my_list[1] = my_list[1], my_list[0]
    
    return my_list
