# ZUGFeRD Feldzuordnung Überblick

## Einführung

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) ist ein deutscher E-Invoicing-Standard, der auf der UN/CEFACT Cross Industry Invoice (CII) und dem ISO-Standard 19005-3 (PDF/A-3) basiert. Er ermöglicht den Austausch strukturierter Rechnungsdaten in einer PDF-Datei.

DocBits extrahiert Felder aus ZUGFeRD-Dokumenten und gleicht sie mit Infor ERP-Systemen (M3, LN) unter Verwendung von OAGIS BOD-Standards ab.

## Unterstützte ZUGFeRD-Versionen

DocBits unterstützt mehrere Versionen des ZUGFeRD-Standards:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Datenfluss

Der Datenfluss von einem ZUGFeRD-Dokument zu Ihrem ERP-System folgt diesen Schritten:

1. **Extraktion**: DocBits parst die eingebetteten XML-Daten aus der PDF-Datei basierend auf der ZUGFeRD-Version.
2. **DocBits Feldzuordnung**: Extrahierte Daten werden Standard-DocBits-Feldern zugeordnet.
3. **ERP-Abgleich**: DocBits-Felder werden Infor BOD (Business Object Document) Feldern oder M3/LN-spezifischen API-Feldern zugeordnet.
4. **Export**: Die zugeordneten Daten werden in das Infor-System exportiert.

## Mapping-Standards

Die Zuordnung basiert auf den folgenden Standards:
* **UN/CEFACT CII**: Die Basis für die ZUGFeRD XML-Struktur.
* **OAGIS/OASIS**: Der Standard für Infor BODs.
* **EN 16931**: Der europäische Standard für E-Invoicing, dem ZUGFeRD 2.x entspricht.
