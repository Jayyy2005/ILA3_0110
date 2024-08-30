from tkinter import messagebox
from tkinter import END

# Contactlist
contactlist = [
]

# Select
def Selected(select):
    if len(select.curselection()) == 0:
        messagebox.showerror("Fehler", "Bitte wählen Sie einen Kontakt aus")
        return None
    else:
        return int(select.curselection()[0])

# Add contact
def AddContact(Name, Number, select):
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set(select)
        messagebox.showinfo("Bestätigung", "Neuer Kontakt wurde erfolgreich hinzugefügt!")
    else:
        messagebox.showerror("Fehler", "Bitte füllen Sie aus")

# Update detail
def UpdateDetail(Name, Number, select):
    index = Selected(select)
    if index is not None:
        if Name.get() and Number.get():
            contactlist[index] = [Name.get(), Number.get()]
            Select_set(select)
            messagebox.showinfo("Bestätigung", "Kontaktinformation wurde erfolgreich aktualisiert!")
        else:
            messagebox.showerror("Fehler", "Bitte füllen Sie aus")

# Delete contact
def Delete_Entry(select):
    index = Selected(select)
    if index is not None:
        result = messagebox.askyesno('Bestätigung', 'Möchten Sie wirklich den ausgewählten Kontakt löschen?')
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
