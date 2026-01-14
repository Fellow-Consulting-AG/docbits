# Obecnie Obsługiwane Standardy E-Faktur

## Obsługiwane Formaty

DocBits obsługuje następujące formaty e-fakturowania:

* **FatturaPA**
* **PEPPOL BIS Billing 3.0**
* **Factur-X Basic**
* **EDIFACT INVOIC02**
* **ZUGFeRD 1.0**
* **ZUGFeRD 2.1**
* **ZUGFeRD 2.3**
* **XRechnung UBL 1.2**
* **XRechnung UBL 2.1**
* **XRechnung UBL 3.0**

## Oczekiwane Identyfikatory Dostosowania (Customization IDs)

Dla każdego obsługiwanego formatu wymagane są następujące Identyfikatory Dostosowania:

* **PEPPOL BIS Billing 3.0**
  Oczekiwany Identyfikator Dostosowania to:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
```

* **Factur-X Basic**
  Oczekiwany identyfikator ram to:

```xml
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:factur-x.eu:1p0:basic</ram:ID>
```

* **ZUGFeRD 1.0**
  Oczekiwany identyfikator ram to:

```xml
<ram:ID>urn:ferd:CrossIndustryDocument:invoice:1p0:
```

* **ZUGFeRD 2.1** 
  Oczekiwane identyfikatory ram to:

```xml
urn:factur-x.eu:1p0:basic</ram:ID>
urn:factur-x.eu:1p0:basicwl</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017</ram:ID>
urn:factur-x.eu:1p0:extended</ram:ID>
urn:factur-x.eu:1p0:minimum</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.1</ram:ID>
```

* **ZUGFeRD 2.3**
  Oczekiwany identyfikator ram to:

```xml
urn:zugferd:2p1:comfort
urn:zugferd:2p1:en16931
urn:zugferd:2p1:extended
urn:zugferd:2p1:basic
```

* **XRechnung UBL 1.2**
  Oczekiwany Identyfikator Dostosowania to:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_1.X</cbc:CustomizationID>
```

<pre class="language-xml"><code class="lang-xml"><strong> &#x3C;cbc:CustomizationID>urn:cen.eu:de16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_1.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 2.1**
  Oczekiwany Identyfikator Dostosowania to:

<pre class="language-xml"><code class="lang-xml"><strong>&#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

<pre class="language-xml"><code class="lang-xml"><strong>    &#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 3.0**
  Oczekiwany Identyfikator Dostosowania to:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.X</cbc:CustomizationID>

```

*   **EDIFACT INVOIC02**

    Oczekiwany identyfikator to:

```xml
<INVOIC02>
```

## Mapa Drogowa dla Nadchodzącego Wdrożenia

{% content-ref url="roadmap.md" %}
[roadmap.md](roadmap.md)
{% endcontent-ref %}
