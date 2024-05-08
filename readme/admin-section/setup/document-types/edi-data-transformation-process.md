---
layout:
title:
visible: true
description:
visible: true
tableOfContents:
visible: true
outline:
visible: true
pagination:
visible: true
---

# Proces transformacije EDI podataka

####

<figure><img src="../../../.gitbook/assets/EDI (1).png" alt=""><figcaption></figcaption></figure>

#### Korak 1: Opis strukture

* **Format**: JSON
* **Svrha**: Ovaj korak uključuje definisanje strukture EDI podataka. To uključuje određivanje segmenata poput `SAC`, `N1` i `PO1`, i detaljno opisuje polja koja se nalaze unutar svakog segmenta. Za segmente koji sadrže ugniježđene strukture, definišu se petlje kako bi se pravilno organizovala hijerarhija podataka.
```json
{
"SAC": {"fields": ["SAC", "DTM", "TX1", "TD5"]},
"N1": {"fields": ["N1", "N2", "N3", "N4", "PER"]},
"PO1": {
"fields": ["PO1", "REF"],
"loops": {
"SAC": {"fields": ["SAC", "TX1", "DTM"]}
}
}
}
```
#### Korak 2: Transformacija korišćenjem XSLT

* **Format**: XSLT
* **Svrha**: Ovaj korak uključuje transformisanje strukturiranih JSON podataka u strukturirani XML format, posebno prilagođavanje izlaza kako bi se ispunili zahtevi za dalju obradu ili integraciju. Ova transformacija pomaže u izdvajanju preciznih informacija poput tipova potvrda, detalja porudžbina i uslovnih elemenata na osnovu specifičnih vrednosti.
```xml
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" />
<xsl:template match="/">
<ORDER_CONFIRMATION>
<ACKNOWLEDGEMENT_TYPE>
<xsl:value-of select="//BAK/VALUE_2/text()" />
</ACKNOWLEDGEMENT_TYPE>
<ACKNOWLEDGEMENT_TYPE_DESCRIPTION>
<xsl:choose>
<xsl:when test="//BAK/VALUE_2='AD'">With detail, no change</xsl:when>
<xsl:when test="//BAK/VALUE_2='AC'">With detail and change</xsl:when>
<xsl:otherwise>Unknown</xsl:otherwise>
</xsl:choose>
</ACKNOWLEDGEMENT_TYPE_DESCRIPTION>
<!-- Additional fields and conditions are similarly transformed -->
</ORDER_CONFIRMATION>
</xsl:template>
</xsl:stylesheet>

```
#### Korak 3: Pregled (Konverzija u HTML)

* **Format**: XSLT (izlaz u HTML-u)
* **Svrha**: Konvertuje XML podatke iz Koraka 2 u HTML format radi pregledanja transformisanih podataka na čitljiv i vizuelno privlačan način. HTML raspored uključuje stilove za prezentaciju i strukturira podatke poput narudžbenica, detalja dobavljača i uslova narudžbe radi lakšeg pregledanja.
```xml
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" />
<xsl:template match="/">
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Preview of Transformed EDI Data</title>
<!-- Styles and head elements -->
</head>
<body>
<div>
<!-- HTML structure mimicking an invoice or other document type, with data bindings from the transformed XML -->
</div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>


```
#### Korak 4: Putanje ekstrakcije

* **Format**: JSON
* **Svrha**: Specificira JSON putanje za ekstrakciju ključnih vrednosti iz XML podataka proizvedenih u Koraku 2. Ove putanje se koriste za dobijanje određenih podataka kao što su narudžbine i valuta, koje su ključne za obradu nizvodno i integraciju u druge sisteme.
```json
{
"fields": {
"purchase_order": "//ORDER_CONFIRMATION/PURCHASE_ORDER/text()",
"currency": "//ORDER_CONFIRMATION/CURRENCY/text()",
...
},
"tables": [
{
"name": "ORDER_CONFIRMATION_TABLE",
"row_path": "//ORDER_CONFIRMATION/ORDER_LINES/ORDER_LINE",
"columns": [
{"name": "POSITION", "path": "POSITION/text()"},
...
]
}
]
}
```
Ova ažurirana sekvenca osigurava temeljan proces, pretvarajući sirove EDI podatke u strukturirane, upotrebljive informacije koristeći JSON za strukturiranje podataka, XSLT za transformaciju i HTML pregled, zatim JSON putanje za ekstrakciju podataka i integraciju.
