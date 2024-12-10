from tkinter import*
from PIL import ImageTk, Image
import sqlite3 as sq

root = Tk()
root.geometry('400x400')
# Connecting to the new database about to be created

conn = sq.connect('address_book2.db')

# Creating cursor
curs = conn.cursor()

# Executing a command
#curs.execute("""CREATE TABLE mine(
#             first_name text,
#             last_name text,
#             address text,
#             zipcode integer)""")

# Creating the interface for entering data
first_name = Entry(root, width=45)
first_name.grid(row=0,column=1)
last_name = Entry(root, width=45)
last_name.grid(row=1,column=1)
address = Entry(root, width=45)
address.grid(row=2,column=1)
zipcode = Entry(root, width=45)
zipcode.grid(row=3,column=1)
delete_record = Entry(root, width=45)
delete_record.grid(row=8, column=1)

# Labels to be aside the entry boxes
first_label = Label(root, text='First Name:')
first_label.grid(row=0, column=0)
last_label = Label(root, text='Last Name:')
last_label.grid(row=1, column=0)
address_label = Label(root, text='Address:')
address_label.grid(row=2, column=0)
zipcode_label = Label(root, text='Zipcode:')
zipcode_label.grid(row=3, column=0)
delete = Label(root, text='ID:')
delete.grid(row=8, column=0)


# Button to submit all the work
def submit():
    # clearing everything from the screen and sending it to the database
    conn = sq.connect('address_book2.db')
    c = conn.cursor()

    c.execute("INSERT INTO mine VALUES(:first_name, :last_name, :address, :zipcode)",
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

def query():
    # Function for showing the data in the database we are working on
    conn = sq.connect('address_book2.db')
    curs = conn.cursor()
    curs.execute("SELECT *,oid FROM mine")  # oid are the primary keys that are created by python automatically
    # Fetching all the data
    records = curs.fetchall()
    print(records)
    print_records = ''

    # iterating through the records in order to get individual groups
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + '\n'

    butt = Label(root, text=print_records)
    butt.grid(row=11, column=0, columnspan=2)

def delete():
    conn = sq.connect('address_book2.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM mine WHERE oid=" + delete_record.get())

    # Remove everything from the input box
    delete_record.delete(0, END)

    # commit and close
    conn.commit()
    conn.close()




def edit():

    global second_root
    global first_name_editor
    global last_name_editor
    global address_editor
    global zipcode_editor
    second_root = Tk()
    second_root.geometry('400x400')
    # Connecting to the new database about to be created

    conn = sq.connect('address_book2.db')

    # Creating cursor
    curs = conn.cursor()

    # Executing a command
    # curs.execute("""CREATE TABLE mine(
    #             first_name text,
    #             last_name text,
    #             address text,
    #             zipcode integer)""")

    # Creating the interface for entering data
    first_name_editor = Entry(second_root, width=45)
    first_name_editor.grid(row=0, column=1)
    last_name_editor = Entry(second_root, width=45)
    last_name_editor.grid(row=1, column=1)
    address_editor = Entry(second_root, width=45)
    address_editor.grid(row=2, column=1)
    zipcode_editor = Entry(second_root, width=45)
    zipcode_editor.grid(row=3, column=1)

    # Iterate through the database
    records_editor = delete_record.get()
    curs.execute("SELECT * FROM mine WHERE oid= " + records_editor)
    c = curs.fetchall()
    # Show Info when the second window is created
    for record in c:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        zipcode_editor.insert(0, record[3])

    # Labels to be aside the entry boxes
    first_label_editor = Label(second_root, text='First Name:')
    first_label_editor.grid(row=0, column=0)
    last_label_editor = Label(second_root, text='Last Name:')
    last_label_editor.grid(row=1, column=0)
    address_label_editor = Label(second_root, text='Address:')
    address_label_editor.grid(row=2, column=0)
    zipcode_label_editor = Label(second_root, text='Zipcode:')
    zipcode_label_editor.grid(row=3, column=0)

    # Button to save and exit the editing window

    def edit_close():

        # Connecting to the new database about to be created
        conn3 = sq.connect('address_book2.db')

        # Creating cursor
        curs3 = conn3.cursor()
        # execute command
        curs3.execute("""UPDATE mine SET
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    zipcode = :zipcode

                    WHERE zipcode = :zipcode""",
                     {
                         'first': first_name_editor.get(),
                         'last': last_name_editor.get(),
                         'address': address_editor.get(),
                         'zipcode': zipcode_editor.get(),

                     })

        # Commit and close
        conn3.commit()
        conn3.close()
        
    edit_button_close = Button(second_root, text='Save Info', command=edit_close)
    edit_button_close.grid(row=9, column=0, columnspan=2, ipadx=137)
    # Commit and close
    conn.commit()
    conn.close()

sub = Button(root, text='Submit Info', command=submit, padx=137, pady=5)
sub.grid(row=4, column=0, columnspan=2)

show = Button(root, text='Show Records', command=query, padx=132, pady=5)
show.grid(row=5, column=0, columnspan=2)

delete_but = Button(root, text='Delete This record', command=delete, padx=137, pady=5)
delete_but.grid(row=9, column=0, columnspan=2)

edit_button = Button(root, text='Edit that Record', command=edit)
edit_button.grid(row=10, column=0, columnspan=2, ipadx=139)

# Committing changes that might be made to the new database file
conn.commit()

# Disconnecting from the database
conn.close()

root.mainloop()