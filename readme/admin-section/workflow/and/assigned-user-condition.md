# Atanmış Kullanıcı Koşulu

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, bir görevin veya belgenin belirli bir kullanıcıya veya kullanıcı grubuna atanıp atanmadığına bağlı olarak operasyonların yürütülmesini yönetir. Belirli eylemleri tetiklemek veya engellemek için koşullu mantık kullanır ve kullanıcıya özgü işlemler gerektiren iş akışları için idealdir.

**Kartın Bileşenleri**

1. **Operatör**
* **Açıklama**: Kullanıcı atamasına uygulanacak mantıksal koşulu tanımlar.
* **Seçenekler**:
* **IS**: Belgenin veya görevin atanmış kullanıcısı belirtilen listedeki herhangi bir kullanıcıyla eşleşiyorsa işlemi tetikler.
* **IS NOT**: Belgenin veya görevin atanmış kullanıcısı belirtilen listedeki hiçbir kullanıcıyla eşleşmiyorsa işlemi tetikler.
2. **Kullanıcı Listesi**
* **Açıklama**: Atanmış kullanıcı ile karşılaştırılacak kullanıcıların listesi veya seçimi.
* **Detay**: Bu liste, kartın tekil ve çoklu kullanıcı koşullarını etkili bir şekilde ele almasına izin vermek için bir veya birden fazla kullanıcı içerebilir. Seçim, onay kutuları, çoklu seçim açılır menüsü veya benzeri UI öğeleri aracılığıyla yapılabilir.

**İşlevsellik**

* **Kullanıcı Atama Tanımlama**: ERP sistemi içinde belirli bir göreve veya belgeye atanmış olan kullanıcıyı veya kullanıcıları otomatik olarak tanımlar.
* **Koşul Değerlendirmesi**:
* **IS** operatörünü kullanarak, kart atanmış kullanıcının Kullanıcı Listesinde listelenenler arasında olup olmadığını kontrol eder.
* **IS NOT** operatörünü kullanarak, kart atanmış kullanıcının listelenenler arasında olmadığından emin olur.
* **Eylem Yürütme**:
* **Doğru Koşul**: Kullanıcı ataması koşulu karşılanıyorsa (ya IS ya da IS NOT), bildirimler, görev başlatmaları, onaylar veya diğer iş akışı adımları gibi ilgili eylemler tetiklenir.
* **Yanlış Koşul**: Koşul karşılanmazsa, belge veya görev farklı yönlendirmelerden geçebilir veya alternatif eylemler belirtilebilir.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, bir operatör seçerek ve Kullanıcı Listesinden ilgili kullanıcıları belirleyerek kartı yapılandırır. Kurulum, potansiyel olarak büyük kullanıcı tabanlarından seçimleri kolayca yapabilmek için kullanıcı dostu ve sezgisel olmalıdır.
* **İzleme ve Raporlama**: ERP sistemi, bu kart tarafından tetiklenen operasyonları izlemek ve raporlamak için işlevsellik sağlamalı, atama doğruluğu ve işlem verimliliği hakkında içgörüler sunmalıdır.
* **Hata İşleme ve Bildirimler**: Kullanıcılar, atamalarda sorunlar olduğunda (atanmamış görevler veya kullanıcı seçiminde hatalar gibi) uyarılar veya bildirimler almak için seçeneklere sahip olmalıdır.

#### Sonuç

"Atanmış Kullanıcı Koşulu" iş akışı kartı, kullanıcı atamalarına bağlı belge ve görev iş akışlarını yönetmek için kritik bir araçtır. Belirli kullanıcılara göre görev veya belgenin atanıp atanmadığına bağlı koşullara izin vererek, iş akışlarının yalnızca uygun kullanıcı etkileşimleri tarafından tetiklenmesini sağlar, böylece ekip içinde hem sorumluluk hem de görev uyumunu artırır. Bu kartın açık bir şekilde belgelenmesi, kullanıcıların önemini anlamasına ve iş akışlarına etkin bir şekilde entegre etmelerine yardımcı olacak, kullanıcı rolleri ve sorumluluklarına uygun olarak düzenlenmiş sorunsuz ve verimli işlemleri sağlayacaktır.
