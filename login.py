from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x300')

# Title of the Website 
Label(root, text ="              Gym Barcode               ", font='arial 15 bold').grid(row=0, column=5)

# Labels of entrys for login 
username = Label(root, text= '  Username  ')
password = Label(root, text= '  Password ')

# Label postions 
username.grid(row=1, column=5)
password.grid(row=2, column=5)

# Variables
usernamevalue = StringVar
passwordvalue = StringVar

usernameentry = Entry(root, textvariable = usernamevalue)
passwordentry =  Entry(root, textvariable = passwordvalue)

# Entrybox for inputs
usernameentry.grid (row=1, column= 3)
passwordentry.grid(row=2, column= 3)


root.mainloop()
