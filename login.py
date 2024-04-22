from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x300')

Label(root, text ="Gym Barcode", font='arial 15 bold').grid(row=0, column=3)

username = Label(root, text='Username')
password = Label(root, text='Password')
barcode = Label(root, text='Barcode')

username.grid(row=1,column=2)
password.grid(row=2,column=2)
barcode.grid(row=3,column=2)

root.mainloop()
