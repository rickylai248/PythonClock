from tkinter import *
from tkinter.ttk import *

from time import strftime

# File initialization testing statements
#msg = "Hello World"
#print(msg)
#

root = Tk();
root.title("PythonClock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Times", 24), background = "white", foreground = "black")
label.pack(anchor='center')
time()

mainloop()