# Padrões de Fatura Eletrônica Atualmente Suportados

{% embed url="https://youtu.be/li8KjWO18eU" %}
DocBits E-Invoice Tutorial: Process XRechnung & ZUGFeRD/Factur-X, Validate Data & Automate Workflows
{% endembed %}

## Formatos Suportados

DocBits suporta os seguintes formatos de faturamento eletrônico:

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

## IDs de Personalização Esperados

Para cada formato suportado, os seguintes IDs de Personalização são necessários:

* **PEPPOL BIS Billing 3.0**
  O ID de Personalização esperado é:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
```

* **Factur-X Basic**
  O ID ram esperado é:

```xml
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:factur-x.eu:1p0:basic</ram:ID>
```

* **ZUGFeRD 1.0**
  O ID ram esperado é:

```xml
<ram:ID>urn:ferd:CrossIndustryDocument:invoice:1p0:
```

* **ZUGFeRD 2.1** 
  Os IDs ram esperados são:

```xml
urn:factur-x.eu:1p0:basic</ram:ID>
urn:factur-x.eu:1p0:basicwl</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017</ram:ID>
urn:factur-x.eu:1p0:extended</ram:ID>
urn:factur-x.eu:1p0:minimum</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.1</ram:ID>
```

* **ZUGFeRD 2.3**
  O ID ram esperado é:

```xml
urn:zugferd:2p1:comfort
urn:zugferd:2p1:en16931
urn:zugferd:2p1:extended
urn:zugferd:2p1:basic
```

* **XRechnung UBL 1.2**
  O ID de Personalização esperado é:

<pre class="language-xml"><code class="lang-xml"><strong> <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_1.X</strong></code></pre>

<pre class="language-xml"><code class="lang-xml"><strong> &#x3C;cbc:CustomizationID>urn:cen.eu:de16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_1.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 2.1**
  O ID de Personalização esperado é:

<pre class="language-xml"><code class="lang-xml"><strong>&#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

<pre class="language-xml"><code class="lang-xml"><strong>    &#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 3.0**
  O ID de Personalização esperado é:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.X</cbc:CustomizationID>

```

*   **EDIFACT INVOIC02**

    O ID esperado é:

```xml
<INVOIC02>
```

## Roteiro para Implementação Futura

{% content-ref url="roadmap.md" %}
[roadmap.md](roadmap.md)
{% endcontent-ref %}