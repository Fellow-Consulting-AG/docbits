---
düzen:
başlık:
görünür: true
açıklama:
görünür: true
içindekiler:
görünür: true
taslak:
görünür: true
sayfalandırma:
görünür: true
---

# EDI Veri Dönüşüm Süreci

####

<figure><img src="../../../.gitbook/assets/EDI (1).png" alt=""><figcaption></figcaption></figure>

#### Adım 1: Yapı Tanımlayıcı

* **Format**: JSON
* **Amaç**: Bu adım, EDI verisinin yapısını tanımlamayı içerir. `SAC`, `N1` ve `PO1` gibi segmentleri belirtmeyi ve her bir segment içinde bulunan alanları detaylandırmayı içerir. İç içe geçmiş yapıları içeren segmentler için veri hiyerarşisini düzgün bir şekilde organize etmek için döngüler tanımlanır.
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
#### Adım 2: XSLT Kullanarak Dönüşüm

* **Format**: XSLT
* **Amaç**: Bu adım, yapılandırılmış JSON verilerini yapılandırılmış bir XML formatına dönüştürmeyi içerir, özellikle çıktıyı daha fazla işleme veya entegrasyon için gereksinimleri karşılayacak şekilde özelleştirir. Bu dönüşüm, belirli değerlere dayalı olarak doğrulama türleri, sipariş detayları ve koşullu unsurlar gibi kesin bilgilerin çıkarılmasına yardımcı olur.
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
#### Adım 3: Önizleme (HTML Dönüşümü)

* **Format**: XSLT (HTML çıktısı)
* **Amaç**: Adım 2'den gelen XML verilerini, dönüştürülmüş verileri okunabilir ve görsel olarak çekici bir formatta önizlemek için HTML formatına dönüştürür. HTML düzeni, sunum için stiller içerir ve satın alma siparişleri, tedarikçi detayları ve sipariş koşulları gibi verileri yapılandırarak kolay görüntüleme sağlar.
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
#### Adım 4: Çıkarma Yolları

* **Format**: JSON
* **Amaç**: Adım 2'de üretilen XML verilerinden anahtar değerleri çıkarmak için JSON yollarını belirtir. Bu yollar, satın alma siparişleri ve para birimi gibi belirli veri noktalarını almak için kullanılır ve aşağı akış işlemleri ve diğer sistemlere entegrasyon için önemlidir.
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
Bu güncellenmiş sıra, ham EDI verilerini yapılandırılmış, işlenebilir bilgilere dönüştürmek için JSON'u veri yapılandırması için, dönüşüm ve HTML önizleme için XSLT'yi ve ardından veri çıkarma ve entegrasyon için JSON yollarını kullanarak kapsamlı bir süreç sağlar.
