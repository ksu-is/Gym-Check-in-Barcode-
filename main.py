from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
import barcode  
from barcode.writer import ImageWriter
from createaccount import barcodeentry
from login import username
from login import password 

root = Tk()
root.geometry('500x300')

#Title of the main window
Label(root, text='        Welcome!', font='arial 15 bold').grid(row=0,column=6)

Label(root,text= '   Scan barcode below to sign in ', font= 'arial 12').grid(row=1, column=3)
 

# Barcode entered from createaccount.py generated 
def barcode_generator(barcodeentry):
    if barcodeentry == ' ':
       image_barcode = barcode.get_barcode_class('code128', writer=ImageWriter)
       image_barcode.save('barcode.png')
       barcodeentry('barcode.png')








root.mainloop()
