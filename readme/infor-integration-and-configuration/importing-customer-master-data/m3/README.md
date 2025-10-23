# M3

## Importazione di un API Connection Template in Infor M3

Questa guida spiega come importare un API Connection Template per configurare rapidamente le impostazioni chiave per l’integrazione con Infor M3. Usare un template consente di stabilire una configurazione di connessione predefinita, semplificando il processo e garantendo coerenza.

<mark style="color:red;">**Nota**</mark>: Per la configurazione dettagliata di aree specifiche come Auto Accounting, integrazione fornitori, ordini di acquisto o estrazione tabelle per elementi di costo, fai riferimento alla documentazione corrispondente:

* [Contabilità automatica](auto-accounting.md)
* [Fornitori e Ordini di acquisto](suppliers-and-purchase-orders.md)
* [Come importare tutti i fornitori](how-to-import-all-suppliers.md)
* [Estrazione tabelle per elemento di costo](table-extraction-for-costing-element.md)

### **Scarica il Template**

Prima di importare, scarica il template di connessione richiesto usando il file seguente:

{% file src="../../../.gitbook/assets/DocBits-Dev-Import-Template.xml" %}

### Importazione del Template

#### Passaggi per importare un Connection Template

1. **Accedi a Infor ION Desk:**
   *   Vai su **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Importa il Template:**
   *   Fai clic sul pulsante **Import**.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_2.png)
   * Seleziona il **Template File** appropriato dal tuo sistema locale.
   *   Fai clic su **OK** per iniziare il processo di importazione.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_3.png)
3. **Conferma:**
   *   Se l’importazione riesce, verrà visualizzato un messaggio di conferma.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_4.png)
4. **Configurazione post-importazione:**
   * Dopo aver importato il template, puoi personalizzare le impostazioni di connessione specifiche secondo necessità.
   * Non dimenticare di importare o configurare il tuo **Service Account** per l’autenticazione e il controllo degli accessi.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_5.png)
