from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x300')

def getvals():
    print("Accepted")

#Title of the website
Label(root, text ="              Gym Barcode              ", font='arial 15 bold').grid(row=0, column=3)
#Labels of the entrys
firstname = Label(root, text= ' First Name')
lastname = Label (root, text= 'Last Name')
username = Label(root, text='  Username ')
password = Label(root, text='  Password ')
barcode = Label(root, text='   Barcode ')
#The positions of the labels
firstname.grid(row=1,column=2)
lastname.grid(row=2,column=2)
username.grid(row=3,column=2)
password.grid(row=4,column=2)
barcode.grid(row=5,column=2)

#Variables for storing the labels
firstnamevalue = StringVar
lastnamevalue = StringVar
usernamevalue = StringVar
passwordvalue = StringVar
barcodevalue = StringVar
checkvalue = IntVar

firstnameentry = Entry(root, textvariable = firstnamevalue)
lastnameentry = Entry(root, textvariable = lastnamevalue)
usernameentry = Entry(root, textvariable = usernamevalue)
passwordentry = Entry(root, textvariable = passwordvalue) 
barcodeentry = Entry(root, textvariable = barcodevalue)

#Entrybox to input information 
firstnameentry.grid(row=1, column=3)
lastnameentry.grid(row=2,column=3)
usernameentry.grid(row=3, column=3)
passwordentry.grid(row=4,column=3)
barcodeentry.grid(row=5, column=3)

# Create Account button 
Button(text="Create Account", command=getvals).grid(row=7,column=3)

root.mainloop()


