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
| 2.2             | Der Benutzer möchte einen Kontakt löschen.    | Im Pop-Up auf "Löschen"-Button klicken.             | Ein Pop-Up Formular zur Bearbeitung der Kontaktinformationen wird angezeigt. |
| 3.1             | Der Benutzer erstellt einen vorhandenen Kontakt (Name).    | Eingabefeldern (vorhandene Name) ausfüllen und Klick auf "Erstellen"-Button.              | Fehlermeldung wird angezeigt. |
| 3.2             | Der Benutzer erstellt einen Kontakt ohne Name.    | Eingabefelder (Name) leer lassen und Klick auf "Erstellen"-Button.              | Fehlermeldung wird angezeigt. |
| 3.3             | Der Benutzer versucht die Kontaktliste zu speichern, obwohl keine Kontakte vorhanden sind.    | Klick auf "Speichern".              | Fehlermeldung wird angezeigt. |
| 4.1             | Der Benutzer möchte die Kontaktliste speichern.       | Klick auf "Speichern".                               | Kontaktliste wird im Download-Ordner gespeichert.                                     |
| 5.1             | Der Benutzer informiert sich über die App.         | Klick auf Info Icon.             | Pop-Up wird geöffnet und Informationen werden angezeigt.                                            |

## Planen


| AP-№ | Zuständig | Beschreibung                            | Geplante Zeit | Frist        |
| ---- | --------- | --------------------------------------- | ------------- | ------------ |
| 0.0  | Raviraj   | Projekt erstellen und informieren  | 4 Stunden     | 16.08.2024   |
| 1.A  | Raviraj   | Python Recherchieren     | 4 Stunden     | 23.08.2024  |
| 2.A  | Raviraj   | CRUD Funktion erstellen         | 4 Stunden    | 30.08.2024   |
| 2.B  | Raviraj   | Kontaktliste erstellen | 4 Stunden | 06.09.2024   |
| 3.A  | Raviraj   | Speicherfunktion erstellen | 2 Stunden | 13.09.2024   |
| 3.B  | Raviraj   | Info Icon erstellen         | 2 Stunden     | 20.09.2024   |
| 4.A  | Raviraj   | Mahara Portfolio erstellen        | 4 Stunden    | 27.09.2024   |
| 4.B  | Raviraj   | Projektdokumentation        | 4 Stunden    | 01.11.2024   |

## 3 Entscheiden

Keine

## Use Case Diagramm

![Untitled Diagram drawio](https://github.com/user-attachments/assets/bfc669be-a7c5-4d18-981d-5bfb6d135a18)


## 4 Realisieren

| AP-№ | Zuständig | Geplante Zeit | Tatsächliche Zeit | Datum      |
| ---- | --------- | ------------- | ----------------- | ---------- |
| 0.0  | Raviraj   | 4 Stunden      | 3 Stunden         | 16.08.2024 |
| 1.A  | Raviraj   | 4 Stunden      | 5 Stunden      | 23.08.2024 |
| 2.A  | Raviraj   | 4 Stunden      | 4 Stunden         | 30.08.2024 |
| 2.B  | Raviraj   | 4 Stunden      | 4 Stunden        | 06.09.2024 |
| 3.A  | Raviraj   | 2 Stunden      | 2 Stunden         | 13.09.2024 |
| 3.B  | Raviraj   | 2 Stunden     | 2 Stunden        | 20.09.2024 |
| 4.A  | Raviraj   | 4 Stunden      | 4 Stunden         | 27.09.2024 |
| 4.B  | Raviraj   | 4 Stunden      | 4 Stunden         | 01.11.2024 |

## 5 Kontrollieren

### Testprotokoll

| Testfall-№ | Resultat | Tester  | Datum     |
| -----------| ---------| --------| ----------|
| 0.1        | OK       | Raviraj | 01.11.2024|
| 0.2        | OK       | Raviraj | 01.11.2024|
| 1.1        | OK       | Raviraj | 01.11.2024|
| 2.1        | OK       | Raviraj | 01.11.2024|
| 2.2        | OK       | Raviraj | 01.11.2024|
| 3.1        | OK       | Raviraj | 01.11.2024|
| 3.2        | OK       | Raviraj | 01.11.2024|
| 3.3        | OK       | Raviraj | 01.11.2024|
| 4.1        | OK       | Raviraj | 01.11.2024|
| 5.1        | OK       | Raviraj | 01.11.2024|

## Mahara-Link
https://portfolio.bbbaden.ch/view/view.php?t=71946df6824f374ee0c3
