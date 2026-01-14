# XRechnung

## Überblick

Im XRechnung-Verwaltungspanel werden Sie auf die folgenden Hauptkomponenten stoßen:

## 1. Transformation

### Zweck

Der Transformationsprozess ist entscheidend für die Umwandlung von Rohdaten, normalerweise im XML-Format, in ein strukturiertes Format, das spezifische Anforderungen erfüllt, wie z. B. das Generieren einer Rechnung. Bei XRechnung wird dies hauptsächlich mit XSLT (Extensible Stylesheet Language Transformations) erreicht. XSLT ist eine Sprache, die für die Transformation von XML-Dokumenten in andere Dokumenttypen wie ein anderes XML, HTML oder Klartext entwickelt wurde.

### Wie es funktioniert

* XSLT-Vorlage: Die XSLT-Datei definiert, wie die XML-Daten verarbeitet werden und wie die endgültige Ausgabe aussehen soll. Sie wendet Regeln und Vorlagen an, um die Daten aus dem XML-Dokument zu extrahieren, zu manipulieren und auszugeben.
* Elemente und Attribute: Die XSLT-Datei enthält spezifische Elemente und Attribute, die den Transformationsprozess steuern. Zum Beispiel wird \<xsl:value-of> verwendet, um den Wert eines bestimmten Knotens aus dem XML-Dokument zu extrahieren.

### Admin-Funktionen

* Ändern der XSLT:
* Vorhandene Vorlagen bearbeiten: Ein Administrator kann die vorhandenen XSLT-Vorlagen ändern, um die Transformation der XML-Eingabedaten zu ändern. Wenn beispielsweise zusätzliche Informationen aus dem XML-Dokument extrahiert werden müssen, kann ein Administrator neue Regeln in der XSLT-Datei hinzufügen.
* Neue Versionen erstellen: Wenn Änderungen erforderlich sind, kann ein Administrator eine neue Version der XSLT-Vorlage erstellen. Dadurch wird sichergestellt, dass frühere Versionen als historische Referenz oder für ein Rollback erhalten bleiben.

### Beispiel:

Angenommen, die XSLT-Vorlage extrahiert die Rechnungs-ID mit:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Wenn ein neues Feld, wie z. B. eine Kundenreferenznummer, extrahiert werden muss, kann ein Administrator Folgendes hinzufügen:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Vorschau

### Zweck

Mit der Vorschaufunktion können Administratoren die durch die XSLT-Transformation generierte Ausgabe anzeigen, bevor sie sie fertigstellen. Dieser Schritt ist entscheidend, um sicherzustellen, dass die Transformationsregeln korrekt funktionieren und die Ausgabe den erforderlichen Standards entspricht.

### Wie es funktioniert

* Echtzeit-Validierung: Die Vorschaufunktion bietet eine Echtzeit-Darstellung, wie die transformierten Daten aussehen werden, wenn sie auf ein tatsächliches Dokument (wie eine Rechnung) angewendet werden. Dies hilft dabei, Fehler oder Formatierungsprobleme frühzeitig zu erkennen.
* Anpassungen: Wenn die Vorschau Diskrepanzen oder Fehler anzeigt, können Anpassungen direkt in der Transformationsdatei (XSLT) vorgenommen werden.

### Admin-Funktionen

* Anpassen der Vorschau:
* Vorschaueinstellungen ändern: Ein Administrator kann anpassen, welche Teile der Transformation in der Vorschau angezeigt werden. Er könnte sich beispielsweise auf bestimmte Abschnitte des Dokuments konzentrieren oder neue Regeln testen, die der XSLT-Vorlage hinzugefügt wurden.
* Speichern und Iterieren: Nach dem Vornehmen von Anpassungen kann die Vorschau aktualisiert werden, um die Änderungen zu sehen. Dieser iterative Prozess ermöglicht eine Feinabstimmung, bis das gewünschte Ergebnis erreicht ist.

### Beispiel:

Wenn ein Administrator bemerkt, dass das Datumsformat in der Vorschau falsch ist (z. B. YYYY-MM-DD anstelle von DD-MM-YYYY), kann er die XSLT ändern, um das Datum korrekt zu formatieren, und das Ergebnis sofort in der Vorschau sehen.

## 3. Extraktionspfade

### Zweck

Extraktionspfade definieren die spezifischen Pfade innerhalb einer XML- oder JSON-Struktur, aus denen Daten extrahiert werden sollen. Dieser Prozess ist entscheidend für die Isolierung wichtiger Informationen innerhalb des Dokuments, die in der Transformation oder für andere Verarbeitungsaufgaben verwendet werden.

### Wie es funktioniert

* XPath und JSONPath: Extraktionspfade verwenden Sprachen wie XPath (für XML) oder JSONPath (für JSON), um den Speicherort der Daten im Dokument anzugeben. Diese Pfade sind entscheidend, um dem System genau mitzuteilen, wo es die erforderlichen Informationen finden und wie es sie extrahieren soll.

### Admin-Funktionen

* Definieren und Ändern von Pfaden:
* Vorhandene Pfade ändern: Ein Administrator kann die Extraktionspfade ändern, wenn sich die Datenstruktur ändert oder zusätzliche Daten extrahiert werden müssen. Dies kann die Änderung der XPath- oder JSONPath-Ausdrücke beinhalten.
* Neue Pfade hinzufügen: Für neue Felder oder Datenpunkte kann ein Administrator neue Extraktionspfade definieren. Dies würde die Angabe des korrekten Pfads im XML- oder JSON-Dokument beinhalten.

### Beispiel:

Wenn in einem XML-Rechnungsdokument der Pfad zur Rechnungs-ID definiert ist als:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

Und ein neues Feld, wie z. B. eine Lieferadresse, hinzugefügt werden muss, kann ein Administrator Folgendes hinzufügen:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```
