# Düzen Yöneticisi

<figure><img src="../../../../.gitbook/assets/docbits_layout_manager_overview.png" alt="Docbits Layout Manager Overview"><figcaption></figcaption></figure>

#### Genel Bakış

Düzen Yöneticisi, yöneticilere belge türlerinin düzenini görsel olarak yapılandırmalarını ve değiştirmelerini sağlar. Belgeye tarandığında veya DocBits'a yüklendiğinde çeşitli veri alanları ve gruplar için özellikler belirleyerek çıkarma modellerinin ve manüel veri giriş noktalarının belgenin yapısıyla tam olarak hizalanmasına yardımcı olur.

#### Ana Bileşenler

1. **Gruplar ve Alanlar**:
* **Gruplar**: Belge türü içinde ilgili alanları kategorize eden organizasyon birimleri (örneğin, Fatura Detayları, Ödeme Detayları). Bunlar genişletilebilir veya daraltılabilir ve gerçek belgedeki mantıksal gruplamayı yansıtmak üzere düzenlenebilir.
* **Alanlar**: Her gruptaki bireysel veri noktaları (örneğin, Fatura Numarası, Ödeme Koşulları). Her alan, verinin nasıl yakalandığı, görüntülendiği ve işlendiği için özelleştirilebilir.
2. **Özellikler Paneli**:
* Bu panel, seçilen alanın veya grubun özelliklerini gösterir ve ayrıntılı yapılandırmaya olanak tanır, örneğin:
* **Etiket**: Kullanıcı arayüzünde alan için görünür etiket.
* **Alan Adı**: Sistem içinde kullanılan teknik tanımlayıcı.
* **Yüzde Cinsinden Eleman Genişliği**: Alanın belge düzenine göre genişliğini belirler.
* **Sekme İndeksi**: Gezinme için sekmelerin sırasını kontrol eder.
* **Değişiklik Durumunda Komut Dosyası Çalıştır**: Alan değeri değiştiğinde bir komut dosyasının yürütülüp yürütülmeyeceği.
* **Etiketi Sola Al**: Etiketin alanın solunda mı yoksa üstünde mi görüntülendiğini belirler.
* **Metin Alanı mı**: Alanın daha fazla metni içerecek şekilde bir metin alanı olup olmadığını belirtir.
* **Model Türünü Seç**: Bu alanın çıkarımını hangi model türünün yapacağını seçme seçeneği.
* **Alan Uzunluğu**: Bu alanda kabul edilecek verinin maksimum uzunluğu.
* **Yasaklı Anahtar Kelimeler**: Alan içinde izin verilmeyen anahtar kelimeler.
3. **Şablon Önizleme**:
* Mevcut düzen yapılandırmasına dayanarak belgenin nasıl görüneceğini gerçek zamanlı olarak gösterir. Bu, düzenin gerçek belge yapısıyla eşleştiğinden emin olmada yardımcı olur ve belge işleme kurulumunu test etmek ve iyileştirmek için hayati önem taşır.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
