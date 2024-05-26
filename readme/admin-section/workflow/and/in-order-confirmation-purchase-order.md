# Sipariş Onayı Satın Alma Siparişi

### Satın Alma Siparişi ile Karşılaştırma:&#x20;

**Sipariş Onayı Satın Alma Siparişi**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Mantık Kartı: Miktar veya Birim Fiyatı veya İndirim Eşleşmesi

Bu mantık kartı, bir sipariş onayındaki miktarın, birim fiyatın veya indirimin, satın alma siparişindeki karşılık gelen rakamlarla eşleşip eşleşmediğini otomatik olarak doğrulamak için tasarlanmıştır. Bu doğrulama, sipariş edilen ürünler ile tedarikçinin teslim etmeyi onayladığı ürünler arasındaki tutarlılık ve doğruluğu sağlar.

#### Tetikleme Koşulu

Mantık, sipariş onayında aşağıdaki koşullardan herhangi biri, orijinal satın alma siparişine göre karşılandığında etkinleştirilir:

* **Miktar**: Sipariş edilen ürün miktarı, tedarikçi tarafından onaylanan miktarla eşleşir.
* **Birim Fiyat**: Kabul edilen her bir ürün fiyatı, tedarikçinin onayıyla eşleşir.
* **İndirim**: Uygulanan indirimler, satın alma siparişi ile sipariş onayı arasında tutarlıdır.

#### Sonuçlar

* **Eşit**: Eğer sipariş onayındaki miktar, birim fiyat veya indirim satın alma siparişi ile tam olarak eşleşirse, sistem onayı geçerli kabul eder ve satın alma sürecindeki sonraki adımlara devam eder.
* **Eşit Değil**: Miktar, birim fiyat veya indirimde bir uyumsuzluk varsa, sistem sipariş onayını manuel inceleme için işaretler. Bu, herhangi bir uyumsuzluğun ilerlemesinden önce çözülmesini sağlar.

#### Faydalar

* **Doğruluk ve Tutarlılık**: Satın alma sürecinde doğruluğu korur, ödemelerin ve teslimatların doğru rakamlara dayalı olarak yapılmasını sağlar.
* **Verimlilik**: Doğrulama sürecini otomatikleştirerek manuel kontrollerin ihtiyacını azaltır ve sipariş işleme sürecini hızlandırır.
* **Maliyet Kontrolü**: Uyumsuzlukları erken tespit ederek aşırı ödemeleri veya yanlış teslimatları önlemeye yardımcı olur.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Karşılaştırma Parametrelerini Tanımlayın**: Mantık kartının eşleşmeyi kontrol edeceği belirli alanları (miktar, birim fiyat, indirim) ayarlayın.
2. **Doğrulamayı Otomatikleştirin**: Bir sipariş onayı alındığında sistemde bu detayları otomatik olarak karşılaştırmak için yapılandırın.
3. **Uyarıları Özelleştirin**: Uyumsuzlukları ele alma iş akışını belirleyin, manuel inceleme için uyarıları özelleştirin.

Bu mantık kartı, bir sipariş onayının detaylarının orijinal satın alma siparişi ile uyumlu olduğundan emin olmak için hayati öneme sahiptir ve satın alma döngüsünün bütünlüğünü korur. \`\`
