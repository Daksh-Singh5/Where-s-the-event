import tkinter as tk


def ferinheitTOCelsius():
    ferinhiet = ent_temprature.get()
    celsius = (5/9)*(float(ferinhiet)-32)
    Result["text"] = f"{round(celsius,2)} /N{degree celsius}"

window = tk.Tk()
window.title("covertor")
window.resizable(width=False,height=False)


frmEntry = tk.Frame(master=window)
ent_temprature = tk.Entry(master=frmEntry, width=10)
