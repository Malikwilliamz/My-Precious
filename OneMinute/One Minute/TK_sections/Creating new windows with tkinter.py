from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Creating new windows')


def open_window3():
     top2 = Toplevel()
#Function to be controlled by a button to open up the next window
def open_window():
    global my_img1
    #Creating new window and its details
    top = Toplevel()
    top.title('Second One')
    #Putting a new image on the second window
    my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/HP/Documents/malo\'s/astro/astro1.jpg'))
    labl = Label(top, image=my_img1).pack()
    button2 = Button(top, text='Open third window', command= open_window3).pack()


#The buton to open the second window
bt_open = Button(root, text='Open second window', command=open_window).pack()




root.mainloop()
