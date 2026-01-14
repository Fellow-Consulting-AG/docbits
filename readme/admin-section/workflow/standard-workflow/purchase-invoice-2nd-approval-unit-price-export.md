# Satın Alma Faturası - 2. Onay Birimi Fiyatı Dışa Aktarımı

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Satın alma Sipariş Dışa aktar 5"><figcaption></figcaption></figure>

Bu başlık, satın alma faturalarının ikinci onay aşamasını yönetmek için kuralların kurulduğunu ve birim fiyatına odaklandığını gösterir, böylece anlaşılan şartlarla eşleştiğinden emin olunur.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, kuralın yalnızca fatura olarak tanımlanan belgeler için etkinleştirildiğinden, iş akışını doğru şekilde yönlendirmek için önemlidir.
2. **Ve…**
* **Belge Durumu Bekleyen İkinci Onay ise**: Bu, faturanın ikinci onayı beklediğini belirtir. Bu aşama genellikle işlemi sonlandırmadan önce doğruluğu sağlamak için ek denetim sağlar.
* **Belge Alanı Fatura Alt Türü Satın Alma Faturası ise**: Bu koşul, kuralın yalnızca özellikle "Satın Alma Faturaları" olarak kategorize edilen faturalara uygulandığını belirtir, diğer fatura türlerinden ayırır.
* **Mantık Birim Fiyatı sipariş onayı ile Satın Alma Siparişi eşittir**: Bu koşul, sipariş onayında listelenen birim fiyatının satın alma siparişindeki birim fiyatıyla eşleşip eşleşmediğini kontrol eder. Fiyatlandırmada tutarlılık olduğundan emin olur ve bütçeleme ve finansal raporlama için kritiktir.

#### Eylem (O zaman…):

* **Dışa Aktarmayı Başlat**: Fatura belirtilen koşulları karşıladığında (yani, birim fiyatlar sipariş onayı ile satın alma siparişi arasında eşleşirse), "Dışa Aktarmayı Başlat" eylemi tetiklenir. Bu muhtemelen fatura verilerinin başka bir finansal sistem veya raporlama amaçları için daha fazla işleme aktarılmasını içerir.

#### Bu Kuralın Amacı:

* **Doğruluğu ve Tutarlılığı Sağlamak**: Sipariş onayı ile satın alma siparişi arasındaki birim fiyatların eşleştiğini doğrulayarak, sistem finansal doğruluğu korumaya ve aşırı ücretlendirme veya eksik ücretlendirmeyi önlemeye yardımcı olur.
* **Finansal İşlemleri Hızlandırmak**: Fiyatlar onaylandıktan sonra verilerin otomatik olarak dışa aktarılması, manuel işlemleri azaltır ve finansal işlem döngüsünü hızlandırır.
* **Uyumluluğu ve Denetimi Artırmak**: Fiyat doğrulaması için ikinci bir onay gerektirmek, finansal politika ve kontrollerle uyum sağlamak için kritik olan ek bir denetim katmanı ekler.

Bu kural, iş akışı otomasyonunun, özellikle titiz doğrulama gerektiren büyük hacimli işlemler bağlamında, bir organizasyon içinde finansal belgelerin hassas ve verimli bir şekilde ele alınmasını sağlamak için etkili bir şekilde nasıl kullanılabileceğinin bir örneğidir.
