# Regeln für den Bestellabgleich

## Einführung: Bestellung und PO-Regelverwaltung

Der Abgleich von Bestellungen (Purchase Order, PO) ist ein kritischer Prozess, um die Konsistenz zwischen Bestellungen und entsprechenden eingehenden Rechnungen oder Wareneingängen sicherzustellen. Ein robustes Regelwerk ist unerlässlich, um eine hohe Rate an automatischen Abgleichen zu erreichen, Betrug zu verhindern und korrekte Zahlungen sicherzustellen.

Diese Konfigurationsseite dient dazu, die Regeln zu definieren und zu verwalten, die bestimmen, _wie_ PO-Positionen mit dem entsprechenden eingehenden Beleg (Rechnung, Auftragsbestätigung) abgeglichen werden.

***

## Zugriff

1.  Navigieren Sie zu **Einstellungen --> Globale Einstellungen --> Belegtypen**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Wählen Sie den gewünschten Belegtyp aus und klicken Sie auf **Weitere Einstellungen**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Gehen Sie dann zum Abschnitt Bestellung und klicken Sie auf die Schaltfläche (PO match serverseitig) und danach auf Regeln für den Bestellabgleich konfigurieren.

    <figure><img src="../../../../../../.gitbook/assets/docbits_field_validation_formatting.png" alt="Docbits Field Validation Formatting"><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Globale Einstellungen (Basisregeln)

Diese Einstellungen bilden den Rahmen, der für alle Abgleichsregeln gilt:

* **Einstellung:** Menge abgleichen auf
  * **Zweck:** Definiert, welches spezifische Mengenfeld primär als Referenzpunkt für den Abgleich von Bestellungspositionen über alle Regeln hinweg verwendet werden soll.
  * **Gültige Werte:** Menge oder andere im System verfügbare Mengenfelder, abhängig von der Datenstruktur (z. B. ein alternatives normalisiertes Mengenfeld).
  * **Abhängigkeit:** Bestimmt die Basis für alle Abgleichsregeln, die die Menge in ihre Vergleichskriterien einbeziehen.
* **Einstellung:** Standardtoleranz (Vorgabetoleranz)
  * **Zweck:** Definiert die zulässige prozentuale Abweichung der Menge, damit ein Abgleich als gültig betrachtet wird. Sie gleicht geringfügige Rundungs- oder Mengendifferenzen aus.
  * **Gültiger Wert:** Eine Dezimalzahl (z. B. 0,005 entspricht 0,5 %).
  * **Abhängigkeit:** Gilt für Regeln, die Mengenfelder für den Abgleich verwenden und bei denen die Option "Toleranz zulassen" aktiviert ist.

***

## Regelliste

Die Regelliste zeigt alle verfügbaren Abgleichsregeln an und verwaltet deren Ausführungsreihenfolge.

#### Struktur und Ausführung

* **Priorität:** Dieses numerische Feld (z. B. 1, 2, 3) bestimmt die Ausführungsreihenfolge der Regeln. Regeln mit einer niedrigeren Prioritätszahl werden zuerst versucht. Dies ermöglicht Administratoren den Aufbau einer Hierarchie, die typischerweise mit den spezifischsten und strengsten Regeln beginnt (z. B. Abgleich nach Positionsnummer und Artikelnummer) und auf allgemeinere oder weniger restriktive Regeln zurückfällt.
* **Name & Beschreibung:** Bietet eine klare Identifizierung und Kontext für die Regel und erläutert die verwendeten Primärkriterien (z. B. "Standardregel Nr. 1: Abgleich basierend auf Positionsnummer, Artikel-ID und Menge").
* **Aktiv:** Ein einfacher Schalter, der die sofortige Aktivierung oder Deaktivierung der Regel ermöglicht, ohne deren Konfiguration löschen zu müssen.

**Ausführungsfluss:** Das System führt den Abgleich in einer kaskadierenden Sequenz durch. Wenn eine Regel (z. B. Priorität 1) eine Position erfolgreich abgleicht, stoppt der Prozess für diese Position. Wenn kein Abgleich gefunden wird, fährt das System mit der nächsten Regel in der Prioritätsfolge fort (z. B. Priorität 2).

***

## Regelkonfiguration (Detail-Einstellungen)

Dieser detaillierte Konfigurationsbereich definiert die spezifische Logik und die Kriterien für eine einzelne Regel.

#### Basisparameter

* **Regeltyp (z. B. Einzelabgleich):** Gibt die Kardinalität des Abgleichs an. Einzelabgleich (Single Match) ist der gebräuchlichste Typ und erfordert eine Eins-zu-eins-Zuordnung (eine PO-Position zu einer Rechnungsposition). Andere Typen könnten n-zu-1- oder 1-zu-n-Abgleiche für aggregierte Artikel oder Teillieferungen umfassen.
* **Automatischer Abgleich:** Wenn aktiviert, versucht das System, diese Regel vollständig automatisch anzuwenden. Für die automatische Verarbeitung ist ein hohes Vertrauen in die Kriterien erforderlich.
* **Manueller Abgleich:** Wenn aktiviert, kann diese Regel dem Benutzer während des manuellen Abgleichschritts präsentiert oder von ihm angewendet werden, wobei ihm ein vordefinierter Satz von Vergleichskriterien zur Lösung von Ausnahmen angeboten wird.

#### Spaltenvergleich (Abgleichskriterien)

Dies ist der Kern der Regellogik und legt fest, welche Felder zwischen den Belegen übereinstimmen müssen.

1. Definition der zu vergleichenden Spalten:
   * **PO-Spalten:** Das aus den Bestelldaten gezogene Feld (z. B. Positionsnummer).
   * **Extrahierte Tabellenspalten:** Das entsprechende Feld, das aus dem eingehenden Beleg (Rechnung/Auftragsbestätigung) extrahiert oder analysiert wurde (z. B. `POSITION`).
2. **Vergleichstyp:** Definiert die Art der erforderlichen Übereinstimmung (z. B. Tt für Text-/String-Vergleich, der eine exakte Übereinstimmung Zeichen für Zeichen erfordert; # für numerischen Vergleich).
3. **Toleranz zulassen:** Bei numerischen Feldern (Menge, Preis) weist die Aktivierung dieser Option das System an, die zuvor definierte globale Standardtoleranz anzuwenden. Wenn dies für ein numerisches Feld _nicht_ aktiviert ist, müssen die Werte exakt übereinstimmen.
4. **Bei manuellem Abgleich ignorieren:** Wenn aktiviert, wird dieses Kriterium bei manuellem Eingreifen gelockert. Dies ist nützlich für Felder wie Beschreibungen oder interne Referenzen, die leicht variieren können, und ermöglicht es dem Benutzer, geringfügige, unkritische Nichtübereinstimmungen zu überstimmen.

**Beispiel: Strenge PO-Abgleichsregel (`DefaultRule#1`)**

Eine typische strenge Regel kombiniert obligatorische Identitätsprüfungen mit Werteprüfungen:

* **Obligatorische Identität:** Positionsnummer und Artikelkennung müssen exakt übereinstimmen (Textvergleich, keine Toleranz).
* **Werteprüfungen:** Effektive normalisierte Menge und effektiver normalisierter Einzelpreis müssen übereinstimmen (numerischer Vergleich, Toleranz zulässig). Nur wenn alle vier Kriterien erfüllt sind (bei Werten mit Toleranz), wird ein automatischer Abgleich durchgeführt.

***

## Auswirkungen auf den PO-Abgleichsprozess

Das definierte Regelwerk steuert direkt die Effizienz und Integrität des Workflows für den Bestellabgleich:

* **Priorisierung und Fallbacks:** Die definierte Priorität stellt sicher, dass das System zuerst die zuverlässigste Abgleichsmethode versucht. Wenn die strengen Regeln mit hoher Priorität fehlschlagen, fällt das System auf allgemeinere Regeln zurück, mit dem Ziel, die Anzahl der Ausnahmen, die an Benutzer weitergeleitet werden, zu minimieren.
* **Steuerung der Abgleichsqualität:** Strengere Regeln (die exaktere Übereinstimmungen und weniger Toleranz erfordern) führen zu weniger, aber höchst zuverlässigen automatischen Abgleichen. Lockerere Regeln erhöhen die automatische Abgleichsrate, erhöhen jedoch das Risiko von fälschlicherweise positiven Ergebnissen.
* **Ausnahmebehandlung (Manueller Abgleich):** Durch die Aktivierung von Regeln für den manuellen Abgleich bietet das System den Benutzern strukturierte Optionen. Wenn eine Transaktion die automatischen Abgleichskriterien nicht erfüllt, wird sie zu einer Ausnahme. Der Benutzer kann dann versuchen, die Ausnahme zu beheben, indem er eine vordefinierte manuelle Regel anwendet, die möglicherweise gelockerte Kriterien aufweist (z. B. Ignorieren einer geringfügigen Textabweichung gemäß der Einstellung "Bei manuellem Abgleich ignorieren").

***

## Anpassen der PO-Abgleichsregeln

Um die PO-Abgleichsregeln zu bearbeiten, kann die Standardversion geklont werden, indem Sie auf **"Versionierung konfigurieren"** klicken und die Option **"Als Entwurf klonen"** aus den verfügbaren Kartenoptionen verwenden.

<figure><img src="../../../../../../.gitbook/assets/docbits_doc_type_export_formats.png" alt="Docbits Doc Type Export Formats"><figcaption></figcaption></figure>
