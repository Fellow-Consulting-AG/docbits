# Architektur

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits** integriert nahtlos mit Infor LN/M3 über ION API, ION Desk und Infor Standard BODs. Unsere API-Integration ermöglicht es uns, Daten an Infor zu exportieren und eine Validierung der Stammdateien in Doc**Bits** durchzuführen.

## Datenexport nach Infor

Wir verwenden die ION API, um das PDF mit Attributen an IDM zu senden und das BOD Sync.CaptureDocument an ION Desk. In ION Desk transformieren wir das Sync.CaptureDocument in die gewünschten Ziel-BODs basierend auf dem verarbeiteten Dokumententyp. Diese transformierten Infor BODs werden dann automatisch in LN oder M3 importiert.

## Validierung der Stammdateien in DocBits

Um den Lieferanten zu identifizieren oder Bestellpositionen zu vergleichen/abzugleichen, aktivieren wir einen Trigger in LN/M3, der die Sync.RemitToPartyMaster, Sync.SupplierPartyMaster und Sync.PurchaseOrder BODs an Doc**Bits** sendet. Wir konfigurieren diesen Prozess in ION Desk, indem wir den Datenfluss zu einem spezifischen Verbindungspunkt zu Doc**Bits** definieren.
