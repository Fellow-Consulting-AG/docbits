# Dışa Aktar

## Genel Bakış

Dışa Aktarma sayfası, aktif veya pasif olup olmadıkları da dahil olmak üzere yapılandırılmış tüm dışa aktarma ayarlarını görüntüler. Buradan kullanıcılar şunları yapabilir:

* Mevcut dışa aktarma yapılandırmalarını görüntüleme ve yönetme
* Yeni dışa aktarma bağlantıları oluşturma (örneğin, **Infor**, **Infor & IDM**, **Webhook** veya **SFTP**'ye)
* Mevcut dışa aktarma yapılandırmalarını düzenleme veya silme

## Nerede Bulunur

Şurada bulabilirsiniz: **Ayarlar** → **Belge İşleme** → **Dışa Aktar**

<figure><img src="../../../.gitbook/assets/image (442).png" alt=""><figcaption></figcaption></figure>

## **Dışa Aktarma Sayfasını Kullanma**

Dışa Aktarma sayfasını açtığınızda, mevcut tüm dışa aktarma yapılandırmalarının bir listesini göreceksiniz.

Listedeki her satır şunları gösterir:

* **Durum Göstergesi**
  * **Yeşil**, dışa aktarmanın aktif olduğu anlamına gelir
  * **Kırmızı**, dışa aktarmanın devre dışı olduğu anlamına gelir
* **Ad** – dışa aktarma yapılandırmasının adı
* **Belge Türü** – dışa aktarmanın yapılandırıldığı belge türü
* **Alt Organizasyon** – dışa aktarmanın belirli bir alt organizasyonla sınırlı olup olmadığı
* **Dışa Aktarma Yöntemi** – belgenin nereye gönderileceği (örneğin, Infor, IDM, SFTP)
* **Eylemler** – yapılandırmayı **düzenlemek, silmek** veya **etkinleştirmek/devre dışı bırakmak** için düğmeler

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_7.png" alt="DocBits Satın alma Sipariş Dışa aktar 7"><figcaption></figcaption></figure>

#### **Dışa Aktarma Yapılandırması için Önemli Kurallar**

Her **belge türü** için **belirli bir organizasyon veya alt organizasyon içinde** aşağıdaki kurallar geçerlidir:

* **Yalnızca bir aktif Infor dışa aktarımına** sahip olabilirsiniz
* **Yalnızca bir aktif Infor olmayan dışa aktarıma** sahip olabilirsiniz (örneğin, Webhook, SFTP)

Ancak, şunlara sahip olmak mümkündür:

* Aynı belge türü için aynı anda **bir aktif Infor dışa aktarımı** _ve_ **bir aktif Infor olmayan dışa aktarım**
* **Farklı alt organizasyonlar için farklı dışa aktarma yapılandırmaları** — örneğin, Alt-Org A için bir Infor dışa aktarımı ve Alt-Org B için başka bir Infor dışa aktarımı

## **Yeni Bir Dışa Aktarma Oluşturma**

Yeni bir dışa aktarma oluşturmak için:

1. **“Yeni”** düğmesine tıklayın.
   ![](<../../../.gitbook/assets/image (1) (1) (1) (1).png>)
2. Yapılandırmak istediğiniz **Dışa Aktarma Türü**nü seçin (örneğin, Infor, IDM, SFTP).
3. Dışa aktarma türüne göre gerekli alanları doldurun.
4. Yapılandırmayı kaydedin.

## Dışa Aktarma Seçenekleri

#### Webhook

<details>

<summary>Webhook</summary>

<figure><img src="../../../.gitbook/assets/image (14) (1) (3).png" alt=""><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **Dışa Aktarma URL'si**
  Belgenin dışa aktarılacağı hedef URL.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_4.png" alt="DocBits Satın alma Sipariş 4"><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **Kullanıcı Adı**
  SFTP sunucusunda kimlik doğrulaması yapmak için kullanılan kullanıcı adı.
* **Şifre**
  SFTP hesabı için ilgili şifre. Hesabın belirtilen klasöre yazma erişimi olduğundan emin olun.
* **Sunucu URL'si**
  Hedef SFTP sunucusunun ana bilgisayar adı veya IP adresi.
* **Port**
  SFTP sunucusuna bağlanmak için kullanılan port.
* **Klasör**
  Belgelerin yükleneceği SFTP sunucusundaki yol (örneğin, `/incoming/invoices/`).
  Mevcut ve yazılabilir olmalıdır.
*   **XSLT Dosyası (İsteğe Bağlı)**

    **XSLT dosyası**, varsayılan DocBits dışa aktarma formatının dönüştürülmesine izin verir.

    * **Ne zaman kullanılır:**
      Yalnızca alıcı sistem farklı bir yapı veya DocBits varsayılanından farklı belirli bir format gerektiriyorsa.
    * Varsayılan dışa aktarma formatı gereksinimleri karşılıyorsa **boş bırakın**.

</details>

#### SFTP'ye Infor Dışa Aktarımı

<details>

<summary>SFTP'ye Infor Dışa Aktarımı</summary>

<figure><img src="../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **IDM Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? IDM Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? BOD Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Klasör**
  Belgelerin yükleneceği SFTP sunucusundaki yol (örneğin, `/incoming/invoices/`).
  Mevcut ve yazılabilir olmalıdır.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

<figure><img src="../../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **Kullanıcı Adı**
  SMB paylaşımına bağlanmak için kullanılan kullanıcı adı.
* **Şifre**
  SMB kimlik doğrulaması için ilgili şifre.
* **Sunucu URL'si**
  SMB sunucusunun adresi.
* **Port**
  SMB paylaşımına erişmek için kullanılan port numarası.
* **Klasör**
  Belgelerin kaydedileceği SMB paylaşımındaki klasör yolu (örneğin, `/incoming/invoices/`).
  Mevcut ve yazılabilir olmalıdır.
*   **JPL Eşleme Dosyası (İsteğe Bağlı)**

    **JPL dosyası**, dışa aktarılan verilerin SMB paylaşımına yazılmadan önce dönüştürülmesini tanımlamak için kullanılır.

    * **Ne zaman kullanılır:**
      Yalnızca dışa aktarılan belge verilerinin harici formatlama veya sistem beklentileriyle eşleşecek şekilde ayarlanması gerektiğinde.
    * Dönüşüm gerekmiyorsa **boş bırakın**.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

<figure><img src="../../../.gitbook/assets/image (12) (1) (3).png" alt=""><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **ION Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
* **IDM Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? IDM Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Bulut / Yerinde Geçişi**
  Infor dağıtım türünü belirtmek için bir anahtar:
  * **Bulut**: Infor CloudSuite müşterisiyseniz bunu seçin.
  * **Yerinde**: Infor kendi sunucularınızda barındırılıyorsa bunu seçin.

</details>

#### **InforION**

<details>

<summary>Infor ION</summary>

<figure><img src="../../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **ION Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
* **BOD Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? BOD Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Bulut / Yerinde Geçişi**
  Infor dağıtım türünü belirtmek için bir anahtar:
  * **Bulut**: Infor CloudSuite müşterisiyseniz bunu seçin.
  * **Yerinde**: Infor kendi sunucularınızda barındırılıyorsa bunu seçin.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

<figure><img src="../../../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **ION Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
* **IDM Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? IDM Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? BOD Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Bulut / Yerinde Geçişi**
  Infor dağıtım türünü belirtmek için bir anahtar:
  * **Bulut**: Infor CloudSuite müşterisiyseniz bunu seçin.
  * **Yerinde**: Infor kendi sunucularınızda barındırılıyorsa bunu seçin.

</details>

### Infor CloudSuite müşterileri için

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

<figure><img src="../../../.gitbook/assets/docbits_settings_email.png" alt="DocBits Ayarlar E-posta"><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **ION Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
* **IDM Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? IDM Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? LN Eşleme Örneğini Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

<figure><img src="../../../.gitbook/assets/docbits_settings.png" alt="DocBits Ayarlar"><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **ION Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
* **IDM Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? IDM Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? M3 Eşleme Örneğini Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_5.png" alt="DocBits İş akışı Satın alma Sipariş 5"><figcaption></figcaption></figure>

**Alan Açıklamaları**

* **Başlık**
  Dışa aktarma yapılandırmasının adı. Bu, dışa aktarma listesinde görünecektir.
* **Alt Organizasyon** _(isteğe bağlı)_
  Mevcut tüm alt organizasyonları içeren bir açılır menü.
  * Boş bırakılırsa: ana organizasyon için geçerlidir.
  * Seçilirse: dışa aktarma yalnızca seçilen alt organizasyon için geçerli olacaktır.
* **Belge Türü**
  Mevcut tüm belge türlerini listeleyen açılır menü.
  Bu, bu dışa aktarma yapılandırmasının hangi belge türü için geçerli olduğunu belirler.
* **ION Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
* **IDM Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? IDM Eşleme Kılavuzunu Görüntüle](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Eşleme Dosyası**
  Dosya yöneticisinden bir eşleme dosyası seçin veya kural yöneticisi ile oluşturulan bir toml dosyasını kullanmak için toml seçeneğini kullanın.
  [Bir tane oluşturmak için yardıma mı ihtiyacınız var? Kural Yöneticisi Kılavuzunu Görüntüle](rule-manager/)

</details>
