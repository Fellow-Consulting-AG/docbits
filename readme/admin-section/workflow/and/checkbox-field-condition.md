# Onay Kutusu Alanı Koşulu

<figure><img src="../../../.gitbook/assets/userlmn_b689c7ce31284b4635be85f674a90917.png" alt=""><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, ERP sisteminizdeki bir onay kutusunun durumuna (işaretli veya işaretli değil) bağlı olarak eylemleri otomatikleştirmek için tasarlanmıştır. Onay kutusunun durumunu değerlendirerek belirli süreçlerin tetiklenmesini veya uygulama içinde belirli kuralların uygulanmasını kolaylaştırır.

**Kartın Bileşenleri**

1. **Alan Adı**
* **Açıklama**: Değerlendirilecek onay kutusu alanının adını belirtir.
* **Detay**: Bu, sistemde kullanılan tam alan etiketi veya tanımlayıcıyla eşleşmelidir. Hangi onay kutusunun durumunun izlendiğini belirler.
2. **Boolean**
* **Açıklama**: İş akışını tetikleyen koşulu tanımlar.
* **Seçenekler**:
* **True**: Onay kutusu işaretli ise iş akışı tetiklenir.
* **False**: Onay kutusu işaretli değilse iş akışı tetiklenir.

**İşlevsellik**

* **Durum Tespiti**: Kart, belirtilen onay kutusu alanının durumunu sürekli olarak izler.
* **Koşul Değerlendirmesi**:
* Sistem, Boolean koşulu tarafından belirtilen durumda (işaretli veya işaretli değil) onay kutusunun olup olmadığını kontrol eder.
* **Eylem Yürütme**:
* **True Koşulu**: Eğer onay kutusunun durumu belirtilen Boolean koşuluyla eşleşirse (ya işaretli ise true ya da işaretli değilse false), sistem ilişkili eylemleri başlatır. Bunlar, form alanlarını etkinleştirme veya devre dışı bırakma, bildirimleri tetikleme, iş akışlarını başlatma veya kayıtları güncelleme gibi şeyleri içerebilir.
* **False Koşulu**: Eğer onay kutusunun durumu koşulla eşleşmiyorsa, iş akışı kurulumuna bağlı olarak alternatif veya hiçbir eylem alınmayabilir.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, mevcut alanların listesinden onay kutusu alanını seçerek ve Boolean koşulunu ayarlayarak kartı yapılandırır. Bu kurulum süreci genellikle alan seçimi için basit bir açılır menü ve Boolean koşulu için bir geçiş içerir.
* **İzleme ve Raporlama**: Kullanıcılara, bu koşulun durumunu izlemeleri için işlevsellik sağlar, muhtemelen hangi koşulların etkin veya tetiklendiğini gerçek zamanlı olarak gösteren bir panelden.
* **Hata İşleme ve Bildirimler**: Kullanıcıların, onay kutusu durumunu okuma işleminde herhangi bir uyumsuzluk veya hata olması durumunda bildirim almasını sağlar.

#### Sonuç

"Onay Kutusu Alanı Koşulu" iş akışı kartı, kullanıcı girişlerinin sonraki veri işlemlerini belirleyebileceği bir ERP sistemi içinde dinamik formları ve belgeleri yönetmek için temel bir araçtır. Bir onay kutusunun durumuna bağlı olarak eylemleri otomatikleştirerek, bu kart iş akışı verimliliğini artırır ve sistem davranışlarının kullanıcı girişleriyle uyumlu olmasını sağlar. Bu kartın açık belgeleri, kullanıcıların işlemlerinde etkili bir şekilde uygulamalarına yardımcı olacak, form davranışları ve işlem otomasyonları üzerinde daha iyi kontrol sağlayacaktır.
