from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
root.geometry('600x600')

#creating the widget
#vertical
vertical = Scale(root, from_=0, to=200)
vertical.pack()
#Horizontal
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

def clicked():
    #Displaying the reading on the slider
    label_value = Label(root, text=horizontal.get()).pack()
    label_value2 = Label(root, text=vertical.get()).pack()
    

But = Button(root, text='Click to see', command=clicked).pack()
root.mainloop()
