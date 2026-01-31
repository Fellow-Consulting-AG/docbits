# Przegląd mapowania pól ZUGFeRD

## Wprowadzenie

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) to niemiecki standard fakturowania elektronicznego oparty na UN/CEFACT Cross Industry Invoice (CII) i normie ISO 19005-3 (PDF/A-3). Umożliwia wymianę ustrukturyzowanych danych faktur w pliku PDF.

DocBits wyodrębnia pola z dokumentów ZUGFeRD i dopasowuje je do systemów ERP Infor (M3, LN) przy użyciu standardów OAGIS BOD.

## Obsługiwane wersje ZUGFeRD

DocBits obsługuje wiele wersji standardu ZUGFeRD:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Przepływ danych

Przepływ danych z dokumentu ZUGFeRD do systemu ERP odbywa się w następujących krokach:

1. **Ekstrakcja**: DocBits analizuje osadzone dane XML z pliku PDF w oparciu o wersję ZUGFeRD.
2. **Mapowanie pól DocBits**: Wyodrębnione dane są mapowane na standardowe pola DocBits.
3. **Dopasowanie do ERP**: Pola DocBits są mapowane na pola Infor BOD (Business Object Document) lub pola API specyficzne dla M3/LN.
4. **Eksport**: Zmapowane dane są eksportowane do systemu Infor.

## Standardy mapowania

Mapowanie opiera się na następujących standardach:
* **UN/CEFACT CII**: Podstawa struktury XML ZUGFeRD.
* **OAGIS/OASIS**: Standard dla BOD Infor.
* **EN 16931**: Europejska norma dotycząca fakturowania elektronicznego, z którą zgodny jest ZUGFeRD 2.x.
