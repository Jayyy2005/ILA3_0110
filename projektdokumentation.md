## Informieren

### User Stories

| US-№ | Verbindlichkeit | Art          | Beschreibung                                                       |
| ---- | --------------- | ------------ | ------------------------------------------------------------------|
| 0    | Muss            | Funktional   | Als User muss ich in der Lage sein, die App zu steuern. |
| 1    | Muss            | Funktional   | Als User muss ich in der Lage sein, Kontakte zu erstellen. |
| 2    | Muss            | Funktional   | Als User muss ich in der Lage sein, vorhandene Kontakte zu verwalten. |
| 3    | Muss            | Funktional   | Als User werde ich über Fehlermeldungen informiert. |
| 4    | Muss            | Funktional   | Als User muss ich in der Lage sein, Kontakten zu speichern. |
| 5    | Muss            | Funktional   | Als User habe ich die Möglichkeit, mich über die App zu informieren. |



### Testfälle

| Testfall-Nummer | Ausgangslage                                  | Eingabe                                        | Erwartete Ausgabe                                                      |
| --------------- | --------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------- |
| 0.1             | Der Benutzer öffnet die App.                  | Doppelklick auf das Programm.                  | Die Startseite wird angezeigt.                                         |
| 0.2             | Der Benutzer beendet die App.                 | Klick auf "X".                | Die App wird beendet.                                                  |
| 1.1             | Der Benutzer erstellt einen Kontakt.| Eingabefeldern ausfüllen und Klick auf "Erstellen"-Button. | Kontakt wird in der Kontaktliste angezeigt.                   |
| 2.1             | Der Benutzer möchte vorhandene Kontakte verwalten.    | Kontakt auswählen und Klick auf "Bearbeiten"-Button.             | Ein Pop-Up Formular zur Bearbeitung der Kontaktinformationen wird angezeigt. |
| 2.2             | Der Benutzer möchte einen Kontakt Löschen.    | Im Pop-Up auf "Löschen"-Button klicken.             | Ein Pop-Up Formular zur Bearbeitung der Kontaktinformationen wird angezeigt. |
| 3.1             | Der Benutzer erstellt einen vorhandenen Kontakt (Name).    | Eingabefeldern (vorhandene Name) ausfüllen und Klick auf "Erstellen"-Button.              | Fehlermeldung wird angezeigt. |
| 3.1             | Der Benutzer erstellt einen Kontakt ohne Name.    | Eingabefeldern leer lassen und Klick auf "Erstellen"-Button.              | Fehlermeldung wird angezeigt. |
| 3.2             | Der Benutzer bearbeitet Kontaktinformationen. | Klick auf den "Bearbeiten"-Button.             | Ein Formular zur Bearbeitung der Kontaktinformationen wird angezeigt.  |
| 3.2             | Der Benutzer löscht einen Kontakt.            | Klick auf den "Löschen"-Button.                | Der Kontakt wird aus der Liste entfernt.                               |
| 4.1             | Der Benutzer möchte die Kontaktliste speichern.       | Klick auf "Speichern"                               | Kontaktliste wird im Download-Ordner gespeichert.                                     |
| 5.1             | Der Benutzer möchte über die App wissen         | Klick auf Info Icon             | Pop-Up wird geöffnet und Informationen werden angezeigt.                                            |

## Planen


| AP-№ | Zuständig | Beschreibung                            | Geplante Zeit | Frist        |
| ---- | --------- | --------------------------------------- | ------------- | ------------ |
| 0.0  | Raviraj   | Erstellung der Projektdokumentation    | 3 Stunden     | 16.08.2024   |
| 1.A  | Raviraj   | Recherchieren von Python     | 1 Stunde     | 16.08.2024  |
| 2.A  | Raviraj   | Kontaktliste Basisfunktionen         | 1 Stunde    | 16.08.2024   |
| 3.A  | Raviraj   | GUI Anpassen  | 1 Stunde | 16.08.2024   |
| 3.B  | Raviraj   | JSON für Speicherung | 2 Stunden | 16.08.2024   |
| 4.A  | Raviraj   | Kontaktliste erweitern         | 2 Stunden     | 16.08.2024   |
| 5.A  | Raviraj   | Mahara Portfolio erstellen        | 1 Stunde    | 16.08.2024   |
| 5.B  | Raviraj   | Projektdokumentation        | 1 Stunde    | 16.08.2024   |

## 3 Entscheiden

Keine

## 4 Realisieren

| AP-№ | Zuständig | Geplante Zeit | Tatsächliche Zeit | Datum      |
| ---- | --------- | ------------- | ----------------- | ---------- |
| 0.0  | Raviraj   | 2 Stunden      | 2 Stunden         | 16.08.2024 |
| 1.A  | Raviraj   | 1 Stunde      | 1 Stunde      | 16.08.2024 |
| 2.A  | Raviraj   | 1 Stunde      | 1 Stunde         | 16.08.2024 |
| 3.A  | Raviraj   | 1 Stunde      | 1 Stunde        | 16.08.2024 |
| 3.B  | Raviraj   | 2 Stunden      | 2 Stunden         | 16.08.2024 |
| 4.A  | Raviraj   | 1 Stunde     | 1 Stunde        | 16.08.2024 |
| 5.A  | Raviraj   | 1 Stunde      | 1 Stunde         | 16.08.2024 |
| 5.B  | Raviraj   | 1 Stunde      | 1 Stunde         | 16.08.2024 |

## 5 Kontrollieren

### Testprotokoll

| Testfall-№ | Resultat | Tester  | Datum     |
| -----------| ---------| --------| ----------|
| 0.1        | OK       | Raviraj | 01.11.2024|
| 1.1        | OK       | Raviraj | 16.08.2024|
| 2.1        | OK       | Raviraj | 16.08.2024|
| 2.2        | OK       | Raviraj | 16.08.2024|
| 3.1        | OK       | Raviraj | 16.08.2024|
| 3.2        | OK       | Raviraj | 16.08.2024|
| 4.1        | OK       | Raviraj | 16.08.2024|
| 4.2        | OK       | Raviraj | 16.08.2024|
| 5.1        | OK       | Raviraj | 16.08.2024|
| 6.1        | OK       | Raviraj | 16.08.2024|

