# Pregled mapiranja polja ZUGFeRD

## Uvod

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) je nemački standard za elektronsko fakturisanje zasnovan na UN/CEFACT Cross Industry Invoice (CII) i ISO standardu 19005-3 (PDF/A-3). Omogućava razmenu strukturiranih podataka o fakturama u PDF datoteci.

DocBits izvlači polja iz ZUGFeRD dokumenata i usklađuje ih sa Infor ERP sistemima (M3, LN) koristeći OAGIS BOD standarde.

## Podržane verzije ZUGFeRD-a

DocBits podržava više verzija ZUGFeRD standarda:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Tok podataka

Tok podataka od ZUGFeRD dokumenta do vašeg ERP sistema prati ove korake:

1. **Ekstrakcija**: DocBits analizira ugrađene XML podatke iz PDF-a na osnovu verzije ZUGFeRD-a.
2. **DocBits mapiranje polja**: Izvučeni podaci se mapiraju na standardna DocBits polja.
3. **ERP usklađivanje**: DocBits polja se mapiraju na Infor BOD (Business Object Document) polja ili M3/LN specifična API polja.
4. **Izvoz**: Mapirani podaci se izvoze u Infor sistem.

## Standardi mapiranja

Mapiranje se zasniva na sledećim standardima:
* **UN/CEFACT CII**: Osnova za ZUGFeRD XML strukturu.
* **OAGIS/OASIS**: Standard za Infor BOD-ove.
* **EN 16931**: Evropski standard za e-fakturisanje sa kojim je ZUGFeRD 2.x usklađen.
