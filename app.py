from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry(800 x 600)
root.resizable(False, False)
root.title('Contakt')
contactlist = [
    ['Person One', '0123']
    ['Person Two', '0234']
    ['Person Three', '0345']
 ]

Vorname = StringVar()
Nachname = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(fram)