from tkinter import *
from tkinter import ttk


def running():
    root = Tk()
    root.title('Scrollbar Tings')
    root.geometry('800x800')
    # root.resizable(False, False)

    frame1 = LabelFrame(root)
    frame2 = LabelFrame(root)

    canvas1 = Canvas(frame1)
    canvas1.pack(side=LEFT)

    scroll = ttk.Scrollbar(frame1, orient='vertical', command=canvas1.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas1.configure(yscrollcommand=scroll.set)

    frame3 = Frame(canvas1)
    frame3.pack()
    canvas1.create_window((0, 0), window=frame3, anchor='nw')
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox('all')))

    # Creating a textbox inside the frame/canvas
    text_box = Text(frame1, width=90, height=80)
    text_box.pack(anchor=W, side='top')

    # Button to enter info
    butt = Button(frame3, text='Enter Data', padx=50)
    butt.pack(side=BOTTOM, anchor=W)

    frame1.pack(fill='both', expand='yes', padx=10, pady=10)


    root.mainloop()

running()











# Dictionary testing




# Checkboxes onto screen
# a.grid(row=0, column=0, sticky=W)
# b.grid(row=1, column=0, sticky=W)
# c.grid(row=2, column=0, sticky=W)
# d.grid(row=3, column=0, sticky=W)


# bolded = font.Font(weight='bold') # will use the default font
# box.config(font=bolded)








root.mainloop()

button_rooty = Button(root2, text='click please', command=rooty)
button_rooty.pack()
