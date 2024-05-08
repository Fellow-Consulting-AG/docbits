# Docbits İçin Genişletilmiş Fatura Numaraları Oluşturma Betiği

### Genel Bakış

Bu kılavuz, fatura yönetimini ve takibini geliştirmek için kritik bir özellik olan Docbits'te genişletilmiş fatura numaralarının otomatik oluşturulmasına odaklanmaktadır. "Genişletilmiş Fatura Numaraları Oluşturma" betiği, fatura kimliği ve satın alma siparişi numarası gibi çeşitli belge tanımlayıcıları birleştirerek her fatura için kapsamlı ve benzersiz bir kimlik oluşturur.

### Amaç

Bu betiğin temel amacı, genişletilmiş fatura numaralarının otomatik olarak oluşturulmasını sağlamak ve birden fazla tanımlayıcıyı tek bir benzersiz numaraya birleştirerek faturaların daha kolay takip edilmesini ve yönetilmesini sağlamaktır.

### Betik Uygulaması

#### Kod Parçacığı
```python
# Retrieve the values of invoice ID and purchase order number from the document
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Concatenate the invoice ID and purchase order number with a hyphen if both exist
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check and update the 'invoice_extended_number' field with the concatenated value
if extended_number:
if 'invoice_extended_number' not in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

