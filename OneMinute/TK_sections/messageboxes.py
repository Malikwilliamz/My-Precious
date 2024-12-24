from tkinter  import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('MessageBox')

#Types of messageboxes are:askquestion, askokcancel, askyesno, showinfo, showerror, showwarning

def popup():
    messagebox.showinfo('Malo', 'Malo You Are The Most Awsome')
    Label(root, text=response).pack()# for some reason the response function does not work in this script

    
Button(root, text='Click Me', command=popup).pack()


mainloop()
