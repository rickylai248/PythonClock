from tkinter import *
# https://docs.python.org/3/library/tkinter.html#:~:text=The%20tkinter%20package%20(%E2%80%9CTk%20interface,it%20is%20maintained%20at%20ActiveState.)
from tkinter.ttk import *

from time import strftime

# File initialization testing statements
#msg = "Hello World"
# print(msg)
#

root = Tk();
# https://docs.python.org/3/library/tkinter.html
root.title("PythonClock")

def time():
    string = strftime('%H:%M:%S %p')
    # time formatting
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Times", 24), background = "white", foreground = "black")
label.pack(anchor='center')
time()

mainloop()
# calls mainloop() once when ready for application to run
# similar to while True: statement
#while True:
#    event=wait_for_event()
#    event.process()
#    if main_window_has_been_destroyed(): 
 #       break