# Satın Alma Faturası - 2. Onay Miktarı İhracatı

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 15.00.53.png" alt=""><figcaption></figcaption></figure>

Bu başlık, miktar detaylarına vurgu yaparak satın alma faturaları için ikinci onay aşamasını yönetmek üzere kuralların oluşturulduğunu göstermektedir, fatura üzerindeki miktarların orijinal satın alma siparişindeki miktarlarla eşleşmesini sağlar.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, kuralın yalnızca fatura olarak tanımlanan belgeler için etkinleştirildiğinden, iş akışını doğru şekilde yönlendirmek için kritiktir.
2. **Ve…**
* **Belge Durumu İkinci Onay Bekliyor ise**: Bu, faturanın şu anda ikinci onayda beklediğini belirtir. Bu aşama, işlemin kesinleşmeden önce doğruluğunu sağlamak için genellikle ek denetim sağlar.
* **Belge Alanı Fatura Alt Türü Satın Alma Faturası ise**: Bu koşul, kuralın yalnızca özel olarak "Satın Alma Faturaları" olarak kategorize edilen faturalara uygulandığını belirtir, diğer fatura türlerinden ayırır.
* **Mantık Miktarı sipariş onayı ile satın alma siparişi eşittir**: Bu koşul, sipariş onayında listelenen miktarın satın alma siparişindeki miktarla eşleşip eşleşmediğini kontrol eder. Miktarların tutarlı olması, envanter yönetimi ve finansal doğruluk için kritiktir ve fatura işleminin yalnızca miktarlar tutarlıysa ilerlemesini sağlar.

#### Eylem (O zaman…):

* **İhracatı Başlat**: Fatura belirtilen koşulları karşıladığında (yani, miktarlar sipariş onayı ile satın alma siparişi arasında eşleşiyorsa), "İhracatı Başlat" eylemi tetiklenir. Bu muhtemelen fatura verilerinin başka bir finansal sistem veya raporlama amaçları için daha fazla işleme ihraç edilmesini içerir.

#### Bu Kuralın Amacı:

* **Doğruluğu ve Tutarlılığı Sağlamak**: Sipariş onayı ile satın alma siparişi arasındaki miktarların eşleştiğini doğrulayarak, sistem envanter doğruluğunu korumaya yardımcı olur ve finansal raporlama veya stok yönetimini etkileyebilecek tutarsızlıkları önler.
* **Finansal İşlemleri Hızlandırmak**: Miktarlar onaylandıktan sonra verilerin otomatik olarak ihraç edilmesi, manuel işlemleri azaltır ve finansal işlem döngüsünü hızlandırır.
* **Uyumluluğu ve Denetimi Artırmak**: Miktar doğrulaması için ikinci bir onay gerektirmek, finansal politika ve kontrollerle uyumu sağlamak için ek bir denetim katmanı ekler.

Bu kural, özellikle titiz doğrulama gerektiren büyük hacimli işlemleri içeren satın alma süreçlerinin organizasyon içinde finansal belgelerin hassas ve verimli bir şekilde işlenmesini sağlamak için iş akışı otomasyonunun etkili bir şekilde nasıl kullanılabileceğinin açık bir örneğidir.
