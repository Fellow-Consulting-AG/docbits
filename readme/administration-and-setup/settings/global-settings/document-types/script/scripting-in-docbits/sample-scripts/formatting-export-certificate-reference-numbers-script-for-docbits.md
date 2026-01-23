# Skript zur Formatierung von Exportzertifikat-Referenznummern für Docbits

Dieses Dokument beschreibt das Skript "Formatting Export Certificate Reference Numbers", das darauf abzielt, Referenznummern auf Exportzertifikaten in Docbits zu standardisieren. Eine ordnungsgemäße Formatierung stellt sicher, dass Referenznummern den Anforderungen externer Systeme oder behördlicher Vorschriften entsprechen.

### Zweck

Das Hauptziel des Skripts ist die Formatierung von Referenznummern auf Exportzertifikaten, um sicherzustellen, dass sie eine vordefinierte Längenanforderung erfüllen, indem sie mit führenden Nullen aufgefüllt werden. Diese Konsistenz hilft, ein standardisiertes Format für alle über Docbits verarbeiteten Exportdokumente aufrechtzuerhalten.

### Skriptübersicht

Das Skript identifiziert das Feld `reference_number` in einem Exportzertifikat, überprüft dessen Länge und füllt die Nummer bei Bedarf mit führenden Nullen auf, um sicherzustellen, dass sie die Mindestlängenanforderung erfüllt.

#### Code-Ausschnitt

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```


