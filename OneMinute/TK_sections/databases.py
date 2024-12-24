from tkinter import *
from PIL import ImageTk, Image
import sqlite3 as sq








impo = sqlite3.connect('Member_Dets.db')
cur = impo.cursor()

cur.execute('SELECT *, oid FROM info3')
things = cur.fetchall()
dicty = {}
egg = 1
while egg < len(things):
    for it in things:
        les = str(it[0] + ' ' + it[1])
        chic = f'var{egg}'
        dicty[str(les)] = StringVar()
        egg += 1
for x, y in dicty.items():
    g = Checkbutton(root_att, text=x, variable=y, onvalue='Present', offvalue='Absent').pack()


def clickedy():
    eggse = 3
    while eggse < len(dicty):
        for p, h in dicty.items():
            Label(root_att, text=h.get()).pack()
        print(h.get())
        eggse += 1


butty = Button(root_att, text='Submit', command=clickedy)
butty.pack()

impo.commit()
impo.close()











root = Tk()
root.title('Databases')
root.geometry('500x500')


# Connecting to the database file and creating cursor
connect = sq.connect('address_book.db')
curs = connect.cursor()

#Creating Table
#curs.execute("""CREATE TABLE addresses(
#            first_name text,
#           last_name text,
#            address text,
#            zipcode integer
#            )
#         """)
# Creating the interface for entering data
first_name = Entry(root, width=20)
first_name.grid(row=0,column=1)
last_name = Entry(root, width=20)
last_name.grid(row=1,column=1)
address = Entry(root, width=20)
address.grid(row=2,column=1)
zipcode = Entry(root, width=20)
zipcode.grid(row=3,column=1)

# Labels to be aside the entry boxes
first_label = Label(root, text='First Name:')
first_label.grid(row=0, column=0)
last_label = Label(root, text='Last Name:')
last_label.grid(row=1, column=0)
address_label = Label(root, text='Address:')
address_label.grid(row=2, column=0)
zipcode_label = Label(root, text='Zipcode:')
zipcode_label.grid(row=3, column=0)
#Button to submit all the work
def submit():
    # clearing everything from the screen and sending it to the database
    conn = sq.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES(:first_name, :last_name, :address, :zipcode)",
              {
                  'first_name' : first_name.get(),
                  'last_name' : last_name.get(),
                  'address' : address.get(),
                  'zipcode' : zipcode.get()
              })

    conn.commit()

    conn.close()
    # clearing things from the screen
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    zipcode.delete(0, END)

sub = Button(root, text='Submit Info', command=submit)
sub.grid(row=4, column=0, columnspan=2)


# Commiting the changes
connect.commit()

# Disconnecting from database
connect.close()


#Always remember that the cursor class is not used when commiting or cutting the connection



root.mainloop()
