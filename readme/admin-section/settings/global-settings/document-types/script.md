# Script

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.43.25.png" alt=""><figcaption></figcaption></figure>

#### Genel Bakış

DocBits'teki betikler genellikle sistem Python tarafından desteklenen bir betik dilinde yazılır. Bunlar, verinin daha fazla işlenmeden veya depolanmadan önce karmaşık iş mantığı uygulamak veya veri bütünlüğünü ve doğruluğunu sağlamak için belge işleme iş akışı sırasında tetiklenir.

#### Temel Özellikler ve Seçenekler

1. **Betik Yönetimi**:
* **Ad**: Her betiğe tanımlama için benzersiz bir ad verilir.
* **Belge Türü**: Betiği belirli bir belge türüyle ilişkilendirir ve betiğin uygulanacağı belgeleri belirler.
* **Tetikleme Zamanı**: Betiğin ne zaman tetiklendiğini tanımlar (örneğin, belge yükleme sırasında, veri dışa aktarımından önce, veri doğrulamasından sonra).
* **Aktif/Pasif Durum**: Yöneticilerin betikleri silmeden etkinleştirip devre dışı bırakmasına olanak tanır, test etme ve dağıtma esnekliği sağlar.
2. **Betik Düzenleyici**:
* Betiklerin yazılabileceği ve düzenlenebileceği bir arayüz sağlar. Düzenleyici genellikle sözdizimi vurgulama, hata vurgulama ve betik geliştirmede yardımcı olacak diğer özellikleri destekler.
* **Örnek Betik**: Betikler, fatura satırlarında döngü yaparak toplamları doğrulamak veya belirli kriterleri karşılamayan girişleri kaldırmak gibi işlemleri içerebilir.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.43.37.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2498" %}
