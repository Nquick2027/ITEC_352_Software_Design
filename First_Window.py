import tkinter as tk
from tkinter import ttk

def click_button1():
    root.title("You clicked the button 1")

def click_button2():
    root.title("You clicked the button 2")


root = tk.Tk()
root.title("Future Value Calculator")
root.geometry("300x200")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

investmentLabel = ttk.Label(frame, text="Monthly Investment")
investmentLabel.pack()

# Below is a way to make the label in one line
# ttk.Label(frame, text="Monthly Investment").pack()

investmentText = tk.StringVar()
investmentEntry = ttk.Entry(frame, width=25, textvariable= investmentText)
investmentEntry.pack()

button1 = ttk.Button(frame, text="Click Me!", command=click_button1)
button1.pack()

button2 = ttk.Button(frame, text="No, click me!", command=click_button2)
button2.pack()

root.mainloop()


