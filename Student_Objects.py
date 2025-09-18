#!/usr/bin/env python3

class Student:
    # constructor that initializes 4 attributes (self not included)
    def __init__(self, firstName, lastName, classification, major):
        self.firstName = firstName
        self.lastName = lastName
        self.classification = classification
        self.major = major
    
    # Method that displays the schedule
    def getClassSchedule(self):
        print("This method will print the class schedule for " + self.firstName + " " + self.lastName)

    # Method that displays the class credits
    def getClassCredits(self):
        print("This method will print the class credits for " + self.firstName + " " + self.lastName)
