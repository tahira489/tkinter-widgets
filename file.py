from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('my image')
root.geometry('300x300')

upload = Image.open("photo.jpg")
image = ImageTk.PhotoImage(upload)

label = Label(root, image = image, height=300, width=280)
label.place(x=20, y=0)

root.mainloop()