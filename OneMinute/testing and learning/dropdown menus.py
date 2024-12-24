from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Dropdown Menus')
root.geometry('400x400')

#Creating and packing
options = ['Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday']
clicked = StringVar()
clicked.set('Dropdown Menu')
drop = OptionMenu(root, clicked, *options)
drop.pack()

root.mainloop()
