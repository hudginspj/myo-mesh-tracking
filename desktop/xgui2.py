from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()

w, h = top.winfo_screenwidth(), top.winfo_screenheight()
# use the next line if you also want to get rid of the titlebar
top.overrideredirect(1)
top.geometry("%dx%d+0+0" % (w, h))


def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
B.place(bordermode=OUTSIDE, height=100, width=100)
top.mainloop()