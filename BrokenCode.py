# # Nathan Quick
# # Broken Code

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# num1 = int(num1)
# num2 = string(num2)

# print("The sum is: " +str(num1 + num2))

# print("The difference is: " +str(num1 - num2))
# print("The difference is also: " +str(num2 - num1))

# print("The product is: " +str(num1 * num2))

# print("The quotient is: " +str(num1 / num2))
# print("The quotient is also: " +str(num2 * num1))

# print()


# display a welcome message

print("The Test Scores program")

print()

print("Enter 3 test scores")

print("======================")



# get scores from the user

total_score = 0   # initialize the variable for accumulating scores

total_score += int(input("Enter test score: ")) # Fixed total_scre which was undefined variable

total_score += int(input("Enter test score: ")) # Fixed .input which is a syntax error

total_score += int(input("Enter test score: "))



# calculate average score

average_score = round(total_score / 3)

       

# format and display the result

print("======================")

print("Total Score: ", total_score,

   "\nAverage Score:", average_score) # Fixed averagescore which is an undefined variable

print()

print("Bye")