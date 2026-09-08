# 8 Eylül 2026 Hotfixleri

> Satın alma siparişi eşleştirme: 8 Eylül 2026'da dağıtılan hotfixlerle neler değişti. Aşağıdaki davranış geliştirme ortamında canlıdır ve sonraki yükseltmelerle stage, sandbox ve üretim ortamlarına ulaşır.

## Satın alma siparişi eşleştirme

- **Eşleşme kaydetme işleminden sonra korunur.** Bir dönüşüm kuralının her kaydetmede sessizce düşürdüğü (satır öğelerini yeniden oluşturan kurallar) satın alma siparişi eşleşmesi, kural aynı satırları ürettiği sürece artık korunur. Bir kural gerçekten eşleşen satırları değiştirdiğinde, belge kuralı kaydeder ve ekran bunu belirtir.
- **Kaydetme işleminde eşleştirme tekrar çalışır.** Belgedeki satın alma siparişi numarası değiştiğinde — veya ana veriler işlemden sonra bunu doldurduğunda ve henüz bir eşleştirme çalışması yapılmadığında — kaydetme işlemi belgeyi hemen eşleştirir. Mevcut bir eşleşme asla kaydetme ile üzerine yazılmaz.
- **Ekran neden eşleşme olmadığını belirtir.** Satın Alma Siparişi Eşleştirme ekranı, satın alma siparişi alanının üzerinde bir cümle gösterir: satın alma siparişi numarası yok, satın alma siparişi ERP’de bulunamadı, henüz bakılmadı, yüklendi ama bağlanmadı, satır eşleşmiyor, tablo yok, tablo sütunları eşlenmedi, açık satır kalmadı. Bir kenara konulan adaylar nedenleriyle birlikte listelenir (örneğin satın alma siparişi sütununa okunmuş bir fatura numarası).
- **Düşürülen eşleşme asla kaydedilmiş olarak raporlanmaz.** Sunucu bir eşleşmeyi tutmazsa, ekran bunu geri yükler, belgeyi kaydedilmemiş olarak işaretler ve "kaydedildi" yerine reddetme nedenini bildirir.
- **Eşleştirme geçmişi dönüşüm kurallarını gösterir.** Bir belgenin eşleştirme geçmişinde artık ilk eşleştirme aşamasından önce _Dönüşüm kuralları_ adımı vardır; çalışan kuralları ve bunlardan birinin eşleşmeyi düşürüp düşürmediğini listeler. Yöneticiler kurala bağlantı alır.
- **Satın alma siparişi birim fiyatı net tutardan alınır.** _Satın alma siparişi birim fiyatını hesapla_ açıkken, fiyat artık önce satın alma siparişi satırının **net** tutarından türetilir, net tutar yoksa toplamdan alınır. Infor’dan gelen satın alma siparişleri satır toplamında vergi taşır; net fiyatlandırılmış faturalar tam olarak vergi oranı kadar "birim fiyat düşük eşleşti" olarak görünürdü. Hesaplanan fiyat her eşleşmede yenilenir, böylece mevcut belgeler satın alma siparişini yeniden yüklemeden faydalanır.
- **Fatura numaraları artık satın alma siparişi numarası ile karıştırılmaz.** Satır öğesi sütunundan veya önceki bir aramadan gelen ve belgenin kendi fatura numarasına eşit olan aday kenara konur.

## Dokümantasyon

- Yeni sayfa [Dönüşüm Kuralları](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md).
- [Satın Alma Siparişi Eşleştirme Kuralları](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) artık kural türlerini, etkinleştirme koşullarını, yedek kuralları, varsayılan kural setini, tolerans türlerini ve geçerli sütunları kapsar.
- [Satın alma siparişi birim fiyatını hesapla](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/calculate-po-unit-price.md) net tutar hesaplamasını açıklar.
- [Satın Alma Siparişi Eşleştirme Ekranı](../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) "neden eşleşme yok" mesajlarını ve eşleştirme geçmişini açıklar.