#!/usr/bin/env python3

# display a welcome message
print("The Calculate Total program")
print()

# get input from the user
retail_price= float(input("Enter Retail Price:\t\t"))
quantity = float(input("Enter Quantity:\t"))


# calculate total
total = retail_price * quantity
            
# format and display the result
print()
print("Total is:\t\t" + str(total))
print()
print("Bye")
