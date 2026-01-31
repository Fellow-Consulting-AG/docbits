# ZUGFeRD Yapılandırması

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Fatura Eğitimi: XRechnung / ZUGFeRD (Factur-X) İşleme, Verileri Doğrulama ve İş Akışlarını Otomatikleştirme
{% endembed %}

## **Desteklenen ZUGFeRD Sürümleri**

DocBits, aşağıdakiler dahil tüm önemli ZUGFeRD sürümlerini destekler:

* **1.0**
* **2.0**
* **2.1** (FACTUR-X 1.0.05 ile uyumlu)
* **2.2**
* **2.3** (FACTUR-X 1.07.2 ile uyumlu)
* **2.3.2**

#### Standart Etkinleştirme ve Değiştirme

ZUGFeRD standardı varsayılan olarak her zaman etkindir, ancak gerekirse üzerinde değişiklik yapabilirsiniz.

### **ZUGFeRD Ayarlarını Değiştirme Adımları:**

1. **Ayarlar → Genel Ayarlar → Belge Türleri → Fatura** bölümüne gidin.
2. **E-Doc** üzerine tıklayın.
    
    <figure><img src="../../../../../.gitbook/assets/zugferd_1.png" alt=""><figcaption></figcaption></figure>
3. Mevcut tüm e-belgelerin bir listesi görünecektir.
4. Değiştirmek istediğiniz **ZUGFeRD** sürümünü bulun.

    <figure><img src="../../../../../.gitbook/assets/zugferd_2.png" alt=""><figcaption></figcaption></figure>

## **Dönüşüm ve XML Yolu Yapılandırması:**

**Dönüşüm ayarlarında**, XML dosyası içindeki belirli bilgileri bulmak için yolu tanımlayabilir ve verilere erişimi kolaylaştıracak şekilde yeni bir yapıda kaydedebilirsiniz.
<mark style="color:red;">**Not**</mark>: Bu işlevi kullanırsanız, **Önizleme** ve **Çıkarma Yolu**'nda orijinal XML yollarını değil, yeni oluşturulan XML yollarını kullanmalısınız.

### **Dönüşüm Dosyasını Değiştirme Adımları:**

1. **Dönüşüm**'ü açın.
2. **Kalem simgesine** tıklayarak yeni bir taslak oluşturun.
3. Yeni oluşturulan taslağı seçin.
4. Ya yeni bir alan oluşturun ya da mevcut bir alanı değiştirin.
5. Veri çıkarma için istediğiniz yolu ayarlayın.
6. **Kaydet**'e tıklayın.

### Önemli Notlar:

* **Önizleme dosyası** yalnızca **FACTUR-X** için kullanılır, **ZUGFeRD** için kullanılmaz. ZUGFeRD orijinal **PDF**'yi kullanacaktır.

## Önizleme PDF Yapılandırması

**Önizleme PDF Yapılandırması**, belgenin kullanıcı tarafından okunabilir bir sürümünü oluşturmak için kullanılır. İhtiyaçlarınıza göre HTML ile özelleştirebilirsiniz.

### **Önizleme Dosyasını Değiştirme Adımları:**

1. **Önizleme**''yi açın.
2. **Kalem simgesine** tıklayarak yeni bir taslak oluşturun.
3. Yeni oluşturulan taslağı seçin.
4. Ya yeni bir alan oluşturun ya da mevcut bir alanı değiştirin.
5. Veri çıkarma için istediğiniz yolu ayarlayın.
6. **Kaydet**'e tıklayın.

## Çıkarma Yolları Yapılandırması

**Çıkarma Yolları Yapılandırması**, verileri çıkarmak ve fatura tablosu veya fatura düzeninde yapılandırılan alanlar gibi **doğrulama ekranındaki** alanları doldurmak için kullanılır.

### **Çıkarma Yollarını Değiştirme Adımları:**

1. **Çıkarma Yolları**'nı açın.
2. **Kalem simgesine** tıklayarak yeni bir taslak oluşturun.
3. Yeni oluşturulan taslağı seçin.
4. Yeni bir alan oluşturun veya mevcut bir alanı değiştirin.
5. Sol taraf, **Ayarlar → Genel Ayarlar → Belge Türleri → Fatura → Alanlar** bölümünde bulunabilen **DocBits alan kimliğini** temsil eder.

    <figure><img src="../../../../../.gitbook/assets/zugferd_3.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/zugferd_4.png" alt=""><figcaption></figcaption></figure>
6. Sağ taraf, Dönüşümde oluşturulan **alanın yolunu** temsil eder.
7. **Kaydet**'e tıklayın.

Bu adımları izleyerek, ZUGFeRD faturaları için doğru veri çıkarımı ve doğrulama sağlayabilirsiniz.
