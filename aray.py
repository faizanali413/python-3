# Function to remove negative numbers from the array
def remove_negatives(arr):
    """
    Removes negative numbers from the array.

    Parameters:
    - arr (list): The array of numbers.

    Returns:
    - list: The modified array with no negative numbers.
    """
    # Use list comprehension to filter out negative numbers
    arr = [num for num in arr if num >= 0]
    return arr

# Example usage
numbers = [12, -7, 5, -3, 9, -1, 0, 4]
print("Original array:", numbers)

# Remove negative numbers
numbers = remove_negatives(numbers)
print("Array after removing negatives:", numbers)
