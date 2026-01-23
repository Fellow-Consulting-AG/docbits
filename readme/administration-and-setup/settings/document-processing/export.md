# Esportazione

## Panoramica

La pagina Esportazione mostra tutte le configurazioni di esportazione impostate, incluso se sono attive o inattive. Da qui, gli utenti possono:

* Visualizzare e gestire le configurazioni di esportazione esistenti
* Creare nuove connessioni di esportazione (ad es. verso **Infor**, **Infor & IDM**, **Webhook** o **SFTP**)
* Modificare o eliminare configurazioni di esportazione esistenti

## Dove Trovarlo

Lo trovi in: **Impostazioni** → **Elaborazione documenti** → **Esportazione**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(442).png)

## **Utilizzo della Pagina Esportazione**

Quando apri la pagina Esportazione, vedrai un elenco di tutte le configurazioni di esportazione esistenti.

Ogni riga nell'elenco mostra:

* **Indicatore di Stato**
  * **Verde** significa che l'esportazione è attiva
  * **Rosso** significa che l'esportazione è disattivata
* **Name** – il nome della configurazione di esportazione
* **Document Type** – il tipo di documento per cui è configurata l'esportazione
* **Sub-Organization** – se l'esportazione è limitata a una sotto-organizzazione specifica
* **Export Method** – dove verrà inviato il documento (ad es. Infor, IDM, SFTP)
* **Actions** – pulsanti per **modificare, eliminare** o **attivare/disattivare** la configurazione

![DocBits Acquisto Ordine Esporta 7](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_purchase_order_export_7.png)

#### **Regole Importanti per la Configurazione dell'Esportazione**

Per ogni **tipo di documento** **all'interno di una data organizzazione o sotto-organizzazione**, si applicano le seguenti regole:

* Puoi avere **solo un'esportazione Infor attiva**
* Puoi avere **solo un'esportazione non-Infor attiva** (ad es. Webhook, SFTP)

Tuttavia, è possibile avere:

* **Un'esportazione Infor attiva** _e_ **un'esportazione non-Infor attiva** contemporaneamente per lo stesso tipo di documento
* **Diverse configurazioni di esportazione per diverse sotto-organizzazioni** — ad esempio, un'esportazione Infor per la Sotto-Org A e un'altra esportazione Infor per la Sotto-Org B

## **Creazione di una Nuova Esportazione**

Per creare una nuova esportazione:

1. Clicca sul pulsante **"Nuovo"**.\
   ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1)%20(1)%20(1).png)
2. Seleziona il **Tipo di Esportazione** che vuoi configurare (ad es. Infor, IDM, SFTP).
3. Compila i campi richiesti in base al tipo di esportazione.
4. Salva la configurazione.

## Opzioni di Esportazione

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(15)%20(1).png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **Export URL**\
  L'URL di destinazione dove il documento deve essere esportato.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![DocBits Acquisto Ordine 4](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_purchase_order_4.png)

**Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **Username**\
  Il nome utente utilizzato per l'autenticazione sul server SFTP.
- **Password**\
  La password corrispondente per l'account SFTP. Assicurati che l'account abbia accesso in scrittura alla cartella specificata.
- **Server URL**\
  Il nome host o l'indirizzo IP del server SFTP di destinazione.
- **Port**\
  La porta utilizzata per connettersi al server SFTP.
- **Folder**\
  Il percorso sul server SFTP dove devono essere caricati i documenti (ad es. `/incoming/invoices/`).\
  Deve esistere e essere scrivibile.
-   **XSLT File (Opzionale)**

    Il **file XSLT** permette la trasformazione del formato di esportazione predefinito di DocBits.

    * **Quando usarlo:**\
      Solo se il sistema ricevente richiede una struttura diversa o una formattazione specifica che differisce dal formato predefinito di DocBits.
    * **Lascialo vuoto** se il formato di esportazione predefinito soddisfa i requisiti.

</details>

#### Infor Export to SFTP

<details>

<summary>Infor Export to SFTP</summary>

![DocBits Esporta Sftp](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_sftp.png)

**Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **IDM Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **BOD Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Folder**\
  Il percorso sul server SFTP dove devono essere caricati i documenti (ad es. `/incoming/invoices/`).\
  Deve esistere e essere scrivibile.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![DocBits Esporta Smb](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_smb.png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **Username**\
  Il nome utente utilizzato per connettersi alla condivisione SMB.
- **Password**\
  La password corrispondente per l'autenticazione SMB.
- **Server URL**\
  L'indirizzo del server SMB.
- **Port**\
  Il numero di porta utilizzato per accedere alla condivisione SMB.
- **Folder**\
  Il percorso della cartella all'interno della condivisione SMB dove devono essere salvati i documenti (ad es. `/incoming/invoices/`).\
  Deve esistere e essere scrivibile.
-   **JPL Mapping File (Opzionale)**

    Il **file JPL** viene utilizzato per definire una trasformazione dei dati esportati prima che vengano scritti nella condivisione SMB.

    * **Quando usarlo:**\
      Solo quando i dati del documento esportato devono essere adattati per corrispondere alla formattazione esterna o alle aspettative del sistema.
    * **Lascialo vuoto** se non è necessaria alcuna trasformazione.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(13)%20(1).png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **ION Mapping File**\
  Seleziona un file di mappatura dal file manager.
- **IDM Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Un interruttore per indicare il tipo di deployment di Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è self-hosted.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(11)%20(1).png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **ION Mapping File**\
  Seleziona un file di mappatura dal file manager.
- **BOD Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Un interruttore per indicare il tipo di deployment di Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è self-hosted.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![DocBits Esporta Ion Bod](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_ion_bod.png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **ION Mapping File**\
  Seleziona un file di mappatura dal file manager.
- **IDM Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **BOD Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Un interruttore per indicare il tipo di deployment di Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è self-hosted.

</details>

### Per i clienti Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![DocBits Impostazioni E-mail](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_settings_email.png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **ION Mapping File**\
  Seleziona un file di mappatura dal file manager.
- **IDM Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)

* **LN Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta l'Esempio di Mappatura LN](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![DocBits Impostazioni](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_settings.png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **ION Mapping File**\
  Seleziona un file di mappatura dal file manager.
- **IDM Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **M3 Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta l'Esempio di Mappatura M3](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![DocBits Flusso di lavoro Acquisto Ordine 5](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_workflow_purchase_order_5.png)

#### **Descrizione dei Campi**

* **Title**\
  Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_\
  Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type**\
  Menu a tendina che elenca tutti i tipi di documento disponibili.\
  Questo determina a quale tipo di documento si applica questa configurazione di esportazione.

- **ION Mapping File**\
  Seleziona un file di mappatura dal file manager.
- **IDM Mapping File**\
  Seleziona un file di mappatura dal file manager.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida alla Mappatura IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **M3 toml Mapping File**\
  Seleziona un file di mappatura dal file manager o usa l'opzione seleziona Toml per usare un toml creato con il gestore delle regole.\
  [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Gestore delle Regole](rule-manager/)

</details>
