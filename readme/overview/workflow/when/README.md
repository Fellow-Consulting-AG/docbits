# Ne Zaman

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-04 um 16.25.45.png" alt=""><figcaption></figcaption></figure>

#### İş Akışı Yapılandırmalarındaki "Ne Zaman"ın Anlaşılması

**"Ne Zaman"ın Amacı**

* Bir iş akışı yapılandırmasındaki "Ne Zaman" bölümü, belirli bir iş akışı eylemini başlatan tetikleme koşullarını tanımlar. Bu koşullar, ERP sistemi içinde belirtilen belge özellikleri veya kullanıcı etkinlikleri ile ilgili belirli kriterlere dayanmaktadır.

**Nasıl Çalışır**

* Arayüzünüzde, "Ne Zaman" kullanıcıların farklı tetikleyici kartlar seçebileceği bir başlangıç noktası gibi görünmektedir. Her kart, ardışık eylemlerin (muhtemelen "Eylem" olarak etiketlenmiş başka bir bölümde tanımlanan) hangi koşullar altında yürütüleceğini belirtir.

**Belge Türü Koşul Kartları**

* Ekran görüntüsünde görünen kartlar, işlenen belgenin türüne bağlı olarak iş akışlarını tetiklemek için kullanılan "Belge Türü" koşullarının çeşitleridir. Gösterilen her tür koşul kartının ayrıntıları şöyle:
* **Belge türü (Operatör) biri (Tür)**: Bu kart, bir belgenin türünün belirtilen listedeki türlerden biriyle eşleştiğinde bir eylemi tetikler. Operatör, "şu türdür" veya "şu türde değildir" gibi seçenekler içerebilir, kapsayıcı veya dışlayıcı koşullara izin verir.
* **Belge türü (Operatör) (Tür)**: Bu daha basit varyant, tek bir belge türü koşuluna dayalı olarak tetiklenir. Genellikle belge türünün belirli bir tür olup olmadığını kontrol eder, birden fazla tür arasından seçim yapma seçeneği olmadan.

#### Bir "Ne Zaman" Tetik Kartı Kurma

1. **Koşul Türünün Seçimi**: Kullanıcılar, otomatikleştirmek istedikleri iş akışıyla ilgili olan bir koşul türünü seçerek başlarlar. Bu durumda, belge türleri odak noktasıdır.
2. **Operatörün Tanımlanması**: Kullanıcılar, gerçek belge türlerini tanımlanan koşullara karşı karşılaştırmak için temel oluşturan "şu türdedir" veya "şu türde değildir" gibi mantıksal operatörü belirlemelidir.
3. **Belge Türlerinin Belirtilmesi**: Kartın türüne bağlı olarak, kullanıcılar işlenen belgelerin bu türlerden birini veya birkaçını seçebilir ve iş akışının bu belge türlerini işlediğinde tetiklenecektir.
4. **Tetikleyiciyi Tamamlama**: Koşul kurulduğunda, bu, iş akışında tanımlanan belirli eylemleri tetiklemek için temel olur. Bir belge belirli bir koşulu karşılarsa, tanımlanan eylemler otomatik olarak başlatılacaktır.

#### Pratik Uygulama

Uygulamada, bu tetik kartları onayları, bildirimleri veya ele alınan belgenin türüne bağlı olan herhangi bir prosedürü otomatikleştirmek için hayati öneme sahiptir. Örneğin, bir belge türü "Fatura" ise ve "Ne Zaman" kartında belirlenen koşullara uyuşuyorsa, iş akışı belgeyi ödeme işlemi için otomatik olarak yönlendirebilir.

Bu kurulum, iş akışlarının sadece verimli olmasını değil, aynı zamanda organizasyonun belirli işletme ihtiyaçlarına uygun olmasını sağlayarak manuel denetimi azaltır ve belge işleme süreçlerini hızlandırır.

Özetle, iş akışı yapılandırmanızdaki "Ne Zaman" kısmı, belirli, önceden tanımlanmış koşullara dayalı olarak otomatik eylemler için sahneyi ayarlamakla ilgilidir. Bu, ERP sisteminizin işletmenin ihtiyaçlarına dinamik olarak tepki vermesini sağlayan güçlü bir araçtır, belge yönetiminde hem verimliliği hem de doğruluğu artırır.
