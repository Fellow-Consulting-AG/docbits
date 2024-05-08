# Düzen Yöneticisi

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.46.24.png" alt=""><figcaption></figcaption></figure>

#### Genel Bakış

Düzen Yöneticisi, yöneticilere belge türlerinin düzenini görsel olarak yapılandırmalarını ve değiştirmelerini sağlayarak belge içindeki çeşitli veri alanları ve gruplar için özellikler belirlemelerine olanak tanır. Bu arayüz, çıkarım modellerinin ve manüel veri giriş noktalarının taranan veya Docbits'e yüklenen belgenin yapısıyla tam olarak hizalanmasını sağlar.

#### Ana Bileşenler

1. **Gruplar ve Alanlar**:
* **Gruplar**: Belge türü içinde ilgili alanları kategorize eden organizasyon birimleri (örneğin, Fatura Detayları, Ödeme Detayları). Bunlar genişletilebilir veya daraltılabilir ve gerçek belgedeki mantıksal gruplamayı yansıtmak üzere düzenlenebilir.
* **Alanlar**: Her grup içindeki bireysel veri noktaları (örneğin, Fatura Numarası, Ödeme Koşulları). Her alan, verinin nasıl yakalandığı, görüntülendiği ve işlendiği konusunda özelleştirilebilir.
2. **Özellikler Paneli**:
* Bu panel, seçilen alanın veya grubun özelliklerini gösterir ve ayrıntılı yapılandırmaya olanak tanır, örneğin:
* **Etiket**: Kullanıcı arayüzünde alan için görünür etiket.
* **Alan Adı**: Sistem içinde kullanılan teknik tanımlayıcı.
* **Yüzde Cinsinden Eleman Genişliği**: Alanın belge düzenine göre genişliğini belirler.
* **Sekme İndeksi**: Gezinme için sekmeler arasındaki sırayı kontrol eder.
* **Değişiklik Durumunda Komut Dosyasını Çalıştır**: Alan değeri değiştiğinde bir komut dosyasının çalıştırılıp çalıştırılmayacağı.
* **Etiketi Solda Göster**: Etiketin alanın solunda mı yoksa üstünde mi gösterileceğini belirler.
* **Metin Alanı mı**: Alanın metin alanı olup olmadığını belirtir, daha fazla metni içerecek şekilde.
* **Model Türünü Seç**: Bu alanın çıkarımını hangi model türünün ele alacağını seçme seçeneği.
* **Alan Uzunluğu**: Bu alanda kabul edilecek verinin maksimum uzunluğu.
* **Yasaklı Anahtar Kelimeler**: Alan içinde izin verilmeyen anahtar kelimeler.
3. **Şablon Önizleme**:
* Mevcut düzen yapılandırmasına dayanarak belgenin nasıl görüneceğini gerçek zamanlı olarak gösterir. Bu, düzenin gerçek belge yapısıyla eşleştiğinden emin olmada yardımcı olur ve belge işleme kurulumunu test etmek ve iyileştirmek için hayati öneme sahiptir.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
