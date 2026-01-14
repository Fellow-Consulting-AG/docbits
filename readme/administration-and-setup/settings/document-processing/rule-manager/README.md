# Kural Yöneticisi (Rule Manager)


Bu belge, DocBits faturalama sisteminde kullanılan çakışma çözümleme kurallarının derinlemesine bir açıklamasını sunar. Bu kurallar, fatura ayrıntıları ile satın alma siparişi (PO) verileri arasındaki tutarsızlıkları otomatik olarak ele almak ve doğru finansal mutabakat sağlamak için tasarlanmıştır. Sistem bu kuralları fatura kalemlerini, masrafları ve vergileri işlemek için uygular ve gerektiğinde uygun düzeltmeleri veya notları oluşturur.

## Kuralların Yapısı

### 1. Meta Veriler

• sürüm (version): Eşleme dosyasının sürümünü tanımlar.

• revizyon (revision): Değişiklikleri izlemek için revizyon numarası.

• yazar (author): Eşleme dosyasını oluşturanı belirtir.

• açıklama (description): Dosyanın amacının kısa bir açıklaması.

• oluşturulma_tarihi (created_at) ve güncellenme_tarihi (updated_at): Dosyanın ne zaman oluşturulduğuna ve en son ne zaman güncellendiğine dair zaman damgaları.

### 2. Dışa Aktarma Yapılandırması (Export Configuration)

Dışa aktarma yapılandırması bölümü, sistemdeki veri alanları ile dışa aktarma dosyalarındaki karşılık gelen alanlar arasındaki eşlemeyi tanımlar.

• Başlık (Header): Dışa aktarılan fatura verileri için başlık alanlarını tanımlar.

• Vergi Kalemleri (Tax Lines): Dışa aktarımdaki vergi kalemleri için alanları belirtir.

• Sipariş Başlığı Masrafları (Order Header Charges): Sipariş başlığı düzeyindeki ek masraflarla ilgili alanları eşler.

• Makbuz Kalemleri (Receipt Lines): Bir makbuzdaki tekil kalemler için alanları eşler.

• Sipariş Kalemi Masrafları (Order Line Charges): Belirli sipariş kalemleriyle ilgili masraflar için alanları tanımlar.

• Maliyet Kalemleri (Cost Lines): Maliyet dağıtım kalemleri için alanları belirtir.

• Borç Notu (Debit Note) ve Alacak Notu (Credit Note): Tutarsızlık durumlarında borç ve alacak notları oluşturmak için alanları tanımlar.

### 3. Çakışma Çözümleme Kuralları

Bu kurallar, fatura verileri ile ilgili PO verileri arasındaki tutarsızlıkları ele alır. Her kural birkaç bileşenden oluşur:

• Ad (Name): Kuralın açıklayıcı adı, ele aldığı tutarsızlık türünü belirtir.

• Bölüm (Section): Kuralın faturanın hangi bölümüne (örneğin, makbuz_kalemleri, kalem_masrafları) uygulanacağını belirtir.

• Aktif (Active): Kuralın şu anda aktif olup olmadığını belirten boolean değer (true veya false).

• Eşleşme Kriterleri (Match Criteria): Gerçek fatura verileri ile beklenen PO verileri arasındaki karşılaştırmalara dayanarak kuralı tetikleyen koşullar.

• Eylemler (Actions): Değerleri ayarlama, masrafları uygulama veya alacak/borç notları oluşturma dahil olmak üzere, kural tetiklendiğinde sistemin ne yapması gerektiğini tanımlar.

## Kurallardaki Ortak Öğeler

### Karşılaştırma Operatörleri

Bu operatörler, gerçek fatura değerlerinin beklenen PO değerleriyle nasıl karşılaştırılacağını tanımlar:

• eşit (equal)

• büyüktür (greater than)

• büyüktür veya eşittir (greater than or equal to)

• küçüktür (less than)

• küçüktür veya eşittir (less than or equal to)

• tolerans dahilinde (within tolerance)

• tolerans dışında (outside tolerance)


### Onay Durumu

Bir tutarsızlığın onaylanıp onaylanmadığını belirtir:

• onaylandı (approved)

• reddedildi (rejected)

• herhangi biri (any)


### Eylem Türleri

Bir tutarsızlık algılandığında gerçekleştirilecek belirli eylemleri tanımlar:


• makbuz kalemi (receipt line)

• maliyet kalemi (cost line)

• başlık masrafı (header charge)

• kalem masrafı (line charge)

• vergi kalemi (tax line)

• borç notu makbuz kalemi (debit note receipt line)

• borç notu maliyet kalemi (debit note cost line)

• borç notu başlık masrafı (debit note header charge)

• borç notu kalem masrafı (debit note line charge)

• alacak notu makbuz kalemi (credit note receipt line)

• alacak notu maliyet kalemi (credit note cost line)

• alacak notu başlık masrafı (credit note header charge)

• alacak notu kalem masrafı (credit note line charge)

• alacak notu vergi kalemi (credit note tax line)


### Kural Örnekleri

#### [Durum 1, 2, 3: Tolerans Dahilinde Miktar ve Birim Fiyat](transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md)


• Amaç: Faturadaki hem miktarın hem de birim fiyatın PO'ya kıyasla kabul edilen tolerans sınırları içinde olduğu senaryoları ele alır.

• Eylem: Sistem fatura değerlerini kabul eder ve toplam tutarı hesaplar.



#### [Durum 4, 5: Tolerans Dahilinde Miktar, Tolerans Dışında Birim Fiyat (Onaylandı)](./#case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved)

• Amaç: Miktarın tolerans dahilinde olduğu ancak birim fiyatın tolerans dışında olduğu ve onaylandığı durumlarda uygulanır.

• Eylem: Sistem, birim fiyatı PO ile eşleşecek şekilde ayarlar ve gerekli kalem masraflarını uygular.



#### [Durum 6: Tolerans Dahilinde Miktar, Negatif Tolerans Dışında Birim Fiyat (Reddedildi)](transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

• Amaç: Birim fiyatın beklenenden düşük ve tolerans aralığının dışında olduğu ve reddedilmeye yol açtığı durumlarla ilgilenir.

• Eylem: Sistem, birim fiyatı PO ile eşleşecek şekilde ayarlar, fark için bir alacak notu oluşturur ve gerektiğinde başlık masraflarını uygular.


### Masrafları ve Vergileri İşleme

### Birim Başına Masraf Toleransı

• Bu kategori altındaki kurallar, masrafın tolerans dahilinde mi yoksa dışında mı olduğuna ve onaylanıp onaylanmadığına veya reddedilip reddedilmediğine bağlı olarak belirli eylemlerle birim başına masraflardaki tutarsızlıkları ele alır.

### Vergi Kalemi Ayarlamaları

• Bu kurallar, fatura ve PO vergi verileri arasındaki farklara dayanarak vergi kalemlerini ayarlayarak veya ilgili alacak veya borç notlarını oluşturarak vergi tutarsızlıklarını yönetir.

### Numaralandırmalar (Enums) ve Seçenekler

• Enums: Kurallar arasında tutarlılık sağlayan önceden tanımlanmış değer listeleri (örneğin, karşılaştırma operatörleri, onay türleri).

• Seçenekler: Miktarları veya birim fiyatları işlemek için önceden tanımlanmış seçimler, kural tanımlarında esneklik sunar.

## Ekran Görüntüleri Açıklaması

### Ekran Görüntüsü 1: Kural Yönetimi Arayüzü

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-08-02 um 17.20.56.png" alt=""><figcaption></figcaption></figure>

Bu ekran görüntüsü, yöneticilerin tüm çakışma çözümleme kurallarını görüntüleyebileceği ve yönetebileceği Kural Yönetimi arayüzünü gösterir. Temel öğeler şunlardır:

• Kural Ekle Düğmesi: Yeni kurallar eklemeye olanak tanır.

• Kuralların Listesi: Ad, bölüm ve aktif durum gibi ayrıntılarla birlikte tüm aktif kuralları görüntüler.

• Bölüm Açılır Menüsü: Kuralları uygulandıkları bölüme göre filtreler (örneğin, Makbuz Kalemleri, Kalem Masrafları).

### Ekran Görüntüsü 2: Ayrıntılı Kural Düzenleme

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-08-02 um 17.21.06.png" alt=""><figcaption></figcaption></figure>

Bu ekran görüntüsü, düzenlenen belirli bir kuralın ayrıntılı görünümünü göstermektedir. Temel öğeler şunlardır:

• Kriterler Bölümü: Kuralın tetiklendiği koşulları tanımlar. Örneğin kriterler, miktar ve birim fiyatın PO'dan farklı olması ancak tolerans dahilinde olması durumunda kuralın uygulanması gerektiğini belirtebilir.

• Eylemler Bölümü: Kriterler karşılandığında hangi eylemlerin gerçekleştirilmesi gerektiğini belirtir. Bu, fatura kalemlerini ayarlamayı, alacak veya borç notları oluşturmayı veya ek masraflar uygulamayı içerebilir.

• Belge Türü ve Maliyet Kalemleri: Yöneticinin belirli eylemleri belge türlerine ve maliyet kalemlerine eşlemesine olanak tanıyarak farklı senaryoları ele almada esneklik sağlar.
