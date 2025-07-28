# Campi di addestramento Linee/Tabella di addestramento

## Tabella di addestramento: Quando e come utilizzarla

DocBits utilizza l'estrazione tabellare basata sull'IA per impostazione predefinita, che funziona con tutti i fornitori. Tuttavia, quando hai bisogno di un maggiore controllo su come vengono estratti gli elementi di linea per un fornitore specifico, puoi utilizzare **Tabella di addestramento** per definire manualmente la struttura.

#### **Importante: Addestramento specifico del fornitore**

L'addestramento tabellare è **specifico per ogni fornitore**. Se addestri un layout tabellare per un fornitore, le regole si applicano solo ai documenti di quel fornitore.\
Gli altri fornitori continueranno a utilizzare l'estrazione tabellare basata sull'IA a meno che non vengano addestrati separatamente.

#### Quando dovresti utilizzare la Tabella di addestramento?

Utilizza la Tabella di addestramento **solo quando il layout del documento è stabile**, e desideri garantire un'estrazione coerente e di alta qualità. È particolarmente adatta per i fornitori che:

* Utilizzano un **formato di fattura fisso** nel tempo.
* Richiedono un **mapping preciso** degli elementi di linea su campi specifici.
* Sono **fornitori ad alto volume**, dove l'automazione coerente è preziosa.

#### Quando non utilizzare la Tabella di addestramento

Evita di utilizzare la Tabella di addestramento se:

* Il fornitore **cambia frequentemente il layout della fattura** (ad esempio, ogni paio di mesi).
* Non ricevi regolarmente documenti da quel fornitore.
* L'estrazione basata sull'IA predefinita funziona **abbastanza bene** senza addestramento manuale.

In tali casi, riaddestrare ripetutamente la tabella sarebbe inefficiente e richiederebbe tempo.

## Come utilizzarla:

La **Modalità di addestramento** viene utilizzata per insegnare a DocBits come estrarre correttamente gli elementi di linea dal layout del documento di un fornitore specifico.

Quando sei in Modalità di addestramento, definisci:

* **Dove si trova la tabella** nel documento.
* **Quali aree corrispondono a ciascuna colonna** (ad esempio, Quantità, Descrizione, Prezzo unitario).

Questa modalità crea un **modello di estrazione riutilizzabile** per quel fornitore, quindi i documenti futuri con lo stesso layout verranno elaborati automaticamente, senza la necessità di un nuovo addestramento.

**Caratteristiche chiave:**

* Le **colonne mappate sono in sola lettura** — non è possibile modificare manualmente il testo.
* **Non puoi aggiungere o eliminare righe**.
* L'attenzione è sul **mapping delle posizioni**, non sulla correzione dei valori.
* Una volta completato il mapping della tabella e delle sue colonne, fai clic su **"Salva regole"** in modo che DocBits apprenda e applichi questo addestramento a documenti simili dello stesso fornitore.

La **Modalità di correzione** ti consente di **correggere gli errori di estrazione** nei dati tabellari per il documento corrente. Viene utilizzata quando DocBits ha già tentato di estrarre la tabella, ma i risultati necessitano di piccole correzioni.

Utilizza la Modalità di correzione quando:

* Alcuni **valori mancano o sono disallineati**.
* È stata estratta una **riga vuota o duplicata** che deve essere rimossa.

**Cosa puoi fare in Modalità di correzione:**

* **Regolare manualmente i valori** nelle colonne mappate (ad esempio, correggere gli spostamenti).
* **Eliminare righe** che non dovrebbero far parte della tabella.
* **Aggiungere righe** che sono state completamente trascurate durante l'estrazione.
