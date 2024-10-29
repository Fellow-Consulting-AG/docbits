# Version

## Änderungen

## Änderungen vom  4. November 2024

## Neue Funktionen:

## Verbesserungen beim E-Mail-Import

IMAP-E-Mail-Einstellungen wurden so konfiguriert, um Benachrichtigungen über Importergebnisse automatisch zu senden. Erfolgreiche Importbenachrichtigungen bestätigen die erfolgreiche Verarbeitung von Dateien, während Fehlermeldungen die Dateinamen und spezifische Fehlerdetails für eine schnelle Fehlersuche enthalten.

<figure><img src=".gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Überarbeitung der Stammdatenabfrage

Die Einstellungen zur Stammdatenabfrage wurden überarbeitet und verfeinert, um eine schnellere und genauere Abfrage verschiedener Stammdatentypen zu ermöglichen. Diese Verbesserung optimiert den Datenzugriff, indem Stammdaten in unterschiedliche Kategorien organisiert werden, was die Sucheffizienz und -genauigkeit erheblich steigert. Benutzer können nun die relevanten Daten schneller finden, was die Produktivität in der Anwendung verbessert.

<figure><img src=".gitbook/assets/image2.png" alt=""><figcaption></figcaption></figure>

## Leistungsverbesserungen

Ein robustes Caching-System wurde implementiert, um die Anwendungsleistung erheblich zu steigern, insbesondere bei hohen Anfragen. Diese Verbesserung reduziert die Serververarbeitungszeit, indem häufig abgerufene Daten vorübergehend gespeichert werden, was schnellere Antwortzeiten und ein reibungsloseres Benutzererlebnis ermöglicht. Das neue Caching-System verwaltet den erhöhten Datenverkehr effizient und sorgt für zuverlässige und konstante Leistung, selbst in Spitzenlastzeiten.

## Verbesserung der Dokumentensperrfunktion

Die Funktionalität zum Sperren von Dokumenten wurde verbessert, um gleichzeitige Bearbeitung zu verhindern, die Datenintegrität zu gewährleisten und Konflikte zu minimieren. Dokumente werden nun während der aktiven Bearbeitung automatisch gesperrt, wobei den Benutzern klare Hinweise gegeben werden, wenn ein Dokument in Verwendung ist, und andere daran gehindert werden, Änderungen vorzunehmen, bis die Bearbeitung abgeschlossen ist. Diese Verbesserung optimiert die kollaborativen Arbeitsabläufe und verringert das Risiko von Datenüberschreibungen.

## Verbesserungen bei Navigation und Benutzererfahrung

* **Breadcrumb-Navigation**: Breadcrumbs wurden auf den Seiten der Anwendung hinzugefügt, um die Navigation zu verbessern, sodass Benutzer leicht zurückverfolgen und zu vorherigen Abschnitten zurückkehren können. Dies ermöglicht ein intuitiveres Surferlebnis.
* **Optimierte Benutzeroberfläche**: Die Pop-up-Benachrichtigung "neue Version" wurde entfernt, um einen reibungsloseren, ununterbrochenen Arbeitsablauf zu schaffen. Ablenkungen werden reduziert und die allgemeine Benutzerfreundlichkeit verbessert.

## Fehlerbehebungen:

* Benutzerbezogene Probleme, wie z.B. Anhangsfehler von verschlüsselten oder signierten E-Mails, wurden behoben.
* Probleme mit der Kartenanzeige und dem Ablauf wurden behoben.
* Routing-Probleme mit den Schaltflächen "Nächste/Vorherige" wurden behoben.
* Fehler im Zusammenhang mit Entscheidungstabellen wurden behoben.
* Die Benutzeroberfläche für das Passwortfeld wurde überarbeitet, um die Benutzerfreundlichkeit zu verbessern.
* Probleme mit nicht korrekt angezeigten Aufgabenzähler wurden behoben
* Benutzeroberflächenproblem mit der KI-Tabelle wurde behoben.
* Fehler bei der Dokumentenextraktion während des Tabellentrainings wurden behoben.
* Warnung wurde hinzugefügt, wenn ein PO während der Umformatierung übereinstimmt. Es wird sichergestellt, dass übereinstimmende Zeilen entfernt werden.
* Das Datumsformat wurde korrigiert, um sicherzustellen, dass Daten korrekt nach Tages- und Wochenfiltern geladen, und Dokumenttypen ordnungsgemäß angezeigt werden.
* Die Anzeige von Dokumenten auf Dual-Monitoren wurde korrigiert.
* Problem, bei dem das Trennen einer PO-Zeile alle Zeilen entfernt hat, wurde behoben.
* Falsche Übersetzungen in der gesamten Anwendung wurden behoben.
* Problem, bei dem lange Beschreibungen im Regelmanagement Scrollen in der Liste verursachte, wurde behoben.
* Fehlende "Zuweisen"-Funktionalität für Nicht-Admin-Benutzer wurde wiederhergestellt.
