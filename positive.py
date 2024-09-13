def factorial(n):
    """
    Calculates the factorial of a positive integer using a while loop.
    
    Parameters:
    - n (int): A positive integer for which to calculate the factorial.
    
    Returns:
    - int: The factorial of the input number.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    counter = n
    
    while counter > 0:
        result *= counter  
        counter -= 1       
    
    return result

number = int(input("enter the factorial number :"))
print(f"Factorial of {number} is: {factorial(number)}")  
