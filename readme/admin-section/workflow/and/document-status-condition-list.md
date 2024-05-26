# Belge Durumu Koşul Listesi

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Amaç**

Bu kart, belgenin mevcut durumuna bağlı olarak iş akışı eylemlerini kontrol etmek için tasarlanmıştır, belirli süreçleri tetiklemek veya kısıtlamak için koşullu mantığı kullanır. Belgelerin önceden belirlenmiş durum kriterlerini karşıladığında yalnızca iş akışları boyunca ilerlemesini sağlar.

**Kartın Bileşenleri**

1. **Operatör**
* **Açıklama**: Belgenin durumunun belirli bir koşula karşı nasıl değerlendirileceğini belirler.
* **Seçenekler**:
* **is**: Belgenin mevcut durumu belirtilen durumlardan biriyle eşleşirse ilişkili eylemleri tetikler.
* **is not**: Belgenin durumu belirtilen durumlardan hiçbirine uymazsa eylemleri tetikler.
2. **Durum ( Liste )**&#x20;
* **Açıklama**: Belgenin mevcut durumunun karşılaştırılacağı belirli durumları listeler.
* **Örnekler**: "Hata", "Dışa Aktarma Hatası", "Doğrulamada Hazır", "İncelemede Hazır", "Onay Bekliyor", "İkinci Onay Bekliyor". Bu, bir belgenin iş akışı sürecinde olabileceği farklı aşamaları veya koşulları temsil eder.

**İşlevsellik**

* **Durum Tanımlama**: Belgenin mevcut durumunu ERP sisteminin iş akışı içinde ilerlerken otomatik olarak tanımlar.
* **Koşul Değerlendirmesi**: Seçilen operatörü (is veya is not) belgenin durumu ile listelenen durumlar karşılaştırılır:
* Eğer **is** ise, belgenin durumunun listedeki herhangi bir durumla eşleşip eşleşmediğini kontrol eder.
* Eğer **is not** ise, belgenin durumunun listede görünmediğini kontrol eder.
* **Eylem Yürütme**: Koşul değerlendirmesinin sonucuna bağlı olarak:
* **Doğru**: Koşul karşılandığında önceden tanımlanmış eylemleri veya iş akışlarını yürütür.
* **Yanlış**: Koşul karşılanmadığında iş akışlarını atlar veya alternatif iş akışlarını tetikler.
* **İş Akışı Entegrasyonu**: Diğer iş akışı bileşenleriyle sorunsuz entegre olur, belge işleme işleminin sistem genelinde koordine edilmesini sağlar.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, operatörü seçerek ve ilgili durumları belirterek kartı yapılandırır. Bu kurulum, durumları ve operatörleri seçmek için basit açılır menüler veya onay kutularını içerebilir.
* **İzleme ve Yönetim**: Kullanıcılar, durum koşullarının izlendiği ve bu koşullara dayalı olarak alınan eylemlerin içgörülerini sağlayan bir gösterge paneli aracılığıyla kartın etkinliğini takip edebilir.
* **Hata İşleme ve Uyarılar**: Beklenen belge durumlarındaki hatalar veya uyuşmazlıklar için uyarıların ayarlanmasını destekler, operasyonel sorunlara hızlı yanıtlar sağlar.

#### Sonuç

"Belge Durumu Koşul" iş akışı kartı, belgelerin mevcut durumlarına göre doğru bir şekilde işlenmesini sağlamak için hayati öneme sahiptir, ERP sistemi içinde kontrolü ve verimliliği artırır. Bu kartın sistem kılavuzunda açıkça belgelenmesi, kullanıcıların etkili bir şekilde uygulamasına ve yönetmesine yardımcı olacak, işleyişini sürdürmek ve uygun belge iş akışlarını sürdürmek için işlevselliğinden yararlanacaktır. Bu kart, belge yaşam döngülerini yönetmede özellikle yararlıdır ve yalnızca belirli kriterleri karşılayan belgelerin iş süreçlerinin sonraki aşamalarına ilerlemesini sağlar.
