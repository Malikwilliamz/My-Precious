from tkinter import *
import sqlite3
from datetime import date
from tkinter import filedialog
import os

# Global Variables
global checkbox_variables_2
global text_box
global checked_people_list
global f_entry_edit
global l_entry_edit
global p_entry_edit
global h_entry_edit

# Creating database for member
main_member_database_access = sqlite3.connect('Member_Dets.db')
main_member_database_cursor = main_member_database_access.cursor()

# Configuring main window
root = Tk()
#root.iconbitmap("C:/Users/Malik/Desktop/Code/OneMinute/one minute.ico")
root.title('One Minute At A Time')
root.geometry('670x560')
root.configure(background='khaki')
# Frames Required for main window
title_frame = LabelFrame(root, background='pale goldenrod')
frame2 = LabelFrame(root, text='Attendance List', padx=30, pady=80, background='ivory2')
frame = LabelFrame(root, text='Options', padx=20, pady=76, background='ivory2')  # Frame for enclosing various buttons
frame_info = LabelFrame(root, text='Help', padx=50, pady=70, background='ivory2')
frame.grid(row=1, column=1)
frame2.grid(row=1, column=0, sticky=W)
title_frame.grid(row=0, column=0, columnspan=15, pady=5)
frame_info.grid(row=2, column=0, columnspan=4)
title = Label(title_frame, text='One Minute At  A Time', font=('Times', 20, 'bold italic'), padx=160)
title.grid(row=0, column=0,  sticky=W)


# Event window function
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


def show_file():  # Function for show events button
    filedialog.askopenfilename(initialdir='C:/Users/malik/Documents', title=('All files', '*.*'))


def member_details_button():  # Function for show member details button
    from tkinter import ttk
    root_member_details = Tk()
    root_member_details.title('Member Info')
    member_details_table = ttk.Treeview(root_member_details)
    member_addition_frame = LabelFrame(root_member_details, text='New Member')
    member_edit_frame = LabelFrame(root_member_details, text='Edit')
    member_edit_frame.grid(row=2, column=0, columnspan=2)
    member_addition_frame.grid(row=0, column=1)
    # Creating columns
    member_details_table['columns'] = ('ID', 'Name', 'House Number', 'Phone Number')
    # Formatting columns
    member_details_table.column('#0', width=2, minwidth=0)
    member_details_table.column('ID', width=50)
    member_details_table.column('Name', width=180, anchor=W)
    member_details_table.column('Phone Number', width=130, anchor=E)
    member_details_table.column('House Number', width=120, anchor=CENTER)
    # Naming column headings
    member_details_table.heading('#0', text='')
    member_details_table.heading('ID', text='ID')
    member_details_table.heading('Name', text='Name', anchor=W)
    member_details_table.heading('House Number', text='House Number', anchor='center')
    member_details_table.heading('Phone Number', text='Phone Number', anchor=E)
    # Sorting out data
    member_database_access = sqlite3.connect('Member_Dets.db')
    member_database_cursor = member_database_access.cursor()

    member_database_cursor.execute('SELECT *,oid FROM info3')
    member_details = member_database_cursor.fetchall()
    print(len(member_details))
    member_list_counter = 0
    while member_list_counter <= (len(member_details) - 1):
        for record in member_details:
            member_details_table.insert(parent='', index='end', iid=member_list_counter, text='',
                                        values=(record[4],str(record[0] + ' ' + record[1]), record[2], record[3]))
            member_list_counter += 1

    member_details_table.grid(row=0, column=0)

    def exiting():
        pass

    # creating the entry and labels
    f_name = Label(member_addition_frame, text='First Name:', font=('Times', 10))
    l_name = Label(member_addition_frame, text='Last Name:', font=('Times', 10))
    h_number = Label(member_addition_frame, text='House Number:', font=('Times', 10))
    p_number = Label(member_addition_frame, text='Phone Number:', font=('Times', 10))
    f_entry_edit = Entry(member_addition_frame, width=35, font=('Helvetica', 10))
    l_entry_edit = Entry(member_addition_frame, width=35, font=('Helvetica', 10))
    h_entry_edit = Entry(member_addition_frame, width=35, font=('Helvetica', 10))
    p_entry_edit = Entry(member_addition_frame, width=35, font=('Helvetica', 10))

    def data():  # Adding data to database
        member_database_cursor.execute("INSERT INTO info3 VALUES(:F_Name, :L_Name, :House_Number, :Phone_Number)",
                      {
                          'F_Name': f_entry_edit.get(),
                          'L_Name': l_entry_edit.get(),
                          'House_Number': h_entry_edit.get(),
                          'Phone_Number': p_entry_edit.get()

                      })
        member_database_cursor.execute('SELECT *, oid FROM info3')
        fetched_member_info = member_database_cursor.fetchall()
        member_info_list = []
        for member_info in fetched_member_info:
            member_info_list.append(str(member_info[0] + member_info[1]))
        for entered_info in member_info_list:
            Checkbutton(frame2, text=entered_info).grid(row=4, column=0)

        # Committing, closing and clearing
        member_database_access.commit()
        f_entry_edit.delete(0, END)
        l_entry_edit.delete(0, END)
        h_entry_edit.delete(0, END)
        p_entry_edit.delete(0, END)

    # Button in new_member_frame
    entry_button = Button(member_addition_frame, text='Enter Details', padx=50, command=data)

    # Placing the new_member_frame widgets on the screen
    f_name.grid(row=0, column=0, sticky=W)
    f_entry_edit.grid(row=0, column=1, pady=5, sticky=W)
    l_name.grid(row=1, column=0, sticky=W)
    l_entry_edit.grid(row=1, column=1, pady=5, sticky=W)
    h_number.grid(row=2, column=0, sticky=W)
    h_entry_edit.grid(row=2, column=1, pady=5, sticky=W)
    p_number.grid(row=3, column=0, sticky=W)
    p_entry_edit.grid(row=3, column=1, pady=5, sticky=W)
    entry_button.grid(row=4, column=0, columnspan=2, pady=5)

    # Edit_frame widgets
    id_entry_label = Label(member_edit_frame, text='Enter ID:', font=('Times', 10))
    id_entry_chamber = Entry(member_edit_frame, width=35, font=('Helvetica', 10))

    def window_edit():
        global f_entry_edit
        global l_entry_edit
        global p_entry_edit
        global h_entry_edit
        editing_root = Tk()
        editing_root.title('Editing Member Info')
        #editing_root.iconbitmap('C:/Users/malik/Desktop/Code/OneMinute/one minute.ico')

        entered_id = id_entry_chamber.get()
        member_database_cursor.execute("SELECT * FROM info3 WHERE oid= " + entered_id)
        editing_details = member_database_cursor.fetchall()
        print(editing_details)

        # Function for exiting window
        def editing_window():
            editing_root.destroy()

        # creating the entry and labels
        f_name_edit = Label(editing_root, text='First Name:', font=('Times', 10))
        l_name_edit = Label(editing_root, text='Last Name:', font=('Times', 10))
        h_number_edit = Label(editing_root, text='House Number:', font=('Times', 10))
        p_number_edit = Label(editing_root, text='Phone Number:', font=('Times', 10))
        f_entry_edit = Entry(editing_root, width=35, font=('Helvetica', 10))
        l_entry_edit = Entry(editing_root, width=35, font=('Helvetica', 10))
        h_entry_edit = Entry(editing_root, width=35, font=('Helvetica', 10))
        p_entry_edit = Entry(editing_root, width=35, font=('Helvetica', 10))

        def saving_edited_info():
            member_database_cursor.execute("""UPDATE info3 SET
                              F_Name = :first,
                              L_Name = :last,
                              House_Number = :house,
                              Phone_Number = :phone      


                              WHERE House_Number = :house""",
                                           {
                                              'first': f_entry_edit.get(),
                                              'last': l_entry_edit.get(),
                                              'house': h_entry_edit.get(),
                                              'phone': p_entry_edit.get()
                                           })

            # Commit and close
            member_database_access.commit()

        edit_entry_button = Button(editing_root, text='Save Details', padx=50, command=saving_edited_info)
        edit_exit_button = Button(editing_root, text='Exit', padx=50, command=editing_window)

        # placing edit_window widgets on the screen
        f_name_edit.grid(row=0, column=0, sticky=W)
        f_entry_edit.grid(row=0, column=1, sticky=W)
        l_name_edit.grid(row=1, column=0, sticky=W)
        l_entry_edit.grid(row=1, column=1, sticky=W)
        h_number_edit.grid(row=2, column=0, sticky=W)
        h_entry_edit.grid(row=2, column=1, sticky=W)
        p_number_edit.grid(row=3, column=0, sticky=W)
        p_entry_edit.grid(row=3, column=1, sticky=W)
        edit_entry_button.grid(row=4, column=0, columnspan=2, pady=5)
        edit_exit_button.grid(row=5, column=0, columnspan=2)
        if len(editing_details) == 0 or id_entry_chamber.get() == str():
            editing_root.destroy()
            root_info = Tk()
            root_info.title('Error')
            #root_info.iconbitmap('C:/Users/malik/Desktop/Code/OneMinute/one minute.ico')
            label_error = Label(root_info, text='Non-existent number \nPlease try again', font=('Helvetica', 30))
            label_error.grid(row=0, column=0, sticky=N + E + W + S)
            root_info.mainloop()
        else:
            for edit_detail in editing_details:
                f_entry_edit.insert(0, edit_detail[0])
                l_entry_edit.insert(0, edit_detail[1])
                h_entry_edit.insert(0, edit_detail[2])
                p_entry_edit.insert(0, edit_detail[3])

    def deleting_member_info():  # Deleting record
        member_database_cursor.execute('DELETE FROM info3 WHERE oid=' + id_entry_chamber.get())
        member_database_access.commit()
        id_entry_chamber.delete(0, END)

    def refreshing_member_list():
        from tkinter import ttk
        refreshed_member_info_list = ttk.Treeview(root_member_details)
        # Creating columns
        refreshed_member_info_list['columns'] = ('ID', 'Name', 'House Number', 'Phone Number')
        # Formatting columns
        refreshed_member_info_list.column('#0', width=2, minwidth=0)
        refreshed_member_info_list.column('ID', width=50)
        refreshed_member_info_list.column('Name', width=180, anchor=W)
        refreshed_member_info_list.column('Phone Number', width=130, anchor=E)
        refreshed_member_info_list.column('House Number', width=120, anchor=CENTER)
        # Naming column headings
        refreshed_member_info_list.heading('#0', text='')
        refreshed_member_info_list.heading('ID', text='ID')
        refreshed_member_info_list.heading('Name', text='Name', anchor=W)
        refreshed_member_info_list.heading('House Number', text='House Number', anchor='center')
        refreshed_member_info_list.heading('Phone Number', text='Phone Number', anchor=E)
        # Sorting out data
        member_database_cursor.execute('SELECT *, oid FROM info3')
        refreshed_member_details = member_database_cursor.fetchall()
        print(refreshed_member_details)
        refreshed_list_counter = 0
        while refreshed_list_counter <= (len(refreshed_member_details) - 1):
            for refreshed_detail in refreshed_member_details:
                refreshed_member_info_list.insert(parent='', index='end', iid=refreshed_list_counter, text='',
                                                  values=(refreshed_detail[4], str(refreshed_detail[0] + ' ' +
                                                                                   refreshed_detail[1]),
                                                          refreshed_detail[2], refreshed_detail[3]))
                refreshed_list_counter += 1

        refreshed_member_info_list.grid(row=0, column=0)

    member_list_refresh_button = Button(root_member_details, text='Refresh',
                                        command=refreshing_member_list)  # Refresh button
    enter_button = Button(member_edit_frame, text='Edit Details', padx=40, command=window_edit)
    delete_button = Button(member_edit_frame, text='Delete', command=deleting_member_info)
    # Putting on the screen
    member_list_refresh_button.grid(row=1, column=0)
    delete_button.grid(row=2, column=0, columnspan=2)
    enter_button.grid(row=1, column=0, columnspan=2)
    id_entry_chamber.grid(row=0, column=1, sticky=W)
    id_entry_label.grid(row=0, column=0, sticky=W)

    root_member_details.mainloop()


# Checkboxes on the main screen
def main_screen_checkboxes():
    root.geometry('700x620')
    global checkbox_variables_2
    global checked_people_list
    checkbox_open_button.destroy()
    checkbox_variables_1 = {
        'f1': StringVar(),
        'f2': StringVar()
    }

    checkbox_variables_2 = {
        'Malik Williams': checkbox_variables_1['f1'],
        'Irene Mwaniki': checkbox_variables_1['f2']
    }

    checkbox_database_access = sqlite3.connect('Member_Dets.db')
    checkbox_database_cursor = checkbox_database_access.cursor()
    checkbox_database_cursor.execute('SELECT *,oid FROM info3')
    fetched_checkbox_info = checkbox_database_cursor.fetchall()
    for checkbox_info in fetched_checkbox_info:
        checkbox_variables_2[str(checkbox_info[0] + ' ' + checkbox_info[1])] = StringVar()

    checkbox_counter = 0
    while checkbox_counter < len(checkbox_variables_2):
        for x, y in checkbox_variables_2.items():
            button_configuration = Checkbutton(frame2, text=x, variable=y, onvalue='Present', offvalue='Absent').grid(
                row=checkbox_counter, column=0)
            button_configuration = Checkbutton(frame2, text=x, variable=y, onvalue='Present',
                                               offvalue='Absent').deselect()
            checkbox_counter += 1

    def checkbox_checked():
        global checked_people_list
        submit_button.destroy()
        checked_people_list = []
        for x3, y3 in checkbox_variables_2.items():
            checked_people_list.append(y3.get())
        print(checked_people_list)
        print(checkbox_variables_2.items())

    submit_button = Button(frame2, text='Submit', command=checkbox_checked)
    submit_button.grid(row=checkbox_counter+1, column=0)


def open_writing_window():  # Function for Start writing button
    global checkbox_variables_2
    global text_box
    global checked_people_list

    root_writing = Tk()
    root_writing.title('One Minute At A Time')
    #root_writing.iconbitmap('C:/Users/User/Desktop/Code/OneMinute/one minute.ico')
    root_writing.geometry('1020x660')

    # Create Frame1
    frame_test = LabelFrame(root_writing, text='Writing')
    frame_test.grid(row=0, column=0)
    # Creating canvas
    cav = Canvas(frame_test, width=1000, height=500)
    cav.grid(sticky=W)
    # Creating the scrollbar
    scroll_test = Scrollbar(frame_test, orient='vertical', command=cav.yview)
    scroll_test.grid(sticky=E + N + S, row=0, rowspan=100)
    # Configuring canvas
    cav.configure(yscrollcommand=scroll_test.set)
    # Creating another frame within the canvas
    frame_in = Frame(cav)
    frame_in.grid(row=0, column=0)
    cav.create_window((0, 0), window=frame_in, anchor='n')
    cav.bind('<Configure>', lambda screen: cav.configure(scrollregion=cav.bbox('all')))

    #  Attendance Setup
    member_access_writing = sqlite3.connect('Member_Dets.db')
    member_access_writing_cursor = member_access_writing.cursor()
    member_access_writing_cursor.execute('SELECT *,oid FROM info3')
    caught_member_info = member_access_writing_cursor.fetchall()
    att = Label(frame_in, text='ATTENDANCE:', font=('Helvetica', 10))
    att.grid(row=0, column=0)

    sc1 = Scrollbar(frame_in)
    sc1.grid(row=0, column=2, sticky=E + N + S)

    att_text = Text(frame_in, width=90, height=20, relief='groove', wrap='word', yscrollcommand=sc1.set)
    att_text.grid(row=0, column=1, pady=40, sticky=N)
    egg_count = float(1)
    print(float(len(checked_people_list)))
    while egg_count < float(len(checked_people_list)):
        for name, status in checkbox_variables_2.items():
            att_text.insert(egg_count, name + '\t' + status + '\n')

    sc1.config(command=att_text.yview)

    # Agendas' setup
    tag = Label(frame_in, text='AGENDAS:', font=('Helvetica', 10))
    tag.grid(row=1, column=0, sticky=W)

    sc = Scrollbar(frame_in)
    sc.grid(row=1, column=2, sticky=E + N + S)

    text_box = Text(frame_in, width=90, height=20, relief='groove', wrap='word', yscrollcommand=sc.set)
    text_box.grid(row=1, column=1, sticky=W)

    sc.config(command=text_box.yview)

    test_fr = LabelFrame(frame_test, text='Names', padx=40)
    test_fr.grid(row=1, column=0, pady=20, sticky=W)

    test_lab = Label(test_fr, text='Chairman:')
    entry_chair = Entry(test_fr)
    entry_chair.grid(row=0, column=1)
    test_lab.grid(row=0, column=0)

    date_lab = Label(test_fr, text='Date:')
    date_lab.grid(row=2, column=0)
    date_entry = Entry(test_fr)
    date_entry.insert(0, date.today())
    date_entry.grid(row=2, column=1)

    test_lab2 = Label(test_fr, text='Secretary:')
    sec_entry = Entry(test_fr)
    sec_entry.grid(row=1, column=1)
    test_lab2.grid(row=1, column=0)

    # Minutes setup
    tag2 = Label(frame_in, text='MINUTES:', font=('Helvetica', 10))
    tag2.grid(row=2, column=0, sticky=W)

    sc2 = Scrollbar(frame_in)
    sc2.grid(row=2, column=2, sticky=E + N + S)

    text_box2 = Text(frame_in, width=90, height=20, relief='groove', wrap='word', yscrollcommand=sc2.set)
    text_box2.grid(row=2, column=1, pady=40, sticky=W)

    sc2.config(command=text_box2.yview)

    # AOB setup
    tag3 = Label(frame_in, text='AOB:', font=('Helvetica', 10))
    tag3.grid(row=3, column=0, sticky=W)

    sc3 = Scrollbar(frame_in)
    sc3.grid(row=3, column=2, sticky=E + N + S)

    text_box3 = Text(frame_in, width=90, height=20, relief='groove', wrap='word', yscrollcommand=sc3.set)
    text_box3.grid(row=3, column=1, pady=40, sticky=W)
    sc3.config(command=text_box3.yview)

    # Button to save the minutes and function to destroy window

    def save_minutes():
        """"
        Some of the file functions are:
        r+:read and write(beginning of file)
        r:read only
        w:write only(overwritten)
        w+:write and read(overwritten)
        a:append only(end of file) 
        a+:append and read(end of file)

        """
        root_save = Tk()
        root_save.geometry('200x200')
        root_entry = Entry(root_save)
        root_chose = (str(root_entry.get()) + '.txt ')

        def finish():
            root_save.destroy()
            word = open(root_chose, 'w')
            word.write(text_box.get(1.0, END) + '\n' + text_box2.get(1.0, END) + '\n' + text_box3.get(1.0, END) + '\n'
                       + (entry_chair.get() + '\n') + (sec_entry.get() + '\n') + date_entry.get())
            word.close()
            os.startfile(root_chose)
        root_button = Button(root_save, text='Save', command=finish)
        root_entry.grid(row=0, column=0)
        root_button.grid(row=1, column=0)

    save_button = Button(frame_test, text='Save Minutes', padx=30, command=save_minutes)
    save_button.grid(row=1, column=0, pady=10)
    root_writing.mainloop()


# Buttons On the first frame
member_info_button = Button(frame, text='Member Info', command=member_details_button)
events_list_button = Button(frame, text='Events', command=event_all)
previous_minutes_button = Button(frame, text='Open Previous Minutes', command=show_file)
start_meeting_button = Button(frame, text='Start Meeting', command=open_writing_window
                              , padx=40)  # Button to go to the another window and start writing

info_info = Label(
    frame_info,
    text='Start Meeting -->Click the button only after filling in the attendance list \n'
         'Member Info -->Click to see all members\' details and edit them if need be\n'
         'Events -->Click to see the events scheduled, add, edit or delete an even\n'
         'Open Previous Minutes -->Click to open the previous minutes which will be saved in a common folder'
)

# Buttons in frame 2 Onto Screen
member_info_button.grid(row=3, column=0)
events_list_button.grid(row=1, column=0)
previous_minutes_button.grid(row=2, column=0)
start_meeting_button.grid(row=0, column=0)
info_info.grid(row=0, column=0)
checkbox_open_button = Button(frame2, text='Open', command=main_screen_checkboxes)

# Checkboxes onto screen
checkbox_open_button.grid(row=0, column=0, sticky='news')

# Committing and closing
main_member_database_access.commit()

root.mainloop()
