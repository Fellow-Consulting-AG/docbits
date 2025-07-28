# Schulung Linienfelder/Tabelle Schulung

## Tabelle Schulung: Wann und wie man sie verwendet

DocBits verwendet standardmäßig eine KI-basierte Tabellenauswertung, die bei allen Lieferanten funktioniert. Wenn Sie jedoch mehr Kontrolle darüber benötigen, wie Zeilen für einen bestimmten Lieferanten extrahiert werden, können Sie **Tabellenschulung** verwenden, um die Struktur manuell zu definieren.

#### **Wichtig: Lieferantenspezifische Schulung**

Die Tabellenschulung ist **spezifisch für jeden Lieferanten**. Wenn Sie ein Tabellenlayout für einen Lieferanten schulen, gelten die Regeln nur für die Dokumente dieses Lieferanten. Andere Lieferanten werden weiterhin die KI-basierte Tabellenauswertung verwenden, es sei denn, sie werden separat geschult.

#### Wann sollten Sie die Tabellenschulung verwenden?

Verwenden Sie die Tabellenschulung **nur, wenn das Layout des Dokuments stabil ist** und Sie eine konsistente, hochwertige Extraktion sicherstellen möchten. Sie eignet sich am besten für Lieferanten, die:

* Über ein **festes Rechnungsformat** im Laufe der Zeit verfügen.
* Eine **präzise Zuordnung** von Zeilen zu bestimmten Feldern benötigen.
* **Hochvolumige Lieferanten** sind, bei denen eine konsistente Automatisierung wertvoll ist.

#### Wann sollten Sie die Tabellenschulung nicht verwenden?

Vermeiden Sie die Verwendung der Tabellenschulung, wenn:

* Der Lieferant **häufig das Layout seiner Rechnung ändert** (z. B. alle paar Monate).
* Sie nicht regelmäßig Dokumente von diesem Lieferanten erhalten.
* Die standardmäßige KI-Auswertung ohne manuelle Schulung **gut genug funktioniert**.

In solchen Fällen wäre es ineffizient und zeitaufwändig, die Tabelle wiederholt neu zu schulen.

## Wie man sie verwendet:

Der **Schulungsmodus** wird verwendet, um DocBits beizubringen, wie Zeilen aus dem Layout eines bestimmten Lieferanten korrekt extrahiert werden.

Wenn Sie sich im Schulungsmodus befinden, definieren Sie:

* **Wo sich die Tabelle im Dokument befindet**.
* **Welche Bereiche den einzelnen Spalten entsprechen** (z. B. Menge, Beschreibung, Stückpreis).

Dieser Modus erstellt eine **wiederverwendbare Extraktionsvorlage** für diesen Lieferanten, sodass zukünftige Dokumente mit demselben Layout automatisch verarbeitet werden - keine erneute Schulung erforderlich.

**Hauptmerkmale:**

* **Zugeordnete Spalten sind schreibgeschützt** - Sie können den Text nicht manuell ändern.
* Sie **können keine Zeilen hinzufügen oder löschen**.
* Der Fokus liegt auf **der Zuordnung von Positionen**, nicht auf der Korrektur von Werten.
* Sobald Sie die Tabelle und ihre Spalten zugeordnet haben, klicken Sie auf **"Regeln speichern"**, damit DocBits diese Schulung für ähnliche Dokumente desselben Lieferanten lernt und anwendet.

Der **Korrekturmodus** ermöglicht es Ihnen, **Extraktionsfehler** in den Tabellendaten des aktuellen Dokuments zu beheben. Er wird verwendet, wenn DocBits bereits versucht hat, die Tabelle zu extrahieren, aber die Ergebnisse kleine Korrekturen benötigen.

Verwenden Sie den Korrekturmodus, wenn:

* Einige **Werte fehlen oder falsch ausgerichtet sind**.
* Eine **leere oder doppelte Zeile** extrahiert wurde und entfernt werden muss.

**Was Sie im Korrekturmodus tun können:**

* **Werte in zugeordneten Spalten manuell anpassen** (z. B. falsch platzierte Werte korrigieren).
* **Zeilen löschen**, die nicht Teil der Tabelle sein sollten.
* **Zeilen hinzufügen**, die bei der Extraktion vollständig übersehen wurden.
