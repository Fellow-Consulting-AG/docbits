# Ne Zaman

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-04 um 16.25.45.png" alt=""><figcaption></figcaption></figure>

#### İş Akışı Yapılandırmalarındaki "Ne Zaman"ın Anlaşılması

**"Ne Zaman"ın Amacı**

* Bir iş akışı yapılandırmasındaki "Ne Zaman" bölümü, belirli bir iş akışı eylemini başlatan tetikleme koşullarını tanımlar. Bu koşullar, ERP sistemi içinde belirtilen belge özellikleri veya kullanıcı etkinlikleri ile ilgili belirli kriterlere dayanmaktadır.

**Nasıl Çalışır**

* Arayüzünüzde, "Ne Zaman" kullanıcıların farklı tetikleme kartlarını seçebileceği bir başlangıç noktası gibi görünmektedir. Her kart, ardışık eylemlerin (muhtemelen "Eylem" olarak etiketlenmiş başka bir bölümde tanımlanan) hangi koşullar altında yürütüleceğini belirtir.

**Belge Türü Koşul Kartları**

* Ekran görüntüsünde görünen kartlar, işlenen belgenin türüne göre iş akışlarını tetiklemek için kullanılan "Belge Türü" koşullarının çeşitleridir. Gösterilen her tür koşul kartının ayrıntıları şöyle:
* **Belge türü (Operatör) biri (Tür)**: Bu kart, bir belgenin türünün, listede belirtilen türlerden biriyle eşleştiğinde bir eylemi tetikler. Operatör, "şudur" veya "şu değildir" gibi seçenekler içerebilir, kapsayıcı veya dışlayıcı koşullara izin verir.
* **Belge türü (Operatör) (Tür)**: Bu daha basit varyant, tek bir belge türü koşuluna dayalı olarak tetiklenir. Genellikle belge türünün belirli bir tür olup olmadığını kontrol eder, birden fazla tür arasından seçim yapma seçeneği olmadan.

#### Bir "Ne Zaman" Tetikleme Kartı Kurulumu

1. **Koşul Türünün Seçimi**: Kullanıcılar, otomatikleştirmek istedikleri iş akışıyla ilgili olan bir koşul türünü seçerek başlarlar. Bu durumda, odak noktası belge türleridir.
2. **Operatörün Tanımlanması**: Kullanıcılar, gerçek belge türlerini belirlenen koşullara karşı karşılaştırmak için temel oluşturan "şudur" veya "şu değildir" gibi mantıksal operatörü belirlemelidir.
3. **Belge Türlerinin Belirtilmesi**: Kartın türüne bağlı olarak, kullanıcılar işlenen belgelerin bu türlerinden hangilerinin iş akışını tetikleyeceğini seçebilirler.
4. **Tetikleyiciyi Tamamlama**: Koşul ayarlandığında, bu, iş akışında tanımlanan belirli eylemleri tetikleme temeli haline gelir. Bir belge belirlenen koşulu karşılarsa, belirlenen eylemler otomatik olarak başlatılır.

#### Pratik Uygulama

Uygulamada, bu tetikleme kartları, onayları, bildirimleri veya belgenin işlenen türüne bağlı olan herhangi bir prosedürü otomatikleştirmek için hayati öneme sahiptir. Örneğin, bir belge türü "Fatura" ise ve "Ne Zaman" kartında belirlenen koşullara uyuşuyorsa, iş akışı belgeyi ödeme işlemi için otomatik olarak yönlendirebilir.

Bu kurulum, iş akışlarının sadece verimli olmasını değil, aynı zamanda organizasyonun belge yönetiminde manuel denetimi azaltarak işletmenin belirli operasyonel ihtiyaçlarına uyarlanmasını sağlar ve belge işleme süreçlerini hızlandırır.

Özetle, iş akışı yapılandırmanızın "Ne Zaman" kısmı, belirli, önceden tanımlanmış koşullara dayalı olarak otomatik eylemler için sahneyi ayarlamakla ilgilidir. İşletmenin ihtiyaçlarına dinamik olarak tepki veren ERP sisteminizin hem verimliliğini hem de belge yönetiminde doğruluğunu artırmak için güçlü bir araçtır.
