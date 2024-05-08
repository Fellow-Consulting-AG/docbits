# Maksimum Tutarın Altında

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.48.55.png" alt=""><figcaption></figcaption></figure>

Bu başlık, belirlenen bir maksimum tutara eşit veya daha az olan faturalarla başa çıkmak için kurulan kuralın veya koşulun tasarlandığını önermektedir.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, işlenen belgenin bir fatura olup olmadığını kontrol eder. Bu, kuralın yalnızca faturalara ve diğer belge türlerine uygulanmadığından emin olmak için önemlidir.
2. **Ve…**
* **Belge Durumu Onay Bekliyor ise**: Bu, faturanın "Onay Bekliyor" durumunda olması gerektiğini belirtir. Bu durum kontrolü, kuralın yalnızca onay bekleyen faturalara uygulanmasını sağlar.
* **İki Alanı Karşılaştır: Toplam Tutar Az veya Eşit Onaylayıcı Maksimum Tutarı**: Bu koşul, faturanın toplam tutarını bir onaylayıcının maksimum yetkilendirilmiş tutarıyla karşılaştırır. Eğer faturanın toplam tutarı bu maksimum tutara eşit veya daha azsa, kural bir sonraki adıma devam eder. Bu muhtemelen belirli sınırlar içinde küçük sapmaları mümkün kılan bir tolerans seviyesini içerir.

#### Eylem (O zaman…):

* **Onaylayıcı Adı alanından kullanıcı atayın, yedek olarak kullanıcı Kullanıcıyı kullanın**: Belirtilen koşullar karşılandığında, fatura otomatik olarak bir alana belirtilen onaylayıcıya atanır. Bu alan boş veya kullanılamazsa, onay işlemini yönetmek için bir yedek kullanıcı (muhtemelen bir yönetici veya başka bir belirlenmiş personel üyesi) atanır.

#### Arayüz Elemanları:

* **Kart Ekle**: Bu düğme, kullanıcıların kurala daha fazla koşul veya eylem eklemelerine olanak tanır, iş akışının esnekliğini ve özgünlüğünü artırır.
* **Kaydet**: Yapılandırılan kuralı sisteme kaydeder.

#### Bu Kuralın Amacı:

Bu yapı, faturaların onay sürecini otomatik olarak miktarına göre uygun onaylayıcıya yönlendirerek ve yalnızca belirli bir eşik içinde olanların bu otomatik şekilde ele alınmasını sağlayarak iyileştirmeyi amaçlar. Finansal kontrolleri yönetmede ve her fatura için manuel kontrolleri azaltarak iş akışını hızlandırmada yardımcı olur.
