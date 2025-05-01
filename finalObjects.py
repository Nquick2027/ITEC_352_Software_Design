#!/usr/bin/env/python3

# Importing the dataclass decorator for creating simple data structures
from dataclasses import dataclass

# Define the Employee class using the @dataclass decorator
@dataclass
class Employee:
    employeeID: int
    fname: str
    lname: str
    position: str

# Define the Attendance class using the @dataclass decorator
@dataclass
class Attendance:
    attendanceID: int
    employeeID: int
    date: str
    clockIn: int
    clockOut: int = None