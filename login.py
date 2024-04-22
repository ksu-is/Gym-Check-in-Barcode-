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
username.grid(row=1,column=2)
password.grid(row=2,column=2)
barcode.grid(row=3,column=2)

#Variables for storing the labels
usernamevalue = StringVar
passwordvalue = StringVar
barcodevalue = StringVar
checkvalue = IntVar

usernameentry = Entry(root, textvariable = usernamevalue)
passwordentry = Entry(root, textvariable = passwordvalue) 
barcodeentry = Entry(root, textvariable = barcodevalue)

#Entrybox to input information 
usernameentry.grid(row=1, column=3)
passwordentry.grid(row=2,column=3)
barcodeentry.grid(row=3, column=3)

# Save login button
savebutton = Checkbutton(text="Keep me signed in", variable = checkvalue)
savebutton.grid(row=6, column=3)

# Create Account button 
Button(text="Create Account", command=getvals).grid(row=7,column=3)

root.mainloop()


