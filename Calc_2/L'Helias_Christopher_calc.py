# Author: Christopher L'Helias
# Date: 5/22/23
# Description: This program function as a calculator. It has an add function will can be used to add 2 numbers selected by the user. 
# It has a subtract function that can be used to subract two numbers selected by the user. It has a check_float function that asks the user to will ask the user to enter an intege. 
# The function will then try to convert the user's input into a float and return it. If there is an error in doing that, then print to please enter a integer. 
# It also has a multiplication function that will get the product of two numbers selected by the user. It also has a divide function that will divide to numbers, selected by the user, 
# and get the result. For both the divide and multiplication function, the check_float function is used to check that the numbers the user inputs are valid floats. 
# It also has an exponent function that will ask the user to enter a base and a power and return the result. It also has a sum function that will create a list, 
# ask the user to enter numbers for said list, and will allow the user to see the sum of all the numbers in the list. It also has a max function that will create a list, 
# allow users to enter numbers into the list, and allow the user to see the highest number in the list. The program will ask the user what they would like to do and respond accordingly. 
# The check_float function is used periodically throughout the code to check that the user's inputs are valid floats. 
# Challenges: 
# Exponent Function
# Max Function
# Main Function calls all of my functions
# Radical Function
# Bugs: None
# Source: https://realpython.com/python-square-root-function/

import math # Import math module

def add(number_1, number_2): # Define function to do addition
    print(number_1 + number_2) # Print the sum of the user's two numbers
def subtract(number_1, number_2): # Define function to do subtraction
    return number_1 - number_2 # Return the difference between the user's two numbers
def check_float(): # Define a function that will check that the user's input is a valid float
    while True: # Creates loop
        number = input("Please enter an integer") # The variable number is equal to the user's input on what integer they would like

        try: # try
            return float(number) # converting the user's input into a float and returning it.
        except ValueError: # If an error occurs
            print("Please enter a valid integer") # Tell the user to enter a valid float

def multiply(): # Define function to multiply
    number_1 = check_float() # Gets the first number and checks that it is a valid float
    number_2 = check_float() # Gets the second number and checks that it is a valid float
    return(number_1 * number_2) # Return the product of both numbers
def divide(): # Define a function to divide
    number_1 = check_float() # Gets the numertor and checks that it is a valid float
    number_2 = check_float() # Gets the  denominator and checks that it is a valid float
    return(number_1 / number_2) # return the result 
def exponent(): # Define a function to find the answer to a number with a certain exponent
    base = check_float() # Gets the base and checks that it is a valid float
    power = check_float() # Gets the power and checks that it is a valid float
    return base ** power # Return the result of the base and exponent
def sum(numbers): # Define a function to get the sum of many numbers
    total = 0 # The total starts off at 0
    for number in numbers: # Check each number in the list
        total += number # Add each number to the total
    return total # return the total 
def max(numbers): # Define a function that finds the highest number in a list
    if len(numbers) == 0: # If the list has no numbers
        print("The list has no numbers") # Print that the list has no numbers
        return None # Return none because there is no max
    max_num = numbers[0] # Start the max number as the first number in the list
    for number in numbers: # Check each number in the list
        if number > max_num: # If the current number is greater than the max number
            max_num = number # Set the current number as the max number
    return max_num # Return the max number
def radical(): # Define a function to get square roots
    root_num = check_float() # Get the float of a integer the user enters
    print(math.sqrt(root_num)) # Get the square root of the user's number
def main(): # Define the main function

    while True: # Create loop
        functions = input("What would you like to do: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Sum, 6. Exponent, 7. Max, 8. Square Root, 9. Stop the Program.") # Ask the user what they would like to do
        if functions == "1": # If user input equals 1 
            number_1 = check_float() # Get the first number and check that it is a valid float
            number_2 = check_float() # Get the second number and check that it is a valid float
            add(number_1, number_2) # Add the two numbers
        elif functions == "2": # Else if the user's input equals 2
            number_1 = check_float() # Get the first number and check that it is a valid float
            number_2 = check_float() # Get the second number and check that it is a valid float
            print(subtract(number_1, number_2)) # Print the difference between the two numbers
        elif functions == "3": # Else if the user's input equals 3 
            print(multiply()) # Print and go through the multiply function
        elif functions == "4": # Else if user's input is equal to 4
            print(divide()) # Divide the user's two numbers and print the result
        elif functions == "5": # Else if the user's input is equal to 5
            numbers = [] # Create an empty list called numbers
            while True: # Create loop
                print(f"Current list is {numbers}") # Print the current list
                new_num = input("Enter a new number for the list or 'sum' to sum it.") # new_num is equal to the user's input to "Enter a new number for the list or 'sum' to sum it."
                if new_num == 'sum': # if user's inpit is equal to sum
                    break # End the loop
                try: # Try
                    numbers.append(float(new_num)) # Converting the user's input to a float and adding it to the numbers list
                except: # Except 
                    print("Invalid try again") # Tell the user their input is invalid and to try again
            print(sum(numbers)) # Print the sum of all the numbers in the list
        elif functions == "6": # Else if the user's input is equal to 6
            print(exponent()) # Get the base and exponent the user wants and print the result
        elif functions == "7": # Else if the user's input equals 7
            numbers = [] # Create an empty list called numbers
            while True: # Create loop
                print(f"Current list is {numbers}") # Print the current list of numbers
                new_num = input("Enter a new number for the list or 'max' to find the maximum number.") # New_num is equal to the user's input to "Enter a new number for the list or 'max' to find the maximum number."
                if new_num == 'max': # If user's input is equal to max
                    break # Break the loop
                try: # Try
                   numbers.append(float(new_num)) # Convert the input to a float and add it to the list
                except: # Except if an error occurs
                    print("Invalid try again") # print that the user's input is invalid
            max_num = max(numbers) # Find the max number in the list
            if max_num is not None: # If there is a max number
                print(f"The maximum number is {max_num}") # Print the max number
        elif functions == "8": # Else if user's input is 8
            radical() # Run the radical function
        elif functions == "9": # Else if the user's input is 8
            print("Stopping...") # Print that the program is stopping
            break # End program
        else: # else
            print("Invalid try again") # Tell the user their input is invalid
main() # Call main
