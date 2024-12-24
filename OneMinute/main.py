from tkinter import *
import sqlite3
from datetime import date
from tkinter import filedialog
import os
from event_editing import event_all
from member_info import member_details_button

# Global Variables
global checkbox_variables_2
global text_box
global checked_people_list
checked_people_list = []
global f_entry_edit
global l_entry_edit
global p_entry_edit
global h_entry_edit

# Creating database for member
main_member_database_access = sqlite3.connect('Member_Dets.db')
main_member_database_cursor = main_member_database_access.cursor()

# Configuring main window
root = Tk()
root.iconbitmap('one minute.ico')
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



def show_file():  # Function for show events button
    filedialog.askopenfilename(initialdir='C:/Users/malik/Documents', title=('All files', '*.*'))


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
    root_writing.iconbitmap('one minute.ico')
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
    for name, status in checkbox_variables_2.items():
        att_text.insert(egg_count, name + '\t' + status.get() + '\n')

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
        

        def finish():
            root_chose = (root_entry.get() + '.txt ')
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
