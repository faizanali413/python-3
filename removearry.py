def remove_odds(arr):
    """
    Removes all odd numbers from the array.

    Parameters:
    - arr (list): The array of numbers.

    Returns:
    - list: The modified array with no odd numbers.
    """
    # Use list comprehension to filter out odd numbers
    arr = [num for num in arr if num % 2 == 0]
    return arr

# Example usage
numbers = [10, 15, 20, 25, 30, 35, 40]
print("Original array:", numbers)

# Remove odd numbers
numbers = remove_odds(numbers)
print("Array after removing odd numbers:", numbers)
