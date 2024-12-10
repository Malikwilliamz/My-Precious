from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x400')
root.title('Checboxes')
root.iconbitmap(bitmap = 'C:/Users/HP/Documents/malo\'s/download.ico') # Always use front-slash when including a file path

#Creting the checkboxes
var =StringVar()  # Choosing the format for the infomation next to the checkbox
var1=IntVar()        # -->StringVar() = string format/data type
var2 =IntVar()       #-->IntVar = integer data type
var3 =IntVar()

# Creating a checkbutton is almost similar to creating a button or label
a =Checkbutton(root, text='Manchester City', variable=var, onvalue='Yeeeees', offvalue='NOooooooo')
a.deselect() # Function used to make sure that the checkboxes are not checked when the program runs
a.pack(anchor=W)

b =Checkbutton(root, text='Manchester United', variable=var1)
b.pack(anchor=W)

c =Checkbutton(root, text='Chelsea FC', variable=var2)
c.pack(anchor=W)

d = Checkbutton(root, text='Arsenal', variable=var3)
d.pack(anchor=W)

def teams():
    my_label = Label(root, text=var.get()).pack() # Var_sth.get() is used to get the information gotten from clicking the checkbox as set by the creator
    my_label1 = Label(root, text=var1.get()).pack()
    my_label2 = Label(root, text=var2.get()).pack()
    my_label3 = Label(root, text=var3.get()).pack()
    

BUt = Button(root, text='Choose Team', command=teams).pack()



root.mainloop()

