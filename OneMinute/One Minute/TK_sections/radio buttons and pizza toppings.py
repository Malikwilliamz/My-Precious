from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('radio buttons')

#Creating a list to iterate through when calling the toppings

MODES = [('pepperoni','pepperoni'),
         ('cheese','cheese'),
         ('mushroom', 'mushroom'),
         ('onion', 'onion'),
         ]


pizza =StringVar()
pizza.set('Start choosing')

#Function to change the displayed topping
def place_another(topping):
    top = Label(root, text=topping)
    top.pack()

#creating the radiobuttons with the toppings
for text, other in MODES:
    Radiobutton(root, text=text, variable=pizza, value=other,command=lambda:place_another(pizza.get())).pack(anchor=W)

root.mainloop()
