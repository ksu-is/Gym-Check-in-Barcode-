from tkinter import *
from tkinter import ttk

# Open file as read-on;y
# .strip() to remove the whitespace 
# Save username, password and barcode to main.py
def log_in(): 
    entered_username = usernamevalue.get()
    entered_password = passwordvalue.get()
    account_2 = open('account.txt', 'r')
    savedusername = account_2.readline().strip()
    savedpassword = account_2.readline().strip()
    savedbarcode = account_2.readline().strip()
    
    if entered_username == savedusername and entered_password == savedpassword:
        print("Success")
        return True 
    else: 
        print("Try again")
        return False
if __name__ == '__main__': 
    root = Tk()
    root.geometry('500x300')
    # Title of the Website 
    Label(root, text ="              Gym Barcode               ", font='arial 15 bold').grid(row=0, column=5)
    
    # Labels of entrys for login 
    username_label = Label(root, text= '  Username  ')
    password_label = Label(root, text= '  Password ')
    
    # Label postions 
    username_label.grid(row=1, column=4)
    password_label.grid(row=2, column=4)
    # Variables
    usernamevalue = StringVar()
    passwordvalue = StringVar()
    usernameentry = Entry(root, textvariable = usernamevalue)
    passwordentry =  Entry(root, textvariable = passwordvalue)
    # Entrybox for inputs
    usernameentry.grid (row=1, column= 5)
    passwordentry.grid(row=2, column= 5)
    # Sign in button 
    Button(text="Sign in", command= log_in).grid(row=7, column=5)
    
    root.mainloop()
