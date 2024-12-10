from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title('Learning radio buttons')

#variable
r = StringVar()

#Function to change the value according to the radiobutton selected
def place(valu):
    lab = Label(root, text=valu)
    lab.pack()

#Creating the radiobuttons and packing them on the screen
Radiobutton(root, text='Option1', variable=r, value='1', command=lambda:place(r.get())).pack()
Radiobutton(root, text='Option2', variable=r, value='2', command=lambda:place(r.get())).pack()

#creting a label to show the value of the radiobuttons
#lab =Label(root,text=r.get())
#lab.pack()


root.mainloop()
