# Alanlar

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.02.31.png" alt=""><figcaption></figcaption></figure>

#### Genel Bakış

Alanlar ayarı, yöneticilerin belge türüyle ilişkilendirilen bireysel veri alanlarının özelliklerini ve davranışını yönetebileceği bir kullanıcı arayüzü sağlar. Her alan, veri yakalama ve doğrulama işlemlerini optimize etmek için ayarlanabilir.

#### Temel Özellikler ve Seçenekler

1. **Alan Yapılandırması**:
* **Alan Adları**: Genellikle belgedeki veri öğelerine karşılık gelen alan adlarını listeler, örneğin "Fatura Numarası" veya "Satın Alma Siparişi Tarihi".
* **Gerekli**: Yöneticiler, belge işleminin tamamlanması için bu alanlara veri girilmesini veya yakalanmasını sağlamak için alanları gerekli olarak işaretleyebilir.
* **Salt Okunur**: Alanlar, veri yakalama sonrası veya belge işleminin belirli aşamalarında değişikliği önlemek için salt okunur olarak ayarlanabilir.
* **Gizli**: Alanlar, hassas bilgiler veya kullanıcı iş akışlarını basitleştirmek için kullanıcı arayüzünde görüntülenmekten gizlenebilir.
2. **Gelişmiş Ayarlar**:
* **Zorunlu Doğrulama**: Bir alana girilen verinin kabul edilmeden önce belirli doğrulama kurallarını geçmesini sağlar.
* **OCR (Optik Karakter Tanıma)**: Bu anahtar, belirli bir alanda OCR işlemini etkinleştirmek için açılabilir; taramalı veya dijital belgelerden otomatik veri çıkarma için kullanışlıdır.
* **Eşleşme Puanı**: Yöneticiler, veri tanıma veya eşleşme güvenilirlik düzeyini belirlemek için kullanılan bir eşleşme puanı tanımlayabilir; veri doğrulama ve kalite kontrollerinin nasıl gerçekleştirileceğini etkiler.
3. **Eylem Düğmeleri**:
* **Yeni Alan Oluştur**: Belge türüne yeni alanlar eklemeyi sağlar.
* **Düzenle Simgeleri**: Her alanın bir düzenleme simgesi vardır; bu simge, yöneticilerin veri türü, varsayılan değerler veya bağlı iş mantığı gibi alan özgü ayarları daha fazla yapılandırmasına olanak tanır.
* **Ayarları Kaydet**: Alan yapılandırmalarına yapılan değişiklikleri kaydeder.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
