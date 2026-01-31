# Resumen de mapeo de campos ZUGFeRD

## Introducción

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) es un estándar alemán de facturación electrónica basado en el UN/CEFACT Cross Industry Invoice (CII) y el estándar ISO 19005-3 (PDF/A-3). Permite el intercambio de datos de factura estructurados en un archivo PDF.

DocBits extrae campos de documentos ZUGFeRD y los alinea con los sistemas ERP de Infor (M3, LN) utilizando los estándares OAGIS BOD.

## Versiones de ZUGFeRD compatibles

DocBits es compatible con varias versiones del estándar ZUGFeRD:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Flujo de datos

El flujo de datos desde un documento ZUGFeRD hasta su sistema ERP sigue estos pasos:

1. **Extracción**: DocBits analiza los datos XML incrustados del PDF basándose en la versión de ZUGFeRD.
2. **Mapeo de campos de DocBits**: Los datos extraídos se mapean a los campos estándar de DocBits.
3. **Alineación con el ERP**: Los campos de DocBits se mapean a los campos de Infor BOD (Business Object Document) o a los campos de la API específicos de M3/LN.
4. **Exportación**: Los datos mapeados se exportan al sistema Infor.

## Estándares de mapeo

El mapeo se basa en los siguientes estándares:
* **UN/CEFACT CII**: La base para la estructura XML de ZUGFeRD.
* **OAGIS/OASIS**: El estándar para los BOD de Infor.
* **EN 16931**: El estándar europeo para la facturación electrónica con el que cumple ZUGFeRD 2.x.
