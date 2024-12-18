# Currently Supported E-Invoice Standards

## Supported Formats

DocBits supports the following e-invoicing formats:

* **FatturaPA**
* **PEPPOL BIS Billing 3.0**
* **Factur-X Basic**
* **ZUGFeRD**
* **XRechnung UBL 1.2**
* **XRechnung UBL 2.1**

## Expected Customization IDs

For each supported format, the following Customization IDs are required:

* **PEPPOL BIS Billing 3.0**\
  The expected Customization ID is:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
```

* **Factur-X Basic**\
  The expected ram ID is:

```xml
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:factur-x.eu:1p0:basic</ram:ID>

```

* **XRechnung UBL 1.2**\
  The expected Customization ID is:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_1.2</cbc:CustomizationID>
```

<pre class="language-xml"><code class="lang-xml"><strong> &#x3C;cbc:CustomizationID>urn:cen.eu:de16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_1.2&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 2.1**\
  The expected Customization ID is:

<pre class="language-xml"><code class="lang-xml"><strong>&#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_2.1&#x3C;/cbc:CustomizationID>
</strong></code></pre>

<pre class="language-xml"><code class="lang-xml"><strong>    &#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.1&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 3.0**\
  The expected Customization ID is:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0</cbc:CustomizationID>
```

\


## Roadmap for Upcoming Implementation

{% content-ref url="roadmap.md" %}
[roadmap.md](roadmap.md)
{% endcontent-ref %}
