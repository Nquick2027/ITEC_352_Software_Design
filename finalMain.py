#!/usr/bin/env/python3

# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
import finalDB
from finalObjects import Attendance

# Function to connect to the database and display a success or error message
def connect_to_db():
    try:
        finalDB.connect()
        messagebox.showinfo("Success", "Connected to the database!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to the database: {e}")

# Function to populate a Combobox with employee names from the database
def populate_combobox(combobox):
    try:
        finalDB.connect()
        names = finalDB.get_Names()  # Fetch a list of concatenated first and last names
        combobox['values'] = names
    except Exception as e:
        messagebox.showerror("Error", f"Failed to populate Combobox: {e}")

# Function to populate a Treeview with employee details based on the selected name
def populate_treeview(treeview, selected_name):
    """Populate the Treeview with employee details based on the selected name."""
    try:
        finalDB.connect()
        employees = finalDB.get_Employees()

        # Clear the Treeview before adding new data
        for row in treeview.get_children():
            treeview.delete(row)

        # Filter employees by the selected name and insert matching rows into the Treeview
        for employee in employees:
            full_name = f"{employee.fname} {employee.lname}"
            if full_name == selected_name:
                treeview.insert("", "end", values=(employee.employeeID, employee.fname, employee.lname, employee.position))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to populate Treeview: {e}")

# Function to log attendance (clock-in or clock-out) for the selected employee
def log_attendance(selected_name, hour, minute, date, clock_out=False):
    """Log attendance for the selected employee."""
    try:
        finalDB.connect()
        # Split the selected name into first and last name
        first_name, last_name = selected_name.split(" ")
        # Fetch the employee object by name
        employee = finalDB.get_Employee_By_Name(first_name, last_name)

        if employee:
            if clock_out:
                # Update the clock-out time for the employee if the date matches
                finalDB.update_Attendance_ClockOut(employee.employeeID, date, f"{hour}:{minute}")
                messagebox.showinfo("Success", "Clock-out time updated successfully!")
            else:
                # Log a new clock-in attendance record
                attendance = Attendance(
                    attendanceID=0,  # Auto-incremented by the database
                    employeeID=employee.employeeID,
                    date=date,
                    clockIn=f"{hour}:{minute}"
                )
                finalDB.log_Attendance(attendance)
                messagebox.showinfo("Success", "Clock-in time logged successfully!")
        else:
            messagebox.showerror("Error", "Employee not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to log attendance: {e}")

# Main function to set up the GUI
def main():
    root = tk.Tk()
    root.title("Employee Attendance System")  # Set the window title

    # Function to close the database connection when the application exits
    def on_closing():
        finalDB.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the close event to the on_closing function

    # Create frames for organizing the layout
    dataFrame = ttk.Frame(root)
    dataFrame.pack()
    displayFrame = ttk.Frame(root)
    displayFrame.pack()
    selectionFrame = ttk.Frame(root)
    selectionFrame.pack()

    # Label and Combobox for selecting employee names
    attendanceLabel = tk.Label(dataFrame, text="Attendance Log")
    attendanceLabel.grid(row=0, column=1, padx=10, pady=10)
    combobox_var = tk.StringVar(value="-- Select Your Name --")
    namesCombobox = ttk.Combobox(dataFrame, textvariable=combobox_var, state="readonly")
    namesCombobox.grid(row=1, column=1, padx=10, pady=10)

    # Populate the Combobox with employee names
    populate_combobox(namesCombobox)

    # Set the default selection if there are values in the Combobox
    if namesCombobox['values']:
        namesCombobox.current(0)

    # Labels and input fields for hour, minute, and date
    hourLabel = tk.Label(dataFrame, text="Hour:")
    hourLabel.grid(row=2, column=0, padx=10, pady=10)
    dateLabel = tk.Label(dataFrame, text="Date:")
    dateLabel.grid(row=2, column=1, padx=10, pady=10)
    minuteLabel = tk.Label(dataFrame, text="Minute:")
    minuteLabel.grid(row=2, column=2, padx=10, pady=10)

    hourSpin = tk.Spinbox(dataFrame, from_=0, to=23, width=2)  # Spinbox for hour input
    hourSpin.grid(row=3, column=0, padx=10, pady=10)
    dateField = tk.Text(dataFrame, height=1, width=10)  # Text field for date input
    dateField.grid(row=3, column=1, padx=10, pady=10)
    dateField.insert(tk.END, "MM-DD-YYYY")  # Placeholder text for the date field
    minuteSpin = tk.Spinbox(dataFrame, from_=0, to=60, width=2)  # Spinbox for minute input
    minuteSpin.grid(row=3, column=2, padx=10, pady=10)

    # Treeview for displaying employee details
    treeview = ttk.Treeview(displayFrame, columns=("ID", "First Name", "Last Name", "Position"), show="headings")
    treeview.heading("ID", text="Employee ID")
    treeview.heading("First Name", text="First Name")
    treeview.heading("Last Name", text="Last Name")
    treeview.heading("Position", text="Position")
    treeview.pack(padx=10, pady=10)

    # Event binding for Combobox selection to populate the Treeview
    def on_combobox_select(event):
        selected_name = combobox_var.get()
        if selected_name != "-- Select Your Name --":
            populate_treeview(treeview, selected_name)

    namesCombobox.bind("<<ComboboxSelected>>", on_combobox_select)

    # Buttons for clocking in and clocking out
    clockInButton = tk.Button(selectionFrame, text="Clock In", command=lambda: log_attendance(combobox_var.get(), hourSpin.get(), minuteSpin.get(), dateField.get("1.0", tk.END).strip()))
    clockInButton.grid(row=0, column=0, padx=10, pady=10)
    clockOutButton = tk.Button(selectionFrame, text="Clock Out", command=lambda: log_attendance(combobox_var.get(), hourSpin.get(), minuteSpin.get(), dateField.get("1.0", tk.END).strip(), clock_out=True))
    clockOutButton.grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()  # Start the Tkinter event loop

# Executes the main fuction, starting the application
if __name__ == '__main__':
    main()