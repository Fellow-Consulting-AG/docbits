# Fields

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.02.31.png" alt=""><figcaption></figcaption></figure>

#### Übersicht

Die Felder-Einstellung bietet eine Benutzeroberfläche, über die Administratoren die Eigenschaften und das Verhalten einzelner Datenfelder verwalten können, die mit einem Dokumententyp verknüpft sind. Jedes Feld kann angepasst werden, um die Genauigkeit und Effizienz der Datenerfassung und -validierung zu optimieren.

#### Hauptfunktionen und Optionen

1. **Feldkonfiguration**:

* **Feldnamen**: Listet die Namen der Felder auf, die in der Regel den Datenelementen im Dokument entsprechen, wie z.B. "Rechnungsnummer" oder "Bestelldatum".
* **Erforderlich**: Administratoren können Felder als erforderlich markieren, um sicherzustellen, dass Daten für diese Felder eingegeben oder erfasst werden müssen, um die Dokumentenverarbeitung abzuschließen.
* **Schreibgeschützt**: Felder können auf schreibgeschützt gesetzt werden, um Änderungen nach der Datenerfassung oder während bestimmter Phasen der Dokumentenverarbeitung zu verhindern.
* **Versteckt**: Felder können in der Benutzeroberfläche ausgeblendet werden, was für sensible Informationen oder zur Vereinfachung der Benutzerworkflows nützlich ist.

2. **Erweiterte Einstellungen**:

* **Validierung erzwingen**: Stellt sicher, dass die in ein Feld eingegebenen Daten bestimmte Validierungsregeln bestehen, bevor sie akzeptiert werden.
* **OCR (Optische Zeichenerkennung)**: Dieser Schalter kann aktiviert werden, um die OCR-Verarbeitung für ein bestimmtes Feld zu ermöglichen, was für die automatisierte Datenauslese aus gescannten oder digitalen Dokumenten nützlich ist.
* **Übereinstimmungswert**: Administratoren können einen Übereinstimmungswert definieren, eine Schwelle, die zur Bestimmung des Vertrauensniveaus der Datenerkennung oder -übereinstimmung verwendet wird und sich darauf auswirkt, wie Datenvalidierung und Qualitätsprüfungen durchgeführt werden.

3. **Aktionsbuttons**:

* **Neues Feld erstellen**: Ermöglicht das Hinzufügen neuer Felder zum Dokumententyp.
* **Bearbeitungssymbole**: Jedes Feld verfügt über ein Bearbeitungssymbol, das es Administratoren ermöglicht, feldspezifische Einstellungen wie Datentyp, Standardwerte oder verbundene Geschäftslogik weiter zu konfigurieren.
* **Einstellungen speichern**: Übernimmt die vorgenommenen Änderungen an den Feldkonfigurationen.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
