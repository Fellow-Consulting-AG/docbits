# Entscheidungsbäume

### Übersicht

Entscheidungsbäume sind eine leistungsstarke Funktion, die einen automatisierten Routing- und Entscheidungsprozess basierend auf vordefinierten Regeln ermöglicht. Diese Funktion ist besonders nützlich in komplexen Umgebungen, in denen verschiedene Bedingungen bewertet werden müssen, um den richtigen Handlungsverlauf zu bestimmen, wie z.B. die Preiszuweisung, die Bestimmung von Mengen oder das Routing von Dokumenten.

#### Hauptkomponenten

* **Entscheidungsbaum-Liste**: Dies ist die Hauptschnittstelle, in der alle vorhandenen Entscheidungsbäume aufgelistet sind. Jeder Entscheidungsbaum kann mit einem bestimmten Dokumenttyp wie einer `RECHNUNG` oder `ANGEBOT` verknüpft werden.
* **Entscheidungsbaum-Editor**: Diese Schnittstelle ermöglicht die Erstellung und Bearbeitung von Entscheidungsbäumen, in denen Sie Regeln, Operatoren und Aktionen definieren können, die ausgeführt werden sollen, wenn bestimmte Bedingungen erfüllt sind.

### Entscheidungsbaum-Schnittstelle

#### Entscheidungsbaum-Liste

Die Entscheidungsbaum-Liste zeigt alle verfügbaren Entscheidungsbäume an. Jeder Eintrag zeigt:

* **Name**: Der Name des Entscheidungsbaums.
* **Dokumenttyp**: Der Typ des mit dem Entscheidungsbaum verknüpften Dokuments (z.B. `RECHNUNG`, `ANGEBOT`).

#### Entscheidungsbaum-Editor

Der Entscheidungsbaum-Editor ermöglicht es Ihnen, Regeln zu konfigurieren, die bestimmen, wie Entscheidungen getroffen werden.

**Komponenten des Entscheidungsbaum-Editors**

* **Regeln**: Jede Regel besteht aus Bedingungen und Aktionen.
* **Quelle auswählen**: Dieses Dropdown-Menü ermöglicht es Ihnen, das Quellfeld auszuwählen, das bewertet werden soll.
* **Operator auswählen**: Definiert den logischen Operator (z.B. `<=`, `>=`, `=`, `!=`), der auf das Quellfeld angewendet werden soll.
* **Ergebnis**: Definiert das Ergebnis oder die Aktion, die ausgeführt werden soll, wenn die Bedingungen erfüllt sind.
* **Neue Zeile hinzufügen**: Ermöglicht es Ihnen, zusätzliche Regeln zum Entscheidungsbaum hinzuzufügen.

#### Beispiel einer Entscheidungsbaum-Konfiguration

1. **Regel 1**:
   * **Quelle**: Menge
   * **Operator**: `<=`
   * **Wert**: `250000`
   * **Ergebnis**: Zuweisen an `CATMGR_CMM`
2. **Regel 2**:
   * **Quelle**: Preis
   * **Operator**: `>`
   * **Wert**: `500000`
   * **Ergebnis**: Zuweisen an `PROCUREMENT_DIRECTOR`

Jede Regel wird nacheinander bewertet, und die entsprechende Aktion wird ausgeführt, wenn die Bedingungen erfüllt sind.

### Entscheidungsbaum-Richtlinie

Die Entscheidungsbaum-Richtlinie definiert, wie mehrere Regeln innerhalb eines Entscheidungsbaums verarbeitet werden. Sie können aus mehreren Richtlinien wählen:

* **Eindeutig**: Stellt sicher, dass nur eine Regel übereinstimmen kann. Wenn mehr als eine Regel übereinstimmt, wird ein Fehler im Entscheidungsbaum angezeigt.
* **Erste**: Die erste übereinstimmende Regel wird angewendet, und keine weiteren Regeln werden bewertet.
* **Priorität**: Regeln werden basierend auf ihrer Prioritätsreihenfolge bewertet. Die Regel mit der höchsten Priorität wird angewendet.
* **Sammeln (Summe)**: Sammelt alle übereinstimmenden Regeln und summiert die Ergebnisse.
* **Sammeln (min/max/anzahl)**: Sammelt alle übereinstimmenden Regeln und wählt entweder das Minimum, Maximum oder zählt die Vorkommen.
* **Regelreihenfolge**: Wendet Regeln in der Reihenfolge an, in der sie im Entscheidungsbaum erscheinen.
* **Beliebig**: Jede übereinstimmende Regel kann angewendet werden, was mehrere Ergebnisse ermöglicht.

#### Beispiel einer Entscheidungsbaum-Richtlinie in Aktion

Im Entscheidungsbaum "Direktgruppenpreis":

* **Ausgewählte Richtlinie**: `Erste`
* Das bedeutet, dass, sobald eine Regelbedingung erfüllt ist, die zugehörige Aktion angewendet wird und keine weiteren Regeln bewertet werden.

### Exportieren und Speichern

* **Speichern**: Speichert die aktuelle Konfiguration des Entscheidungsbaums.
* **Exportieren**: Ermöglicht es Ihnen, die Konfiguration des Entscheidungsbaums zu exportieren, die dann in eine andere Umgebung importiert oder zu Backup-Zwecken verwendet werden kann.