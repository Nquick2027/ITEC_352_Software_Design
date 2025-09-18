#!/usr/bin/env python3
# Nathan Quick
# 02/10/2025
import csv

def read_trips():
    trips = []
    try:
        with open('trips.csv', mode = 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                trips.append(row)
    except FileNotFoundError:
        print('No trips file found. Starting with an empty trips list')
    return trips

def write_trips(trips):
    with open('trips.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def list_trips(trips):
    print('Trips:   ')
    print('---------')
    for trip in trips:
        print(trip)

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    trips = read_trips() 
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        singleTrip = []
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        singleTrip = [miles_driven, gallons_used, mpg]   
        trips.append(singleTrip)

        more = input("More entries? (y or n): ")
    
    write_trips(trips)
    print("Bye")

if __name__ == "__main__":
    main()

