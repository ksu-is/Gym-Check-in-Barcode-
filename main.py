from tkinter import * 
from tkinter import Label, Tk
from PIL import Image, ImageTk
import barcode  
from barcode.writer import ImageWriter
from login import login 

root = Tk()
root.geometry('500x300')

#Title of the main window
Label(root, text='        Welcome!', font='arial 15 bold').grid(row=0,column=6)

Label(root,text= '   Scan barcode below to sign in ', font= 'arial 12').grid(row=1, column=3)
 
 # Read the file and strip 
def main():
    new_account = open('account.txt', 'r')
    username = new_account.readline().strip 
    password = new_account.readline().strip()
    barcode = new_account.readline().strip()

if __name__ == "__main__":
    main()


# Barcode entered from createaccount.py generated 
# Generated barcode image 
# Called the function
# Display the barcode 
def barcode_generator(barcodeentry):
    if barcodeentry.strip():
       image_barcode = barcode.get_barcode_class('code128', writer=ImageWriter)
       image_barcode.save('barcode.png')
       barcodeentry('barcode.png')
       openbarcode() 


# Open the barcode image
# Adding the image to Tkinter 
# Create a label for image in Tkinter 
def openbarcode(): 
    b_image = Image.open('barcode.png')
    b_photo = ImageTk.PhotoImage(b_image)
    barcodelabel = Label(root, image=b_photo)
    barcodelabel.image = b_photo
    barcodelabel.grid(row=2,column=1)
    barcode_title = Label(root, text= 'Barcode Display')
    barcode_title.grid(row=3,column=1)










root.mainloop()
