def sum_array(arr):
    """
    Calculates the sum of all numbers in the array using a while loop.
    
    Parameters:
    - arr (list): The array of numbers.
    
    Returns:
    - int: The sum of all numbers in the array.
    """
    total = 0  
    index = 0 
    
   
    while index < len(arr):
        total += arr[index]  
        index += 1           
    
    return total

numbers = [1, 2, 3, 4, 5]
print("Sum of array:", sum_array(numbers)) 
