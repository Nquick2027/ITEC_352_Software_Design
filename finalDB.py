#!/usr/bin/env/python3

# Import necessary libraries
import sqlite3
from contextlib import closing
from finalObjects import Employee, Attendance

# Global variable to hold the database connection
conn = None

# Function to establish a connection to the database
def connect():
    global conn
    if not conn:  # If no connection exists, create one
        DB_FILE = r"C:\Users\crims\OneDrive\Documents\ITEC352 Software Design\Final_Project\employees.db"
        conn = sqlite3.connect(DB_FILE)  # Connect to the SQLite database
        conn.row_factory = sqlite3.Row  # Enable access to rows as dictionaries

# Function to close the database connection
def close():
    if conn:  # If a connection exists, close it
        conn.close()

# Function to retrieve the first and last names of all employees
def get_Names():
    query = '''SELECT FIRST_NAME, LAST_NAME FROM Employees'''  # SQL query to fetch names
    with closing(conn.cursor()) as c:  # Use a context manager to ensure the cursor is closed
        c.execute(query)  # Execute the query
        results = c.fetchall()  # Fetch all results
    # Return a list of full names (first name + last name)
    return [f"{row['FIRST_NAME']} {row['LAST_NAME']}" for row in results]

# Function to retrieve all employee details
def get_Employees():
    query = '''SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, POSITION FROM Employees'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    # Return a list of Employee objects created from the query results
    return [Employee(row["EMPLOYEE_ID"], row["FIRST_NAME"], row["LAST_NAME"], row["POSITION"]) for row in results]

# Function to log an employee's clock-in attendance
def log_Attendance(attendance):
    query = '''
        INSERT INTO Attendance (EMPLOYEE_ID, DATE, CLOCK_IN)
        VALUES (?, ?, ?)
    '''  # SQL query to insert a new attendance record
    with closing(conn.cursor()) as c:  # Use a context manager to ensure the cursor is closed
        # Execute the query with the provided attendance data
        c.execute(query, (attendance.employeeID, attendance.date, attendance.clockIn))
        conn.commit()  # Commit the transaction to save changes

# Function to retrieve an employee's details by their first and last name
def get_Employee_By_Name(first_name, last_name):
    query = '''
        SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, POSITION
        FROM Employees
        WHERE FIRST_NAME = ? AND LAST_NAME = ?
    '''  # SQL query to fetch an employee by name
    with closing(conn.cursor()) as c:
        c.execute(query, (first_name, last_name))
        result = c.fetchone()  # Fetch a single result
    if result:  # If a result is found, return an Employee object
        return Employee(result["EMPLOYEE_ID"], result["FIRST_NAME"], result["LAST_NAME"], result["POSITION"])
    return None  # Return None if no employee is found

# Function to update an employee's clock-out time for a specific date
def update_Attendance_ClockOut(employee_id, date, clock_out_time):
    query = '''
        UPDATE Attendance
        SET CLOCK_OUT = ?
        WHERE EMPLOYEE_ID = ? AND DATE = ?
    '''  # SQL query to update the clock-out time
    with closing(conn.cursor()) as c:
        c.execute(query, (clock_out_time, employee_id, date))
        conn.commit()

# Function to retrieve all attendance records for a specific employee
def get_Attendance_By_Employee(employee_id):
    query = '''
        SELECT ATTENDENCE_ID, EMPLOYEE_ID, DATE, CLOCK_IN, CLOCK_OUT
        FROM Attendance
        WHERE EMPLOYEE_ID = ?
    '''  # SQL query to fetch attendance records for an employee
    with closing(conn.cursor()) as c:
        c.execute(query, (employee_id,))
        results = c.fetchall()
    # Return a list of Attendance objects created from the query results
    return [Attendance(row["ATTENDENCE_ID"], row["EMPLOYEE_ID"], row["DATE"], row["CLOCK_IN"], row["CLOCK_OUT"]) for row in results]