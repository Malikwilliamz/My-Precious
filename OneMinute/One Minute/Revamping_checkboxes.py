from tkinter import *

root = Tk()
root.title("Malo trying checkboxes")

var = StringVar()

def changing_value():
	changed_label = Label(root, text=var.get())
	changed_label.pack()

c = Checkbutton(root, text="Ayoo fahm, Allow it", variable=var, onvalue="Eloooo", offvalue="nonono")
c.deselect()
button_change = Button(root, text="Clickmeat", command=changing_value)
c.pack()
button_change.pack()

print(var.get())

root.mainloop()