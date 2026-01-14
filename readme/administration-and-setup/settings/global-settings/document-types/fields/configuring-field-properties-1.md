# Konfigurieren von Feldeigenschaften

## Detaillierte Anweisungen zum Festlegen von Eigenschaften wie "Pflichtfeld", "Schreibgeschützt", "Ausgeblendet" und "OCR".

### Pflichtfeld (Required):

<figure><img src="../../../../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

Wenn ein Feld als Pflichtfeld markiert ist, bedeutet dies, dass dieses Feld ausgefüllt werden muss, bevor der Beleg gespeichert oder verarbeitet werden kann.

**So legen Sie diese Eigenschaft fest:**

* Navigieren Sie zu den Einstellungen des Feldes in Ihrem DocBits-System.
* Aktivieren Sie die Option "Pflichtfeld" für das entsprechende Feld.

**Auswirkung:**

* Diese Einstellung stellt sicher, dass wichtige Informationen erfasst werden und keine Belege ohne die erforderlichen Daten verarbeitet werden können.

### Schreibgeschützt (Read Only):

<figure><img src="../../../../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

Wenn ein Feld als schreibgeschützt markiert ist, bedeutet dies, dass Benutzer den Inhalt dieses Feldes sehen, aber keine Änderungen daran vornehmen können.

**So legen Sie diese Eigenschaft fest:**

* Gehen Sie zu den Feldoptionen. Aktivieren Sie die Option "Schreibgeschützt" für das gewünschte Feld.

**Auswirkung:**

* Diese Einstellung kann nützlich sein, um sensible Informationen zu schützen oder sicherzustellen, dass wichtige Daten nicht versehentlich geändert werden.

### Ausgeblendet (Hidden):

<figure><img src="../../../../../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

Wenn ein Feld als "Ausgeblendet" markiert ist, bedeutet dies, dass das Feld in der Benutzeroberfläche ausgeblendet wird und Benutzer es nicht sehen oder darauf zugreifen können.

**So legen Sie diese Eigenschaft fest:**

* Gehen Sie zu den Feldoptionen.
* Aktivieren Sie die Option "Ausgeblendet" für das entsprechende Feld.

**Auswirkung:**

* Diese Einstellung wird häufig verwendet, um interne oder technische Felder auszublenden, die für den Endbenutzer irrelevant sind oder nur für die interne Verarbeitung benötigt werden.

### OCR (Optische Zeichenerkennung):

<figure><img src="../../../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

Wenn ein Feld für OCR konfiguriert ist, bedeutet dies, dass das System versucht, den Text aus dem Beleg zu extrahieren und in dieses Feld einzufügen. Diese Einstellung wird normalerweise für Felder verwendet, die automatisch ausgefüllt werden sollen.

**So richten Sie dies ein:**

* Aktivieren Sie die OCR-Option für das entsprechende Feld.
* Konfigurieren Sie bei Bedarf die OCR-Parameter wie Sprache, Schriftart usw.

**Auswirkung:**

* Die Verwendung von OCR ermöglicht die automatische Verarbeitung von Belegen, indem Informationen aus Texten extrahiert und in die entsprechenden Felder eingetragen werden, was den manuellen Aufwand reduziert und die Effizienz steigert.

### Erzwungene Validierung (Forced validation):

<figure><img src="../../../../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

Konfigurieren Sie die Validierungsregeln entsprechend, z. B. numerische Grenzwerte, reguläre Ausdrücke oder Beziehungen zu anderen Feldern.

**So richten Sie dies ein:**

* Speichern Sie die Änderungen.

**Auswirkung:**

* Die erzwungene Validierung prüft die eingegebenen Daten anhand der angegebenen Kriterien, um sicherzustellen, dass sie gültig sind. Dies hilft, Fehler frühzeitig zu erkennen und die Datenqualität zu verbessern.

### Übereinstimmungswert (Match Score):

<figure><img src="../../../../../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

Durch den Vergleich von Eingabedaten mit Referenzdaten kann der Match Score dazu beitragen, die Genauigkeit und Gültigkeit der Daten zu bestätigen. Wenn der Match Score einen bestimmten Schwellenwert überschreitet, gilt die Übereinstimmung als erfolgreich.

**So richten Sie dies ein:**

* Aktivieren Sie die Option "Match Score" und legen Sie den gewünschten Schwellenwert fest.
* Speichern Sie die Änderungen.

**Auswirkung:**

* Der Match Score wird verwendet, um die Genauigkeit von Übereinstimmungen zwischen Eingabedaten und Referenzwerten zu bewerten. Wenn der erzielte Wert den festgelegten Schwellenwert überschreitet, gilt die Übereinstimmung als erfolgreich. Dies ist besonders nützlich für Felder, die eine Datenvalidierung oder einen Datenabgleich erfordern, wie z. B. Felder mit Name oder E-Mail-Adresse, z. B. bei der Überprüfung von Kundendaten.

<figure><img src="../../../../../.gitbook/assets/image (117).png" alt="" width="258"><figcaption></figcaption></figure>

Durch die sorgfältige Konfiguration dieser Feldeigenschaften können Sie die Belegverarbeitungs-Workflows optimieren und sicherstellen, dass Ihre Daten korrekt erfasst, geschützt und effizient verarbeitet werden.
