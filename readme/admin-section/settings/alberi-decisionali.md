# Alberi Decisionali

#### Panoramica

Gli Alberi Decisionali sono una funzionalità potente che consente il routing automatizzato e il processo decisionale basato su regole predefinite. Questa funzionalità è particolarmente utile in ambienti complessi dove è necessario valutare varie condizioni per determinare il corretto corso d'azione, come l'assegnazione dei prezzi, la determinazione delle quantità o il routing dei documenti.

**Componenti Chiave**

* **Elenco Alberi Decisionali**: Questa è l'interfaccia principale dove sono elencati tutti gli alberi decisionali esistenti. Ogni albero decisionale può essere associato a un tipo di documento specifico come una `FATTURA` o un `PREVENTIVO`.
* **Editor Alberi Decisionali**: Questa interfaccia consente la creazione e la modifica degli alberi decisionali, dove è possibile definire regole, operatori e azioni da intraprendere quando vengono soddisfatte determinate condizioni.

#### Interfaccia Albero Decisionale

**Elenco Alberi Decisionali**

L'elenco degli Alberi Decisionali visualizza tutti gli alberi decisionali disponibili. Ogni voce mostra:

* **Nome**: Il nome dell'albero decisionale.
* **Tipo di Documento**: Il tipo di documento associato all'albero decisionale (ad es., `FATTURA`, `PREVENTIVO`).

**Editor Alberi Decisionali**

L'Editor Alberi Decisionali consente di configurare regole che governano come vengono prese le decisioni.

**Componenti dell'Editor Alberi Decisionali**

* **Regole**: Ogni regola consiste in condizioni e azioni.
* **Seleziona Fonte**: Questo menu a discesa consente di specificare il campo sorgente da valutare.
* **Seleziona Operatore**: Definisce l'operatore logico (ad es., `<=`, `>=`, `=`, `!=`) da applicare al campo sorgente.
* **Risultato**: Definisce l'esito o l'azione che dovrebbe essere intrapresa quando le condizioni sono soddisfatte.
* **Aggiungi Nuova Riga**: Consente di aggiungere ulteriori regole all'albero decisionale.

**Esempio di Configurazione di un Albero Decisionale**

1. **Regola 1**:
   * **Fonte**: Quantità
   * **Operatore**: `<=`
   * **Valore**: `250000`
   * **Risultato**: Assegna a `CATMGR_CMM`
2. **Regola 2**:
   * **Fonte**: Prezzo
   * **Operatore**: `>`
   * **Valore**: `500000`
   * **Risultato**: Assegna a `PROCUREMENT_DIRECTOR`

Ogni regola viene valutata in sequenza e l'azione corrispondente viene eseguita se le condizioni sono soddisfatte.

#### Politica dell'Albero Decisionale

La Politica dell'Albero Decisionale definisce come vengono elaborate più regole all'interno di un albero decisionale. Puoi scegliere tra diverse politiche:

* **Unica**: Garantisce che solo una regola possa corrispondere. Se più di una regola corrisponde, l'albero decisionale segnalerà un errore.
* **Prima**: La prima regola corrispondente viene applicata e non vengono valutate ulteriori regole.
* **Priorità**: Le regole vengono valutate in base al loro ordine di priorità. La regola corrispondente con la priorità più alta viene applicata.
* **Raccogli (somma)**: Raccoglie tutte le regole corrispondenti e somma i risultati.
* **Raccogli (min/max/count)**: Raccoglie tutte le regole corrispondenti e seleziona il minimo, il massimo o conta le occorrenze.
* **Ordine delle Regole**: Applica le regole nell'ordine in cui appaiono nell'albero decisionale.
* **Qualsiasi**: Qualsiasi regola corrispondente può essere applicata, consentendo molteplici esiti.

**Esempio di Politica dell'Albero Decisionale in Azione**

Nell'albero decisionale "Prezzo Gruppo Diretto":

* **Politica Selezionata**: `Prima`
* Questo significa che non appena una condizione di regola è soddisfatta, la sua azione associata viene applicata e non vengono valutate ulteriori regole.

#### Esporta e Salva

* **Salva**: Salva la configurazione attuale dell'albero decisionale.
* **Esporta**: Consente di esportare la configurazione dell'albero decisionale, che può poi essere importata in un altro ambiente o utilizzata per scopi di backup.
