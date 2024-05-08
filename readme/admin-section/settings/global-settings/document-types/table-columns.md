# Tabellenspalten

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.57.49.png" alt=""><figcaption></figcaption></figure>

#### Übersicht

Die Tabellenspalten-Schnittstelle in Docbits wird verwendet, um die Spalten festzulegen, die in Daten tabellen für jeden Dokumententyp angezeigt werden. Jede Spalte kann so konfiguriert werden, dass sie bestimmte Arten von Daten enthält, wie z. B. Zeichenfolgen oder numerische Werte, und kann für Sortier-, Filter- und Berichtsfunktionen innerhalb von Docbits unerlässlich sein.

#### Hauptfunktionen und Optionen

1. **Spaltenkonfiguration**:
* **Spaltenname**: Der Bezeichner für die Spalte in der Datenbank.
* **Titel**: Der für den Benutzer lesbare Titel für die Spalte, der in der Benutzeroberfläche angezeigt wird.
* **Spaltentyp**: Definiert den Datentyp der Spalte (z. B. STRING, BETRAG), der bestimmt, welche Art von Daten in der Spalte gespeichert werden können.
* **Tabellenname**: Gibt an, zu welcher Tabelle die Spalte gehört, indem sie mit einem bestimmten Dokumententyp wie INVOICE\_TABLE verknüpft wird.
2. **Aktionen**:
* **Bearbeiten**: Ändern Sie die Einstellungen einer vorhandenen Spalte.
* **Löschen**: Entfernen Sie die Spalte aus der Tabelle, was nützlich ist, wenn die Daten nicht mehr benötigt werden oder wenn sich die Datenstruktur des Dokumententyps ändert.
3. **Hinzufügen neuer Spalten und Tabellen**:
* **Neue Tabellenspalte hinzufügen**: Öffnet einen Dialog, in dem Sie eine neue Spalte definieren können, einschließlich ihres Namens, ob sie erforderlich ist, ihres Datentyps und der Tabelle, zu der sie gehört.
* **Neue Tabelle erstellen**: Ermöglicht die Erstellung einer neuen Tabelle, wobei ein eindeutiger Name definiert wird, der zur Speicherung von Daten im Zusammenhang mit einer bestimmten Gruppe von Dokumententypen verwendet wird.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.58.01.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.58.11.png" alt=""><figcaption></figcaption></figure>

Dieser Abschnitt ist entscheidend für die Aufrechterhaltung der strukturellen Integrität und Benutzerfreundlichkeit von Daten innerhalb des Docbits-Systems und stellt sicher, dass die aus Dokumenten extrahierten Daten auf organisierte und zugängliche Weise gespeichert werden.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2493" %}
