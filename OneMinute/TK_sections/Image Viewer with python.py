from tkinter import * # Calling the module to help with the widgets
from PIL import ImageTk, Image # Module for working with images in tkinter


root = Tk()
root.title('Malo works') #Title of the screen 
root.iconbitmap(bitmap='C:/Users/HP/Documents/malo\'s/download.ico') #Having an icon for the window(changeable)

# Packing an image onto the screen after calling it
my_img1=ImageTk.PhotoImage(Image.open('C:/Users/HP/Documents/malo\'s/astro/astro1.jpg'))
my_img2 =ImageTk.PhotoImage(Image.open('C:/Users/HP/Documents/malo\'s/astro/astro2.jpg'))
my_img3 =ImageTk.PhotoImage(Image.open('C:/Users/HP/Documents/malo\'s/astro/astro3.jpg'))
my_img4 =ImageTk.PhotoImage(Image.open('C:/Users/HP/Documents/malo\'s/astro/malo.jpg'))



#List with the images to be iterated through
img_list = [my_img1, my_img2, my_img3, my_img4]

   #Status Bar
status = Label(root, text='Image 1 of' + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_pic = Label(image=my_img1)
my_pic.grid(row=0, column=0, columnspan=3)
#Functions for my_back and my_forward functionality
def forward(image_number):
    global current
    global my_pic
    global my_forward
    global my_back

    
     # Status Bar

    status = Label(root, text='Image' + str((image_number+1)) + 'of' + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    my_pic.grid_forget()# Removes the prior image
    
    my_pic = Label(image=img_list[image_number])
    my_forward = Button(root, text='>>', command=lambda:forward(image_number+1))
    my_back = Button(root, text='<<', command=lambda:back(image_number-1))

    if image_number == 3:
        my_forward =Button(root, text='>>', state=DISABLED)

    my_pic.grid(row=0, column=0, columnspan=3)
    my_forward.grid(row=1, column=2)
    my_back.grid(row=1, column=0)

    
    
def back(image_number):
    global current
    global my_pic
    global my_forward
    global my_back
      
     #Status Bar
    status = Label(root, text='Image' + str((image_number + 1)) + 'of' + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    my_pic.grid_forget()#Removes the prior image

    my_pic = Label(image=img_list[image_number])
    my_forward = Button(root, text='>>', command=lambda:forward(image_number+1))
    my_back = Button(root, text='<<', command=lambda:back(image_number-1))

    if image_number == 0:
        my_back = Button(root, text='<<', state=DISABLED)
        
    my_pic.grid(row=0, column=0, columnspan=3)
    my_forward.grid(row=1, column=2)
    my_back.grid(row=1, column=0)
   

my_forward = Button(root, text='>>', command=lambda:forward(1))#Button to move to the next image
my_exit = Button(root, text='Exit Image Viewer', command=root.destroy)#Button to be able to exit the Screen
my_back = Button(root, text='<<', command=lambda:back(1),state=DISABLED) #Button to go back to the previous image

#Shoving to screen
my_forward.grid(row=1, column=2, pady=10)
my_back.grid(row=1, column=0)
my_exit.grid(row=1, column=1)


#Keeping the screen running 
root.mainloop()
