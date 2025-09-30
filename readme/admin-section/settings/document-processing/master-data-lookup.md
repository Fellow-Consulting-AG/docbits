# Stammdaten

## Übersicht

Die "Stammdaten" in Ihren Einstellungen zur Verarbeitung von Dokumenten ermöglichen einen umfassenden und integrierten Ansatz zur Verwaltung und Validierung Ihrer Dokumentdaten, indem sie mit Ihrem Infor-ERP-System synchronisiert werden. So unterstützt es die Optimierung der Validierung und Verbesserung der Verarbeitung von Dokumenten in Ihrer ERP-Umgebung:

1. **Zentralisierte Datenverwaltung**: Diese Funktion dient als zentrale Ablage, in der Daten aus verschiedenen Quellen wie Lieferanten, Kundenadressen, Steuercodes und mehr gespeichert und verwaltet werden können. Sie bietet einen einzigen Referenzpunkt für alle Stammdaten und stellt so Konsistenz und Genauigkeit in Ihrem Unternehmen sicher.
2. **Validierung gegen ERP-Daten**: Durch die Synchronisierung von Stammdaten wie Lieferanteninformationen von Infor zu DocBits können die aus Dokumenten extrahierten Daten automatisch gegen Ihre ERP-Daten validiert werden. So wird sichergestellt, dass die verarbeiteten Informationen (wie Lieferantennamen, Adressen und Steuercodes) mit den in Ihrem ERP-System hinterlegten Daten übereinstimmen, wodurch Fehler und Abweichungen minimiert werden.
3. **Ermöglicht Automatisierung**: Ein robustes Stammdaten-Lookup-System unterstützt die Automatisierung der Verarbeitung eingehender Dokumente. Beispielsweise können Bestellungen oder Rechnungen automatisch auf die Korrektheit der Lieferantendaten überprüft, bei Übereinstimmung freigegeben oder bei Abweichungen zur Überprüfung markiert werden.
4. **Steigert die Datenintegrität**: Regelmäßige Aktualisierungen aus Ihrem ERP-System in die Stammdaten stellen sicher, dass die für die Verarbeitung von Dokumenten verwendeten Daten aktuell sind. Dadurch verringert sich das Risiko, Dokumente auf Basis veralteter Informationen zu verarbeiten, was die Integrität von Geschäftsvorgängen insgesamt erhöht.
5. **Effizienz in der Verarbeitung von Dokumenten**: Mit direkt verknüpften und laufend aktualisierten Stammdaten wird die Verarbeitung von Dokumenten effizienter. Dokumente können automatisch klassifiziert und anhand der in den Stammdaten definierten Kriterien weitergeleitet werden, z. B. spezifische Lieferantenkonditionen oder steuerliche Vorschriften, die für unterschiedliche Transaktionsarten gelten.

{% hint style="info" %}
Hier erfahren Sie, wie Sie Stammdaten importieren
{% endhint %}

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_1.png)

## **Zugriff auf Stammdaten**

Um den Bereich **Stammdaten** aufzurufen, navigieren Sie zu:\
**Einstellungen → Verarbeitung von Dokumenten → Stammdaten**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_mater_data_lookup.png)

## **Einstellungen**

Sie greifen auf die Einstellungen für die **Stammdaten** zu, indem Sie auf das Symbol **Einstellungen** in der unteren linken Ecke des **Stammdaten**-Bildschirms klicken. Die folgenden Konfigurationsoptionen stehen zur Verfügung:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_2.png)

### **Lieferanten-BOD**

* **Synchronisierung mehrerer Lieferantenkonten zulassen**:
  * **Aktiviert**:\
    Ein einzelner Lieferant kann mehrere Elemente vom Typ `<FinancialParty>` im BOD (Business Object Document) haben, häufig aufgrund mehrerer zugeordneter IBANs oder Finanzkonten. Wenn diese Einstellung aktiviert ist, werden alle Einträge `<FinancialParty>` für den Lieferanten extrahiert und in der Lieferantentabelle gespeichert, sodass mehrere finanzielle Attribute gespeichert werden können.
  * **Deaktiviert**:\
    Es wird nur das letzte für den Lieferanten im BOD gefundene Element `<FinancialParty>` extrahiert. Frühere finanzielle Attribute (z. B. zusätzliche IBANs) werden ignoriert, und nur die Daten aus dem letzten Vorkommen werden in der Lieferantentabelle gespeichert.

### **Löschung von Bestellungen**

*   **Bestellung löschen nach**: Geben Sie an, wann geschlossene Bestellungen gelöscht werden sollen. Nach dem ausgewählten Zeitraum werden die Datensätze automatisch entfernt.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_3.png)
