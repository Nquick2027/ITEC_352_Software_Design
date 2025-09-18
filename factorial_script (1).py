def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_even_or_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    # Variables and Data Types
    integer_var = 10
    float_var = 20.5
    string_var = "Hello, Python!"
    list_var = [1, 2, 3, 4, 5]
    tuple_var = (10, 20, 30)
    dict_var = {'name': 'Alice', 'age': 25}

    # Basic Input/Output
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}!")

    # Control Flow: If-Else
    number = int(input("Enter a number: "))
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    # Control Flow: Loops
    # For loop to iterate over a list
    print("List elements:")
    for item in list_var:
        print(item)

    # While loop to print numbers from 1 to 5
    print("Numbers from 1 to 5:")
    counter = 1
    while counter <= 5:
        print(counter)
        counter += 1

    # Function call
    fact_of_5 = factorial(5)
    print(f"The factorial of 5 is: {fact_of_5}")

    # Test the is_even_or_odd function
    test_number = 7
    result = is_even_or_odd(test_number)
    print(f"{test_number} is {result}.")

    print("Day 2 review completed!")

if __name__ == "__main__":
    main()
