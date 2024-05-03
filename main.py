from tkinter import * 
from PIL import Image, ImageTk
from barcode import Code128
from barcode.writer import ImageWriter
from createaccount import getvals 

root = Tk()
root.geometry('500x400')

#Title of the main window
Label(root, text='Welcome!', font='arial 15 bold').grid(row=0,column=4)

Label(root,text= '   Scan barcode below to sign in ', font= 'arial 12').grid(row=1, column=3)
 
 # Read the file and strip 
 # Call barcode_generator()
def main():
    new_account = open('account.txt', 'r')
    username = new_account.readline().strip() 
    password = new_account.readline().strip()
    barcode_data = new_account.readline().strip()

    barcode_generator(barcode_data)


# Barcode entered from createaccount.py generated 
# Generated barcode image 
# Called the function
# Display the barcode 
def barcode_generator(barcode_data):
    if barcode_data.strip():
       image_barcode = Code128(barcode_data, writer=ImageWriter())
       barcode_i = image_barcode.render()
       barcode_i.save('barcode.png')
       openbarcode() 


# Open the barcode image
# Adding the image to Tkinter 
# Create a label for image in Tkinter 
def openbarcode(): 
    b_image = Image.open('barcode.png')
    b_photo = ImageTk.PhotoImage(b_image)
    barcodelabel = Label(root, image=b_photo)
    barcodelabel.image = b_photo
    barcodelabel.grid(row=2,column=4)
    barcode_title = Label(root, text= 'Barcode Display')
    barcode_title.grid(row=3,column=4)

if __name__ == "__main__":
    main()
    root.mainloop()
