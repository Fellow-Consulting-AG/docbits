# DocBits İçin Dışa Aktarma Sertifika Referans Numaraları Script'inin Biçimlendirilmesi

Bu belge, DocBits'te dışa aktarma sertifikaları arasındaki referans numaralarını standartlaştırmayı amaçlayan "Dışa Aktarma Sertifika Referans Numaralarını Biçimlendirme" script'ini açıklar. Doğru biçimlendirme, referans numaralarının harici sistemlere veya düzenleyici gereksinimlere uygun olmasını sağlar.

### Amaç

Script'in temel amacı, dışa aktarma sertifikalarındaki referans numaralarını biçimlendirmektir; böylece belirli bir uzunluk gereksinimini karşılamak için sayıları başında sıfırlarla doldurur. Bu tutarlılık, DocBits aracılığıyla işlenen tüm dışa aktarma belgeleri için standart bir formun korunmasına yardımcı olur.

### Script Genel Bakış

Script, bir dışa aktarma sertifikasındaki `reference_number` alanını tanımlar, uzunluğunu kontrol eder ve gerektiğinde sayıyı başında sıfırlarla doldurarak belirli bir minimum uzunluk gereksinimini karşıladığından emin olur.

#### Kod Parçacığı
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

