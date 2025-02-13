# Layout-Manager

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.46.24.png" alt=""><figcaption></figcaption></figure>

#### Überblick

Der Layout-Manager ermöglicht es Administratoren, das Layout von Dokumententypen visuell zu konfigurieren und anzupassen, indem sie Eigenschaften für verschiedene Datenfelder und Gruppen innerhalb eines Dokuments festlegen. Diese Benutzeroberfläche hilft sicherzustellen, dass die Extraktionsmodelle und manuellen Dateneingabepunkte genau mit der Struktur des gescannten oder hochgeladenen Dokuments in DocBits übereinstimmen.

#### Hauptkomponenten

1. **Gruppen und Felder**:
* **Gruppen**: Organisatorische Einheiten innerhalb eines Dokumententyps, die verwandte Felder kategorisieren (z. B. Rechnungsdetails, Zahlungsdetails). Diese können erweitert oder zusammengeklappt und so angeordnet werden, dass sie die logische Gruppierung im tatsächlichen Dokument widerspiegeln.
* **Felder**: Einzelne Datenpunkte innerhalb jeder Gruppe (z. B. Rechnungsnummer, Zahlungsbedingungen). Jedes Feld kann angepasst werden, um festzulegen, wie Daten erfasst, angezeigt und verarbeitet werden.
2. **Eigenschaften-Panel**:
* Dieses Panel zeigt die Eigenschaften des ausgewählten Feldes oder der Gruppe an und ermöglicht eine detaillierte Konfiguration, wie z. B.:
* **Beschriftung**: Die sichtbare Beschriftung für das Feld in der Benutzeroberfläche.
* **Feldname**: Der technische Bezeichner, der im System verwendet wird.
* **Elementbreite in Prozent**: Bestimmt die Breite des Feldes im Verhältnis zum Dokumentenlayout.
* **Tab-Index**: Steuert die Reihenfolge der Navigation per Tabulatortaste.
* **Skript bei Änderung ausführen**: Ob ein Skript ausgeführt werden soll, wenn sich der Feldwert ändert.
* **Beschriftung links anzeigen**: Ob die Beschriftung links vom Feld oder darüber angezeigt wird.
* **Ist Textbereich**: Gibt an, ob das Feld ein Textbereich sein soll, der größere Textmengen aufnehmen kann.
* **Modelltyp auswählen**: Option zur Auswahl des Modelltyps, der die Extraktion dieses Feldes durchführt.
* **Feldlänge**: Maximale Länge der Daten, die in diesem Feld akzeptiert werden sollen.
* **Verbotene Schlüsselwörter**: Schlüsselwörter, die im Feld nicht erlaubt sind.
3. **Vorlagen-Vorschau**:
* Zeigt eine Echtzeitvorschau, wie das Dokument basierend auf der aktuellen Layoutkonfiguration aussehen wird. Dies hilft sicherzustellen, dass das Layout der tatsächlichen Dokumentenstruktur entspricht und ist entscheidend für das Testen und Verfeinern des Dokumentenverarbeitungs-Setups.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
