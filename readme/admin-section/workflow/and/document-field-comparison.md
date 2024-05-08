# Belge Alanı Karşılaştırması

<figure><img src="../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, belgedeki belirli iki alanın değerlerini tanımlanan bir operatöre göre otomatik olarak karşılaştırmak için tasarlanmıştır. Veri bütünlüğünü sağlamak ve belge verilerinin iş kurallarına veya koşullara uygun olup olmadığını garanti etmek için kullanılır.

**Kartın Bileşenleri**

1. **Alan Adları**
* **Açıklama**: Karşılaştırılacak belgedeki iki alanın adlarını belirtir.
* **Detay**: Kullanıcılar, alanların sistemde göründüğü gibi tam adlarını girmelidir. Bu alanlar, karşılaştırmayı destekleyen herhangi bir veri türü olabilir, örneğin sayısal, tarih veya metin alanları.
2. **Operatör**
* **Açıklama**: İki alanın değerleri arasındaki ilişkiyi değerlendirmek için kullanılan karşılaştırma operatörü.
* **Seçenekler**:
* **Eşit (==)**: İlk alanın değerinin ikinci alanın değerine eşit olup olmadığını kontrol eder.
* **Eşit Değil (!=)**: İlk alanın değerinin ikinci alanın değerine eşit olmadığını kontrol eder.
* **Büyük (>)**: İlk alanın değerinin ikinci alanın değerinden büyük olup olmadığını kontrol eder.
* **Büyük veya Eşit (>=)**: İlk alanın değerinin ikinci alanın değerinden büyük veya eşit olup olmadığını kontrol eder.
* **Küçük (<)**: İlk alanın değerinin ikinci alanın değerinden küçük olup olmadığını kontrol eder.
* **Küçük veya Eşit (<=)**: İlk alanın değerinin ikinci alanın değerinden küçük veya eşit olup olmadığını kontrol eder.

**İşlevsellik**

* **Alan Seçimi**: Kullanıcılar, karşılaştırılacak iki alanın adlarını girmek veya seçmektedir. Bu genellikle kart kurulumu içinde bir form veya açılır menü aracılığıyla yapılır.
* **Operatör Seçimi**: Kullanıcılar, alanların nasıl karşılaştırılacağını tanımlayan mevcut seçenekler listesinden bir operatör seçer.
* **Karşılaştırma Yürütme**:
* Sistem, belirtilen alanlardan değerleri okur ve seçilen operatörü uygulayarak aralarındaki ilişkiyi değerlendirir.
* Karşılaştırmanın sonucuna bağlı olarak (doğru veya yanlış), ardışık eylemler tetiklenebilir. Örneğin, bir karşılaştırma başarısız olursa, sistem belgeyi gözden geçirmek, daha fazla işlemi engellemek veya sorumlu tarafları bilgilendirmek için işaretleyebilir.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, alan adlarını girerek ve bir operatör seçerek karşılaştırmayı yapılandırır. Bu kurulumun açık ve yönlendirici olması, muhtemelen yardım metni veya örneklerle desteklenmelidir.
* **İzleme ve Raporlama**: Sistem, karşılaştırmaların sonuçları hakkında geri bildirim sağlayabilir, yapılan tüm karşılaştırmaları, sonuçlarını ve karşılaştırma sonuçlarına verilen tepkileri kaydedebilir.
* **Hata İşleme ve Bildirimler**: Kullanıcılar, karşılaştırmanın gerçekleştirilemediği durumlarda (örneğin, alanlardan biri belgede bulunamaz veya karşılaştırılabilir bir formatta değilse) uyarılar alır.

#### Sonuç

"Belge Alanı Karşılaştırması" iş akışı kartı, bir ERP sisteminde belgeler arasında veri doğruluğunu ve tutarlılığını korumak için hayati öneme sahiptir. Aksi takdirde manuel, hata yapma eğiliminde olan ve zaman alan kontrolleri otomatikleştirmeye yardımcı olur, belge işleme sürecinde verimliliği ve güvenilirliği artırır. Bu kartın ERP sisteminizin kılavuzunda açık bir şekilde belgelenmesi, kullanıcıların bu özelliği etkili bir şekilde kullanmalarına yardımcı olacak, belgeler arasındaki verinin tutarlı kalmasını ve iş kurallarına uygun olmasını sağlayacaktır.
