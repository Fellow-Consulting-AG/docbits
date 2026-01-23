# Elimina righe con quantità e importo vuoti

#### Parte 1: Elimina Righe con Quantità e Importo Vuoti

Questa sezione dello script elabora una tabella di fattura per rimuovere tutte le righe in cui sia la quantità che l'importo totale sono zero o non forniti.

* **Verifica INVOICE\_TABLE:** Inizia verificando se la chiave `INVOICE_TABLE` esiste nel dizionario `tables_dict`.
* **Itera sulle Righe:** Per ogni riga nella tabella, lo script inizializza flag e variabili per determinare se esistono le colonne `TOTAL_AMOUNT` e `QUANTITY` e per catturare i loro valori.
* **Verifica Nomi Colonne:** Iterando attraverso ogni colonna di una riga, cerca le colonne chiamate `TOTAL_AMOUNT` e `QUANTITY`.
  * Se viene trovato `TOTAL_AMOUNT`, cattura il valore. Se questo valore non è zero, lo converte in un numero a virgola mobile.
  * Similmente per `QUANTITY`, catturando e convertendo il valore se non è zero.
* **Marca Riga per Eliminazione:** Dopo aver verificato entrambe le colonne in una riga, se sia l'importo totale che la quantità sono effettivamente zero (o essendo zero o non esistendo), la riga viene marcata per l'eliminazione impostando `row['is_deleted']` su `True`.

#### Parte 2: Valida Totale Righe contro Totale Fattura

Questa sezione calcola l'importo totale da tutte le righe di una fattura e lo confronta con il totale riportato della fattura per validare la loro coerenza.

* **Inizializza Totale Righe:** Inizia impostando una variabile `lines_total` a 0.0 per accumulare l'importo totale da tutte le righe.
* **Somma Importi Righe:** Itera su ogni riga nella `INVOICE_TABLE`, estraendo il `TOTAL_AMOUNT` da ciascuna e aggiungendolo a `lines_total`.
* **Recupera e Converti Totale Fattura:** Ottiene l'importo totale della fattura usando una funzione helper `get_field_value` e lo converte in un numero a virgola mobile.
* **Confronta Totali:** Infine, verifica se la differenza assoluta tra il totale calcolato delle righe (`lines_total`) e il totale riportato della fattura (`total_amount`) supera una soglia di 0,05. Se sì, marca il campo del totale fattura come invalido usando un'altra funzione helper `set_field_as_invalid`, citando una discrepanza.

```python
##################################################
# Delete lines with empty quantity and amount
##################################################


if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        amount_col_found = False
        quantity_col_found = False
        line_amount = 0.0
        line_quantity = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                amount_col_found = True
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
            if col['name'] == 'QUANTITY':
                quantity_col_found = True
                line_quantity = col.get('value', 0)
                if line_quantity:
                    line_quantity = float(line_quantity)
            if amount_col_found and quantity_col_found:
                break
        if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
            row['is_deleted'] = True

##################################################
# End: Delete lines with empty quantity and amount
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        line_amount = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
                break
        lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Comparing lines total with invoice total
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################





```

#### Riepilogo

Lo script garantisce efficacemente l'integrità dei dati mediante:

1. Rimozione delle righe di dati che non contribuiscono al totale finanziario della fattura a causa di quantità o importi mancanti.
2. Validazione della coerenza tra la somma degli importi delle singole righe e il totale complessivo della fattura, evidenziando le discrepanze per ulteriori azioni.

Questa automazione aiuta a mantenere registri finanziari accurati e può essere cruciale per sistemi come ERP che richiedono dati precisi per la contabilità e la reportistica finanziaria.


