from tkinter import *
from tkinter import font
from datetime import date
import sqlite3 as sq

rootly = Tk()
rootly.title('One Minute At A Time')
rootly.iconbitmap('C:/Users/HP/Documents/malo\'s/One Minute.ico')
rootly.geometry('1020x660')


class Rooty:
    def __init__(self, master):
        self.fire = sq.connect('Member_Dets.db')
        self.embers = self.fire.cursor()
        self.embers.execute('SELECT *,oid FROM info3')
        self.f = self.embers.fetchall()
        self.var = StringVar()
        self.var.set(1)
        self.var2 =  StringVar()
        self.var2.set(1)
        egg=0
        while egg < len(self.f):
            for x in self.f:
                self.lab = Label(master, text=str(x[0]+x[1]))
                self.rad = Radiobutton(master, text='Present', variable=self.var, value='Present')
                self.rad2 = Radiobutton(master, text='Absent', variable=self.var2, value='Absent')
                self.sub_but = Button(master, text='Submit stuff', command=self.sub_stuff)
                self.rad.deselect()
                self.rad2.deselect()

                self.lab.grid(row=egg, column=0)
                self.rad.grid(row=egg, column=1)
                self.rad2.grid(row=egg, column=2)
                self.sub_but.grid(row=0, column=3, rowspan=10, pady=5)
                egg += 1

    def sub_stuff(self):
        print(self.var.get())


roots = Rooty(rootly)
if __name__ == '__main__':
    roots

rootly.mainloop()
