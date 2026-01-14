# Maksimum Tutarın Altında

<figure><img src="../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Fatura"><figcaption></figcaption></figure>

Bu başlık, belirli bir maksimum tutara eşit veya daha az olan faturalarla başa çıkmak için belirlenen kuralın veya koşulun tasarlandığını önermektedir.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, işlenen belgenin bir fatura olup olmadığını kontrol eder. Bu, kuralın yalnızca faturalara ve diğer belge türlerine uygulanmadığından emin olmak için önemlidir.
2. **Ve…**
* **Belge Durumu Onay Bekliyor ise**: Bu, faturanın "Onay Bekliyor" durumunda olması gerektiğini belirtir. Bu durum kontrolü, kuralın yalnızca onay bekleyen faturalara uygulanmasını sağlar.
* **İki Alanı Karşılaştır: Toplam Tutar Az veya Eşit Onaylayıcı Maksimum Tutarı**: Bu koşul, faturanın toplam tutarını bir onaylayıcının maksimum yetkilendirilmiş tutarıyla karşılaştırır. Eğer faturanın toplam tutarı bu maksimum tutara eşit veya daha azsa, kural bir sonraki adıma devam eder. Bu muhtemelen belirli sınırlar içinde küçük sapmaları mümkün kılan bir tolerans seviyesini içerir.

#### Eylem (O zaman…):

* **Onaylayıcı Adı alanından kullanıcı atayın, yedek olarak kullanıcı Kullanıcıyı kullanın**: Belirtilen koşullar karşılandığında, fatura otomatik olarak bir alana belirtilen onaylayıcıya atanır. Bu alan boş veya kullanılamazsa, onay işlemini yönetmek için bir varsayılan kullanıcı (muhtemelen bir yönetici veya başka bir atanmış personel üyesi) yedek olarak atanır.

#### Arayüz Elemanları:

* **Kart Ekle**: Bu düğme, kullanıcıların kurala daha fazla koşul veya eylem eklemelerine olanak tanır, iş akışının esnekliğini ve özgünlüğünü artırır.
* **Kaydet**: Yapılandırılan kuralı sisteme kaydeder.

#### Bu Kuralın Amacı:

Bu yapı, faturaların onay sürecini, miktarına bağlı olarak faturaları otomatik olarak uygun onaylayıcıya yönlendirerek ve yalnızca belirli bir eşik içinde olanların bu otomatik şekilde ele alınmasını sağlayarak optimize etmek için tasarlanmıştır. Finansal kontrolleri yönetmede ve her fatura için manuel kontrolleri azaltarak iş akışını hızlandırmada yardımcı olur.
