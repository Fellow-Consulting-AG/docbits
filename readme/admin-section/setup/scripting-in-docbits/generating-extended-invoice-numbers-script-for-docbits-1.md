# Docbits İçin Genişletilmiş Fatura Numaraları Oluşturma Betiği

Bu belge, Docbits'te genişletilmiş fatura numaralarının oluşturulmasını otomatikleştiren "Genişletilmiş Fatura Numaraları Oluşturma" betiğini detaylandırmaktadır. Genişletilmiş fatura numaraları, fatura kimliği ve satın alma siparişi numarası gibi birden fazla belge kimliğini tek, kapsamlı bir kimlikte birleştirir. Bu betik belge izlenebilirliğini artırır ve kayıt tutmayı basitleştirir.

### Amaç

Bu betiğin amacı, fatura kimliği ve satın alma siparişi numarasını otomatik olarak birleştirerek genişletilmiş fatura numaralarının oluşturulma sürecini kolaylaştırmaktır, böylece her fatura belgesi için birleşik ve benzersiz bir kimlik sağlar.

### Betik Genel Bakışı

Betik, belgede fatura kimliği ve satın alma siparişi numarası alanlarının varlığını kontrol eder, her ikisi de mevcutsa değerlerini birleştirir (bir tire ile ayrılmış olarak) ve birleşik değeri depolamak için mevcut bir alanı günceller veya yeni bir alan oluşturur.

#### Kod Parçacığı
```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
# Updating the 'invoice_extended_number' field with the combined value
if not 'invoice_extended_number' in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

