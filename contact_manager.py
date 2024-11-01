import json
import os
from tkinter import messagebox, Toplevel, Label, Entry, Button, StringVar, END

# Dateipfad zum Speichern von Kontakten
CONTACTS_FILE = "contacts.json"

# Kontakte aus JSON laden und alphabetisch sortieren
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Kontakte in JSON speichern
def save_contacts(contactlist):
    with open(CONTACTS_FILE, 'w') as file:
        # Kontakte vor dem Speichern sortieren
        sorted_contacts = sorted(contactlist, key=lambda c: c["name"].lower())
        json.dump(sorted_contacts, file, indent=4)

# Kontakte laden und sortieren
contactlist = sorted(load_contacts(), key=lambda c: c["name"].lower())

# Eingabe für Telefonnummer validieren (nur Ziffern)
def validate_phone_input(char):
    return char.isdigit() or char == ""  # Nur Ziffern und leer zulassen

# Überprüfen, ob ein Name bereits existiert
def is_duplicate_name(name):
    return any(contact["name"].lower() == name.lower() for contact in contactlist)

# Neuen Kontakt hinzufügen (Name erforderlich; Telefon und E-Mail optional)
def AddContact(Name, Number, Email, select):
    if Name.get():  # Nur überprüfen, ob das Namensfeld ausgefüllt ist
        if is_duplicate_name(Name.get()):
            messagebox.showerror("Fehler", "Dieser Name existiert bereits.")
            return
        contactlist.append({
            "name": Name.get(),
            "phone": Number.get() if Number.get() else "",
            "email": Email.get() if Email.get() else ""
        })
        save_contacts(contactlist)
        update_contact_list(select)
        messagebox.showinfo("Bestätigung", "Neuer Kontakt wurde erfolgreich hinzugefügt!")
    else:
        messagebox.showerror("Fehler", "Bitte füllen Sie das Namensfeld aus.")

# Popup-Fenster zum Bearbeiten eines Kontakts erstellen
def create_edit_popup(index, select):
    popup = Toplevel()
    popup.title("Kontakt bearbeiten")
    popup.geometry("400x400")
    popup.resizable(False, False)  # Grössenänderung deaktivieren

    contact = contactlist[index]  # Ausgewählten Kontakt abrufen
    
    Label(popup, text="Name", font=("Arial", 12)).pack(pady=10)
    name_entry = Entry(popup, width=30)
    name_entry.insert(0, contact['name'])
    name_entry.pack()

    Label(popup, text="Telefon", font=("Arial", 12)).pack(pady=10)
    phone_entry = Entry(popup, width=30)
    phone_entry.insert(0, contact['phone'])
    phone_entry['validatecommand'] = (popup.register(validate_phone_input), '%S')
    phone_entry.pack()

    Label(popup, text="E-Mail", font=("Arial", 12)).pack(pady=10)
    email_entry = Entry(popup, width=30)
    email_entry.insert(0, contact['email'])
    email_entry.pack()

    # Funktion zum Speichern des bearbeiteten Kontakts
    def save_edited_contact():
        if name_entry.get():  # Nur überprüfen, ob das Namensfeld ausgefüllt ist
            if is_duplicate_name(name_entry.get()) and name_entry.get() != contact['name']:
                messagebox.showerror("Fehler", "Dieser Name existiert bereits.")
                return
            contactlist[index] = {
                "name": name_entry.get(),
                "phone": phone_entry.get(),
                "email": email_entry.get()
            }
            save_contacts(contactlist)
            update_contact_list(select)
            messagebox.showinfo("Bestätigung", "Kontakt erfolgreich aktualisiert!")
            popup.destroy()
        else:
            messagebox.showerror("Fehler", "Bitte füllen Sie das Namensfeld aus.")

    # Speichern-Button hinzufügen
    Button(popup, text="Speichern", command=save_edited_contact).pack(pady=20)

    # Funktion zum Löschen des Kontakts
    def delete_contact():
        if messagebox.askyesno("Bestätigung", "Sind Sie sicher, dass Sie diesen Kontakt löschen möchten?"):
            del contactlist[index]  # Kontakt aus der Liste entfernen
            save_contacts(contactlist)  # Aktualisierte Liste speichern
            update_contact_list(select)  # Listbox aktualisieren
            messagebox.showinfo("Bestätigung", "Kontakt erfolgreich gelöscht!")
            popup.destroy()  # Popup schliessen

    # Löschen-Button hinzufügen
    Button(popup, text="Löschen", command=delete_contact, bg="red", fg="white").pack(pady=5)

# Kontaktliste in der Listbox aktualisieren
def update_contact_list(select):
    select.delete(0, END)  # Listbox leeren
    # Kontakte alphabetisch sortieren vor der Anzeige
    sorted_contacts = sorted(contactlist, key=lambda c: c["name"].lower())
    for contact in sorted_contacts:
        select.insert(END, contact["name"])

# Funktion zum Speichern der Kontakte in einer Textdatei
def download_contacts(contactlist):
    if contactlist:
        # Pfad für die Textdatei im Downloads-Ordner
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "downloaded_contacts.txt")
        
        try:
            # Öffnen der Datei und Schreiben der Kontaktdaten im Textformat
            with open(downloads_path, 'w') as file:
                for contact in contactlist:
                    # Format: Name - Telefon - E-Mail
                    file.write(f"Name: {contact['name']}\nTelefon: {contact['phone']}\nE-Mail: {contact['email']}\n\n")
            
            # Erfolgsnachricht anzeigen
            messagebox.showinfo("Download", f"Kontakte erfolgreich gespeichert als '{downloads_path}'")
        
        except Exception as e:
            # Fehlernachricht anzeigen
            messagebox.showerror("Fehler", f"Fehler beim Speichern der Datei: {str(e)}")
    else:
        messagebox.showwarning("Warnung", "Keine Kontakte zum Speichern vorhanden.")

