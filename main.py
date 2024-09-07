from tkinter import *
from tkinter import messagebox
from ctypes import windll, byref, sizeof, c_int
from contact_manager import AddContact, UpdateDetail, Delete_Entry, VIEW, Select_set

# Main Window
root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title('Kontaktverwalter - © 2024 Sanjay Raviraj')
root.config(bg="black") 

HWND = windll.user32.GetParent(root.winfo_id())
title_bar_color = 0x00FF0000
title_text_color = 0x0000FF99
windll.dwmapi.DwmSetWindowAttribute(HWND, 
35, 
byref(c_int(title_bar_color)),
sizeof(c_int))

windll.dwmapi.DwmSetWindowAttribute(HWND, 
35, 
byref(c_int(title_text_color)),
sizeof(c_int))

Name = StringVar()
Number = StringVar()

# Frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Arial', 16), bg="gray", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Design
Label(root, text='Name', font=("Arial", 22, "bold"), bg="black", fg="white").place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Telefon', font=("Arial", 20, "bold"), bg="black", fg="white").place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text="Hinzufügen", font='Arial', bg='light green', width=10, command=lambda: AddContact(Name, Number, select)).place(x=50, y=140)
Button(root, text="Löschen", font='Arial', bg='red', width=10, command=lambda: Delete_Entry(select)).place(x=50, y=200)
Button(root, text="Ansehen", font='Arial', bg='gray', width=10, command=lambda: VIEW(Name, Number, select)).place(x=50, y=325)
Button(root, text="Bearbeiten", font='Arial', bg='gray', width=10, command=lambda: UpdateDetail(Name, Number, select)).place(x=50, y=260)

# Listbox with contacts
Select_set(select)

root.mainloop()
