# Dönüşüm Kuralları

## Genel Bakış

Dönüşüm kuralları, çıkarılan verileri **otomatik olarak** temizler veya yeniden yazar — başlıktaki bir alanı, bir tablodaki bir sütunu, tüm tablo satırlarını veya belgenin bir özniteliğini — her belge işlendiğinde ve her kaydedildiğinde. Bu kurallar, birçok kuruluşun "bu alanı her zaman kırp", "bu sütunu varsayılan olarak 1 yap", "bu tedarikçinin birim kodlarını eşleştir" veya "bu tedarikçinin satır kalemlerini tek bir toplam satırda birleştir" gibi küçük betikler yazmak için kullandığı yöntemlerin yerini alır.

Bir kural, her **belge türü** için tanımlanır ve o türdeki her belge üzerinde çalışır. Kurallar, doğrulamadan, betiklerden ve satın alma siparişi eşleştirmesinden **önce** çalışır, böylece sonraki işlemler zaten dönüştürülmüş değerleri görür.

## Nasıl erişilir

1. **Ayarlar → Genel Ayarlar → Belge Türleri** yolunu izleyin.
2. Belge türünü açın ve **Dönüşüm Kuralları** seçeneğini seçin. Liste, türdeki her kuralı kapsamı, hedefi, önceliği ve aktif olup olmadığı ile gösterir.
3. Yeni bir kural oluşturmak için **Yeni kural** butonuna tıklayın veya mevcut bir kuralı değiştirmek için açın.

## Bir kuralın yapısı

| Bölüm              | Nedir                                                                                                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ad / anahtar**    | Listelerde, mesajlarda ve eşleştirme geçmişinde gösterilen görüntü adı ve kural yeniden adlandırıldığında sabit kalan teknik anahtar.                                                                                              |
| **Kapsam**         | Kuralın yazdığı yer: bir **başlık alanı**, bir **tablo sütunu**, bir **tablo** (tüm satırlar) veya bir **belge özniteliği**. Aşağıya bakınız.                                                                                                  |
| **Hedef**        | Kuralın yazdığı alan, sütun (tablosu ile birlikte) veya tablo.                                                                                                                                                                   |
| **Kaynak**        | İsteğe bağlı. Kuralın girdisini hedefin kendisi yerine okuduğu yer: başlık alanı için `header.<field>`, belge özniteliği için `doc.<attribute>`, aynı satırın başka bir sütunu için (sadece sütun kapsamı) `row.<column>`. |
| **Ne zaman**          | **Her zaman**, veya bir koşul doğru olduğunda **sadece** (Koşullara bakınız).                                                                                                                                                                 |
| **Eylemler**       | Sırayla uygulanan dönüşümler listesi; bir eylemin çıktısı bir sonraki eylemin girdisidir.                                                                                                                                 |
| **Öncelik**      | Aynı kapsamda kurallar artan öncelik sırasına göre (sonra anahtara göre) çalışır. Bir kuralın diğerinin sonucunu görmesi gerektiğinde kullanılır.                                                                                                              |
| **Bir kez çalıştır**      | Kural bir belgeye **en fazla bir kez** uygulanır. Her kayıtta değeri tekrar değiştirecek eylemler (alt dize, regex değiştirme, regex çıkarma) ve satırları tekrar oluşturması istenmeyen tablo kuralları için gereklidir.        |
| **Çalıştırma kaydı** | Her uygulamada bir kayıt satırı yazar — yeni bir kuralı ayarlarken faydalıdır.                                                                                                                                                           |

### Kapsamlar

| Kapsam                  | Yazdığı yer                                                  | Tipik kural                                                                            |
| ---------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Başlık alanı**       | bir çıkarılan başlık alanı (fatura numarası, para birimi, …)   | fatura numarasını kırp ve büyük harfe çevir; "EUR€" değerini "EUR" olarak eşleştir                             |
| **Tablo sütunu**       | bir tablonun her satırındaki bir sütun                         | `UNIT_PRICE_PER` değerini varsayılan olarak 1 yap; ürün numarasından "Art.-Nr." önekini çıkar         |
| **Tablo**              | bir tablonun satırları                                        | satırları temizle ve toplam üzerinden eşleşen bir tedarikçi için tek bir toplam satır ekle       |
| **Belge özniteliği** | Belgenin kendisinin bir özniteliği (şu anda alt organizasyon) | Bir tedarikçinin belgelerini bir alt organizasyona yönlendir                                      |

Kurallar kapsam kapsam şu sırayla çalışır: başlık → belge → tablo → sütun. Bu nedenle bir sütun kuralı, bir tablo kuralının eklediği satırları zaten görür.

### Koşullar ("sadece")

Bir koşul, belgenin bir değerini bir sabitle karşılaştırır. Değer, bir başlık alanından (`header.<field>`), belge özniteliğinden (`doc.<attribute>`) veya sütun kuralları için mevcut satırın bir sütunundan (`row.<column>`) gelir.

| Operatör                          | Anlamı                                    |
| --------------------------------- | ------------------------------------------ |
| is / is not                       | tam karşılaştırma                           |
| is one of / is not one of         | listedeki değer                            |
| contains, starts with, ends with  | metin karşılaştırması                            |
| is empty / is not empty           | değer gerektirmez                            |
| greater than, less than, at least, at most | sayısal karşılaştırma                 |
| matches                           | düzenli ifade                             |

Koşullar **all of** (ve) ve **any of** (veya) ile gruplanabilir ve **not** ile olumsuzlanabilir. Örnek: _sadece `header.supplier_id` `20723` olduğunda_ — kural sadece bir tedarikçi için çalışır.

### Eylemler

Başlık alanları ve tablo sütunları için eylemler (bir boru hattı oluştururlar; değer yukarıdan girer ve aşağıdan çıkar):

| Eylem             | Etkisi                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `trim`             | soldan, sağdan veya her iki taraftan boşlukları (veya verilen karakterleri) kaldırır                                            |
| `case`             | büyük harf, küçük harf, başlık stili veya kelime başı büyük yapar                                                                                   |
| `pad`              | bir karakterle belirli uzunluğa tamamlar, sola veya sağa                                                                     |
| `truncate`         | maksimum uzunluğa keser                                                                                             |
| `affix`            | önek veya sonek ekler ya da birini çıkarır                                                                                |
| `sanitize`         | sadece bir karakter sınıfını tutar (alfanümerik, alfa, sayısal, alfanümerik + boşluk) veya bir karakter kümesini çıkarır        |
| `substring`        | değerin bir parçasını başlangıç ve uzunluk veya bitişe göre alır                                                                 |
| `regex_replace`    | düzenli ifadeyle eşleşeni değiştirir                                                                           |
| `regex_extract`    | düzenli ifadeyle yakalananı tutar                                                                             |
| `value_map`        | değerleri başka değerlere eşler (isteğe bağlı olarak büyük/küçük harf duyarsız, varsayılan ile)                                            |
| `date_format`      | tarihi yeniden biçimlendirir (girdi, DocBits'in `value` içinde sakladığı ISO tarih olmalıdır)                                         |
| `number_format`    | sayıyı yeniden biçimlendirir                                                                                                  |
| `default`          | alan boşsa bir değer atar                                                                            |
| `set_value`        | alan ne içerirse içersin sabit bir değer atar                                                                     |
| `clear`            | alanı boşaltır                                                                                                     |

**Tablo** kapsamı için eylemler (satırlar üzerinde çalışır, değerler üzerinde değil ve yukarıdaki eylemlerle karıştırılamaz):

| Eylem       | Etkisi                                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | tablonun tüm satırlarını siler                                                                                                      |
| `add_row`    | sona veya başa bir satır ekler; her sütun ya sabit bir değer alır ya da başlıktan (`header.<field>`) veya belgeden (`doc.<attribute>`) okunan bir değeri alır |

{% hint style="info" %}
`substring`, `regex_replace` ve `regex_extract` zaten dönüştürülmüş bir değer üzerinde çalıştığında değeri tekrar değiştirir. Bunları **Bir kez çalıştır** ile birleştirin veya düzenli ifadeyi ikinci çalıştırmada değişiklik yapmayacak şekilde yazın.
{% endhint %}

## Kurallar ne zaman çalışır

* İşleme sırasında, çıkarma işleminden sonra ve doğrulama, betikler ve satın alma siparişi eşleştirmeden önce.
* Çıkarılan verinin değiştiği belgede **her kayıtta**. **Bir kez çalıştır** olmayan kurallar her kayıtta tekrar uygulanır; yukarıdaki üç eylem dışında her eylem idempotent olduğu için, hedef biçimde zaten olan bir değer olduğu gibi kalır.

## Dönüşüm kuralları ve satın alma siparişi eşleştirme

Tablo ve sütun kuralları, satın alma siparişi eşleştiricinin gördüğünü değiştirir:

* Satırları **yeniden oluşturan** bir tablo kuralı (örneğin tüm satırları temizleyip tek bir toplam satır eklemek) mevcut satın alma siparişi eşleşmesini, **aynı satırları tekrar ürettiği sürece** korur — değerler anlamlarına göre karşılaştırılır, bu yüzden `1.0` ve `1.00` aynı satırdır. Satırlar kimliklerini korur ve eşleşme her kayıtta devam eder.
* Bir kural **eşleşmiş satırları değiştirir veya kaldırırsa**, eşleşme korunamaz. Belge, hangi kuralın bunu yaptığını kaydeder, Satın Alma Siparişi Eşleştirme ekranı bunu neden olarak gösterir ("_Satın alma siparişi eşleşmesi kaydedilemedi: dönüşüm kuralı "…" tabloyu yeniden oluşturdu_") ve yöneticilere kurala bağlantı verir. Belgenin **eşleştirme geçmişi**, ilk eşleştirme aşamasından önce çalışan kurallarla bir _Dönüşüm kuralları_ adımı gösterir.
* Kurallardan sonra kalan satır sayısı, eşleştirme kurallarının [etkinleştirme koşulları](more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) tarafından sayılır. Bir faturayı **tek** satıra indirgeyen bir kural, yalnızca tek satırlı belgeler için etkin olan toplam üzerinden eşleştirme kuralıyla anlamlıdır (`[[count(table_lines)]] >= 1`).

## Örnekler

**Fatura numarasını temizle** — başlık alanı `invoice_id`, her zaman: `trim` → `case` büyük harf.

**Fiyat temelini varsayılan yap** — satır kalem tablosunun `UNIT_PRICE_PER` sütunu, her zaman: `default` `1`.

**Bir tedarikçinin birim kodlarını eşleştir** — satır kalem tablosunun `UNIT` sütunu, sadece `header.supplier_id` `10040` olduğunda: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Toplam üzerinden eşleşen bir tedarikçi için tek toplam satır** — satır kalem tablosunda tablo kapsamı, sadece `header.supplier_id` `20723` olduğunda: `clear_rows`, sonra `add_row` ile `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Bunu, tek satırlı belgeler için etkin olan toplam üzerinden eşleştirme kuralıyla eşleştirin.

**Bir tedarikçiyi alt organizasyona yönlendir** — belge özniteliği `sub_org_id`, sadece `header.supplier_id` `[…]` listesindeyse: `set_value` `<alt organizasyon id>`.

## Sorun Giderme

| Belirti                                                    | Kontrol Edilecekler                                                                                                                                                                              |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kural hiçbir şeyi değiştirmedi                           | Aktif mi? Belge türü uyuyor mu? Koşul bu belge için doğru mu (boşluklar dahil tam değeri karşılaştırın)? Belgeye zaten **Bir kez çalıştır** kuralı uygulanmış mı? |
| Değer her kayıtta tekrar değişiyor                      | Boru hattında `substring`, `regex_replace` veya `regex_extract` var. **Bir kez çalıştır** açın veya ifadeyi idempotent yapın.                                                              |
| Satın alma siparişi eşleşmesi kaydedildikten sonra kayboluyor              | Bir tablo kuralı eşleşmiş satırları değiştirdi. Belgedeki neden kuralı gösterir; kuralı aynı satırları üretecek şekilde yapın veya **Bir kez çalıştır** olarak ayarlayın.                                        |
| Dönüşümden sonra bir eşleştirme kuralı hiç çalışmıyor        | Kural satır sayısını değiştirdi; eşleştirme kuralının etkinleştirme koşulunu ayarlayın.                                                                                                |