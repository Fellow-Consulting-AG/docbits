# EDI

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.49.21.png" alt=""><figcaption></figcaption></figure>

#### Genel Bakış

Docbits'te, EDI ayarları, faturalar veya satın alma siparişleri gibi çeşitli belge türlerine karşılık gelen EDI mesajlarının yapısını ve formatını tanımlamak ve yönetmek için araçlar sağlar. Ayarlar, farklı ticaret ortakları ve endüstrilere özgü standartlara ve gereksinimlere uygun EDI mesajlarının özelleştirilmesini sağlar.

#### Temel Özellikler ve Seçenekler

1. **EDI Yapılandırma Unsurları**:
* **Yapı Tanımlayıcı**: EDI belgesinin temel yapısını tanımlar, segment sıralamasını, zorunlu alanları ve EDI belgesinin geçerli olması için gerekli nitelendiricileri içerir.
* **Dönüşüm**: Belge verilerini EDI biçimli bir mesaja dönüştürmek için uygulanan dönüşümleri belirtir. Genellikle belge alanlarından EDI segmentlerine ve unsurlarına eşlemeleri belirtmeyi içerir.
* **Önizleme**: Yöneticilere, dönüşümden sonra EDI mesajının nasıl görüneceğini görmelerine olanak tanır, iletim öncesi doğruluğu sağlamaya yardımcı olur.
* **Çıkarma Yolları**: Belgeden değerleri çıkarmak için kullanılan yolları gösterir, bu değerler daha sonra EDI mesajını doldurmak için kullanılır.
2. **XSLT Düzenleyici**:
* Dönüşüm sürecinde kullanılan XSLT (eXtensible Stylesheet Language Transformations) düzenlemek ve doğrulamak için kullanılır. XSLT, XML belgelerini diğer XML belgelerine veya HTML, metin veya hatta diğer XML yapıları gibi diğer biçimlere dönüştürmek için tasarlanmış güçlü bir dildir.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.49.59.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2499" %}
