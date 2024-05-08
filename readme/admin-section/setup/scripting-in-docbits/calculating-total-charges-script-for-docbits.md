# Docbits İçin Toplam Ücret Hesaplama Betiği

### Giriş

Bu belge, Docbits platformundaki "Toplam Ücretleri Hesaplama" betiği hakkında detaylı bir kılavuz sağlar. Betik, farklı bireysel ücretleri toplayarak faturada tahsil edilen toplam tutarı otomatik olarak hesaplamak üzere tasarlanmıştır. Bu otomasyon, belge işleme sürecinde doğruluğu ve verimliliği artırır.

### Amaç

Bu betiğin amacı, faturalardaki toplam ücretlerin hesaplama sürecini kolaylaştırmaktır. Temel ücretler, vergiler ve ek ücretler gibi belirtilen ücretleri otomatik olarak ekleyerek, betik her faturadaki yansıtılan toplam ücretlerin doğru ve kapsamlı olduğunu sağlar.

### Betik Detayları

#### Kod Uygulaması
```python
# Initialize variables to store the values of individual charges
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Calculate the total by converting each charge to a float and summing them up
total = 0
if fracht:
total += float(fracht)
if verpackung:
total += float(verpackung)

# Format the total to two decimal places and update the 'total_charges' field
formatted_total = "{0:.2f}".format(total)
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

