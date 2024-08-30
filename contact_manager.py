from tkinter import messagebox
from tkinter import END

# Contactlist
contactlist = [
    ['Person One', '0123'],
    ['Person Two', '0234'],
    ['Person Three', '0345']
]

# Select
def Selected(select):
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
        return None
    else:
        return int(select.curselection()[0])

# Add contact
def AddContact(Name, Number, select):
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set(select)
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")

# Update detail
def UpdateDetail(Name, Number, select):
    index = Selected(select)
    if index is not None:
        if Name.get() and Number.get():
            contactlist[index] = [Name.get(), Number.get()]
            Select_set(select)
            messagebox.showinfo("Confirmation", "Successfully Updated Contact")
        else:
            messagebox.showerror("Error", "Please fill in the information")

# Delete contact
def Delete_Entry(select):
    index = Selected(select)
    if index is not None:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result == True:
            del contactlist[index]
            Select_set(select)

def VIEW(Name, Number, select):
    index = Selected(select)
    if index is not None:
        NAME, PHONE = contactlist[index]
        Name.set(NAME)
        Number.set(PHONE)

def Select_set(select):
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)
