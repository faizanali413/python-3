def convert_celsius_to_fahrenheit(celsius_list):
    """
    Converts a list of temperatures from Celsius to Fahrenheit.

    Parameters:
    - celsius_list (list): List of temperatures in Celsius.

    Returns:
    - list: List of temperatures converted to Fahrenheit.
    """
    fahrenheit_list = []  # Initialize an empty list for Fahrenheit temperatures
    index = 0  # Start with the first index

    # Use a while loop to iterate through the Celsius list
    while index < len(celsius_list):
        celsius = celsius_list[index]
        fahrenheit = (celsius * 9/5) + 32  # Convert Celsius to Fahrenheit
        fahrenheit_list.append(fahrenheit)  # Add the result to the Fahrenheit list
        index += 1  # Move to the next index

    return fahrenheit_list

# Example usage
def main():
    # Input list of temperatures in Celsius from the user
    input_temps = input("Enter temperatures in Celsius separated by spaces: ")
    
    # Convert the input string to a list of floats
    celsius_list = [float(temp) for temp in input_temps.split()]
    
    # Convert the list of Celsius temperatures to Fahrenheit
    fahrenheit_list = convert_celsius_to_fahrenheit(celsius_list)
    
    # Print the converted temperatures
    print("Temperatures in Fahrenheit:", fahrenheit_list)

# Run the program
if __name__ == "__main__":
    main()
