# TransactionConfig Pro Şablonu

## Finansal Belge İşleme için Kapsamlı Yapılandırma Aracı

_TransactionConfig Pro Şablonu_, faturalar, borç notları ve alacak notları gibi finansal belgelerin işlenmesini yönetmek için kurumsal ortamlar için tasarlanmış güçlü bir yapılandırma aracıdır. Araç, işletmelerin finansal iş akışlarını hassasiyetle otomatikleştirmesine ve özelleştirmesine olanak tanıyan ayrıntılı eşleme ve alan tanımları sağlar. Mevcut Infor ERP sistemleriyle sorunsuz bir şekilde bütünleşen _TransactionConfig Pro Şablonu_, küresel finansal standartlara uyumu korurken karmaşık işlemlerin doğru bir şekilde ele alınmasını sağlar.

### Ana Özellikler

• Ayrıntılı Eşleme: Çeşitli işlem türleri arasında alanların hassas bir şekilde eşlenmesine olanak tanıyarak veri tutarlılığını ve doğruluğunu sağlar.

• Özelleştirme: Belirli iş ihtiyaçlarını karşılamak için finansal belge iş akışlarının özelleştirilmesini destekler.

• Otomasyon: Finansal işlemlerin ele alınmasını otomatikleştirerek manuel hataları azaltır ve verimliliği artırır.

• Entegrasyon: Mevcut Infor M3/LN ERP sistemleriyle kolayca entegre olur ve kuruluşun genel finansal işleme yeteneklerini geliştirir.

• Uyumluluk: Uluslararası finansal standartlara ve düzenlemelere uyumu sağlayarak işletmelerin küresel işlemleri etkili bir şekilde yönetmesine yardımcı olur.



## Çakışma Çözümleme Durumlarının Ayrıntılı Açıklaması

_TransactionConfig Pro Şablonu_, fatura verileri ile satın alma siparişi (PO) verileri arasındaki yaygın tutarsızlıkları ele almak için bir dizi önceden tanımlanmış kural içerir. Bu kurallar, sapmalar meydana geldiğinde karar vermeyi otomatikleştirmek için tasarlanmıştır ve finansal işlemlerde tutarlılık ve doğruluk sağlar.

### [Durum 1, 2, 3: Tolerans Dahilinde Miktar ve Birim Fiyat](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Senaryo:** Faturadaki hem miktar hem de birim fiyat, satın alma siparişine kıyasla kabul edilebilir bir tolerans aralığı içindedir.

• **Eylem:** Sistem fatura değerlerini kabul eder ve sağlanan miktar ve birim fiyata göre toplam tutarı hesaplar.

### [Durum 4, 5: Tolerans Dahilinde Miktar, Tolerans Dışında Birim Fiyat (Onaylandı)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Senaryo:** Faturadaki miktar tolerans dahilindedir, ancak birim fiyat tolerans dışındadır ve bu sapma onaylanmıştır.

• **Eylem:** Sistem, birim fiyatı satın alma siparişiyle eşleşecek şekilde ayarlar ve farkı hesaba katmak için gerekli kalem masraflarını uygular.

### [Durum 6: Tolerans Dahilinde Miktar, Negatif Tolerans Dışında Birim Fiyat (Reddedildi)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Senaryo:** Miktar tolerans dahilindedir, ancak birim fiyat kabul edilebilir aralığın altındadır (negatif tolerans) ve onaylanmamıştır.

• **Eylem:** Sistem birim fiyatı reddeder, satın alma siparişiyle eşleşecek şekilde ayarlar ve fark için bir alacak notu oluşturur. Gerektiğinde ek başlık masrafları uygulanabilir.

### [Durum 7: Tolerans Dahilinde Miktar, Tolerans Dışında Birim Fiyat (Pozitif Reddedildi)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Senaryo:** Miktar tolerans dahilindedir, ancak birim fiyat kabul edilebilir aralığı (pozitif tolerans) aşar ve onaylanmamıştır.

• **Eylem:** Sistem fatura birim fiyatını reddeder, satın alma siparişiyle eşleşecek şekilde ayarlar ve fazla faturalanan tutarı hesaba katmak için bir borç notu oluşturabilir.

### [Durum 8a, 9a: Tolerans Dışında Miktar (Onaylandı), Tolerans Dahilinde Birim Fiyat](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Senaryo:** Faturadaki miktar kabul edilebilir toleransın dışındadır ancak onaylanmıştır, birim fiyat ise tolerans dahilindedir.

• **Eylem:** Sistem onaylanan miktarı ve faturadaki birim fiyatı kabul eder ve işlemi buna göre gerçekleştirir.

### [Durum 11a: Tolerans Dışında Miktar (Pozitif Reddedildi), Tolerans Dahilinde Birim Fiyat](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Senaryo:** Faturadaki miktar kabul edilebilir aralığı (pozitif) aşar ve reddedilir, ancak birim fiyat tolerans dahilindedir.

• **Eylem:** Sistem, miktarı onaylanan seviyeye ayarlar, birim fiyatı korur ve işlemi gerçekleştirir. Fazla miktar reddedilir ve faturalanmaz.

### [Durum 10a: Tolerans Dışında Miktar (Negatif Reddedildi), Tolerans Dahilinde Birim Fiyat](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Senaryo:** Miktar kabul edilebilir aralığın altındadır (negatif tolerans) ve onaylanmamıştır, ancak birim fiyat tolerans dahilindedir.

• **Eylem:** Sistem, miktarı onaylanan seviyeye uyacak şekilde ayarlar ve birim fiyatı tutarlı tutar. İşlem buna göre gerçekleştirir.

### [Durum 8b, 9b: Tolerans Dışında Miktar (Onaylandı), Tolerans Dışında Birim Fiyat (Onaylandı)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Senaryo:** Hem miktar hem de birim fiyat tolerans aralığının dışındadır ancak onaylanmıştır.

• **Eylem:** Sistem, hem miktar hem de birim fiyat için fatura değerlerini kullanarak işlemi gerçekleştirir ve gerekli ayarlamaları veya kalem masraflarını uygular.

### [Durum 10b: Tolerans Dışında Miktar (Negatif Reddedildi), Tolerans Dışında Birim Fiyat (Reddedildi)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Senaryo:** Hem miktar hem de birim fiyat tolerans dışındadır ve hiçbiri onaylanmamıştır.

• **Eylem:** Sistem fatura verilerini reddeder, değerleri satın alma siparişiyle eşleşecek şekilde ayarlar ve gerekli borç veya alacak notlarını oluşturur.

### [Durum 11b: Tolerans Dışında Miktar (Pozitif Reddedildi), Tolerans Dışında Birim Fiyat (Reddedildi)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Senaryo:** Miktar kabul edilebilir aralığı (pozitif) aşar ve reddedilir, birim fiyat da tolerans dışındadır ve reddedilir.

• **Eylem:** Sistem, miktarı ve birim fiyatı satın alma siparişindeki onaylanan seviyelerle eşleşecek şekilde ayarlar, fazlalıkları reddeder ve işlemi gerçekleştirir.

### [Durum 12, 13: Masraf Kalemi - Tolerans Dahilinde Birim Başına Masraf](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Senaryo:** Faturadaki birim başına masraf, satın alma siparişine kıyasla kabul edilebilir tolerans aralığı içindedir.

• **Eylem:** Sistem fatura edildiği şekliyle birim başına masrafı kabul eder ve işlemi ayarlama yapmadan gerçekleştirir.

### [Durum 14: Masraf Kalemi - Tolerans Dışında Birim Başına Masraf (Onaylandı)](charge-per-unit-outside-tolerance-approved-1.md)

**Senaryo:** Birim başına masraf tolerans dışındadır ancak onaylanmıştır.

• **Eylem:** Sistem birim başına masrafı kabul eder ve onaylanan masrafları uygular, işlemi buna göre gerçekleştirir.

### [Durum 15: Masraf Kalemi - Tolerans Dışında Birim Başına Masraf (Reddedildi)](charge-per-unit-outside-tolerance-rejected.md)

**Senaryo:** Birim başına masraf tolerans dışındadır ve onaylanmamıştır.

• **Eylem:** Sistem birim başına masrafı satın alma siparişine veya onaylanan seviyelere uyacak şekilde ayarlar ve gerekli borç veya alacak notlarını oluşturur.

### [Durum 12, 13: Başlık Masrafı - Tolerans Dahilinde Birim Başına Masraf](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Senaryo:** Birim başına başlık masrafı, satın alma siparişine kıyasla kabul edilebilir tolerans aralığı içindedir.

• **Eylem:** Sistem başlık masrafını fatura edildiği gibi gerçekleştirir, ayarlama yapmadan uygular.

### [Durum 14: Başlık Masrafı - Tolerans Dışında Birim Başına Masraf (Onaylandı)](charge-per-unit-outside-tolerance-approved.md)

**Senaryo:** Birim başına başlık masrafı tolerans dışındadır ancak onaylanmıştır.

• **Eylem:** Sistem onaylanan birim başına masrafı gerçekleştirir ve işleme uygular.

### [Durum 15: Başlık Masrafı - Tolerans Dışında Birim Başına Masraf (Reddedildi)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Senaryo:** Birim başına başlık masrafı tolerans dışındadır ve onaylanmamıştır.

• **Eylem:** Sistem başlık masrafını satın alma siparişiyle eşleşecek şekilde ayarlar, işlemi buna göre gerçekleştirir ve gerekli notları oluşturur.

### [tax-lines.md](tax-lines.md "mention")

**Senaryo:** Fatura ve satın alma siparişi arasındaki vergi tutarlarındaki tutarsızlıkları ele alır.

• **Eylem:** Sistem, vergi kalemlerini onaylanan vergi oranlarına ve tutarlarına göre ayarlayarak geçerli vergi düzenlemelerine uyumu sağlar.
