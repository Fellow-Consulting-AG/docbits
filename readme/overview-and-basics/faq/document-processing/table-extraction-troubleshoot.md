# Risoluzione dei Problemi di Estrazione delle Tabelle

## **Passaggio 1: Aprire la Vista OCR per Risultati di Estrazione Scadenti**

Se i risultati dell'addestramento all'estrazione delle tabelle non sono buoni:

1. Aprire la **Vista OCR** facendo clic sull'icona della lente d'ingrandimento con scritto **OCR**.
2. Esaminare i risultati dell'estrazione e verificare se il processo OCR può migliorare la cattura dei dati.
3. Se i risultati sembrano ancora scadenti, provare con un documento diverso per verificare se il problema è specifico del documento.
4. Se il problema è specifico del documento, utilizzare un altro documento per l'estrazione.
   * Se il problema persiste, seguire i passaggi successivi.

## **Passaggio 2: Verificare la Disponibilità dell'E-Text**

1. Verificare se il documento dispone di **e-text** disponibile.
   * È possibile verificare ciò utilizzando uno strumento come **Adobe Acrobat**.
   * Se il documento contiene e-text, seguire il **Passaggio 3**.
   * Se il documento non contiene e-text, seguire il **Passaggio 4**.

## **Passaggio 3: Attivare l'Estrazione dell'E-Text**

Se il documento contiene e-text, si hanno due opzioni:

1. **Attivare l'estrazione dell'e-text solo per questo fornitore**:
   * Tornare alla **Convalida dei Campi dei Documenti**.
   * Fare clic sul quadrato con i tre punti nella barra degli strumenti sul lato sinistro.
   * Qui, attivare l'opzione **Usa E-text se disponibile** per attivarla solo per questo fornitore.
2. **Attivare l'estrazione dell'e-text per tutti i fornitori**:
   * Andare a **Impostazioni** > **Elaborazione dei Documenti** > **Impostazioni OCR**.
   * In questa sezione, troverai l'opzione **Usa E-text se disponibile** e potrai attivarla per tutti i fornitori.
3. Dopo aver attivato l'estrazione dell'e-text, riprovare l'**addestramento all'estrazione delle tabelle**.
   * Se i risultati migliorano, il problema è risolto.
   * Se i risultati non sono ancora buoni, procedere al **Passaggio 4**.

## **Passaggio 4: Nessun E-Text Disponibile - Cambiare la Versione dell'AI OCR**

Se il documento non dispone di e-text disponibile:

1. Andare a **Impostazioni** > **Elaborazione dei Documenti** > **Impostazioni OCR**.
2. Cambiare la **Versione dell'AI OCR** con una versione diversa.
3. Tornare all'**Addestramento all'Estrazione delle Tabelle** e riprovare.
4. Se il risultato è migliore:
   * Verificare altri documenti da fornitori diversi per garantire che i risultati dell'estrazione per quei fornitori non siano influenzati da questo cambiamento.
   * **Fare attenzione, poiché questo cambiamento può influenzare i risultati di estrazione di altri fornitori.**
   * Questo cambiamento può influenzare altri fornitori, quindi assicurarsi di verificare attentamente i risultati per garantire che non influiscano negativamente sulle estrazioni dei documenti di altri fornitori.
5. Se il risultato non è migliorato dopo aver cambiato la versione dell'AI OCR, si prega di **contattarci** per ulteriore assistenza.
