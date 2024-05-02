from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x300')

# Save username, password and barcode to file
# Create a file and open it in write mode
def getvals():
    username = usernamevalue.get()
    password = passwordvalue.get()
    barcode = barcodevalue.get()
    new_account = open('account.txt','w')
    print(new_account)
    new_account.write(username + "\n")
    new_account.write(password + "\n")
    new_account.write(barcode)
    print("Account created")
    new_account.close()

#Title of the website
Label(root, text ="              Gym Barcode              ", font='arial 15 bold').grid(row=0, column=3)
#Labels of the entrys
firstname_label = Label(root, text= ' First Name')
lastname_label = Label (root, text= 'Last Name')
username_label = Label(root, text='  Username ')
password_label = Label(root, text='  Password ')
barcode_label = Label(root, text='   Barcode ')
#The positions of the labels
firstname_label.grid(row=1,column=2)
lastname_label.grid(row=2,column=2)
username_label.grid(row=3,column=2)
password_label.grid(row=4,column=2)
barcode_label.grid(row=5,column=2)

#Variables for storing the labels
firstnamevalue = StringVar()
lastnamevalue = StringVar()
usernamevalue = StringVar()
passwordvalue = StringVar()
barcodevalue = StringVar()

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


