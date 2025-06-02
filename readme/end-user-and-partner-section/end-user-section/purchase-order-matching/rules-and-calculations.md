# Regeln und Berechnungen

Auf dieser Seite finden Sie, welche Spalten abgeglichen werden, die Regeln, die sie befolgen, und wie die resultierende Berechnung durchgeführt wird.

## Welche Spalten werden abgeglichen?

Der Prozess des Abgleichs von Bestellungen gleicht nur bestimmte Spalten ab. Die folgende Liste zeigt, welche Spalten abgeglichen werden, sofern verfügbar. Wenn keine [Toleranz](rules-and-calculations.md#toleranzen-akzeptieren) festgelegt ist, werden die Spalten nur abgeglichen, wenn sie eine exakte (100%) Übereinstimmung aufweisen.

* [Menge](rules-and-calculations.md#menge) (Menge | Empfangene Menge | Empfangene Lieferung Offene Menge)
* Einzelpreis
* Bestellnummer
* Artikelnummer/Lieferantenartikel-ID
* Bestätigtes Lieferdatum

## Menge

Sie haben drei Optionen für den Abgleich der Menge.

* Menge
* Empfangene Menge
* Empfangene Lieferung Offene Menge

Sie können diese Option in **Einstellungen → Globale Einstellungen → Dokumenttypen → Weitere Einstellungen → Bestellung → Bestellung** festlegen.

## Toleranzen akzeptieren

Sie können angeben, dass eine bestimmte Toleranz während des Abgleichsprozesses akzeptabel ist. Standardmäßig werden nur exakte (100%) Übereinstimmungen als gültig betrachtet. Für weitere Informationen siehe die [detaillierte Dokumentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Status deaktivieren

Sie können bestimmte Zeilen mit bestimmten Status vom Abgleich ausschließen. Für weitere Informationen siehe die [detaillierte Dokumentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md).

## Berechnung

Unter der Tabelle mit den aus Ihrem Dokument extrahierten Informationen finden Sie einfache Berechnungen, um zu überprüfen, ob die gesamten Buchungen übereinstimmen.

### Erfasste Buchungen:

Dies wird basierend auf der erfassten Bestellnummer mit der folgenden Formel berechnet:

```
Erfasste Buchungen = EINZELPREIS * MENGE (basierend auf der Bestellung)
```

### Abgestimmte Summe:

Dies wird basierend auf dem Betrag, der aus dem Dokument extrahiert wurde, mit der folgenden Formel berechnet:

```
 Abgestimmte Summe = EINZELPREIS * MENGE (basierend auf dem Dokument)
```

### **Gebühren:**

In diesem Abschnitt werden alle anfallenden Gebühren hinzugefügt, sofern sie vorhanden sind.

### Offener Betrag:

Die resultierende Differenz wird hier angezeigt und wie folgt berechnet:

```
Offener Betrag = Erfasste Buchungen - Abgestimmte Summe - Gebühren
```
