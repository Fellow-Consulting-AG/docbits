# Boş Miktar ve Tutarı Olan Satırları Sil

#### Bölüm 1: Boş Miktar ve Tutarı Olan Satırları Sil

Bu betik bölümü, hem miktarın hem de toplam tutarın sıfır veya belirtilmemiş olduğu satırları kaldırmak için bir fatura tablosunu işler.

* **INVOICE\_TABLE Kontrol Et:** İlk olarak, `tables_dict` sözlüğünde `INVOICE_TABLE` anahtarının varlığını kontrol ederek başlar.
* **Satırları İşle:** Tablodaki her satır için betik, `TOTAL_AMOUNT` ve `QUANTITY` sütunlarının var olup olmadığını ve değerlerini yakalamak için bayraklar ve değişkenler başlatır.
* **Sütun İsimlerini Kontrol Et:** Her bir satırdaki her sütunu dolaşırken, `TOTAL_AMOUNT` ve `QUANTITY` adında sütunları arar.
* Eğer `TOTAL_AMOUNT` bulunursa, değeri yakalanır. Bu değer sıfırdan farklıysa, bir ondalık sayıya dönüştürülür.
* Benzer şekilde `QUANTITY` için, eğer sıfırdan farklıysa değeri yakalar ve dönüştürür.
* **Satırı Silme İşaretleyin:** Bir satırdaki her iki sütunu da kontrol ettikten sonra, eğer hem toplam tutar hem de miktar etkili bir şekilde sıfırsa (ya sıfır olup olmadığına ya da var olup olmadığına bakılarak), satır silinmek üzere `row['is_deleted']` değeri `True` olarak işaretlenir.

#### Bölüm 2: Satır Toplamını Fatura Toplamına Karşı Doğrulayın

Bu bölüm, bir faturadaki tüm satırlardan toplam tutarı hesaplar ve bunu faturanın bildirilen toplamıyla karşılaştırarak tutarların tutarlılığını doğrular.

* **Satır Toplamını Başlat:** İlk olarak, tüm satırlardan toplam tutarı biriktirmek için `lines_total` adlı bir değişkeni 0.0 olarak ayarlayarak başlar.
* **Satır Tutarlarını Topla:** `INVOICE_TABLE`daki her satırı dolaşarak, her birinden `TOTAL_AMOUNT`'ı çıkarır ve `lines_total`'a ekler.
* **Fatura Toplamını Al ve Dönüştür:** Yardımcı bir işlev olan `get_field_value` kullanarak toplam fatura tutarını alır ve bir ondalık sayıya dönüştürür.
* **Toplamları Karşılaştır:** Son olarak, hesaplanan satır toplamı (`lines_total`) ile bildirilen fatura toplamı (`total_amount`) arasındaki mutlak farkın 0.05 eşiğini aşılıp aşmadığını kontrol eder. Eğer öyleyse, fatura toplamı alanını geçersiz olarak işaretler ve bir uyumsuzluk belirterek başka bir yardımcı işlev olan `set_field_as_invalid` kullanır.
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
#### Özet

Betik, veri bütünlüğünü etkili bir şekilde sağlar:

1. Fatura toplamına katkıda bulunmayan miktar veya tutar eksikliği nedeniyle veri satırlarını kaldırır.
2. Bireysel satır tutarlarının toplamı ile genel fatura toplamı arasındaki tutarlılığı doğrular ve farklılıkları belirleyerek daha fazla işlem için vurgular.

Bu otomasyon, doğru finansal kayıtların tutulmasına yardımcı olur ve muhasebe ve finansal raporlama için hassas verilere ihtiyaç duyan ERP gibi sistemler için hayati öneme sahip olabilir.
