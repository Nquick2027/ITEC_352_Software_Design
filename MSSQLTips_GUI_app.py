import tkinter
from tkinter import ttk
import MSSQLTips_GUI_backend as backend

root = tkinter.Tk()
root.title('MSSQLtips Finance')
# root.iconbitmap('SQLtips.ico')

greeting_frame = tkinter.Frame(root)
textbox_frame = tkinter.Frame(root)
radio_frame = tkinter.LabelFrame(root, text='Select a dataset')
combobox_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
treeview_frame = tkinter.Frame(root)

greeting_frame.pack()
textbox_frame.pack()
radio_frame.pack()
combobox_frame.pack()
button_frame.pack()
treeview_frame.pack()

greeting_label = tkinter.Label(greeting_frame, text= "Welcome to MSSQLTips")
greeting_label.pack()

entry_label = tkinter.Label(textbox_frame, text='Stock Ticker Symbol:')
greeting_label.config(text='Please Enter Stock Ticker Symbol:')
text_entry = tkinter.Entry(textbox_frame)
initial_value = 'GOOG'
text_entry.insert(0, initial_value)
text_entry.delete(0, tkinter.END)
text_entry.insert(0, 'AAPL')
text_entry.get()
text =  tkinter.StringVar(textbox_frame)
text_entry = tkinter.Entry(textbox_frame, textvariable = text)
text.set('GOOG')
text.get()

entry_label.grid(row=0, column=0)
text_entry.grid(row=0, column=1)
number = tkinter.IntVar()
number.set(1)
radio_historical_data = tkinter.Radiobutton(radio_frame, 
                                            text = 'Historical Data', 
                                            value = 1, 
                                            variable = number)
radio_institutional_holders = tkinter.Radiobutton(radio_frame, 
                                                  text='Institutional Holders', 
                                                  value=2, 
                                                  variable = number)
radio_historical_data.grid(row=0, column=0)
radio_institutional_holders.grid(row=0, column=1)

period_label = tkinter.Label(combobox_frame, text='Period:')
period_combobox = ttk.Combobox(combobox_frame, value=['1d','5d','1mo'], state="readonly")
interval_label = tkinter.Label(combobox_frame, text='Interval:')
interval_combobox = ttk.Combobox(combobox_frame, value=['15m','30m','1h'], state="readonly")
period_combobox.current(0)
interval_combobox.current(0)
period_label.grid(row=0, column=0)
period_combobox.grid(row=0, column=1)
interval_label.grid(row=0, column=2)
interval_combobox.grid(row=0, column=3)

period = period_combobox.get()
interval = interval_combobox.get()


text_entry.bind("<ButtonPress-1>", lambda event, initial_message = initial_value: backend.entry_click(event, initial_value))

get_button = tkinter.Button(button_frame, 
                            text = "Get Data",
                            command = lambda:backend.get_data(tree, text_entry, number, period_combobox, interval_combobox))
get_button.pack()

columns = ['col0','col1','col2']
default_headings = ['Datetime', 'Open', 'Close']
tree = ttk.Treeview(treeview_frame, columns = columns, show = 'headings')
for index, col in enumerate(columns):
    tree.column(col, width = 100, anchor = 'center')
    tree.heading(col, text=default_headings[index])
scrollbar = ttk.Scrollbar(treeview_frame, orient = tkinter.VERTICAL, command = tree.yview)
tree.configure(yscroll = scrollbar.set)
tree.grid(row = 0, column = 0)
scrollbar.grid(row = 0, column = 1)
dataset = [['2023-02-14','45.23', '42.65'],
           ['2023-02-15','42.70', '48.92'],
           ['2023-02-16','22.46', '20.98']
           ]
for index in range(len(dataset)):
    tree.insert('', tkinter.END, values=dataset[index])

radio_historical_data = tkinter.Radiobutton(radio_frame, 
                                            text = 'Historical Data', 
                                            value = 1, 
                                            variable = number,
                                            command = lambda:backend.make_selection(tree, number, period_combobox, interval_combobox))
radio_institutional_holders = tkinter.Radiobutton(radio_frame, 
                                                  text='Institutional Holders', 
                                                  value=2, 
                                                  variable = number,
                                                  command = lambda:backend.make_selection(tree, number, period_combobox, interval_combobox))


root.mainloop()