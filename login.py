from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x300')

# Open file as read-on;y
# .strip() to remove the whitespace 
# Save username, password and barcode to main.py
def login(): 
    new_account = open('account.txt', 'r')
    savedusername = new_account.readline().strip()
    savedpassword = new_account.readline().strip()
    savedbarcode = new_account.readline().strip()
    
    if username == savedusername and password == savedpassword and barcode == savedbarcode: 
        print("Success")
        return True 
    else: 
        print("Try again")
        return False
if __name__ == '__main__': 
    login()
    

# Title of the Website 
Label(root, text ="              Gym Barcode               ", font='arial 15 bold').grid(row=0, column=5)

# Labels of entrys for login 
username = Label(root, text= '  Username  ')
password = Label(root, text= '  Password ')

# Label postions 
username.grid(row=1, column=4)
password.grid(row=2, column=4)

# Variables
usernamevalue = StringVar()
passwordvalue = StringVar()

usernameentry = Entry(root, textvariable = usernamevalue)
passwordentry =  Entry(root, textvariable = passwordvalue)

# Entrybox for inputs
usernameentry.grid (row=1, column= 5)
passwordentry.grid(row=2, column= 5)

# Sign in button 
Button(text="Sign in", command= login).grid(row=7, column=5)



root.mainloop()
