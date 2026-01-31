# ZUGFeRD Veldomapping Overzicht

## Inleiding

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) is een Duitse e-facturatiestandaard gebaseerd op de UN/CEFACT Cross Industry Invoice (CII) en de ISO-standaard 19005-3 (PDF/A-3). Het maakt de uitwisseling van gestructureerde factuurgegevens in een PDF-bestand mogelijk.

DocBits extraheert velden uit ZUGFeRD-documenten en lijnt deze uit met Infor ERP-systemen (M3, LN) met behulp van OAGIS BOD-standaarden.

## Ondersteunde ZUGFeRD-versies

DocBits ondersteunt meerdere versies van de ZUGFeRD-standaard:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Gegevensstroom

De gegevensstroom van een ZUGFeRD-document naar uw ERP-systeem volgt deze stappen:

1. **Extractie**: DocBits parseert de ingebedde XML-gegevens uit de PDF op basis van de ZUGFeRD-versie.
2. **DocBits Veldomapping**: Geëxtraheerde gegevens worden toegewezen aan standaard DocBits-velden.
3. **ERP-afstemming**: DocBits-velden worden toegewezen aan Infor BOD (Business Object Document) velden of M3/LN-specifieke API-velden.
4. **Export**: De toegewezen gegevens worden geëxporteerd naar het Infor-systeem.

## Mapping-standaarden

De mapping is gebaseerd op de volgende standaarden:
* **UN/CEFACT CII**: De basis voor de ZUGFeRD XML-structuur.
* **OAGIS/OASIS**: De standaard voor Infor BOD's.
* **EN 16931**: De Europese standaard voor e-facturatie waaraan ZUGFeRD 2.x voldoet.
