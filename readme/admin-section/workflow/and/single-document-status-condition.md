# Tek Belgeli Belge Durumu Koşulu

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, belirli bir belge durumuna dayalı olarak belgeler üzerindeki işlemleri yönetmek için özelleştirilmiştir. Koşulu bir duruma indirgeyerek, kart çok belirli iş akışı tetikleyicilere odaklanır ve ERP sistemi içinde hedeflenen belge işleme faaliyetleri için ideal hale gelir.

**Kartın Bileşenleri**

1. **Operatör**
* **Açıklama**: Belgenin durumunu seçilen koşula karşı değerlendirmek için yöntemi belirtir.
* **Seçenekler**:
* **is**: Belgenin mevcut durumu seçilen durumla eşleşirse işlemi tetikler.
* **is not**: Belgenin mevcut durumu seçilen durumla eşleşmiyorsa işlemi tetikler.
2. **Durum**
* **Açıklama**: Koşulu belirlemek için tek bir belge durumunun seçilmesine izin verir.
* **Durum Örnekleri**: "Hata", "Dışa Aktarma Hatası", "Doğrulamada Hazır", "İncelemede Hazır", "Onay Bekliyor", "İkinci Onay Bekliyor".
* **Detay**: Kullanıcılar açılır menüden veya dizi radyo düğmesinden bir durum seçer. Bu durum daha sonra kartın işlemi için kriter olarak hizmet eder.

**İşlevsellik**

* **Belge Durumu Tanımlama**: ERP sistemi üzerinden işlenirken bir belgenin mevcut durumunu tanımlar.
* **Koşul Değerlendirme**:
* Seçilen operatöre bağlı olarak (`is` veya `is not`), kart belgenin mevcut durumunun seçilen durum kriteriyle uyumlu olup olmadığını kontrol eder.
* **İşlem Yürütme**:
* **Doğru Koşul**: Durum eşleşirse (veya operatöre bağlı olarak eşleşmiyorsa), ilgili işlem başlatılır. Bu, daha fazla işleme yönlendirme, bildirim oluşturma veya diğer önceden tanımlanmış iş akışları olabilir.
* **Yanlış Koşul**: Koşul karşılanmazsa, hiçbir işlem yapılmaz veya alternatif bir yol tetiklenir.
* **Diğer İş Akışlarıyla Entegrasyon**: Tek durum değerlendirmesi için tasarlanmış olsa da, bu kart daha geniş iş akışı dizilerine etkili bir şekilde entegre edilebilir ve belgelerin hassas işlenmesini sağlamak için kullanılabilir.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, bir operatör seçerek ve ardından mevcut seçeneklerden bir durumu seçerek kartı kurar. Bu seçim süreci açıktır ve karışıklığı önlemek amacıyla tasarlanmıştır.
* **İzleme ve Raporlama**: Belgelerin durumlarına göre işlenmesini izleyen sistem tarafından oluşturulan raporlar veya panolar aracılığıyla izleme imkanı sağlar ve uygulanan iş akışlarının etkinliğini denetlemeye yardımcı olur.
* **Hata İşleme ve Bildirimler**: İşleme anormalliklerini kullanıcılara bildirmek veya belirlenen koşulları karşılamayan belgeleri işaretlemek için yapılandırılabilir, böylece hızlı dikkat ve çözüm sağlanır.

#### Sonuç

"Tek Belgeli Belge Durumu Koşulu" iş akışı kartı, belge yönetimini bireysel durum koşullarına odaklanarak basitleştirir. Bu özellik, belge akışları üzerinde kesin kontrol gerektiren durumlarda, özellikle katı işleme kriterlerine sahip ortamlarda yardımcı olur. Bu kartın bu sürümünün açık bir şekilde belgelenmesi, kullanıcıların uygulamasını tam olarak anlamasını sağlar ve günlük operasyonlarına etkin bir şekilde entegre etmelerine yardımcı olarak belge işleme alanında hem uyumluluğu hem de verimliliği artırır.
