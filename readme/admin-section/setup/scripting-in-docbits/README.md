# DocBits Betikleme

## Docbits Betikleme Rehberi

Docbits betikleme rehberine hoş geldiniz! Burada, belgelerinizin işlenmesini otomatikleştirmek ve geliştirmek için betikler kullanmayı öğreneceksiniz. Betikler, çeşitli belge türleri arasında özel alan manipülasyonu, veri dönüşümü ve mantık uygulamasına olanak tanır.

### Başlarken

Docbits'te betikler Python dilinde yazılır. Belge alanları ve meta verileri ile etkileşime girerek basit veri biçimlendirme işlemlerinden karmaşık mantığa kadar geniş bir işlem yelpazesi gerçekleştirirler.

#### Ana Fonksiyonlar

* `get_field_value(fields_dict, field_name, default=None)`: Belirtilen alanın değerini alır.
* `set_field_value(fields_dict, field_name, value)`: Belirtilen alanın değerini ayarlar.
* `create_new_field(field_name, value)`: Belirtilen ad ve değere sahip yeni bir alan oluşturur.
* `format_decimal_to_locale(value, locale)`: Bir ondalık değeri belirli bir yerelle biçimlendirir.

### Örnek Betikler

Aşağıda, yaygın betik görevlerini gösteren birkaç örnek bulunmaktadır.

#### Örnek 1: Faturalar için Para Birimi Eşleme

Standartlaştırılmış para birimi sembollerini veya metni ISO para birimi kodlarına dönüştürün.
```python
currency_map = {
"€": "EUR",
"EURO": "EUR",
"$": "USD",
"£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
currency_value = currency_value.upper()
if currency_value in currency_map:
currency_value = currency_map[currency_value]
set_field_value(fields_dict, "currency", currency_value)
```

