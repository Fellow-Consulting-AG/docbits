# Izbriši redove sa praznom količinom i iznosom

#### Deo 1: Izbriši redove sa praznom količinom i iznosom

Ova sekcija skripte obrađuje tabelu fakture kako bi uklonila sve redove u kojima su i količina i ukupan iznos nula ili nisu navedeni.

* **Provera za INVOICE\_TABLE:** Počinje proverom da li ključ `INVOICE_TABLE` postoji u rečniku `tables_dict`.
* **Iteracija kroz redove:** Za svaki red u tabeli, skripta inicijalizuje oznake i promenljive kako bi odredila da li kolone `TOTAL_AMOUNT` i `QUANTITY` postoje i kako bi zabeležila njihove vrednosti.
* **Provera imena kolona:** Dok iterira kroz svaku kolonu u redu, traži kolone nazvane `TOTAL_AMOUNT` i `QUANTITY`.
* Ako se pronađe `TOTAL_AMOUNT`, zabeležava vrednost. Ako je ova vrednost različita od nule, konvertuje je u float.
* Slično za `QUANTITY`, zabeležava i konvertuje vrednost ako nije nula.
* **Obeležavanje reda za brisanje:** Nakon provere obe kolone u redu, ako su i ukupan iznos i količina efektivno nula (bilo da su nula ili ne postoje), red se obeležava za brisanje postavljanjem `row['is_deleted']` na `True`.

#### Deo 2: Provera ukupnog iznosa linije naspram ukupnog iznosa fakture

Ova sekcija izračunava ukupan iznos svih linija u fakturi i upoređuje ga sa prijavljenim ukupnim iznosom fakture kako bi proverila njihovu konzistentnost.

* **Inicijalizacija ukupnog iznosa linije:** Počinje postavljanjem promenljive `lines_total` na 0.0 kako bi akumulirala ukupan iznos svih linija.
* **Sabiranje iznosa linija:** Iterira kroz svaki red u `INVOICE_TABLE`, izvlačeći `TOTAL_AMOUNT` iz svakog i dodajući ga u `lines_total`.
* **Dohvatanje i konvertovanje ukupnog iznosa fakture:** Dohvata ukupan iznos fakture koristeći pomoćnu funkciju `get_field_value` i konvertuje ga u float.
* **Upoređivanje iznosa:** Na kraju, proverava da li apsolutna razlika između izračunatog ukupnog iznosa linije (`lines_total`) i prijavljenog ukupnog iznosa fakture (`total_amount`) prelazi prag od 0.05. Ako da, obeležava polje ukupnog iznosa fakture kao nevažeće koristeći drugu pomoćnu funkciju `set_field_as_invalid`, navodeći neslaganje.
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
#### Sažetak

Skripta efikasno obezbeđuje integritet podataka tako što:

1. Uklanja redove podataka koji ne doprinose ukupnom finansijskom iznosu fakture zbog nedostatka količina ili iznosa.
2. Validira konzistentnost između sume pojedinačnih iznosa linija i ukupnog iznosa fakture, ističući neslaganja radi daljnjih akcija.

Ova automatizacija pomaže u održavanju tačnih finansijskih zapisa i može biti od suštinskog značaja za sisteme poput ERP-a koji zahtevaju precizne podatke za računovodstvo i finansijsko izveštavanje.
