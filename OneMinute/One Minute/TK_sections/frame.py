from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title('Framing')

frame = LabelFrame(root, text='Framing', padx=10, pady=10)
frame.pack(padx=5, pady=5)

butt = Button(frame, text='I see')
butt2 = Button(frame, text='click and see')

butt.grid(row=0,column=0)
butt2.grid(row=0,column=1)

root.mainloop()
