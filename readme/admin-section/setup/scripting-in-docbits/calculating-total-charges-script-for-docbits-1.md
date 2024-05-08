# Docbits İçin Toplam Ücret Hesaplama Betiği

##

"Toplam Ücretleri Hesaplama" betiği fatura belgeleri içindeki çeşitli ücretleri ve ek miktarları toplamanın otomatikleştirilmiş bir sürecini sağlar. Bu kılavuz, betiğin kurulumu, mantığı ve uygulaması hakkında size rehberlik ederek belgelerinizde doğru toplam ücret hesaplamalarını sağlar.

### Amaç

Bu betiğin amacı, fatura üzerindeki toplam ücretleri hesaplamanın dinamik bir yolunu sağlamaktır. Bu işlem, temel ücretler, navlun (Fracht) ve ambalajlama (Verpackung) gibi farklı ücret türlerini toplayarak fatura üzerindeki toplam ücretleri günceller. Böylece doğru fatura bilgilerini sağlar.

### Betik Genel Bakışı

Betiğ, belirtilen alanlardan değerleri alır, bunları ondalık sayılara dönüştürür, toplar ve ardından `total_charges` alanını hesaplanan toplamla günceller. Eğer `total_charges` alanı mevcut değilse, betik bu alanı oluşturur ve değerini buna göre ayarlar.

#### Kod Parçacığı
```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
fracht = float(fracht)
total += fracht

# Add verpackung to total if it exists
if verpackung:
verpackung = float(verpackung)
total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

