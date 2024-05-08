# Einkaufsrechnung - 2. Genehmigungseinheit Preis Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.59.02.png" alt=""><figcaption></figcaption></figure>

Dieser Titel zeigt an, dass die Regel eingerichtet ist, um die zweite Genehmigungsphase von Einkaufsrechnungen mit Schwerpunkt auf dem Stückpreis zu verwalten und sicherzustellen, dass er den vereinbarten Bedingungen entspricht.

#### Regelkonfiguration:

1. **Wenn…**
* **Dokumententyp ist Rechnung**: Diese Bedingung stellt sicher, dass die Regel nur für als Rechnungen identifizierte Dokumente aktiviert wird, was für die genaue Lenkung des Workflows entscheidend ist.
2. **Und…**
* **Dokumentenstatus ist Ausstehende zweite Genehmigung**: Dies gibt an, dass die Rechnung auf die zweite Genehmigung wartet. Diese Phase bietet oft zusätzliche Überwachung, um die Genauigkeit vor Abschluss der Transaktion sicherzustellen.
* **Dokumentenfeld Rechnungsuntertyp ist Gleich Einkaufsrechnung**: Diese Bedingung spezifiziert weiter, dass die Regel nur für Rechnungen gilt, die speziell als "Einkaufsrechnungen" kategorisiert sind und sie von anderen Arten von Rechnungen unterscheidet.
* **Logik Stückpreis in Auftragsbestätigung ist Gleich Einkaufsbestellung**: Diese Bedingung überprüft, ob der Stückpreis in der Auftragsbestätigung mit dem Stückpreis in der Einkaufsbestellung übereinstimmt. Sie stellt sicher, dass die Rechnungsbearbeitung nur fortgesetzt wird, wenn eine Preiskonsistenz besteht, was für die Budgetierung und Finanzberichterstattung entscheidend ist.

#### Aktion (Dann…):

* **Export starten**: Sobald die Rechnung die spezifizierten Bedingungen erfüllt (d. h. die Stückpreise zwischen der Auftragsbestätigung und der Einkaufsbestellung übereinstimmen), wird die Aktion "Export starten" ausgelöst. Dies beinhaltet wahrscheinlich das Exportieren der Rechnungsdaten für weitere Bearbeitung, möglicherweise in ein anderes Finanzsystem oder für Berichtszwecke.

#### Zweck dieser Regel:

* **Genauigkeit und Konsistenz sicherstellen**: Durch die Überprüfung, ob die Stückpreise zwischen der Auftragsbestätigung und der Einkaufsbestellung übereinstimmen, hilft das System, die finanzielle Genauigkeit zu gewährleisten und Über- oder Unterbelastungen zu verhindern.
* **Finanzielle Bearbeitung optimieren**: Die Automatisierung des Datenexports, sobald die Preise bestätigt sind, reduziert manuelle Bearbeitung und beschleunigt den Finanzbearbeitungszyklus.
* **Compliance und Überwachung verbessern**: Die Anforderung einer zweiten Genehmigung zur Preisüberprüfung fügt eine zusätzliche Überwachungsebene hinzu, die für die Einhaltung finanzieller Richtlinien und Kontrollen entscheidend ist.

Diese Regel ist ein Beispiel dafür, wie die Workflow-Automatisierung effektiv genutzt werden kann, um eine präzise und effiziente Bearbeitung von Finanzdokumenten innerhalb einer Organisation sicherzustellen, insbesondere im Kontext großer Transaktionsvolumina, die eine sorgfältige Validierung erfordern.
