# Izvoz u M3 mapiranje (API)

### Odeljci

M3 fajl za mapiranje izvoza je podeljen u 5 odeljaka, pri čemu je svaki odeljak dalje podeljen na 2 odeljka

* Zaglavlje
* Statička polja zaglavlja
* Polja zaglavlja
* Porezne linije
* Statička polja poreza
* Polja poreza
* Linije prijema
* Statička polja linije prijema
* Polja linije prijema
* Linije naplate narudžbine (Dodatni iznosi)
* Statička polja naplate
* Polja naplate
* Linije troškova
* Statička polja linije troškova
* Polja linije troškova

### Dodavanje i uklanjanje polja

Dodavanje novog polja:

* Prvo treba dodati **naziv polja M3 API-ja** u odgovarajuću listu polja odeljka (npr. Statička polja, Polja zaglavlja, Polja poreza na fakturi)
* Definišite statičku vrednost ili naziv dokumenta za polje API-ja sa odgovarajućim prefiksom za odeljak
* Primer 1: Da biste definisali statičku vrednost **AAA** za polje M3 API-ja **DIVI.** Prvo smo dodali DIVI u **Statička polja**. Zatim dodajemo liniju **SF\_DIVI = AAA** jer je SF\_ prefiks za statička polja
* Primer 2: Da biste mapirali polje zaglavlja **IVDT (podaci o fakturi)** na polje invoice\_date u DocBits-u. Prvo dodajemo IVDT u **Polja zaglavlja**. Zatim dodajemo liniju HF\_IVDT = invoice\_date jer je HF\_ prefiks za polja zaglavlja

Uklanjanje polja:

* Jednostavno uklonite polje iz liste polja odeljka i uklonite liniju koja definiše vrednost za to polje.

#### **Dostupna M3 API polja:**

* Dostupna M3 polja mogu se proveriti otvaranjem odgovarajućeg ekrana u M3.

<figure><img src="../../../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt=""><figcaption></figcaption></figure>

* Slično možete dobiti nazive polja za linije

### Zaglavlje:

<figure><img src="../../../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt=""><figcaption></figcaption></figure>

Lista polja: Statička polja

Prefiks polja odeljka: SF\_

Dostupna polja: Možete mapirati bilo koje polje M3 API-ja sa bilo kojom statičkom vrednošću

#### **Polja zaglavlja**

Lista polja: Polja zaglavlja

Prefiks polja odeljka: HF\_

Dostupna polja: Možete mapirati bilo koje polje DocBits-a sa bilo kojim poljem M3 API-ja

### Porezna linija:

#### Statička polja poreza:

Lista polja: Statička polja poreza na fakturi

Prefiks polja odeljka: IT\_SF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: Možete uneti bilo koju vrednost jer su to statička polja

#### Polja poreza:

Lista polja: Polja poreza na fakturi

Prefiks polja M3: ITF\_

Prefiks polja tabele DocBits-a: TF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: line\_number, tax\_amount, tax\_rate, net\_amount, gross\_amount, tax\_code\_full, tax\_code, tax\_country

### Linija prijema:

#### Statička polja linije prijema:

Lista polja: Statička polja prijema na fakturi

Prefiks polja odeljka: IR\_SF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: Možete uneti bilo koju vrednost jer su to statička polja

#### Polja linije prijema:

Lista polja: Polja prijema na fakturi

Prefiks polja M3: IRF\_

Prefiks polja tabele DocBits-a: TF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: packing\_slip, purchase\_order, line\_number, line\_sequence, delivery\_number, delivery\_line, amount, quantity, total\_net\_amount

### Linija naplate narudžbine:

#### Statička polja naplate:

Lista polja: Statička polja naplate

Prefiks polja odeljka: OC\_SF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: Možete uneti bilo koju vrednost jer su to statička polja

#### Polja naplate:

Lista polja: Polja naplate

Prefiks polja M3: OCF\_

Prefiks polja tabele DocBits-a: TF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: ledger\_account, dimension\_2-7, amount, quantity, quantity2, position

### Linija troškova:

#### Statička polja linije troškova:

Lista polja: Statička polja troškova na fakturi

Prefiks polja odeljka: IC\_SF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: Možete uneti bilo koju vrednost jer su to statička polja

#### Polja linije troškova:

Lista polja: Polja troškova na fakturi

Prefiks polja M3: ICF\_

Prefiks polja tabele DocBits-a: TF\_

Dostupna M3 polja: Molimo proverite M3 API ili UI

Dostupna DocBits polja: ledger\_account, dimension\_1-12, amount, quantity, quantity2, position

Novo ažuriranje
```
###########################
# Header
###########################

## Header Static Fields
StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,GEOC,CONO,BKID
SF_DIVI=AAA
SF_IBTP=20
SF_CONO=780
#SF_BSCD=DE
SF_IMCD=0
SF_TEPY=N00
SF_PYME=SCT
SF_APCD=FABCEO
SF_CRTP=1
SF_GEOC=60290522

## Header Fields
HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,BKID
HF_SUNO=supplier_id
HF_IVDT=invoice_date
HF_SINO=invoice_id
HF_SPYN=supplier_id
HF_CUCD=currency
HF_CUAM=total_net_amount
#HF_VTAM=total_tax_amount
HF_ACDT=invoice_date
#HF_SERS=invoice_sub_type
HF_FTCO=supplier_country_code
HF_PUNO=purchase_order
HF_TXAP=tax_country_1
HF_CORI = correlation_id
HF_PAIN = sqr_field_esr_reference
HF_BKID = custom_field_1


###########################
# Tax Line
###########################

# ## Tax Line Static Fields
# InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
# IT_SF_RDTP=3
# IT_SF_DIVI=AAA
# IT_SF_CONO=780

# ## Tax Line Fields
# InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
# ITF_VTCD=TF_tax_code
# ITF_VTA1=TF_tax_amount
# ITF_VTP1=TF_tax_rate
# ITF_CLAM=TF_gross_amount

###########################
# Receipt Line
###########################

InvoiceReceipt=invoice_table

## Receipt Line Static Fields
InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
IR_SF_RDTP=1
IR_SF_DIVI=AAA
IR_SF_SERS=0
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=780

## Receipt Line Fields
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM
IRF_IVQA = TF_quantity
IRF_PUUN = TF_unit
IRF_PUNO = TF_purchase_order
IRF_PNLI = TF_line_number
IRF_ITNO = TF_item_number
IRF_POPN = TF_item_number
IRF_SUDO = TF_packing_slip
#IRF_NEPR = TF_net_unit_price
IRF_GRPR = TF_gross_unit_price
IRF_PPUN = TF_unit
#IRF_NLAM = TF_net_amount
IRF_GLAM = TF_total_amount

###########################
# Order Charge Line
###########################

OrderCharge=order_charges

## Order Charge Static Fields
OrderChargeStaticFields=RDTP,DIVI,CONO
OC_SF_RDTP=2
OC_SF_DIVI=AAA
OC_SF_CONO=780

## Order Charge Fields
OrderChargeFields=NLAM,CHGT,CEID
OCF_NLAM=TF_amount
OCF_CHGT=TF_voucher_text
OCF_CEID=TF_ledger_account


###########################
# Cost Line
###########################

InvoiceCost=cost_lines

## Cost Line Static Fields
InvoiceCostStaticFields=RDTP,DIVI,CONO
IC_SF_RDTP=8
IC_SF_DIVI=AAA
IC_SF_CONO=780

## Cost Line Fields
InvoiceCostFields=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2
ICF_NLAM=TF_amount
ICF_VTXT=TF_voucher_text
ICF_AIT1=TF_ledger_account
ICF_AIT2=TF_dimension_2
ICF_AIT3=TF_dimension_3
ICF_AIT4=TF_dimension_4
ICF_AIT5=TF_dimension_5
ICF_AIT6=TF_dimension_6
ICF_AIT7=TF_dimension_7
ICF_AO01=TF_accounting_object_1
ICF_AO02=TF_accounting_object_2
ICF_AO03=TF_accounting_object_3
ICF_AO04=TF_accounting_object_4
ICF_AO05=TF_accounting_object_5
ICF_AO06=TF_accounting_object_6
ICF_AO07=TF_accounting_object_7
```

