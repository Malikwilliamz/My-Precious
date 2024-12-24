from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Dialog box')


#Function to be used to open the filedialog box
def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/HP/Documents/malo\'s', title=(('All Files', '*.*')))
    label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_imglab = Label(image=my_img).pack()
   
#opening the filedialog window immediately
button = Button(root, text='Open File', command=open).pack()


root.mainloop()
