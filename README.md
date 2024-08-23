## Informieren

### User Stories

| US-№ | Verbindlichkeit | Art          | Beschreibung                                                       |
| ---- | --------------- | ------------ | ------------------------------------------------------------------|
| 0    | Muss            | Funktional   | Als User muss ich in der Lage sein, die Webseite bedienen können. |
| 1    | Muss            | Funktional   | Als User muss ich in der Lage sein, eine zufällige Zahl zu generieren. |
| 2    | Muss            | Funktional   | Als User muss ich eine Zahl eingeben können. |
| 3    | Muss            | Funktional   | Als User muss ich das Ergebnis einsehen können. |
| 4    | Muss            | Funktional   | Als User muss ich Tipps zur aktuellen Zufallszahl einsehen können. |
| 5    | Muss            | Funktional   | Als User muss ich in der Lage sein, das Spiel neuzustarten. |
| 6    | Kann            | Qualitativ   | Als User kann ich eine einfache Webseite erleben. |




### Testfälle

| Testfall-Nummer | Ausgangslage                                                                  | Eingabe                                  | Erwartete Ausgabe                                                     |
| --------------- | ----------------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| 0.1             | Der User befindet sich auf der URL-Leiste und möchte die Webseite öffnen.                      | URL eingeben und Enter drücken.    | Die Webseite wird geladen und der Besucher befindet sich auf der Startseite mit einem leeren Spiel.    |
| 1.1             | Der User befindet sich auf der Startseite und möchte eine zufällige Zahl generieren.                    | Auf dem Startbutton klicken. | Es wird nach einer zufällige Zahl gefragt. |
| 2.1             | Der User wird nach einer Zahl gefragt und möchte eine Zahl eingeben.                     | Eine Zahl im Textbox eingeben.                      | Die Zahl wird im Textbox gespeichert.     |
| 2.2             | Der User hat eine Zahl eingegeben und möchte sie überprüfen.                               | Den Button zur Überprüfung verwenden.                                           | Ein Pop-Up Dialog wird angezeigt.                                           |
| 3.1             | Der User hat eine falsche Zahl eingegeben.                               | Den Button zur Überprüfung verwenden.                                       | Falsche Guess wird gemeldet                                    |
| 3.2             | Der User hat eine korrekte Zahl eingegeben und möchte sie überprüfen.                               | Den Button zur Überprüfung verwenden.                                               | Das Spiel wird mit der Gewinnmeldung beendet.                                         |
| 4.1             | Der User hat eine tiefere Zahl erratet.               | Den Button zur Überprüfung verwenden.     | Es wird gezeigt, dass die korrekte Zahl höher ist als die erratene Zahl.     |
| 4.2             | Der User hat eine höhere Zahl erratet.               | Den Button zur Überprüfung verwenden.   | Es wird gezeigt, dass die korrekte Zahl tiefer ist als die erratene Zahl.     |
| 5.1             | Der User befindet sich im Spiel und möchte dies neustarten. | Auf dem Button Neustartbutton klicken.         | Das Spiel von der Startseite wird neugestartet mit der Meldung von der eigentliche Zahl.         |
| 6.1             | Der User navigiert die Webseite. | Nutzung der Webseite.         | Der User versteht die einfache Funktionsweise der Webseite.         

## Planen


| AP-№ | Zuständig | Beschreibung                            | Geplante Zeit | Frist        |
| ---- | --------- | --------------------------------------- | ------------- | ------------ |
| 0.0  | Raviraj   | Erstellung der Projektdokumentation    | 3 Stunden     | 16.08.2024   |
| 1.A  | Raviraj   | Einrichtung Gruppenprojekt auf GitHub     | 1 Stunde     | 16.08.2024  |
| 2.A  | Manser   | Einrichtung VSS und LiveShare         | 1 Stunde    | 16.08.2024   |
| 3.A  | Manser   | Replay-Funktion mit JavaScript  | 1 Stunde | 16.08.2024   |
| 3.B  | Greub   | NumberGenerator-Funktion mit JavaScript | 2 Stunden | 16.08.2024   |
| 4.A  | Manser   | Index-HTML erstellen         | 2 Stunden     | 16.08.2024   |
| 5.A  | Greub   | Milestones auf Github erstellen        | 1 Stunde    | 16.08.2024   |
| 5.B  | Greub   | Issues auf Github erstellen        | 1 Stunde    | 16.08.2024   |

## 3 Entscheiden

Keine

## 4 Realisieren

| AP-№ | Zuständig | Geplante Zeit | Tatsächliche Zeit | Datum      |
| ---- | --------- | ------------- | ----------------- | ---------- |
| 0.0  | Raviraj   | 2 Stunden      | 2 Stunden         | 16.08.2024 |
| 1.A  | Raviraj   | 1 Stunde      | 1 Stunde      | 16.08.2024 |
| 2.A  | Manser   | 1 Stunde      | 1 Stunde         | 16.08.2024 |
| 3.A  | Manser   | 1 Stunde      | 1 Stunde        | 16.08.2024 |
| 3.B  | Greub   | 2 Stunden      | 2 Stunden         | 16.08.2024 |
| 4.A  | Manser   | 1 Stunde     | 1 Stunde        | 16.08.2024 |
| 5.A  | Greub   | 1 Stunde      | 1 Stunde         | 16.08.2024 |
| 5.B  | Greub   | 1 Stunde      | 1 Stunde         | 16.08.2024 |

## 5 Kontrollieren

### Testprotokoll

| Testfall-№ | Resultat | Tester  | Datum     |
| -----------| ---------| --------| ----------|
| 0.1        | OK       | Raviraj | 16.08.2024|
| 1.1        | OK       | Raviraj | 16.08.2024|
| 2.1        | OK       | Raviraj | 16.08.2024|
| 2.2        | OK       | Raviraj | 16.08.2024|
| 3.1        | OK       | Raviraj | 16.08.2024|
| 3.2        | OK       | Raviraj | 16.08.2024|
| 4.1        | OK       | Raviraj | 16.08.2024|
| 4.2        | OK       | Raviraj | 16.08.2024|
| 5.1        | OK       | Raviraj | 16.08.2024|
| 6.1        | OK       | Raviraj | 16.08.2024|

