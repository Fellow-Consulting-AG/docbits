# Satın Alma Faturası - 2. Onay Miktarı

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.56.54.png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın özellikle ikincil onay aşamasında satın alma faturalarının işlenmesiyle ilgili olduğunu ve listelenen miktarların doğruluğunun doğrulanmasına odaklandığını göstermektedir.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, kuralın yalnızca fatura olarak sınıflandırılan belgeler için etkinleştirildiğinden emin olur. Bu, iş akışında özgünlüğü ve ilgiyi korumak için esastır.
2. **Ve…**
* **Belge Durumu Bekleyen İkinci Onay ise**: Bu, faturanın şu anda ikinci bir onay için beklediğini belirtir. Bu aşama genellikle faturayı kesinleştirmeden önce ek denetim sağlamayı amaçlar.
* **Belge Alanı Fatura Alt Türü Satın Alma Faturası ise**: Bu koşul, kuralı yalnızca "Satın Alma Faturaları" olarak tanımlanan faturalara uygulamak için daha da rafine eder. Bu kategorizasyon, diğer fatura türlerinden ayırt etmeye yardımcı olur.
* **Mantık Miktarı sipariş onayında Eşit değil satın alma siparişi**: Bu kritik koşul, sipariş onayında belirtilen miktarın orijinal satın alma siparişindeki miktarla eşleşip eşleşmediğini kontrol eder. Bir uyumsuzluk varsa eylem tetiklenir, bu da potansiyel bir hata veya çözülmesi gereken bir sorun olduğunu gösterir.

#### Eylem (O zaman…):

* **Alıcı Adı alanından kullanıcı atayın, yedek olarak kullanıcı Kullanıcıyı kullanın**: Kuralın koşulları karşılanırsa (yani miktarlarda bir uyumsuzluk varsa), fatura, daha fazla inceleme için 'Alıcı Adı' alanında listelenen kişiye otomatik olarak atanır. Bu alan boşsa veya belirtilen kişi uygun değilse, zamanında inceleme ve çözüm sağlamak için varsayılan bir kullanıcı (muhtemelen bir yönetici veya başka bir belirlenmiş personel) devralır.

#### Bu Kuralın Amacı:

* **Doğruluk ve Uyumluluk**: Kural, fatura sürecinin doğru olduğundan ve satın alma siparişinde anlaşılan şartlarla uyumlu olduğundan emin olmak için hayati önem taşır. Finansal uyumsuzlukları ve potansiyel envanter hatalarını önlemeye yardımcı olur.
* **Düzleştirilmiş Onaylar**: Belirli uyumsuzluklar için inceleme sürecini otomatikleştirmek, onayları düzleştirir ve herhangi bir sorunun uygun personel tarafından hızlı bir şekilde ele alınmasını sağlar.
* **Gelişmiş Finansal Denetim**: Miktar doğrulamaları için ikincil bir onay gerektirmek, organizasyon içinde finansal kontrolleri ve sorumluluğu güçlendirir.

Bu kurulum, işletme verimliliğini artırmak ve özellikle bir şirket içinde karmaşık satın alma süreçlerini yönetirken finansal bütünlüğü sağlamak için iş akışı otomasyonunun nasıl kullanılabileceğini örneklemektedir.
