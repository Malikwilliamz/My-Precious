from tkinter import *
import sqlite3 as sq
"""
OBJECTIVE:
Create  A list with certain components then find a way of creating buttons by iterating through the list and making sure
each has a suited function
"""

root = Tk()
root.title('Testing Attendance')


# Creating a class to sort out all the various widgets and their functionality

class Att:
    def __init__(self, master):
        self.people = []  # list to hold all the various names
        self.imp = sq.connect('Member_Dets.db')  # Connecting to the database to acquire the name of the people
        self.curs = self.imp.cursor()
        self.curs.execute('SELECT *,oid FROM info3')
        self.catch = self.curs.fetchall()
        for cat in self.catch:  # Adding the names to the list
            self.people.append(str(cat[0] + ' ' + cat[1]))
        for person in self.people:  # Turning the names into buttons
            self.vj = Button(master, text=person).pack()
            self.v2 = Button(master, text=person, command=self.v2.destroy)

    def destruct_safely(self):
        pass



attend = Att(root)

if __name__ == '__main__':
    attend


root.mainloop()