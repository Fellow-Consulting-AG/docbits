# Panoramica della mappatura dei campi ZUGFeRD

## Introduzione

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) è uno standard tedesco per la fatturazione elettronica basato sull'UN/CEFACT Cross Industry Invoice (CII) e sullo standard ISO 19005-3 (PDF/A-3). Consente lo scambio di dati di fatturazione strutturati in un file PDF.

DocBits estrae i campi dai documenti ZUGFeRD e li allinea con i sistemi ERP Infor (M3, LN) utilizzando gli standard OAGIS BOD.

## Versioni ZUGFeRD supportate

DocBits supporta diverse versioni dello standard ZUGFeRD:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Flusso di dati

Il flusso di dati da un documento ZUGFeRD al sistema ERP segue questi passaggi:

1. **Estrazione**: DocBits analizza i dati XML incorporati nel PDF in base alla versione ZUGFeRD.
2. **Mappatura dei campi DocBits**: I dati estratti vengono mappati sui campi DocBits standard.
3. **Allineamento ERP**: I campi DocBits vengono mappati sui campi Infor BOD (Business Object Document) o sui campi API specifici di M3/LN.
4. **Esportazione**: I dati mappati vengono esportati nel sistema Infor.

## Standard di mappatura

La mappatura si basa sui seguenti standard:
* **UN/CEFACT CII**: La base per la struttura XML ZUGFeRD.
* **OAGIS/OASIS**: Lo standard per i BOD di Infor.
* **EN 16931**: Lo standard europeo per la fatturazione elettronica a cui ZUGFeRD 2.x è conforme.
