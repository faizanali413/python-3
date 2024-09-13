def insert_value(array, index, value):
    """
    Inserts a value at the specified index in the array and returns the modified array.

    Parameters:
    - array (list): The list to insert the value into.
    - index (int): The index at which to insert the value.
    - value (any): The value to insert into the array.

    Returns:
    - list: The modified array with the value inserted.
    """
    # Insert the value at the specified index
    array.insert(index, value)
    return array
my_list = [1, 2, 3, 4]
new_list = insert_value(my_list, 2, 99)
print(new_list)  