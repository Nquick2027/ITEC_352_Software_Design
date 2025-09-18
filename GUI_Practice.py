import tkinter as tk
from tkinter import ttk

# How to create an empty root window
root = tk.Tk()

root.title("Future Value Calculator")
root.geometry("300x200")

# mainloop displays the root window to the user
root.mainloop()

# How to add a frame to the root window
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

# Create two buttons and add them to the frame
button1 = ttk.Button(frame, text="Clicke Me!")
button2 = ttk.Button(frame, text="No, click me!")

button1.pack()
button2.pack()
