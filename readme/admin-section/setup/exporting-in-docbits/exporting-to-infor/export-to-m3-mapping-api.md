# M3 Eşlemesine Aktar (API)

### Bölümler

M3 aktarım eşleme dosyası 5 bölüme ayrılmıştır ve her bölüm daha fazla 2 bölüme ayrılmıştır

* Başlık
* Başlık Statik Alanları
* Başlık Alanları
* Vergi Satırları
* Vergi Satırı Statik Alanları
* Vergi Satırı Alanları
* Fiş Satırları
* Fiş Satırı Statik Alanları
* Fiş Satırı Alanları
* Sipariş Ücret Satırları (Ek Miktarlar)
* Sipariş Ücret Statik Alanları
* Sipariş Ücret Alanları
* Maliyet Satırları
* Maliyet Satırı Statik Alanları
* Maliyet Satırı Alanları

### Alan Ekleme ve Kaldırma

Yeni Alan Ekleme:

* İlk olarak **M3 api alan adını** ilgili bölümün alan listesi özelliğine eklememiz gerekiyor (örneğin StatikAlanlar, BaşlıkAlanları, FaturaVergiAlanları)
* Statik değeri veya belge alan adını api alanı için uygun önek ile tanımlayın
* Örnek 1: **DIVI** M3 api alanı için **AAA** statik değerini tanımlamak için önce DIVI'yi **StatikAlanlar** özelliğine ekledik. Sonra SF\_DIVI = AAA satırını ekledik çünkü SF\_ statik alanlar için önek olarak kullanılır
* Örnek 2: Başlık alanı **IVDT (fatura tarihi)**'yi DocBits'in invoice\_date alanına eşlemek için IVDT'yi **BaşlıkAlanları** özelliğine ekledik. Sonra HF\_IVDT = invoice\_date satırını ekledik çünkü HF\_ başlık alanları için önek olarak kullanılır

Alan Kaldırma:

* Sadece alanı bölümün alan listesi özelliğinden kaldırın ve alan için değeri tanımlayan satırı kaldırın.

#### **Mevcut M3 Api Alanları:**

* Mevcut M3 alanları M3'te ilgili ekrana girilerek kontrol edilebilir.

<figure><img src="../../../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt=""><figcaption></figcaption></figure>

* Benzer şekilde satırlar için alan adlarını alabilirsiniz

### Başlık:

<figure><img src="../../../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt=""><figcaption></figcaption></figure>

Alan Listesi Özelliği: StatikAlanlar

Bölüm Alanları Önek: SF\_

Mevcut Alanlar: Herhangi bir M3 api alanını herhangi bir statik değerle eşleyebilirsiniz

#### **Başlık Alanları**

Alan Listesi Özelliği: BaşlıkAlanları

Bölüm Alanları Önek: HF\_

Mevcut Alanlar: Herhangi bir DocBits alanını herhangi bir M3 api alanına eşleyebilirsiniz

### Vergi Satırı:

#### Vergi Satırı Statik Alanları:

Alan Listesi Özelliği: FaturaVergiStatikAlanlar

Bölüm Alanları Önek: IT\_SF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: Statik alanlar oldukları için herhangi bir değer girebilirsiniz

#### Vergi Satırı Alanları:

Alan Listesi Özelliği: FaturaVergiAlanları

M3 Alanları Önek: ITF\_

DocBits Tablo Alan Öneki: TF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: line\_number, tax\_amount, tax\_rate, net\_amount, gross\_amount, tax\_code\_full, tax\_code, tax\_country

### Fiş Satırı:

#### Fiş Satırı Statik Alanları:

Alan Listesi Özelliği: FaturaFişStatikAlanlar

Bölüm Alanları Önek: IR\_SF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: Statik alanlar oldukları için herhangi bir değer girebilirsiniz

#### Fiş Satırı Alanları:

Alan Listesi Özelliği: FaturaFişAlanları

M3 Alanları Önek: IRF\_

DocBits Tablo Alan Öneki: TF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: packing\_slip, purchase\_order, line\_number, line\_sequence, delivery\_number, delivery\_line, amount, quantity, total\_net\_amount

### Sipariş Ücret Satırı:

#### Sipariş Ücret Statik Alanları:

Alan Listesi Özelliği: SiparişÜcretStatikAlanlar

Bölüm Alanları Önek: OC\_SF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: Statik alanlar oldukları için herhangi bir değer girebilirsiniz

#### Sipariş Ücret Alanları:

Alan Listesi Özelliği: SiparişÜcretAlanları

M3 Alanları Önek: OCF\_

DocBits Tablo Alan Öneki: TF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: ledger\_account, dimension\_2-7, amount, quantity, quantity2, position

### Maliyet Satırı:

#### Maliyet Satırı Statik Alanları:

Alan Listesi Özelliği: FaturaMaliyetStatikAlanlar

Bölüm Alanları Önek: IC\_SF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: Statik alanlar oldukları için herhangi bir değer girebilirsiniz

#### Maliyet Satırı Alanları:

Alan Listesi Özelliği: FaturaMaliyetAlanları

M3 Alanları Önek: ICF\_

DocBits Tablo Alan Öneki: TF\_

Mevcut M3 Alanları: Lütfen M3 API veya UI'ı kontrol edin

Mevcut DocBits Alanları: ledger\_account, dimension\_1-12, amount, quantity, quantity2, position

Yeni güncelleme
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
### ABD Müşterisi için bu eşlemeyi V3'e güncelliyoruz
````
```
# Version 2'den Version 3'e Değişiklikler:
-StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,GEOC,BKID
-SF_DIVI=PJA
+StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO,GEOC
+SF_DIVI=RFP
+SF_CONO=001
-SF_TEPY=J30
-SF_PYME=PTR
+#SF_TEPY=N00
+#SF_PYME=CSH
+#SF_APCD=MHIDALGO
-SF_BKID=001
+SF_GEOC=999999999
+#SF_BKID=DJ1
-HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN
+HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID
-HF_CUAM=total_net_amount
+HF_CUAM=total_net_amount_us
-HF_ACDT=invoice_date
+#HF_ACDT=invoice_date
-HF_CORI = correlation_id
-HF_PAIN = sqr_field_esr_reference
-
+HF_CORI=correlation_id
+HF_PAIN=sqr_field_esr_reference
+HF_TCHG=additional_amount
+HF_CDC1=negative_amount
+HF_APCD=buyer_id
+HF_TEPY=payment_terms
+HF_PYME=payment_method
+HF_BKID=bank_id
+#HF_GEOC=supplier_geoc
-## Vergi Satırı Statik Alanları
-InvoiceTaxStaticFields=RDTP,DIVI,VTCD
-IT_SF_RDTP=3
-IT_SF_DIVI=PJA
+# ## Vergi Satırı Statik Alanları
+# InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
+# IT_SF_RDTP=3
+# IT_SF_DIVI=AAA
+# IT_SF_CONO=780
-## Vergi Satırı Alanları
-InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
-ITF_VTCD=TF_tax_code
-ITF_VTA1=TF_tax_amount
-ITF_VTP1=TF_tax_rate
-ITF_CLAM=TF_gross_amount
+# ## Vergi Satırı Alanları
+# InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
+# ITF_VTCD=TF_tax_code
+# ITF_VTA1=TF_tax_amount
+# ITF_VTP1=TF_tax_rate
+# ITF_CLAM=TF_gross_amount
-InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD
+InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
-IR_SF_DIVI=PJA
-IR_SF_SERS=0
+IR_SF_DIVI=RFP
-IR_SF_VTCD=52
+#IR_SF_VTCD=52
+IR_SF_CONO=001
-InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM
+InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
-#IRF_PUNO = TF_purchase_order
-#IRF_PNLI = TF_line_number
+IRF_PUNO = TF_purchase_order
+IRF_PNLI = TF_line_number
-#IRF_NEPR = TF_net_unit_price
+IRF_NEPR = TF_net_unit_price
-IRF_PPUN = TF_unit
-#IRF_NLAM = TF_net_amount
+IRF_PPUN = TF_unit_code_price
+IRF_NLAM = TF_net_amount
+IRF_TCHG = TF_charges
+IRF_CDC1 = TF_discount
-OrderChargeStaticFields=RDTP,DIVI
+OrderChargeStaticFields=RDTP,DIVI,CONO
-OC_SF_DIVI=PJA
+OC_SF_DIVI=RFP
+OC_SF_CONO=001
-InvoiceCostStaticFields=RDTP,DIVI
+InvoiceCostStaticFields=RDTP,DIVI,CONO
-IC_SF_DIVI=PJA
+IC_SF_DIVI=RFP
+IC_SF_CONO=001
# ITF_VTA1=TF_vergi_miktarı
# ITF_VTP1=TF_vergi_oranı
# ITF_CLAM=TF_brüt_miktar

###########################
# Fiş Satırı
###########################

FaturaFişi=fatura_tablosu

## Fiş Satırı Sabit Alanları
FaturaFişiSabitAlanları=RDTP,DIVI,SERS,RELP,VTCD,CONO
FF_SA_RDTP=1
FF_SA_DIVI=RFP
FF_SA_RELP=1
#FF_SA_VTCD=52
FF_SA_CONO=001

## Fiş Satırı Alanları
FaturaFişiAlanları=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
FFA_IVQA = TF_miktar
FFA_PUUN = TF_birim
FFA_PUNO = TF_satın_alma_siparişi
FFA_PNLI = TF_satır_numarası
FFA_ITNO = TF_ürün_numarası
FFA_POPN = TF_ürün_numarası
FFA_SUDO = TF_paketleme_fiş
FFA_NEPR = TF_net_birim_fiyat
FFA_GRPR = TF_brüt_birim_fiyat
FFA_PPUN = TF_birim_kod_fiyatı
FFA_NLAM = TF_net_miktar
FFA_GLAM = TF_toplam_miktar
FFA_TCHG = TF_masraflar
FFA_CDC1 = TF_indirim

###########################
# Sipariş Masrafı Satırı
###########################

SiparişMasrafı=sipariş_masrafları

## Sipariş Masrafı Sabit Alanları
SiparişMasrafıSabitAlanları=RDTP,DIVI,CONO
SM_SA_RDTP=2
SM_SA_DIVI=RFP
SM_SA_CONO=001

## Sipariş Masrafı Alanları
SiparişMasrafıAlanları=NLAM,CHGT,CEID
SMA_NLAM=TF_miktar
SMA_CHGT=TF_dekont_metni
SMA_CEID=TF_muhasebe_hesabı

###########################
# Maliyet Satırı
###########################

FaturaMaliyeti=maliyet_satırları

## Maliyet Satırı Sabit Alanları
FaturaMaliyetiSabitAlanları=RDTP,DIVI,CONO
FM_SA_RDTP=8
FM_SA_DIVI=RFP
FM_SA_CONO=001

## Maliyet Satırı Alanları
FaturaMaliyetiAlanları=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2
FMA_NLAM=TF_miktar
FMA_VTXT=TF_dekont_metni
FMA_AIT1=TF_muhasebe_hesabı
FMA_AIT2=TF_boyut_2
FMA_AIT3=TF_boyut_3
FMA_AIT4=TF_boyut_4
FMA_AIT5=TF_boyut_5
FMA_AIT6=TF_boyut_6
FMA_AIT7=TF_boyut_7
FMA_AO01=TF_muhasebe_nesnesi_1
FMA_AO02=TF_muhasebe_nesnesi_2
FMA_AO03=TF_muhasebe_nesnesi_3
FMA_AO04=TF_muhasebe_nesnesi_4
FMA_AO05=TF_muhasebe_nesnesi_5
FMA_AO06=TF_muhasebe_nesnesi_6
FMA_AO07=TF_muhasebe_nesnesi_7
```
````

