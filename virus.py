from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x400")

def msg():
    messagebox.showwarning("Alert","Stop virus is found")


button = Button(root,text="scan for virus",command=msg)
button.place(x=70,y=80)

root.mainloop()