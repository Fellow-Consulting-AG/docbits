# Satın Alma Faturası - 2. Onay Birimi Fiyatı

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Onay Fatura 3"><figcaption></figcaption></figure>

Bu başlık, satın alma faturasının ikinci onay aşamasını yönetmek için kuralların oluşturulduğunu ve özellikle birim fiyatının doğrulanmasına odaklandığını göstermektedir.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, kuralın yalnızca fatura olarak tanımlanan belgeler için tetiklendiğinden emin olur, diğer belge türlerini filtreler ve iş akışının ilgisini korur.
2. **Ve…**
* **Belge Durumu Bekleyen İkinci Onay ise**: Bu, faturanın ikinci onayı beklediği aşamada olduğunu belirtir. Bu genellikle nihai işlemden önce ek denetim sağlamak için tasarlanmış bir adımdır.
* **Belge Alanı Fatura Alt Türü Satın Alma Faturası ise**: Bu kuralın uygulanmasını yalnızca "Satın Alma Faturaları" olarak sınıflandırılan faturalara daraltır, diğer fatura alt türlerinden ayırır.
* **Mantıksal Birim Fiyatı sipariş onayında Eşit değil satın alma siparişi**: Bu mantıksal kontrol, sipariş onayında listelenen birim fiyatını orijinal satın alma siparişindeki birim fiyatıyla karşılaştırır. Bu değerler eşleşmiyorsa, çözülmesi gereken bir uyumsuzluğu işaret edebilir ve işlem tetiklenir.

#### Eylem (O zaman…):

* **Alıcı Adı alanından kullanıcı atayın, yedek olarak kullanıcı Kullanıcıyı kullanın**: Belirtilen koşullar karşılandığında (yani birim fiyatlarında uyumsuzluk varsa), fatura otomatik olarak bir alıcıya (‘Alıcı Adı’ alanında belirtilen isim) daha fazla inceleme için atanır. 'Alıcı Adı' alanı boş veya belirtilmemişse, onayı yönetmek için varsayılan bir kullanıcı (muhtemelen bir yönetici veya başka bir atanmış personel) yedek olarak atanır.

#### Bu Kuralın Amacı:

* **Doğruluk ve Uyumluluğu Sağlamak**: Bu kural, fatura sürecinin doğru ve anlaşmalı şartlara uygun olduğundan emin olmak için kritiktir. Birim fiyatlarında bir uyumsuzluk olduğunda inceleme tetikleyerek, sistem finansal hataları veya potansiyel dolandırıcılığı önlemeye yardımcı olur.
* **Onayları Düzenlemek**: Belirli uyumsuzluklara dayalı olarak inceleme atamasını otomatikleştirmek, onay sürecini hızlandırır ve sorunların uygun personel tarafından hızla ele alınmasını sağlar.
* **Finansal Denetim**: Özellikle fiyat eşleştirmeye dayalı olarak ikinci bir onay gerektirmek, organizasyon içinde finansal kontrolleri ve sorumluluğu güçlendirir.
