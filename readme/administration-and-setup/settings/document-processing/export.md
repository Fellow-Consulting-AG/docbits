# Esportazione

## Panoramica

La pagina di Esportazione visualizza tutte le configurazioni di esportazione configurate, inclusa la loro attivazione o disattivazione. Da qui, gli utenti possono:

* Visualizzare e gestire le configurazioni di esportazione esistenti
* Creare nuove connessioni di esportazione (ad esempio, a **Infor**, **Infor & IDM**, **Webhook** o **SFTP**)
* Modificare o eliminare le configurazioni di esportazione esistenti

## Dove Trovarlo

Puoi trovarlo in: **Impostazioni** → **Elaborazione Documenti** → **Esportazione**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6ldlcI2sVUEgDdWb9U4%252Fimage.png%3Falt%3Dmedia%26token%3D8368818d-c899-4bee-ad21-a631d6be5c20\&width=768\&dpr=4\&quality=100\&sign=fbfcbd0c\&sv=2)

## **Utilizzo della Pagina di Esportazione**

Quando apri la pagina di Esportazione, vedrai un elenco di tutte le configurazioni di esportazione esistenti.

Ogni riga nell'elenco mostra:

* **Indicatore di Stato**
  * Il colore **Verde** significa che l'esportazione è attiva
  * Il colore **Rosso** significa che l'esportazione è disattivata
* **Nome** – il nome della configurazione di esportazione
* **Tipo di Documento** – il tipo di documento per il quale è configurata l'esportazione
* **Sotto-Organizzazione** – se l'esportazione è limitata a una specifica sotto-organizzazione
* **Metodo di Esportazione** – dove il documento sarà inviato (ad esempio, Infor, IDM, SFTP)
* **Azioni** – pulsanti per **modificare, eliminare** o **attivare/disattivare** la configurazione

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyN87I5gzXxwGoAqC6zMF%252Fimage.png%3Falt%3Dmedia%26token%3D7df9d573-7e57-4ace-99c6-15a83691b926\&width=768\&dpr=4\&quality=100\&sign=6221cb80\&sv=2)

#### **Regole Importanti per la Configurazione di Esportazione**

Per ogni **tipo di documento** **all'interno di un'organizzazione o sotto-organizzazione specifica**, si applicano le seguenti regole:

* Puoi avere **solo un'esportazione attiva Infor**
* Puoi avere **solo un'esportazione attiva non-Infor** (ad esempio, Webhook, SFTP)

Tuttavia, è possibile avere:

* **Un'esportazione attiva Infor** _e_ **un'esportazione attiva non-Infor** contemporaneamente per lo stesso tipo di documento
* **Diverse configurazioni di esportazione per diverse sotto-organizzazioni** — ad esempio, un'esportazione Infor per la Sotto-Org A e un'altra esportazione Infor per la Sotto-Org B

## **Creazione di una Nuova Esportazione**

Per creare una nuova esportazione:

1. Fai clic sul pulsante **“Nuovo”**. \
   ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FTsHrIAUpe7EqenIzNAaJ%252Fimage.png%3Falt%3Dmedia%26token%3Dd2dbc996-b129-443c-a8df-9927a6f43a36\&width=300\&dpr=4\&quality=100\&sign=8769c331\&sv=2)
2. Seleziona il **Tipo di Esportazione** che desideri configurare (ad esempio, Infor, IDM, SFTP).
3. Compila i campi obbligatori in base al tipo di esportazione.
4. Salva la configurazione.

## Opzioni di Esportazione

#### Webhook

<details>

<summary>Webhook</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCwXUqFdCbRI5lRW49ymw%252Fimage.png%3Falt%3Dmedia%26token%3D798c0f40-6c4a-4650-9320-af2c17634fe9\&width=768\&dpr=4\&quality=100\&sign=15836833\&sv=2)

#### **Descrizioni dei Campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documenti disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **URL di Esportazione** L'URL di destinazione dove il documento dovrebbe essere esportato.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzwUCWTdFETTvuTGl8qAn%252Fimage.png%3Falt%3Dmedia%26token%3D3f94b210-0128-4710-ae69-150a1363ce49\&width=768\&dpr=4\&quality=100\&sign=4ecd353\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **Nome utente** Il nome utente utilizzato per l'autenticazione sul server SFTP.
* **Password** La password corrispondente per l'account SFTP. Assicurarsi che l'account abbia accesso in scrittura alla cartella specificata.
* **URL del Server** Il nome host o l'indirizzo IP del server SFTP di destinazione.
* **Porta** La porta utilizzata per connettersi al server SFTP.
* **Cartella** Il percorso sul server SFTP dove devono essere caricati i documenti (ad es., `/incoming/invoices/`). Deve esistere e essere scrivibile.
*   **File XSLT (Opzionale)**

    Il **file XSLT** consente la trasformazione del formato di esportazione predefinito di DocBits.

    * **Quando utilizzare:** Solo se il sistema ricevente richiede una struttura diversa o una formattazione specifica che differisce dal predefinito di DocBits.
    * **Lasciarlo vuoto** se il formato di esportazione predefinito soddisfa i requisiti.

</details>

#### Esportazione di Infor su SFTP

<details>

<summary>Esportazione di Infor su SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FU0W4Qdy7ZlNoCn3E9wX5%252Fimage.png%3Falt%3Dmedia%26token%3D33673a12-55c4-479b-8ca8-b7c95e7a6a89\&width=768\&dpr=4\&quality=100\&sign=4af07f48\&sv=2)

#### **Descrizioni dei Campi**

* **Titolo** Il nome della configurazione di esportazione. Questo comparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documenti disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **File di Mappatura IDM** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **File di Mappatura BOD** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Cartella** Il percorso sul server SFTP dove i documenti devono essere caricati (ad es., `/incoming/invoices/`). Deve esistere e essere scrivibile.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6e4B9BWQWgHvcHhduXKb%252Fimage.png%3Falt%3Dmedia%26token%3D09e9534e-9268-4221-bd7b-89b621c80670\&width=768\&dpr=4\&quality=100\&sign=b03835a\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documenti disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **Nome Utente** Il nome utente utilizzato per connettersi alla condivisione SMB.
* **Password** La password corrispondente per l'autenticazione SMB.
* **URL del Server** L'indirizzo del server SMB.
* **Porta** Numero di porta utilizzato per accedere alla condivisione SMB.
* **Cartella** Il percorso della cartella all'interno della condivisione SMB dove devono essere salvati i documenti (ad es., `/incoming/invoices/`). Deve esistere e essere scrivibile.
*   **File di Mappatura JPL (Opzionale)**

    Il **file JPL** è utilizzato per definire una trasformazione dei dati esportati prima che venga scritta nella condivisione SMB.

    * **Quando utilizzare:** Solo quando i dati del documento esportato devono essere adattati per corrispondere al formato esterno o alle aspettative del sistema.
    * **Lasciarlo vuoto** se non è necessaria alcuna trasformazione.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FQ1AtdmTRZr1sGkH6oLwP%252Fimage.png%3Falt%3Dmedia%26token%3D720a4184-3f91-4b70-b3da-b846f3cce030\&width=768\&dpr=4\&quality=100\&sign=dc678c2c\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa con tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **File di Mappatura ION** Seleziona un file di mappatura dal gestore dei file.
* **File di Mappatura IDM** Seleziona un file di mappatura dal gestore dei file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Cloud / On-Prem Interruttore** Uno switch per indicare il tipo di distribuzione Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è auto-ospitato.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcYDXwDYH4RSc5vcY4fmr%252Fimage.png%3Falt%3Dmedia%26token%3Da9cfac80-9795-4e8f-a664-e268c9b4856c\&width=768\&dpr=4\&quality=100\&sign=5a4b0bd0\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documenti disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **File di Mappatura ION** Seleziona un file di mappatura dal gestore file.
* **File di Mappatura BOD** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Cloud / On-Prem Interruttore** Un interruttore per indicare il tipo di distribuzione Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è auto-ospitato.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FY13EX2xxOKLZzliAAHB0%252Fimage.png%3Falt%3Dmedia%26token%3D94335922-6342-405f-8c6d-29fdf2f31a2e\&width=768\&dpr=4\&quality=100\&sign=c0322806\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **File di Mappatura ION** Seleziona un file di mappatura dal gestore file.
* **File di Mappatura IDM** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **File di Mappatura BOD** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Cloud / On-Prem Interruttore** Un interruttore per indicare il tipo di distribuzione Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è auto-ospitato.

</details>

### Per i clienti di Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4SfGDqhA4KDrPfJ5vcsT%252Fimage.png%3Falt%3Dmedia%26token%3D4833c0dc-af8b-48a1-a977-6cc8ded20277\&width=768\&dpr=4\&quality=100\&sign=6301596\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di documento** Menu a discesa che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **File di mappatura ION** Seleziona un file di mappatura dal gestore file.
* **File di mappatura IDM** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **File di mappatura LN** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza l'Esempio di Mappatura LN](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAN4T0aQEoogbUA8PUgy9%252Fimage.png%3Falt%3Dmedia%26token%3Da2b91153-858f-4711-abcc-4ed7ad60d49a\&width=768\&dpr=4\&quality=100\&sign=bb6bda83\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **File di Mappatura ION** Seleziona un file di mappatura dal gestore file.
* **File di Mappatura IDM** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **File di Mappatura M3** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza l'Esempio di Mappatura M3](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCdoduCkkbnomw3ahZgul%252Fimage.png%3Falt%3Dmedia%26token%3D4e5c7d08-5eaf-4c3e-9918-5cce58d8e3b3\&width=768\&dpr=4\&quality=100\&sign=e984c4e0\&sv=2)

#### **Descrizioni dei campi**

* **Titolo** Il nome della configurazione di esportazione. Questo apparirà nell'elenco delle esportazioni.
* **Sotto-Organizzazione** _(opzionale)_ Un menu a discesa con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Tipo di Documento** Menu a discesa che elenca tutti i tipi di documenti disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **File di Mappatura ION** Seleziona un file di mappatura dal gestore file.
* **File di Mappatura IDM** Seleziona un file di mappatura dal gestore file. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida alla Mappatura IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **File di Mappatura M3 toml** Seleziona un file di mappatura dal gestore file o utilizza l'opzione Seleziona Toml per utilizzare un toml creato con il gestore regole. [Hai bisogno di aiuto per crearne uno? Visualizza la Guida al Gestore Regole](https://docs.docbits.com/administration-and-setup/settings/document-processing/rule-manager)

</details>

