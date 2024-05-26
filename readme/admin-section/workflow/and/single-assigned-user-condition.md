# Tek Atanmış Kullanıcı Koşulu

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, bir görevin veya belgenin belirli bir kullanıcıya atanmasına dayalı işlemleri kolaylaştırır. Doğrudan koşullu mantık yaklaşımını kullanarak, hedeflenen kullanıcı etkileşimini gerektiren iş akışlarını yönetir ve kullanıcı tabanlı görev işleme konusunda hassasiyet sağlar.

**Kartın Bileşenleri**

1. **Operatör**
* **Açıklama**: Kullanıcı atamasına uygulanacak mantığı belirler.
* **Seçenekler**:
* **IS**: Belgenin veya görevin atanmış kullanıcısı belirtilen kullanıcıyla eşleşirse işlemi tetikler.
* **IS NOT**: Atanmış kullanıcı belirtilen kullanıcıyla eşleşmiyorsa işlemi tetikler.
2. **Kullanıcı**
* **Açıklama**: Atanmış kullanıcının karşılaştırılacağı tek bir kullanıcının seçilmesine izin verir.
* **Detay**: Bu, bir kullanıcının her seferinde seçilebileceği basit bir açılır menü veya otomatik tamamlama alanını içerir.

**İşlevsellik**

* **Kullanıcı Atama Tanımlaması**: Belirli bir göreve veya belgeye şu anda atanmış olan kullanıcıyı tanımlar.
* **Koşul Değerlendirmesi**:
* **IS** operatörü için, kart atanmış kullanıcının seçilen kullanıcıyla aynı olup olmadığını kontrol eder.
* **IS NOT** operatörü için, atanmış kullanıcının seçilen kullanıcıdan farklı olup olmadığını doğrular.
* **Eylem Yürütme**:
* **Doğru Koşul**: Atama belirtilen koşulu karşılarsa (IS veya IS NOT), önceden tanımlanmış eylemleri tetikler; bu eylemler onay sürecine devam etmeyi, ek görevler başlatmayı, bildirimler göndermeyi veya diğer ilgili iş akışlarını içerebilir.
* **Yanlış Koşul**: Koşul başarısız olursa, sistem görevi yeniden yönlendirebilir, inceleme için bekletebilir veya alternatif önceden tanımlanmış eylemleri tetikleyebilir.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, bir operatör seçerek ve kullanıcı alanından bir kullanıcı seçerek kartı yapılandırır. Bu kurulumun basit olması, kullanıcı seçimini ve yapılandırmayı kolaylaştırarak sağlanmalıdır.
* **İzleme ve Raporlama**: Belirli kullanıcı atamaları tarafından tetiklenen görevleri takip etme ve bu tetiklemelerin sonuçlarını izleme gibi kartın performansını izlemek için araçlar sunar.
* **Hata İşleme ve Bildirimler**: Görevlerin yanlış şekilde atanması veya atama sorunları nedeniyle operasyonel hataların meydana gelmesi durumunda kullanıcıları uyaracak mekanizmalar sağlar.

#### Sonuç

"Tek Atanmış Kullanıcı Koşulu" iş akışı kartı, bir ERP sistemi içinde hassas, kullanıcıya özgü belge ve görev yönetimi için önemlidir. Bireysel kullanıcı atamalarına odaklanarak iş akışlarını basitleştirir ve eylemlerin yalnızca kullanıcının rolüne ve sorumluluklarına uygun olduğunda gerçekleştirilmesini sağlar. Bu kartın açık bir şekilde belgelenmesi, kullanıcıların uygulamasını anlamalarına yardımcı olacak ve günlük operasyonlarında etkili bir şekilde yönetmelerine olanak tanıyacaktır. Bu belgeleme, tüm potansiyel kullanıcıların kartın amacını kolayca kavramalarını ve iş akışlarına sorunsuz bir şekilde entegre etmelerini sağlar.
