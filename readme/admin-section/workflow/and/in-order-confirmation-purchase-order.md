# Sipariş Onayı Satın Alma Siparişi

### Satın Alma Siparişi ile Karşılaştır:&#x20;

**Sipariş Onayı Satın Alma Siparişi**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Mantık Kartı: Miktar veya Birim Fiyatı veya İndirim Eşleşmesi

Bu mantık kartı, bir sipariş onayındaki miktarın, birim fiyatın veya indirimin, satın alma siparişindeki karşılık gelen rakamlarla eşleşip eşleşmediğini otomatik olarak doğrulamak için tasarlanmıştır. Bu doğrulama, sipariş edilen ve tedarikçinin teslim etmeyi onayladığı şey arasındaki tutarlılık ve doğruluğu sağlar.

#### Tetikleyici Koşul

Mantık, bir sipariş onayında aşağıdaki koşullardan herhangi biri, orijinal satın alma siparişine göre karşılandığında etkinleştirilir:

* **Miktar**: Sipariş edilen ürün miktarı, tedarikçi tarafından onaylanan miktarla eşleşir.
* **Birim Fiyat**: Kabul edilen her bir ürün fiyatı, tedarikçinin onayıyla eşleşir.
* **İndirim**: Uygulanan indirimler, satın alma siparişi ile sipariş onayı arasında tutarlıdır.

#### Sonuçlar

* **Eşit**: Eğer sipariş onayının miktarı, birim fiyatı veya indirimi tam olarak satın alma siparişiyle eşleşirse, sistem onayı geçerli olarak kabul eder ve tedarik sürecindeki sonraki adımlara devam eder.
* **Eşit Değil**: Miktar, birim fiyatı veya indirimde bir uyumsuzluk varsa, sistem sipariş onayını manuel inceleme için işaretler. Bu, herhangi bir uyumsuzluğun ilerlemeden önce çözülmesini sağlar.

#### Faydalar

* **Doğruluk ve Tutarlılık**: Satın alma sürecinde doğruluğu korur, ödemelerin ve teslimatların doğru rakamlara göre yapılmasını sağlar.
* **Verimlilik**: Doğrulama sürecini otomatikleştirerek manuel kontrollerin azaltılmasına ve sipariş işleme sürecinin hızlandırılmasına yardımcı olur.
* **Maliyet Kontrolü**: Uyumsuzlukları erken tespit ederek aşırı ödemeleri veya yanlış teslimatları önlemeye yardımcı olur.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Karşılaştırma Parametrelerini Tanımlayın**: Mantık kartının eşleşmeyi kontrol edeceği belirli alanları (miktar, birim fiyat, indirim) ayarlayın.
2. **Doğrulamayı Otomatikleştirin**: Bir sipariş onayı alındığında bu detayları otomatik olarak karşılaştırmak için sistemi yapılandırın.
3. **Uyarıları Özelleştirin**: Uyumsuzlukları ele alma iş akışını belirleyin, manuel inceleme için uyarıları özelleştirin.

Bu mantık kartı, bir sipariş onayının detaylarının orijinal satın alma siparişiyle uyumlu olduğundan emin olmak için hayati öneme sahiptir ve satın alma döngüsünün bütünlüğünü korur. \`\`
