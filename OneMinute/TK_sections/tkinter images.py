from tkinter import * # Calling the module to help with the widgets
from PIL import ImageTk, Image # Module for working with images in tkinter


root = Tk()
root.title('Malo works') #Title of the screen 
root.iconbitmap(bitmap='C:/Users/HP/Downloads/download.ico') #Having an icon for the window(changeable)

# Packing an image onto the screen after calling it
my_img =ImageTk.PhotoImage(Image.open('C:/Users/HP/Desktop/malo.jpg'))
my_label = Label(image=my_img)
my_label.pack()

#Keeping the screen running 
root.mainloop()


