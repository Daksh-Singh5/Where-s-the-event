from tkinter import *
window = Tk()
window.title("Event handler")
window.geometry("300x400")

def keyevent(event):
    print(event.char)

window.bind("<Key>",keyevent)

def clickEvent(event):
    print("\n The button was clicked")

button = Button(text="Click Here")
button.pack()

button.bind("<Button-1>", clickEvent)

window.mainloop()

