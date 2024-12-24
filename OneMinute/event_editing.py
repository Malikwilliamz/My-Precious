from tkinter import *
import sqlite3
from datetime import date
from tkinter import filedialog
import os

def event_all():
    from tkinter import ttk
    root_events = Tk()
    root_events.geometry('470x550')
    frame_edit = LabelFrame(root_events, text='Editing')
    frame_add = LabelFrame(root_events, text='Add Event', height=60, width=200)

    frame_add.grid(row=2, column=0, pady=5)
    frame_edit.grid(row=3, column=0, pady=4)

    events_treeview = ttk.Treeview(root_events)
    events_treeview['columns'] = ('ID', 'Event Name', 'Date')   # Creating columns
    # Formatting columns
    events_treeview.column('#0', width=0, minwidth=0)
    events_treeview.column('ID', width=120)
    events_treeview.column('Event Name', width=200, anchor=W)
    events_treeview.column('Date', width=120, anchor=CENTER)
    # Creating headings
    events_treeview.heading('#0', text='')
    events_treeview.heading('ID', text='ID')
    events_treeview.heading('Event Name', text='Event Name')
    events_treeview.heading('Date', text='Date')
    # Sorting out data
    connecting_events_database = sqlite3.connect('Events.db')
    cursor_events_database = connecting_events_database.cursor()

    cursor_events_database.execute('SELECT *, oid FROM plan')
    fetched_event_details = cursor_events_database.fetchall()
    print(fetched_event_details)
    event_details_fetched = 0
    while event_details_fetched <= (len(fetched_event_details) - 1):
        for ite in fetched_event_details:
            events_treeview.insert(parent='', index='end', iid=event_details_fetched, text='', values=(ite[2], ite[0], ite[1]))
            event_details_fetched += 1

    events_treeview.grid(row=0, column=0)

    # Refreshing the treeview widget
    def refreshing_event_list():
        event_list = ttk.Treeview(root_events)
        event_list['columns'] = ('ID', 'Event Name', 'Date')  # Creating columns
        # Formatting columns
        event_list.column('#0', width=0, minwidth=0)
        event_list.column('ID', width=120)
        event_list.column('Event Name', width=200, anchor=W)
        event_list.column('Date', width=120, anchor=CENTER)
        # Creating headings
        event_list.heading('#0', text='')
        event_list.heading('ID', text='ID')
        event_list.heading('Event Name', text='Event Name')
        event_list.heading('Date', text='Date')
        # Sorting out data
        connecting_event_database = sqlite3.connect('Events.db')
        event_database_cursor = connecting_event_database.cursor()

        event_database_cursor.execute('SELECT *, oid FROM plan')
        fetched_event_data = event_database_cursor.fetchall()
        print(fetched_event_data)
        event_database_loop_counter = 0
        while event_database_loop_counter <= (len(fetched_event_data) - 1):
            for event_detail in fetched_event_data:
                event_list.insert(parent='', index='end', iid=event_database_loop_counter, text='', values=(
                    event_detail[2], event_detail[0], event_detail[1]))
                event_database_loop_counter += 1

        event_list.grid(row=0, column=0)
    fresh = Button(root_events, text='Refresh', command=refreshing_event_list)
    fresh.grid(row=1, column=0)

    # "Add Event" frame configure
    info_label = Label(frame_add,
                       text='\tAdd An Event:',
                       font=('Helvetica', 10, 'bold italic'))
    date_label = Label(frame_add, text='Date:', font=('Times', 10))
    date_box = Entry(frame_add, width=35)
    name_label = Label(frame_add, text='Event Name:', font=('Times', 10))
    name_entry = Entry(frame_add, width=35)
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1)

    def data():  # Configuring event-adding interface with event database

        connecting_event_details = sqlite3.connect('Events.db')
        event_details_cursor = connecting_event_details.cursor()

        event_details_cursor.execute("INSERT INTO plan VALUES(:Event, :date)",
                                     {
                                        'Event': name_entry.get(),
                                        'date': date_box.get()
                                                                }

                                     )
        connecting_event_details.commit()
        connecting_event_details.close()
        # Clearing data
        name_entry.delete(0, END)
        date_box.delete(0, END)

    def exiting():  # Erases the data on the screen once you click 'create event' button
        frame_add.destroy()

    save_button = Button(frame_add, text='Create Event', font=('Times', 10), padx=20, command=data)
    exit_button = Button(frame_add, text='Exit', font=('Times', 10), command=exiting)

    # Posting different widgets in the editing frame
    info_label.grid(row=0, column=0, columnspan=3)
    date_label.grid(row=2, column=0)
    date_box.grid(row=2, column=1)
    save_button.grid(row=3, column=0, columnspan=2)
    exit_button.grid(row=4, column=0, columnspan=2, pady=5)

    connecting_events_database.commit()
    connecting_events_database.close()

    #insert event editor here
    def event_editing():  # Configuring editing frame
        event_edit_root = Tk()
        date_label_editor = Label(event_edit_root, text='Date:', font=('Times', 10))
        date_box_editor = Entry(event_edit_root, width=35)
        name_label_editor = Label(event_edit_root, text='Event Name:', font=('Times', 10))
        name_entry_editor = Entry(event_edit_root, width=35)

        cursor_events_database.execute('SELECT * FROM plan WHERE oid='+i_d_entry.get())
        accessed_event_details = cursor_events_database.fetchall()
        for event_detail in accessed_event_details:
            date_box_editor.insert(0, event_detail[1])
            name_entry_editor.insert(0, event_detail[0])

        def database_entry():
            cursor_events_database.execute("""UPDATE plan SET
                
                                      Event = :event,
                                      date = :date
                        
                                      WHERE oid = :oid""",
                                   {
                                      'event': name_entry_editor.get(),
                                      'date': date_box_editor.get(),
                                      'oid': i_d_entry.get()
                                                                        })
            connecting_events_database.commit()

        def editing_exit():  # Clears whatever is in the entry field
            event_edit_root.destroy()

        edit_save_button = Button(event_edit_root, text='Save', font=('Times', 10), padx=20, command=database_entry)
        edit_exit_button = Button(event_edit_root, text='Exit', font=('Times', 10), command=editing_exit)

        name_label_editor.grid(row=1, column=0)
        name_entry_editor.grid(row=1, column=1)
        date_label_editor.grid(row=2, column=0)
        date_box_editor.grid(row=2, column=1)
        edit_save_button.grid(row=3, column=0, columnspan=2)
        edit_exit_button.grid(row=4, column=0, columnspan=2, pady=5)
        event_edit_root.mainloop()

    def delete():  # Deleting entered event details
        deleting_access = sqlite3.connect('Events.db')
        delete_cursor = deleting_access.cursor()

        delete_cursor.execute('DELETE FROM plan WHERE oid=' + i_d_entry.get())
        i_d_entry.delete(0, END)
        deleting_access.commit()
        deleting_access.close()

    delete_frame_info = Label(frame_edit,
                              text='Enter The Id Of event you want to edit',
                              font=('Helvetica', 10, 'bold italic'))
    i_d = Label(frame_edit, text='ID:')
    i_d_entry = Entry(frame_edit, width=35)
    i_d_button = Button(frame_edit, text='Edit', command=event_editing)
    i_d_button_d = Button(frame_edit, text='Delete', command=delete)

    i_d.grid(row=1, column=0)
    i_d_entry.grid(row=1, column=1)
    i_d_button.grid(row=2, column=0, columnspan=3, pady=3)
    i_d_button_d.grid(row=3, column=0, columnspan=3)
    delete_frame_info.grid(row=0, column=0, columnspan=3, sticky=N+W+S+E)

    root_events.mainloop()
