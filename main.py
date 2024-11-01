from tkinter import *
from tkinter import messagebox
import json
import os
from contact_manager import AddContact, create_edit_popup, update_contact_list, validate_phone_input, contactlist, download_contacts

# Eingabefelder leeren
def clear_inputs():
    Name.set("")
    Number.set("")
    Email.set("")

# Hauptfenster
root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title('Konpy')

# Linker Frame 
left_frame = Frame(root, bg="#f0f0f0")  # Heller Hintergrund
left_frame.place(relwidth=0.5, relheight=1)

# Rechter Frame 
right_frame = Frame(root, bg="#d0d0d0")  # Dunklerer Hintergrund
right_frame.place(relx=0.5, relheight=1, relwidth=0.5)

# Variablen für Kontaktdaten
Name = StringVar()
Number = StringVar()
Email = StringVar()
selected_contact_info = StringVar(value="\nWählen Sie einen Kontakt aus.\n")

# Titel
Label(left_frame, text='Konpy', font=("Arial", 28, "bold"), bg="#f0f0f0", fg="black").place(x=30, y=10)

Label(left_frame, text='Neuer Kontakt', font=("Arial", 16), bg="#f0f0f0", fg="black").place(x=30, y=110)

# Eingabeframe
input_frame = Frame(left_frame, bg="#f0f0f0")
input_frame.place(x=30, y=150)

buttonleft_frame = Frame(left_frame, bg="#f0f0f0")
buttonleft_frame.place(x=30, y=300)

# Eingabeelemente
Label(input_frame, text='Name', font=("Arial", 12), bg="#f0f0f0", fg="black").grid(row=0, column=0, pady=10)
Entry(input_frame, textvariable=Name, width=30).grid(row=0, column=1, pady=10, padx=10)
Label(input_frame, text='Telefon', font=("Arial", 12), bg="#f0f0f0", fg="black").grid(row=1, column=0, pady=10)
phone_entry = Entry(input_frame, textvariable=Number, width=30, validate="key")
phone_entry['validatecommand'] = (root.register(validate_phone_input), '%S')
phone_entry.grid(row=1, column=1, pady=10)
Label(input_frame, text='E-Mail', font=("Arial", 12), bg="#f0f0f0", fg="black").grid(row=2, column=0, pady=10)
Entry(input_frame, textvariable=Email, width=30).grid(row=2, column=1, pady=10)

# Buttons zum Hinzufügen von Kontakten
Button(buttonleft_frame, text="Erstellen", font='Arial', width=10,
       command=lambda: AddContact(Name, Number, Email, select)).grid(row=4, column=0, pady=10)

# Button zum Leeren der Eingaben
Button(buttonleft_frame, text="Leeren", font='Arial', width=10,
       command=clear_inputs).grid(row=4, column=1, pady=10, padx=10)

# Label für ausgewählte Kontaktinformation
selected_contact_frame = LabelFrame(right_frame, text="Kontaktinformation", font=("Arial", 16), bg="#d0d0d0", fg="black")
selected_contact_frame.pack(pady=20, fill=X, padx=10)
selected_contact_label = Label(selected_contact_frame, textvariable=selected_contact_info, font=("Arial", 12), bg="#d0d0d0", fg="black", wraplength=300, justify="left", padx=10, pady=10, anchor='w')
selected_contact_label.pack(fill=X)

# Listbox für Kontakte
scroll = Scrollbar(right_frame)
select = Listbox(right_frame, yscrollcommand=scroll.set, font=('Arial', 16), bg="#d0d0d0", width=20, height=15, borderwidth=3, relief="groove", selectmode="browse")
scroll.config(command=select.yview)
select.pack(side=LEFT, fill=BOTH, pady=20, padx=10)

# Funktion zur Aktualisierung der Kontaktinformation
def update_selected_contact_info(event):
    selected_index = select.curselection()
    if selected_index:
        contact = contactlist[selected_index[0]]  # Ausgewählten Kontakt holen
        selected_contact_info.set(f"Name: {contact['name']}\nTelefon: {contact['phone']}\nE-Mail: {contact['email']}")

# Auswahlereignis binden
select.bind('<<ListboxSelect>>', update_selected_contact_info)

# Listbox mit bestehenden Kontakten füllen
update_contact_list(select)

# Frame für Buttons unter der Kontaktansicht
button_frame = Frame(right_frame, bg="#d0d0d0")
button_frame.pack(side=TOP, pady=10)

# Button zum Bearbeiten hinzufügen
Button(button_frame, text="Bearbeiten", font='Arial', width=10,
       command=lambda: create_edit_popup(select.curselection()[0], select) if select.curselection() else None).pack(side=TOP, padx=5, pady=5)


# Button zum Speichern hinzufügen
Button(button_frame, text="Speichern", font='Arial', width=10,
       command=lambda: download_contacts(contactlist)).pack(side=BOTTOM, padx=5, pady=5)

Label(right_frame, text='© 2024 - Sanjay Raviraj', font=("Arial", 7), bg="#d0d0d0", fg="black").place(x=280, y=560)

# Info-Icon
info_icon = PhotoImage(file="info_icon.png")  
info_button = Button(root, image=info_icon, command=lambda: messagebox.showinfo("Information", "Kontaktverwalter App\nLernatelier Projekt von Sanjay Raviraj\nsanjayraviraj2005@gmail.com\n"), bd=0)
info_button.place(x=50, y=550)

# Anwendung starten
root.mainloop()
