# Nathan Quick
# 01/27/2025
# Original Code Source: https://www.geeksforgeeks.org/make-simple-calculator-using-python/

# Python program for a simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2  # Returns the sum of num1 and num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2  # Returns the difference of num1 and num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2  # Returns the product of num1 and num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2  # Returns the result of dividing num1 by num2

# Print menu of operations for the user to choose from
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

# Prompt user to select an operation
select = int(input("Select operations from 1, 2, 3, 4 :"))

# Prompt user to input the first number
number_1 = int(input("Enter first number: "))

# Prompt user to input the second number
number_2 = int(input("Enter second number: "))

# Check which operation the user selected and perform the corresponding calculation
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))  # Calls the add function if selected 1

elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))  # Calls the subtract function if selected 2

elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))  # Calls the multiply function if selected 3

elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))  # Calls the divide function if selected 4

else:
    print("Invalid input")  # Prints a message if the user selects an invalid option