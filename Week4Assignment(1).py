#!/usr/bin/env python3
# Nathan Quick
# 02/10/2025
# Used ChatGPT for aid since I couldn't get the reader to work

# Importing the csv module to read and write CSV files
import csv

# Function to read salaries from the CSV file
def Read_salaries():
    jobs = []  # Initialize an empty list to store job data
    try:
        # Attempt to open the CSV file in read mode with UTF-8 encoding
        # The encode="UTF-8" changes the string values to Unicode Transformation Format 8, removing the need to convert the string later
        with open("EntryLevelITSalaries.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)  # Create a CSV reader object
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two columns (job title and salary)
                    jobs.append(row)  # Add the row to the jobs list
    except FileNotFoundError:
        # Handle case where the file does not exist
        print('No EntryLevelITSalaries.csv file found. Starting with an empty jobs list.')
    return jobs  # Return the list of jobs (can be empty if file is not found)

# Function to write salaries to the CSV file
def Write_salaries(jobs):
    # Open the CSV file in write mode to overwrite existing content
    with open("EntryLevelITSalaries.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)  # Create a CSV writer object
        writer.writerows(jobs)  # Write the entire jobs list to the file
    print("Salaries have been successfully saved.")  # Confirmation message

# Function to display the salaries in a formatted table
def Display_salaries(jobs):
    if not jobs:  # Check if the jobs list is empty
        print("No job salary records found.")  # Inform the user if there are no records
        return

    # Print the header for the salary table
    print(f"{'Job Title':<25}{'Salary ($)'}")
    print("-----------------------------------")
    
    for job in jobs:  # Loop through each job record in the list
        job_title, salary = job[:2]  # Extract the job title and salary (first two elements)
        print(f"{job_title:<25}{salary}")  # Print job title and salary

# Main function to run the program
def main():
    print("The Entry Level IT Salary Application\n")  # Display the program title

    # Read existing salary data from the file
    salaries = Read_salaries()
    # Display the current salaries in the table
    Display_salaries(salaries)

    # Ask user if they want to add a new salary entry
    while True:
        add_entry = input("\nWould you like to add a new job entry? (y/n): ").strip().lower()
        if add_entry == "y":  # User wants to add a new entry
            job_title = input("Enter job title: ")  # Prompt for job title
            salary = input("Enter salary: ")  # Prompt for salary
            if job_title and salary.isdigit():  # Ensure salary is numeric and job title is not empty
                salaries.append([job_title, salary])  # Add the new entry to the list
            else:
                print("Invalid input. Please enter a valid job title and numeric salary.")  # Error message for invalid input
        elif add_entry == "n":  # User does not want to add a new entry
            break  # Exit the loop
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")  # Error message for invalid choice

    # Write the updated list of salaries back to the file
    Write_salaries(salaries)
    print("\nThank you for using this program!")  # Thank you message to the user

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to run the program