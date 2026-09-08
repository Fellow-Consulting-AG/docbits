# Satınalma Siparişi Eşleştirme Kuralları

## Giriş: Satınalma Siparişleri ve PO Kural Yönetimi

Satınalma Siparişi (PO) Eşleştirme, Satınalma Siparişleri (PO) ile ilgili gelen faturalar veya mal kabul belgeleri arasındaki tutarlılığı sağlamak için kritik bir süreçtir. Yüksek oranda otomatik eşleştirme sağlamak, dolandırıcılığı önlemek ve doğru ödemeleri garanti etmek için sağlam bir kural seti gereklidir.

Bu yapılandırma sayfası, PO satır kalemlerinin ilgili gelen belgeye (Fatura, Sipariş Onayı) _nasıl_ eşleştirileceğini belirleyen kuralların tanımlanması ve yönetilmesi için kullanılır.

{% hint style="info" %}
**Önkoşul:** eşleştirme kuralları, belge türü için **PO eşleştirme sunucu tarafı** açık olduğunda kullanılır (Ayarlar → Belge Türleri → Daha Fazla Ayar → Satınalma Siparişi). Anahtar kapalıysa, DocBits yerleşik eşleştiricisiyle (miktar, birim fiyat, malzeme numarası, satınalma siparişi numarası) eşleştirir ve kural setini göz ardı eder.
{% endhint %}

***

## Erişim Yolu

1.  **Ayarlar --> Genel Ayarlar --> Belge Türleri** yolunu izleyin.

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  İstenen belge türünü seçin ve **Daha Fazla Ayar** butonuna tıklayın.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Ardından Satınalma Siparişi bölümüne gidin ve (PO eşleştirme sunucu tarafı) butonuna tıklayın, ardından PO Eşleştirme Kurallarını Yapılandır'a tıklayın.

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Genel Ayarlar (Temel Kurallar)

Bu ayarlar, tüm eşleştirme kurallarına uygulanan çerçeveyi oluşturur:

* **Ayar:** Miktar Eşleştirme Alanı
  * **Amaç:** Satınalma siparişi satırındaki hangi miktarın belge satırı ile karşılaştırılacağını tanımlar — örneğin sipariş edilen miktar veya **fatura açık miktarı** (sipariş edilen eksi zaten faturalandırılan), ki bu faturalarda yaygın tercihtir.
  * **Geçerli Değerler:** Sistem içindeki miktar veya diğer mevcut miktar alanları, veri yapısına bağlı olarak (örneğin alternatif normalize edilmiş miktar alanı).
  * **Bağımlılık:** Miktar karşılaştırma kriteri içeren tüm eşleştirme kuralları için temel oluşturur.
* **Ayar:** Standart Tolerans (Varsayılan Tolerans)
  * **Amaç:** Belgedeki sayısal bir değerin satınalma siparişi değerinden ne kadar sapabileceğini ve yine de eşleşme sayılacağını belirler. Yuvarlama farklarını telafi eder. "Toleransa İzin Ver" etkin olan **her sayısal sütuna** uygulanır — miktar ve birim fiyat dahil.
  * **Geçerli Değer:** Ondalık sayı. Bunun **mutlak değer** (0.005 = karşılaştırılan miktar veya fiyatta 0.005'e kadar sapma) veya **yüzde** (0.5 = karşılaştırılan değerin %0.5'i) olarak okunması, kural setinin **tolerans türü** ile belirlenir (`value` veya `percent`; yeni kural setleri `value` kullanır). Kalem bazlı toleranslar ([Tolerans ayarları](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) ilgili kalem için standart toleransın önüne geçer.
  * **Bağımlılık:** Sayısal alanları kullanan ve "Toleransa İzin Ver" seçeneği etkin olan kurallara uygulanır.

***

## Kural Listesi

Kural Listesi, mevcut tüm eşleştirme kurallarını gösterir ve yürütme sırasını yönetir.

#### Yapı ve Yürütme

* **Öncelik:** Bu sayısal alan (örneğin 1, 2, 3) kuralların yürütme sırasını belirler. Daha düşük öncelik numarasına sahip kurallar önce denenir. Bu, yöneticilerin genellikle en spesifik ve katı kurallarla (örneğin hem satır numarası hem parça numarası ile eşleştirme) başlayıp daha geniş veya daha az kısıtlayıcı kurallara geçerek bir hiyerarşi oluşturmasına olanak tanır.
* **Ad & Açıklama:** Kuralın açık tanımlamasını ve kullanılan temel kriterleri sağlar (örneğin "Standart Kural No. 1: Satır Numarası, Parça ID ve Miktar bazında eşleştirme").
* **Aktif:** Kuralın yapılandırmasını silmeden anında etkinleştirme veya devre dışı bırakma için basit bir açma/kapama anahtarıdır.

**Yürütme Akışı:** Sistem eşleştirmeyi kademeli olarak yapar. Bir kural (örneğin Öncelik 1) bir satır kalemini başarıyla eşleştirirse, o kalem için süreç durur. Eşleşme bulunamazsa, sistem öncelik sırasındaki sonraki kurala (örneğin Öncelik 2) geçer. Her işlem belge üzerinde kaydedilir; Satınalma Siparişi Eşleştirme ekranındaki **eşleştirme geçmişi**, hangi kuralın denendiğini, hangisinin eşleştiğini ve hangilerinin neden atlandığını gösterir.

***

## Kural Yapılandırması (Detay Ayarları)

Bu detaylı yapılandırma alanı, bireysel bir kural için özel mantık ve kriterleri tanımlar.

#### Temel Parametreler

* **Kural Türü:** Eşleştirmenin kardinalitesini belirtir.

| Kural türü          | Ne yapar                                                                                                                                                                                             | Tipik kullanım                                                                 |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Tekli eşleşme**   | Bir satınalma siparişi satırı ile bir belge satırı. Yapılandırılan her sütun (izin verilen tolerans dahil) uyuşmalıdır.                                                                             | Standart durum.                                                               |
| **Çoklu eşleşme**   | Birden fazla satınalma siparişi satırı bir belge satırına veya birden fazla belge satırı bir satınalma siparişi satırına. Miktarlar **toplanır**, birim fiyat **ortalama** olarak karşılaştırılır, diğer sütunlar uyuşmalıdır. | Parçalı teslimatlar, bir fatura satırının birden fazla sipariş satırını kapsaması. |
| **Toplam üzerinden eşleşme** | Genellikle belge satırının net tutarını satınalma siparişi **toplamı** ile karşılaştırır ve tüm satınalma siparişini bir kerede eşleştirir.                                                     | Toplu fatura düzenleyen tedarikçiler, hizmet faturaları, tek satırlı faturalar. |

* **Otomatik Eşleşme:** Etkinleştirilirse, sistem bu kuralı tamamen otomatik uygulamaya çalışır. Otomatik işlem için kriterlerde yüksek güven gerekir.
* **Manuel Eşleşme:** Etkinleştirilirse, bu kural manuel mutabakat adımında kullanıcıya sunulabilir veya uygulanabilir; istisnaları çözmek için önceden tanımlı karşılaştırma kriterleri sağlar.
* **Yedek Kural:** Yedek olarak işaretlenen kural, tüm normal kurallar çalıştıktan sonra hala eşleşmemiş satır çiftleri için daha sonraki aşamada çalışır. Katı kuralların kaçırdıklarını yakalayan "gevşek" kural olarak kullanılır.

#### Aktivasyon Koşulları

Bir kural, çalışmadan önce doğru olması gereken **aktivasyon koşulları** taşıyabilir. Koşul yanlışsa, kural **bu belge için atlanır** (eşleştirme geçmişinde "çalıştırılmadı" olarak ve nedeniyle gösterilir). İfadeler, eşleştirilen satırların sayısını kullanır:

| İfade                     | Anlamı                                                             |
| ------------------------- | ----------------------------------------------------------------- |
| `[[count(po_lines)]]`     | Eşleştirme için mevcut satınalma siparişi satır sayısı            |
| `[[count(table_lines)]]`  | Eşleştirme için haritalanmış belge satır kalemi sayısı            |

Bunları `==`, `!=`, `>`, `>=`, `<`, `<=` ile karşılaştırın ve birden fazla koşulu `&` (ve) ile birleştirin. Örnekler:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — her iki tarafta birden fazla satır olan belgeler için (çoklu eşleşme kuralı için tipik).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — tek satırlı belgeler için tek satırlı sipariş karşısında.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — eşleştirilecek herhangi bir şey olduğunda.

{% hint style="warning" %}
Aktivasyon koşulları, bir kuralın "hiçbir şey yapmamasının" en yaygın nedenidir. `[[count(table_lines)]] > 1` koşuluna sahip bir toplam üzerinden eşleşme kuralı, tek satırlı bir fatura için asla çalışmaz — ve faturayı tek toplam satıra dönüştüren bir [dönüşüm kuralı](../../transformation-rules.md) tam olarak böyle bir belge üretir. Kuralı değiştirmeden önce eşleştirme geçmişindeki sayımları kontrol edin.
{% endhint %}

#### Sütun Karşılaştırması (Eşleştirme Kriterleri)

Bu, kural mantığının temel tanımıdır ve belgeler arasında hangi alanların uyuşması gerektiğini belirtir.

1. Karşılaştırılacak Sütunların Tanımlanması:
   * **PO Sütunları:** Satınalma Siparişi verilerinden alınan alan (örneğin satır numarası).
   * **Çıkarılan Tablo Sütunları:** Gelen belgeden (Fatura/Sipariş Onayı) çıkarılan veya ayrıştırılan karşılık gelen alan (örneğin `POSITION`).
2. **Karşılaştırma Türü:** Gerekli eşleşmenin doğasını tanımlar (örneğin Tt metin/dize karşılaştırması, karakter karakter tam eşleşme gerektirir; # sayısal karşılaştırma).
3. **Toleransa İzin Ver:** Sayısal alanlar (miktar, fiyat) için bu seçenek etkinleştirilirse, sistem daha önce tanımlanan Küresel Standart Toleransı uygular. Bu etkin değilse, değerler tam olarak eşleşmelidir.
4. **Manuel Eşleşmede Yoksay:** İşaretlenirse, bu kriter manuel müdahale sırasında gevşetilir. Açıklamalar veya dahili referanslar gibi küçük farklılıkların kullanıcı tarafından göz ardı edilmesine olanak tanır.

**Hangi sütunlar karşılaştırılabilir**

| Sütun                           | Belge tarafı                             | Satınalma siparişi tarafı               | Not                                                                                                                                                                                                                             |
| ------------------------------- | --------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Satır numarası                  | `POSITION`                              | `line_number`                           | Metin, tam. Yalnızca tedarikçi belgeye sipariş satır numaralarını basıyorsa kullanışlıdır.                                                                                                                                        |
| Malzeme tanımlayıcı             | `ITEM_IDENTIFIER`                       | `item_identifier`                       | Metin, tam. Malzeme numarası veya tedarikçi malzeme numarası, ayrıca [Tedarikçi Malzeme Numarası Haritası](supplier-item-number-map-admin-documentation.md) aracılığıyla.                                                           |
| Etkin normalize edilmiş miktar | `QUANTITY_EFFECTIVE_NORMALIZED`         | `quantity_effective_normalized`         | Sayısal. **Miktar Eşleştirme Alanı** ile seçilen miktar, her iki tarafta aynı birime dönüştürülmüş (birim kodu dönüşümü, "per" miktarları).                                                                                       |
| Etkin normalize edilmiş birim fiyat | `UNIT_PRICE_EFFECTIVE_NORMALIZED`       | `unit_price_effective_normalized`       | Sayısal. İndirimler sonrası ve **Birim Fiyat Bazında** fiyat, ayrıca [PO birim fiyatı hesaplama](calculate-po-unit-price.md) açıksa, sipariş satırının tutar ve miktarından hesaplanan fiyat.                                      |
| Net tutar                      | `NET_AMOUNT`                            | `total_amount`                          | Sayısal. Toplam üzerinden eşleşme kuralları tarafından kullanılır.                                                                                                                                                               |

**Örnek: Katı PO-Eşleşme Kuralı (`DefaultRule#1`)**

Tipik katı bir kural, zorunlu kimlik kontrollerini değer kontrolleriyle birleştirir:

* **Zorunlu Kimlik:** Satır Numarası ve Malzeme Tanımlayıcı tam olarak eşleşmelidir (Metin karşılaştırması, tolerans yok).
* **Değer Kontrolleri:** Etkin Normalize Miktar ve Etkin Normalize Birim Fiyat eşleşmelidir (Sayısal karşılaştırma, Tolerans İzinli). Tüm dört kriter karşılanırsa (değerlerde tolerans dahil) otomatik eşleşme yapılır.

***

## Varsayılan kural seti

Her kuruluş aynı varsayılan kural seti ile başlar. Kendi kurallarınızı oluştururken iyi bir referanstır:

| Kural                       | Tür / öncelik                | Karşılaştırılan sütunlar                                                  | Aktivasyon koşulu                                     |
| -------------------------- | ---------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------- |
| `DefaultRule#1`            | tekli eşleşme, öncelik 1     | satır numarası, malzeme tanımlayıcı, miktar (tol.), birim fiyat (tol.)    | her zaman                                            |
| `DefaultMultiMatchRules#1` | çoklu eşleşme, öncelik 1, yedek | malzeme tanımlayıcı, miktar (tol.), birim fiyat (tol.)                  | `count(po_lines) > 1` ve `count(table_lines) > 1`    |
| `DefaultTotalMatchRules#1` | toplam üzerinden eşleşme, öncelik 1 | net tutar ↔ satınalma siparişi toplamı (tolerans yok)                    | `count(po_lines) >= 1` ve `count(table_lines) > 1`   |
| `DefaultRule#2`            | tekli eşleşme, öncelik 2, yedek | malzeme tanımlayıcı, miktar (tol.), birim fiyat (tol.)                  | her zaman                                            |
| `DefaultRule#3`            | tekli eşleşme, öncelik 2, yedek | miktar (tol.), birim fiyat (tol.)                                      | `count(po_lines) == 1` ve `count(table_lines) == 1`  |

Yukarıdan aşağıya okunur: önce katı kural (satır numarası ve malzemenin belgede basılması gerekir), sonra satır numarası olmayan yedekler, sonra sadece miktar ve fiyat karşılaştıran tek satırlı belgeler için son çare.

***

## PO Eşleştirme Sürecine Etkisi

Tanımlanan kural seti, PO eşleştirme iş akışının verimliliğini ve bütünlüğünü doğrudan yönetir:

* **Önceliklendirme ve Yedekler:** Tanımlanan Öncelik, sistemin önce en güvenilir eşleştirme yöntemini denemesini sağlar. Katı, yüksek öncelikli kurallar başarısız olursa, sistem daha geniş kurallara geçer ve kullanıcıya yönlendirilen istisna sayısını azaltmayı hedefler.
* **Eşleşme Kalitesinin Kontrolü:** Daha katı kurallar (daha kesin eşleşmeler ve daha az tolerans gerektiren) daha az ama çok güvenilir otomatik eşleşme sağlar. Daha gevşek kurallar otomatik eşleşme oranını artırır ancak yanlış pozitif riskini yükseltir.
* **İstisna Yönetimi (Manuel Eşleşme):** Manuel Eşleşme için kurallar etkinleştirilerek, sistem kullanıcılara yapılandırılmış seçenekler sunar. Bir işlem otomatik eşleşme kriterlerini karşılamazsa, istisna olur. Kullanıcı, önceden tanımlı manuel kuralı uygulayarak (örneğin "Manuel Eşleşmede Yoksay" ayarıyla küçük metin farklılıklarını göz ardı ederek) istisnayı çözmeye çalışabilir.

## Sonucu Etkileyen Diğer Faktörler

* **Eşleştirme ne zaman çalışır:** belge işleme sırasında, kullanıcı **Otomatik PO Eşleştir** butonuna tıkladığında ve satınalma siparişi numarası değiştiğinde veya daha önce hiç sorgulanmadıysa **her kaydetmede** (örneğin ana veriler işlem sonrası doldurduğunda). Bir kayıt, zaten var olan bir eşleşmeyi asla üzerine yazmaz.
* **[Dönüşüm kuralları](../../transformation-rules.md)** eşleşmeden önce çalışır ve satır kalemlerini — dolayısıyla aktivasyon koşullarının baktığı satır sayılarını — değiştirebilir. Satırları yeniden oluşturan bir tablo kuralı, satırlar aynı kaldığı sürece mevcut eşleşmeyi korur; eşleşmiş satırları değiştirirse, eşleşme düşer ve kural adı neden olarak gösterilir.
* **[PO birim fiyatı hesaplama](calculate-po-unit-price.md)** kuralların satınalma siparişi tarafında hangi birim fiyatı karşılaştırdığını değiştirir.
* **[Tolerans ayarları](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** ve **[devre dışı durumlar](purchase-order-disable-statuses.md)** karşılaştırmanın ne kadar katı olduğunu ve hangi satınalma siparişi satırlarının sunulduğunu belirler.

## Sorun Giderme

| Belirti                                                        | Kontrol Edilecekler                                                                                                                                                                               |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "Eşleşme yok" ancak tüm değerler uyuyor                       | Eşleştirme geçmişini açın: hangi kural çalıştı, hangi sütunda başarısız oldu (sapma sütun bazında gösterilir), kural aktivasyon koşulu nedeniyle atlandı mı?                                     |
| Birim fiyat tam olarak vergi oranı kadar az eşleşti           | Satınalma siparişi toplamı vergi içeriyor; [PO birim fiyatı hesaplamayı](calculate-po-unit-price.md) açın (önce net tutar) veya satır net tutarını karşılaştırın.                                 |
| Toplam üzerinden eşleşme kuralı asla çalışmıyor               | Aktivasyon koşulu birden fazla belge satırı gerektiriyor. `[[count(table_lines)]] >= 1` olarak ayarlayın veya dönüşüm kuralıyla satırları tek satıra indirgemeyin.                               |
| Kural seti hiç etkili değil                                    | Belge türü için **PO eşleştirme sunucu tarafı** kapalı veya değiştirilen kural seti hâlâ taslak — sürümü etkinleştirin.                                                                           |

***

## PO Eşleştirme Kurallarını Özelleştirme

PO Eşleştirme kurallarını düzenlemek için varsayılan sürüm, **"Sürümlemeyi Yapılandır"** butonuna tıklanarak ve mevcut kart seçeneklerinden **"Taslak olarak Kopyala"** seçeneği kullanılarak klonlanabilir.

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>