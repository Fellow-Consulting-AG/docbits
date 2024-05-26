# Belge Türü İşlemi biri

<figure><img src="../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt=""><figcaption></figcaption></figure>

**Amaç**

Bu kart, belge türlerine bağlı olarak işlemleri yönetmek için tasarlanmış olup, basit koşullu mantık (ise/değilse) kullanarak belirli iş akışlarını tetiklemek veya engellemektedir. Bu, ERP sistemi içinde farklı belge türlerinin nasıl işlendiği üzerinde hassas kontrol sağlar.

**Kartın Bileşenleri**

1. **Operatör**
* **Açıklama**: Belge türlerine uygulanan koşullu mantığı belirler.
* **Seçenekler**:
* **ise**: İşlem, belgenin türü belirtilen türlerden biriyle eşleşirse tetiklenecektir.
* **değilse**: İşlem, belgenin türü listedeki türlerden hiçbiriyle eşleşmiyorsa tetiklenecektir.
2. **Belge Türleri Listesi**
* **Açıklama**: Koşulun uygulanacağı belge türlerinin bir listesini belirtir.
* **Detay**: Bu, "Fatura", "Satın Alma Siparişi", "Sözleşme", "Çalışan Kaydı" gibi çeşitli belge türlerini içerebilir ve koşul (ise/değilse) bu türlere göre değerlendirilecektir.

**İşlevsellik**

* **Belge Tanımlama**: Sistem, her gelen veya mevcut belgenin türünü önceden belirlenmiş öznitelikler veya meta verilere dayanarak tanımlar.
* **Koşul Değerlendirmesi**:
* Eğer operatör **ise** ise, kart belge türünün sağlanan listede olup olmadığını kontrol eder.
* Eğer operatör **değilse** ise, kart belge türünün listede olmadığını kontrol eder.
* **İşlem Tetikleme**: Koşul değerlendirmesinin sonucuna bağlı olarak:
* **Doğru**: Koşul karşılanırsa ilişkili işlemleri veya iş akışlarını başlatır.
* **Yanlış**: Koşul karşılanmazsa işlem atlanır veya alternatif bir işlem tetiklenir.
* **Entegrasyon ve Otomasyon**: Diğer sistem bileşenleriyle sorunsuz entegre olur, belge işleme işlemlerinin otomatikleştirilmesini ve kurumsal iş akışlarına ve politikalarına uyulmasını sağlar.

**Kullanıcı Etkileşimleri**

* **Yapılandırma**: Kullanıcılar kartı kurarken operatörü belirtmeli ve belge türlerini listeleyerek belirtmelidir. Bu kurulum, belge türlerini ve operatörleri seçmek için açılır menüler veya onay kutuları gibi arayüz elemanlarını içerebilir.
* **İzleme ve Ayarlar**: Kullanıcılar, bu kartın sonuçlarını ve etkinliğini ERP sistemi tarafından oluşturulan günlükler ve raporlar aracılığıyla izleyebilir. İş gereksinimlerinin gelişimine bağlı olarak liste veya operatör üzerinde ayarlamalar yapılabilir.
* **Hata İşleme ve Geri Bildirim**: İşlem sırasında karşılaşılan hatalar için geri bildirim mekanizmaları sağlar. Kullanıcılar, koşullar başarısız olduğunda uyarılar ayarlayabilir, böylece sorunlara hızlı bir şekilde dikkat edilir.

#### Sonuç

"Belge Türü Koşulu" iş akış kartı, belge tabanlı işlemleri hassaslık ve esneklikle yönetmede önemli bir rol oynamaktadır. Basit koşullu mantık kullanarak, belgelerin uygun şekilde işlenmesini sağlayarak verimliliği ve uyumu artırır. Bu kartın açık bir şekilde belgelenmesi, kullanıcıların bunu etkili bir şekilde uygulamayı ve kullanmayı anlamalarına yardımcı olur, bu da ERP sisteminizin belgelerinin değerli bir parçası haline gelmesini sağlar.
