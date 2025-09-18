#!/usr/bin/env python3

# There was a problem with the CSV file which prevented the code from working
# I think the error was when ChatGPT added the header to the csv file and I had to manually delete that
# That or there was a problem with the lines in the debugger itself. The current CSV is a new and cleaned file so it works

import csv

def Read_salaries():
    jobs = []
    try:
        with open("EntryLevelITSalaries.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                jobs.append(row)
    except FileNotFoundError:
        print('No EntryLevelITSalaries.csv file found. Starting with an empty jobs list')
    return jobs

def Display_salaries(jobs):
    print('Jobs & Salaries:')
    print('----------------')
    for jobs in jobs:
        print(jobs)

def Write_salaries(job, salary):
    with open('EntryLevelITSalaries.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(str(job), str(salary))

def main():
    print("The Entry Level IT Salary Application")
    print()

    salaries = Read_salaries() 
    Display_salaries(salaries)

    while True:
        print()
        answer = input('Would you like to add a another job? (Y,N): ')

        if answer == 'Y' or answer == 'y':
            try:
                job = input('Enter the job title: ')
                salary = int(input('Enter the salary (as an integer): '))
                Write_salaries(job, salary)
            except:
                print('Invalid Input!')
        elif answer == 'N' or answer == 'n':
            break


if __name__ == "__main__":
    main()