# ZUGFeRD Field Mapping Overview

## Introduction

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) is a German e-invoicing standard based on the UN/CEFACT Cross Industry Invoice (CII) and the ISO standard 19005-3 (PDF/A-3). It allows for the exchange of structured invoice data in a PDF file.

DocBits extracts fields from ZUGFeRD documents and aligns them with Infor ERP systems (M3, LN) using OAGIS BOD standards.

## Supported ZUGFeRD Versions

DocBits supports multiple versions of the ZUGFeRD standard:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Data Flow

The data flow from a ZUGFeRD document to your ERP system follows these steps:

1. **Extraction**: DocBits parses the embedded XML data from the PDF based on the ZUGFeRD version.
2. **DocBits Field Mapping**: Extracted data is mapped to standard DocBits fields.
3. **ERP Alignment**: DocBits fields are mapped to Infor BOD (Business Object Document) fields or M3/LN specific API fields.
4. **Export**: The mapped data is exported to the Infor system.

## Mapping Standards

The mapping is based on the following standards:
* **UN/CEFACT CII**: The base for ZUGFeRD XML structure.
* **OAGIS/OASIS**: The standard for Infor BODs.
* **EN 16931**: The European standard for e-invoicing which ZUGFeRD 2.x is compliant with.
