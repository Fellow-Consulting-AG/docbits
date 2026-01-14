# Normes de Facturation Électronique Actuellement Prises en Charge

## Formats Pris en Charge

DocBits prend en charge les formats de facturation électronique suivants :

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

## ID de Personnalisation Attendus

Pour chaque format pris en charge, les ID de Personnalisation suivants sont requis :

* **PEPPOL BIS Billing 3.0**
  L'ID de Personnalisation attendu est :

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
```

* **Factur-X Basic**
  L'ID ram attendu est :

```xml
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:factur-x.eu:1p0:basic</ram:ID>
```

* **ZUGFeRD 1.0**
  L'ID ram attendu est :

```xml
<ram:ID>urn:ferd:CrossIndustryDocument:invoice:1p0:
```

* **ZUGFeRD 2.1** 
  Les ID ram attendus sont :

```xml
urn:factur-x.eu:1p0:basic</ram:ID>
urn:factur-x.eu:1p0:basicwl</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017</ram:ID>
urn:factur-x.eu:1p0:extended</ram:ID>
urn:factur-x.eu:1p0:minimum</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.1</ram:ID>
```

* **ZUGFeRD 2.3**
  L'ID ram attendu est :

```xml
urn:zugferd:2p1:comfort
urn:zugferd:2p1:en16931
urn:zugferd:2p1:extended
urn:zugferd:2p1:basic
```

* **XRechnung UBL 1.2**
  L'ID de Personnalisation attendu est :

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_1.X</cbc:CustomizationID>
```

<pre class="language-xml"><code class="lang-xml"><strong> &#x3C;cbc:CustomizationID>urn:cen.eu:de16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_1.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 2.1**
  L'ID de Personnalisation attendu est :

<pre class="language-xml"><code class="lang-xml"><strong>&#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

<pre class="language-xml"><code class="lang-xml"><strong>    &#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 3.0**
  L'ID de Personnalisation attendu est :

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.X</cbc:CustomizationID>

```

*   **EDIFACT INVOIC02**

    L'ID attendu est :

```xml
<INVOIC02>
```

## Feuille de Route pour la Prochaine Implémentation

{% content-ref url="roadmap.md" %}
[roadmap.md](roadmap.md)
{% endcontent-ref %}