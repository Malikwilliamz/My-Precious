import sqlite3 as sq
from tkinter import *

root = Tk()
root.title('Att3')

# Large Outer frame
frame_out = LabelFrame(root, text='Outer', height=300)
frame_out.grid(row=0, column=0)
frame_in_people = LabelFrame(frame_out, text='People', height=150)
frame_in_people.grid(row=0, column=0)
frame_in_status = LabelFrame(frame_out, text='Status', height=120)
frame_in_status.grid(row=0, column=1, padx=5)

imp = sq.connect('Member_Dets.db')
cury = imp.cursor()
cury.execute('SELECT *,oid FROM info3')
fet = cury.fetchall()


def clicked():
    global init
    init = Entry(frame_in_status)
    init.grid(row=egg, column=0, pady=4)
    init.insert(9, 'Absent')


def clicked2():
    global init
    init = Entry(frame_in_status)
    init.grid(row=egg, column=0, pady=4)
    init.insert(0, 'Present')


egg = 0
while egg < len(fet):
    for f in fet:
        Label(frame_in_people, text=f[0] + ' ' + f[1]).grid(row=egg, column=0)
        give = Button(frame_in_people, text='Absent', command=clicked).grid(row=egg, column=1)
        take = Button(frame_in_people, text='Present', command=clicked2).grid(row=egg, column=2)
        egg += 1

def subby():
    global init
    global init_list
    init_list = []
    print(init.get())
    init_list.append(init.get())




def subby2():
    global init
    global init_list
    egg2 = 0
    while egg2 < len(init_list):
        for f in fet:
            for l in init_list:
                Label(root, text=(f[0] + ' ' + f[1]) + ':' + l).grid(row=egg2, column=0)
            egg2 += 1
    print(init_list)


sub_but = Button(frame_out, text='Sub', command=subby)
sub_but2 = Button(frame_out, text='Sub All', command=subby2)
sub_but.grid(row=1, column=1)
sub_but2.grid(row=2, column=1)
root.mainloop()