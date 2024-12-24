from tkinter import *
import sqlite3
from datetime import date
from tkinter import filedialog
import os


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
        editing_root.iconbitmap('one minute.ico')

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
            root_info.iconbitmap('one minute.ico')
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


