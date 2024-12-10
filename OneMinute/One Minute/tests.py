from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Tabs')
root.geometry('400x400')
checked_people_list = []
jiji = ''

def creation():
    global checked_people_list
    lissy.append(text.get())
    text.delete(0, END)


def creation2():
    global note
    global yoh
    egg = 0
    while egg < len(checked_people_list):
        for lis in checked_people_list:
            note = ttk.Notebook(root)
            tab = ttk.Frame(note)
            note.add(tab, text=str(lis))
            yoh = Text(tab, width=15, height=6)
            yoh.grid(row=egg, column=0)
            note.grid(row=3, column=egg)
            egg += 1
        print(checked_people_list)


def delete_tab():
    Label(root, text=jiji).grid(row=4, column=0)



butty = Button(root, text='Submit tab', command=creation)
butty2 = Button(root, text='Show all', command=creation2)
butty3 = Button(root, text='Delete Tab', command=delete_tab)
text = Entry(root, width=40)

butty.grid(row=1, column=0, columnspan=1)
butty2.grid(row=2, column=0)
butty3.grid(row=2, column=1)
text.grid(row=0, column=0)


root.mainloop()
