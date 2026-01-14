# Ne Zaman

<figure><img src="../../../.gitbook/assets/docbits_workflow_4.png" alt="DocBits İş akışı 4"><figcaption></figcaption></figure>

#### İş Akışı Yapılandırmalarındaki "Ne Zaman"ın Anlaşılması

**"Ne Zaman"ın Amacı**

* Bir iş akışı yapılandırmasındaki "Ne Zaman" bölümü, belirli bir iş akışı eylemini başlatan tetikleme koşullarını tanımlar. Bu koşullar, ERP sistemi içinde belirtilen belge özellikleri veya kullanıcı etkinlikleri ile ilgili belirli kriterlere dayanmaktadır.

**Nasıl Çalışır**

* Arayüzünüzde, "Ne Zaman" kullanıcıların farklı tetikleme kartlarını seçebileceği bir başlangıç noktası gibi görünmektedir. Her kart, ardışık eylemlerin (genellikle "Eylem" olarak etiketlenmiş başka bir bölümde tanımlanan) hangi koşullar altında yürütüleceğini belirtir.

**Belge Türü Koşul Kartları**

* Ekran görüntüsünde görünen kartlar, işlenen belgenin türüne bağlı olarak iş akışlarını tetiklemek için kullanılan "Belge Türü" koşullarının çeşitleridir. Gösterilen her tür koşul kartının ayrıntıları şöyle:
* **Belge türü (Operatör) biri (Tür)**: Bu kart, bir belgenin türünün listedeki belirtilen türlerden biriyle eşleştiğinde bir eylemi tetikler. Operatör, "şu" veya "değil" gibi seçenekler içerebilir, bu da dahil edici veya hariç tutucu koşullara olanak tanır.
* **Belge türü (Operatör) (Tür)**: Bu daha basit varyant, tek bir belge türü koşuluna dayalı olarak tetiklenir. Genellikle belge türünün belirli bir tür olup olmadığını kontrol eder ve birden fazla tür arasından seçim yapma seçeneği sunmaz.

#### Bir "Ne Zaman" Tetik Kartı Kurulumu

1. **Koşul Türünün Seçimi**: Kullanıcılar, otomatikleştirmek istedikleri iş akışıyla ilgili olan bir koşul türünü seçerek başlarlar. Bu durumda, belge türleri odak noktasıdır.
2. **Operatörün Tanımlanması**: Kullanıcılar, gerçek belge türlerini tanımlanan koşullarla karşılaştırmak için temel oluşturan "şu" veya "değil" gibi mantıksal operatörü belirlemelidir.
3. **Belge Türlerinin Belirtilmesi**: Kartın türüne bağlı olarak, kullanıcılar işlenen belgelerin bu türlerinden hangilerinin iş akışını tetikleyeceğini seçebilirler.
4. **Tetikleyiciyi Tamamlama**: Koşul ayarlandıktan sonra, bu, iş akışında tanımlanan belirli eylemleri tetikleme temeli haline gelir. Bir belge belirli bir koşulu karşılarsa, tanımlanan eylemler otomatik olarak başlatılacaktır.

#### Pratik Uygulama

Uygulamada, bu tetik kartları, onayları, bildirimleri veya ele alınan belgenin türüne bağlı olan herhangi bir prosedürü otomatikleştirmek için hayati öneme sahiptir. Örneğin, bir belge türü "Fatura" ise ve "Ne Zaman" kartında belirlenen koşullara uyuşuyorsa, iş akışı belgeyi ödeme işlemi için otomatik olarak yönlendirebilir.

Bu kurulum, iş akışlarının sadece verimli olmasını değil, aynı zamanda organizasyonun belge yönetiminde manuel denetimi azaltarak işletmenin belirli operasyonel ihtiyaçlarına özgü olarak uyarlanmasını sağlar ve belge işleme süreçlerini hızlandırır.

Özetle, iş akışı yapılandırmanızın "Ne Zaman" kısmı, belirli, önceden tanımlanmış koşullara dayalı olarak otomatik eylemler için sahneyi belirleme hakkında bir araçtır. İşletmenin ihtiyaçlarına dinamik olarak tepki veren ERP sisteminizin hem verimliliğini hem de belge yönetiminde doğruluğunu artırmak için güçlü bir araçtır.
