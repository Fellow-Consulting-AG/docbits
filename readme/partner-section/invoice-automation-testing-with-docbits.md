# Rechnungsautomatisierungstests mit DocBits

## Überblick

Dieses Dokument umreißt den Testplan für die Rechnungsautomatisierung mit DocBits mit Infor LN oder M3. Es enthält Details zu Testfällen, Testvorbereitung, Ausführungsschritten und Supportprozessen.

## Testfälle

| ID | Testfall                                                                   | Beschreibung                                                                                                                                                       | Status       |
| -- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 1  | Kostenrechnungen                                                           | Rechnungen ohne Bestellnummer werden erfolgreich in DocBits verarbeitet und als "Kostenrechnung" nach LN exportiert.                                               | ZU TESTEN    |
| 2  | Bestellbezogene Rechnung mit perfekter Übereinstimmung                     | Bestellbezogene Rechnungen werden erfolgreich in DocBits verarbeitet mit einer perfekten Übereinstimmung von Rechnung zu Bestellung, da Artikelnummer, Menge und Stückpreis übereinstimmen. | ZU TESTEN    |
| 3  | Bestellbezogene Rechnungen mit unterschiedlicher Menge                     | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung bei der Menge.                                      | ZU TESTEN    |
| 4  | Bestellbezogene Rechnungen mit unterschiedlichem Stückpreis                | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung beim Stückpreis.                                    | ZU TESTEN    |
| 5  | Bestellbezogene Rechnungen mit unterschiedlicher oder nicht vorhandener Artikelnummer | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung oder eine nicht vorhandene Artikelnummer.         | ZU TESTEN    |
| 6  | Bestellbezogene Rechnungen mit einer Abweichung innerhalb der Toleranz     | Bestellbezogene Rechnungen werden in DocBits verarbeitet, aber im Bestellabgleichsmodul haben wir eine Abweichung bei Menge oder Stückpreis, die jedoch innerhalb der Toleranz liegt. | ZU TESTEN    |
| 7  | Gutschriften                                                               | Gutschriften werden erfolgreich in DocBits verarbeitet und nach LN exportiert. Klären, ob Beträge mit einem positiven oder negativen Vorzeichen exportiert werden sollen. | ZU TESTEN    |

## Plan für Tests mit dem Kunden

### 1. Einrichtung

* **Erstes Treffen**: Planen Sie ein Auftaktgespräch mit dem Kunden, um den Testprozess und die Ziele zu erläutern.
* **Zugriff und Berechtigungen**: Stellen Sie sicher, dass der Kunde alle erforderlichen Zugriffe auf DocBits und Infor LN oder M3 für Testzwecke hat.

### 2. Testvorbereitung

* **Schulung**: Bieten Sie dem Team des Kunden umfassende Schulungen zur Verwendung von DocBits für die Rechnungsverarbeitung an.
* **Dokumentation**: Teilen Sie detaillierte Dokumentationen zu den Testverfahren, einschließlich der erwarteten Ergebnisse für jeden Testfall.

### 3. Ausführung der Testfälle

* **Testumgebung**: Richten Sie eine Testumgebung ein, die das Produktionssystem des Kunden so genau wie möglich nachbildet.
* **Schrittweise Tests**: Arbeiten Sie mit dem Kunden zusammen, um jeden Testfall auszuführen und sicherzustellen, dass sie jeden Schritt verstehen:
  * Rechnungen durch DocBits verarbeiten.
  * Die Ausgabe im Bestellabgleichsmodul überprüfen.
  * Die Exportergebnisse in LN oder M3 überprüfen.

### 4. Fehlerbehebung

* **Verfolgung**: Verwenden Sie ein Verfolgungssystem (wie Jira oder eine einfache Tabelle), um auftretende Probleme oder Abweichungen während des Tests zu protokollieren.
* **Unterstützung**: Bieten Sie sofortige Unterstützung zur Behebung von Problemen und zur Klärung von Zweifeln.

### 5. Überprüfung und Feedback

* **Überprüfung**: Überprüfen Sie nach jedem Testfall die Ergebnisse mit dem Kunden, um die Genauigkeit sicherzustellen.
* **Feedbackschleife**: Sammeln Sie Feedback vom Kunden zum Prozess und zu erforderlichen Verbesserungen.

### 6. Abschluss

* **Dokumentation der Ergebnisse**: Dokumentieren Sie die Ergebnisse jedes Testfalls und erstellen Sie einen Zusammenfassungsbericht für den Kunden.
* **Überprüfungstreffen**: Führen Sie ein Überprüfungstreffen durch, um die Testergebnisse und eventuell erforderliche weitere Schritte vor dem Produktivstart zu besprechen.

### 7. Vorbereitung für den Produktivstart

* **Auffrischung der Schulung**: Bieten Sie bei Bedarf eine Auffrischungsschulung an.
* **Unterstützungsplan**: Entwickeln Sie einen Unterstützungsplan für die anfängliche Produktivstartphase, um einen reibungslosen Übergang sicherzustellen.
