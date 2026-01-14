# Karar Ağaçları

## Genel Bakış

Karar Ağaçları, önceden tanımlanmış kurallara dayalı otomatik yönlendirme ve karar verme sürecine izin veren güçlü bir özelliktir. Bu özellik, fiyatları atama, miktarları belirleme veya belgeleri yönlendirme gibi doğru eylemin belirlenmesi için çeşitli koşulların değerlendirilmesi gereken karmaşık ortamlarda özellikle yararlıdır.

#### Temel Bileşenler

* **Karar Ağacı Listesi**: Mevcut tüm karar ağaçlarının listelendiği ana arayüzdür. Her karar ağacı, `FATURA` veya `TEKLİF` gibi belirli bir belge türüyle ilişkilendirilebilir.
* **Karar Ağacı Tasarımcısı**: Bu arayüz, belirli koşullar karşılandığında alınacak kuralları, operatörleri ve eylemleri tanımlayabileceğiniz karar ağaçlarının oluşturulmasına ve düzenlenmesine olanak tanır.

## Karar Ağacı Arayüzü

#### Karar Ağacı Listesi

Karar Ağacı listesi mevcut tüm karar ağaçlarını görüntüler. Her girdi şunları gösterir:

* **Ad**: Karar ağacının adı.
* **Belge Türü**: Karar ağacıyla ilişkili belge türü (örneğin, `FATURA`, `TEKLİF`).

## Karar Ağacı Tasarımcısı

Karar Ağacı Tasarımcısı, kararların nasıl alınacağını yöneten kuralları yapılandırmanıza olanak tanır.

### **Karar Ağacı Tasarımcısının Bileşenleri**

* **Kurallar**: Her kural koşullar ve eylemlerden oluşur.
* **Kaynak Seç**: Bu açılır menü, değerlendirilecek kaynak alanı belirtmenize olanak tanır.
* **Operatör Seç**: Kaynak alana uygulanacak mantık operatörünü (örneğin, `<=`, `>=`, `=`, `!=`) tanımlar.
* **Sonuç**: Koşullar karşılandığında alınması gereken sonucu veya eylemi tanımlar.
* **Yeni Satır Ekle**: Karar ağacına ek kurallar eklemenizi sağlar.

### Karar Ağacı Yapılandırması Örneği

Bu karar ağacı **Toplam Tutar** alanını değerlendirir ve önceden tanımlanmış koşullara göre farklı gruplara atar. Her kural toplam tutarı belirli bir değerle karşılaştırır ve hangi koşul doğruysa, karşılık gelen **Grup** döndürülür.

<figure><img src="../../../.gitbook/assets/image (335) (1).png" alt=""><figcaption></figcaption></figure>

Bu karar ağacı, hangi grubun atanması gerektiğini belirlemek için iki temel koşulu değerlendirir: **Toplam Tutar** ve **Depo Durumu**. Ağaç, hangi grubun döndürüleceğini tanımlamak için toplam tutara dayalı eşikleri kullanır ve ayrıca deponun "Ana Depo", "Alt Depo" veya "Ana Depo Değil" olarak belirlenip belirlenmediğini ayırt eder.

<figure><img src="../../../.gitbook/assets/image (338).png" alt=""><figcaption></figcaption></figure>

Her kural sırayla değerlendirilir.

## Karar Ağacı Politikası

Karar Ağacı Politikası, bir karar ağacı içindeki birden fazla kuralın nasıl işleneceğini tanımlar. Birkaç politika arasından seçim yapabilirsiniz:

### **1. Benzersiz Politika**

Yalnızca tek bir kuralın eşleşmesini sağlar. Birden fazla kural eşleşirse, karar ağacı yanlış (false) döndürür.

**Örnek:**

| Kural | Koşul | Dönüş Grubu |
| ---- | -------------------- | ------------ |
| 1 | Toplam Tutar <= 1000 | GRUP_1 |
| 2 | Toplam Tutar <= 2000 | GRUP_2 |
| 3 | Toplam Tutar <= 5000 | GRUP_5 |
| 4 | Toplam Tutar <= 4000 | GRUP_4 |
| 5 | Toplam Tutar <= 3000 | GRUP_3 |

Toplam tutar **1500** ise, değerlendirilen kurallar şöyle olacaktır:

* **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
* **Kural 2**: Toplam Tutar <= 2000 (eşleşiyor)
* **Kural 3**: Toplam Tutar <= 5000 (eşleşiyor)
* **Kural 4**: Toplam Tutar <= 4000 (eşleşiyor)
* **Kural 5**: Toplam Tutar <= 3000 (eşleşiyor)

Birden fazla kural eşleştiği için (**Kural 2**, **Kural 3**, **Kural 4**, **Kural 5**), karar ağacı **yanlış** döndürecektir çünkü **Benzersiz** politika yalnızca bir kuralın eşleşebileceğini garanti eder.

### **2. İlk Politika**

İlk eşleşen kural uygulanır ve başka kural değerlendirilmez.

**Örnek:**

| Kural | Koşul | Dönüş Grubu |
| ---- | -------------------- | ------------ |
| 1 | Toplam Tutar <= 1000 | GRUP_1 |
| 2 | Toplam Tutar <= 2000 | GRUP_2 |
| 3 | Toplam Tutar <= 5000 | GRUP_5 |
| 4 | Toplam Tutar <= 4000 | GRUP_4 |
| 5 | Toplam Tutar <= 3000 | GRUP_3 |

Toplam tutar **1500** ise, değerlendirilen kurallar şöyle olacaktır:

* **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
* **Kural 2**: Toplam Tutar <= 2000 (eşleşiyor) → Karar ağacı daha fazla kuralı değerlendirmeyi durdurur ve **GRUP_2**'yi uygular.

### **3. Öncelik Politikası**

Bu seçeneği seçmek, her kural için öncelikler belirlemenizi sağlar. Seçilen sayı ne kadar düşükse, öncelik o kadar yüksektir (yani, öncelik 1 en yüksek önceliğe sahiptir). Kurallar öncelik sırasına göre değerlendirilir. En yüksek önceliğe sahip eşleşen kural uygulanacaktır.

**Örnek:**

<table><thead><tr><th width="137">Kural</th><th width="110">Öncelik</th><th width="268">Koşul</th><th>Dönüş Grubu</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Toplam Tutar &#x3C;= 1000</td><td>GRUP_1</td></tr><tr><td>2</td><td>4</td><td>Toplam Tutar &#x3C;= 2000</td><td>GRUP_2</td></tr><tr><td>3</td><td>3</td><td>Toplam Tutar &#x3C;= 3000</td><td>GRUP_3</td></tr><tr><td>4</td><td>2</td><td>Toplam Tutar &#x3C;= 4000</td><td>GRUP_4</td></tr><tr><td>5</td><td>1</td><td>Toplam Tutar &#x3C;= 5000</td><td>GRUP_5</td></tr></tbody></table>

Toplam tutar **1500** ise, değerlendirilen kurallar şöyle olacaktır:

* **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
* **Kural 2**: Toplam Tutar <= 2000 (eşleşiyor)
* **Kural 3**: Toplam Tutar <= 3000 (eşleşiyor)
* **Kural 4**: Toplam Tutar <= 4000 (eşleşiyor)
* **Kural 5**: Toplam Tutar <= 5000 (eşleşiyor)

Öncelik **5, 4, 3, 2, 1** sırasında uygulandığından, en yüksek önceliğe sahip eşleşen kural **Kural 5** (**GRUP_5**) olacaktır. Karar ağacı **GRUP_5** döndürecektir çünkü **Kural 5** en yüksek önceliğe sahiptir (öncelik 1).

### **4. Topla (sum) Politikası**

Bu politika tüm eşleşen kuralları toplar ve sonuçları toplar. Yalnızca **Dönüş Türü Değer** için çalışır.

**Örnek:**

| Kural | Koşul | Dönüş Değeri |
| ---- | -------------------- | ------------ |
| 1 | Toplam Tutar <= 1000 | 1 |
| 2 | Toplam Tutar <= 2000 | 2 |
| 3 | Toplam Tutar <= 3000 | 3 |
| 4 | Toplam Tutar <= 4000 | 4 |
| 5 | Toplam Tutar <= 5000 | 5 |

**Toplam Tutar = 3500** giriş değeri için, kuralların değerlendirilmesi şöyle olacaktır:

* **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
* **Kural 2**: Toplam Tutar <= 2000 (eşleşmiyor)
* **Kural 3**: Toplam Tutar <= 3000 (eşleşiyor, Dönüş Değeri = 3)
* **Kural 4**: Toplam Tutar <= 4000 (eşleşiyor, Dönüş Değeri = 4)
* **Kural 5**: Toplam Tutar <= 5000 (eşleşiyor, Dönüş Değeri = 5)

**Topla (sum)** politikası uygulandığından, eşleşen kuralların **Dönüş Değerlerini** topluyoruz, bunlar **3, 4, 5**.

**Bu değerlerin toplanması**:

* 5 + 4 + 3 = **12**

Böylece, karar ağacı tarafından döndürülen sonuç **12** olacaktır, bu da tüm eşleşen dönüş değerlerinin toplamıdır.

### **5. Topla (min/maks/say) Politikası**

Bu politika tüm eşleşen kuralları toplar ve **minimum**, **maksimum** değerleri seçer veya oluşumları **sayar**. Yalnızca **Dönüş Türü Değer** için çalışır.

**Örnek:**

| Kural | Koşul | Dönüş Değeri |
| ---- | -------------------- | ------------ |
| 1 | Toplam Tutar <= 1000 | 1 |
| 2 | Toplam Tutar <= 2000 | 2 |
| 3 | Toplam Tutar <= 3000 | 3 |
| 4 | Toplam Tutar <= 4000 | 4 |
| 5 | Toplam Tutar <= 5000 | 5 |

1. **Topla (min)** seçeneği seçilirse, sonuç eşleşen kurallar için **Dönüş Değerlerinin** **minimumunu** döndürür.
   * **Toplam Tutar = 3500** giriş değeri için, kuralların değerlendirilmesi şöyle olacaktır:
     * **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
     * **Kural 2**: Toplam Tutar <= 2000 (eşleşmiyor)
     * **Kural 3**: Toplam Tutar <= 3000 (eşleşiyor, Dönüş Değeri = 3)
     * **Kural 4**: Toplam Tutar <= 4000 (eşleşiyor, Dönüş Değeri = 4)
     * **Kural 5**: Toplam Tutar <= 5000 (eşleşiyor, Dönüş Değeri = 5)
   * **Eşleşen kurallar** Kural 3, Kural 4 ve Kural 5'tir, **Dönüş Değerleri** **3, 4 ve 5**'tir.
   * **Topla (min)** politikası uygulandığından, sonuç **minimum değer** olacaktır, bu da **3**'tür.
   * **Sonuç**: **3**
2. **Topla (maks)** seçeneği seçilirse, sonuç eşleşen kurallar için **Dönüş Değerlerinin** **maksimumunu** döndürür.
   * Yukarıdaki aynı değerlendirme için sonuç şöyle olacaktır:
   * **Sonuç**: **5**
3. **Topla (say)** seçeneği seçilirse, sonuç **eşleşen kural sayısını** sayar.
   * Yukarıdaki aynı değerlendirme için sonuç şöyle olacaktır:
   * **Sonuç**: **3** (çünkü 3 kural eşleşti).

### **6. Kural Sırası Politikası**

Bu politika kuralları karar ağacında göründükleri sırayla uygular ve ilk eşleşen kuralın sonucunu döndürür.

**Örnek:**

| Kural | Koşul | Dönüş Grubu |
| ---- | -------------------- | ------------ |
| 1 | Toplam Tutar <= 1000 | GRUP_1 |
| 2 | Toplam Tutar <= 2000 | GRUP_2 |
| 3 | Toplam Tutar <= 3000 | GRUP_3 |
| 4 | Toplam Tutar <= 4000 | GRUP_4 |
| 5 | Toplam Tutar <= 5000 | GRUP_5 |

Giriş değerinin **Toplam Tutar = 3500** olduğu varsayıldığında, kuralların değerlendirilmesi şöyle olacaktır:

* **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
* **Kural 2**: Toplam Tutar <= 2000 (eşleşmiyor)
* **Kural 3**: Toplam Tutar <= 3000 (eşleşiyor)
* **Kural 4**: Toplam Tutar <= 4000 (eşleşiyor)
* **Kural 5**: Toplam Tutar <= 5000 (eşleşiyor)

**Kural Sırası** altında, ağaç kuralları listelendikleri sırayla işleyecektir. Yani, eşleşen kurallar şunlar olacaktır:

* **Kural 3**: GRUP_3
* **Kural 4**: GRUP_4
* **Kural 5**: GRUP_5

**Sonuç**: **GRUP_3**, **GRUP_4**, **GRUP_5**

### **7. Herhangi Bir (Any) Politika**

Birden fazla kural doğru olabilir, ancak bu kuralların sonucu aynı olmalıdır.

**Örnek:**

| Kural | Koşul | Dönüş Grubu |
| ---- | -------------------- | ------------ |
| 1 | Toplam Tutar <= 1000 | GRUP_1 |
| 2 | Toplam Tutar <= 2000 | GRUP_2 |
| 3 | Toplam Tutar <= 3000 | GRUP_3 |
| 4 | Toplam Tutar <= 4000 | GRUP_4 |
| 5 | Toplam Tutar <= 5000 | GRUP_5 |

Toplam tutar **2500** ise, değerlendirilen kurallar şöyle olacaktır:

* **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
* **Kural 2**: Toplam Tutar <= 2000 (eşleşmiyor)
* **Kural 3**: Toplam Tutar <= 3000 (eşleşiyor)
* **Kural 4**: Toplam Tutar <= 4000 (eşleşiyor)
* **Kural 5**: Toplam Tutar <= 5000 (eşleşiyor)

**Herhangi Bir**'in uygulanabilmesi için, tüm eşleşen kuralların aynı **Dönüş Grubunu** döndürmesi gerekir. Gruplar farklı kurallar arasında eşleşmediği için sonuç **yanlış** olacaktır.

### **8. İlk & Bitişik Politika**

Doğru olan ilk kurala bitişik olan kuralın sonucunu seçer.

**Örnek:**

| Kural | Koşul | Dönüş Grubu |
| ---- | -------------------- | ------------ |
| 1 | Toplam Tutar <= 1000 | GRUP_1 |
| 2 | Toplam Tutar <= 2000 | GRUP_2 |
| 3 | Toplam Tutar <= 3000 | GRUP_3 |
| 4 | Toplam Tutar <= 4000 | GRUP_4 |
| 5 | Toplam Tutar <= 5000 | GRUP_5 |

Toplam tutar **1500** ise, değerlendirilen kurallar şöyle olacaktır:

* **Kural 1**: Toplam Tutar <= 1000 (eşleşmiyor)
* **Kural 2**: Toplam Tutar <= 2000 (eşleşiyor)

**Kural 2** eşleşen ilk kural olduğundan, **İlk & Bitişik**, **Kural 3**: **GRUP_3** sonucunu uygulayacaktır.

## **Karar Ağacını Test Etme**

**Genel Bakış:**
Karar ağacı tasarımcısı, yapılandırılmış kuralların mantığını doğrulamak için bir test özelliği içerir. Bu özellik, kullanıcıların seçilen alanlar için belirli giriş değerleri sağlayarak karar ağacını test etmelerini sağlar.

**Test Özelliğini Kullanma Adımları:**

1.  **Test Düğmesini Bulun:**

    * Karar ağacı tasarımcısında **Test** düğmesini bulun.

    <figure><img src="../../../.gitbook/assets/image (344).png" alt="" width="563"><figcaption></figcaption></figure>
2.  **Test Açılır Penceresini Açın:**

    * **Test** düğmesine tıklayın.
    * Karar ağacında kullanılan kriterlere karşılık gelen giriş alanlarını sağlayan bir açılır pencere görünecektir.

    <figure><img src="../../../.gitbook/assets/image (339).png" alt="" width="421"><figcaption></figcaption></figure>
3. **Giriş Değerlerini Sağlayın:**
   *   Gerçek dünya senaryosunu simüle etmek için giriş alanlarına değerler girin.

       <figure><img src="../../../.gitbook/assets/image (341).png" alt="" width="428"><figcaption></figcaption></figure>
4. **Sonuçları Değerlendirin:**

    * Girişleri girdikten sonra, ağaç bunları seçilen politikaya göre işler.
    * Sistem, sağlanan girişlerle eşleşen kural(lar)ı vurgular.

    <figure><img src="../../../.gitbook/assets/image (342).png" alt="" width="563"><figcaption></figcaption></figure>
5. **Eşleşme Yok İçin Geri Bildirimi İnceleyin:**
   * Hiçbir kural vurgulanmazsa, sistem neden hiçbir kuralın eşleşmediğini açıklayan bir geri bildirim görüntüleyecektir.
   * Girişleri ayarlamak veya potansiyel sorunlar için ağacın yapılandırmasını gözden geçirmek için bu geri bildirimi kullanın.

## Dışa Aktar ve Kaydet

* **Kaydet**: Karar ağacının mevcut yapılandırmasını kaydeder.
* **Dışa Aktar**: Karar ağacı yapılandırmasını dışa aktarmanıza olanak tanır, bu daha sonra başka bir ortama aktarılabilir veya yedekleme amacıyla kullanılabilir.
