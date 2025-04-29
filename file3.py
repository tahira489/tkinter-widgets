from tkinter import *

window=Tk()
window.title("root window")
window.geometry("200x200")

def topwin():
    top = Toplevel()
    top.title("topwindow")
    top.geometry("300x300")
    label = Label(top, text = "this is my toplevel window")
    label.pack()

    top.mainloop()

button = Button(window, text= " click here to openanother window" ,command=topwin)
button.pack()

window.mainloop()