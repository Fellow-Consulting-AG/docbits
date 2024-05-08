# Eksportowanie do mapowania M3 (API)

### Sekcje

Plik mapowania eksportu M3 jest podzielony na 5 sekcji, a każda sekcja jest dodatkowo podzielona na 2 sekcje

* Nagłówek
* Statyczne pola nagłówka
* Pola nagłówka
* Linie podatkowe
* Statyczne pola linii podatkowej
* Pola linii podatkowej
* Linie paragonu
* Statyczne pola linii paragonu
* Pola linii paragonu
* Linie opłat zlecenia (Dodatkowe kwoty)
* Statyczne pola opłat zlecenia
* Pola opłat zlecenia
* Linie kosztów
* Statyczne pola linii kosztów
* Pola linii kosztów

### Dodawanie i usuwanie pól

Dodawanie nowego pola:

* Najpierw musimy dodać **nazwę pola API M3** do właściwej listy pól sekcji (np. StaticFields, HeaderFields, InvoiceTaxFields)
* Zdefiniuj wartość statyczną lub nazwę pola dokumentu dla pola API z odpowiednim prefiksem dla sekcji
* Przykład 1: Aby zdefiniować statyczną wartość **AAA** dla pola API M3 **DIVI.** Najpierw dodaliśmy DIVI do właściwości **StaticFields**. Następnie dodajemy linię **SF\_DIVI = AAA** jako SF\_ to prefiks dla pól statycznych
* Przykład 2: Aby zmapować pole nagłówka **IVDT (data faktury)** na pole invoice\_date w DocBits. Najpierw dodajemy IVDT do właściwości **HeaderFields**. Następnie dodajemy linię HF\_IVDT = invoice\_date jako HF\_ to prefiks dla pól nagłówka

Usuwanie pola:

* Po prostu usuń pole z listy pól sekcji i usuń linię definiującą wartość dla pola.

#### **Dostępne pola API M3:**

* Dostępne pola M3 można sprawdzić, otwierając odpowiedni ekran w M3.

<figure><img src="../../../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt=""><figcaption></figcaption></figure>

* Podobnie można uzyskać nazwy pól dla linii

### Nagłówek:

<figure><img src="../../../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt=""><figcaption></figcaption></figure>

Właściwość listy pól: StaticFields

Prefiks pól sekcji: SF\_

Dostępne pola: Możesz zmapować dowolne pole API M3 z dowolną wartością statyczną

#### **Pola nagłówka**

Właściwość listy pól: HeaderFields

Prefiks pól sekcji: HF\_

Dostępne pola: Możesz zmapować dowolne pole DocBits na dowolne pole API M3

### Linia podatkowa:

#### Statyczne pola linii podatkowej:

Właściwość listy pól: InvoiceTaxStaticFields

Prefiks pól sekcji: IT\_SF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: Możesz wprowadzić dowolną wartość, ponieważ są to pola statyczne

#### Pola linii podatkowej:

Właściwość listy pól: InvoiceTaxFields

Prefiks pól M3: ITF\_

Prefiks pola tabeli DocBits: TF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: line\_number, tax\_amount, tax\_rate, net\_amount, gross\_amount, tax\_code\_full, tax\_code, tax\_country

### Linia paragonu:

#### Statyczne pola linii paragonu:

Właściwość listy pól: InvoiceReceiptStaticFields

Prefiks pól sekcji: IR\_SF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: Możesz wprowadzić dowolną wartość, ponieważ są to pola statyczne

#### Pola linii paragonu:

Właściwość listy pól: InvoiceReceiptFields

Prefiks pól M3: IRF\_

Prefiks pola tabeli DocBits: TF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: packing\_slip, purchase\_order, line\_number, line\_sequence, delivery\_number, delivery\_line, amount, quantity, total\_net\_amount

### Linia opłaty zlecenia:

#### Statyczne pola opłaty zlecenia:

Właściwość listy pól: OrderChargeStaticFields

Prefiks pól sekcji: OC\_SF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: Możesz wprowadzić dowolną wartość, ponieważ są to pola statyczne

#### Pola opłaty zlecenia:

Właściwość listy pól: OrderChargeFields

Prefiks pól M3: OCF\_

Prefiks pola tabeli DocBits: TF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: ledger\_account, dimension\_2-7, amount, quantity, quantity2, position

### Linia kosztów:

#### Statyczne pola linii kosztów:

Właściwość listy pól: InvoiceCostStaticFields

Prefiks pól sekcji: IC\_SF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: Możesz wprowadzić dowolną wartość, ponieważ są to pola statyczne

#### Pola linii kosztów:

Właściwość listy pól: InvoiceCostFields

Prefiks pól M3: ICF\_

Prefiks pola tabeli DocBits: TF\_

Dostępne pola M3: Proszę sprawdzić M3 API lub interfejs użytkownika

Dostępne pola DocBits: ledger\_account, dimension\_1-12, amount, quantity, quantity2, position

Nowa aktualizacja
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

