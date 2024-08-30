from tkinter import *
from tkinter import messagebox
from contact_manager import AddContact, UpdateDetail, Delete_Entry, VIEW, Select_set
from utils import EntryReset

# Initialize window
root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title('Contact')

Name = StringVar()
Number = StringVar()

# Create frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Design
Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text="ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=lambda: AddContact(Name, Number, select)).place(x=50, y=140)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=lambda: UpdateDetail(Name, Number, select)).place(x=50, y=200)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=lambda: Delete_Entry(select)).place(x=50, y=260)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=lambda: VIEW(Name, Number, select)).place(x=50, y=325)
Button(root, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=390)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=root.destroy).place(x=250, y=470)

# Initialize listbox with contacts
Select_set(select)

root.mainloop()
