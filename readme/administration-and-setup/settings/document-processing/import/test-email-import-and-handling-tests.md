# Test: E-posta İçe Aktarma ve İşleme Testleri

## Amaç

Bu testler, sistemimizin e-posta içe aktarmayı doğru şekilde işleyebildiğinden emin olur. Bu, e-posta göndermeyi, almayı ve belirli klasörlere taşımayı, okunmuş veya okunmamış olup olmadıklarını kontrol etmeyi, bunları sisteme aktarmayı ve sonrasında temizlik yapmayı içerir.

## Test Adımları

1. **Kurulum:**
   * **Ortam Ayarlarını Al:** E-posta sunucusu bilgileri ve kimlik bilgileri gibi gerekli ayrıntıları ortam değişkenlerinden yükleyin.
   * **E-posta Şifresini Şifrele:** Güvenli kullanım için e-posta şifresini güvenli bir şekilde şifreleyin.
2. **E-posta Gönderme ve Yönetimi:**
   * **Bir E-posta Gönder:** Belirli bir konu ve ek ile bir e-posta göndermek için bir SMTP işlevi kullanın.
   * **E-postayı Taşı:** E-postayı hedef bir klasöre taşımak için IMAP işlevlerini kullanın.
   * **Klasörleri Listele:** Hedef klasörün var olduğundan emin olun.
   * **E-postayı Sil:** E-postayı klasörden silerek temizlik yapın.
   * **E-posta Durumunu Kontrol Et:** E-postanın okunmuş veya okunmamış olarak işaretlenip işaretlenmediğini doğrulayın.
3.  **Test Sırası**

    **Başlangıç Kurulumu:**

    * **Bağlantıyı Kontrol Et:** E-posta sunucusuna bağlantıyı doğrulayın ve bağlantı kimliğini alın.
    * **Oturum Açma Testi:** Saklanan kimlik bilgileriyle oturum açmanın çalıştığını onaylayın.
    * **Klasör Kontrolü:** Hedef klasörün e-posta sunucusunda var olduğundan emin olun.

    **E-posta İşlemleri:**

    * **Bir Test E-postası Gönder:** Belirli bir konuya sahip bir e-posta gönderin.
    * **E-posta Kimliğini Al:** Gönderilen e-postanın kimliğini gelen kutusundan alın.
    * **E-postayı Taşı:** E-postayı gelen kutusundan hedef klasöre taşıyın.
    * **E-posta Durumunu Kontrol Et:** Hedef klasördeki e-postanın okunmamış olarak işaretlendiğinden emin olun.

    **E-posta İçe Aktarma:**

    * **E-postayı Getir:** E-postayı hedef klasörden sistemimize aktarın.
    * **İçe Aktarılan E-postayı Kontrol Et:** İçe aktarılan e-postanın doğru şekilde getirildiğinden ve günlüğe kaydedildiğinden emin olun.

    **Günlük Doğrulama:**

    * **İçe Aktarma Günlüğünü Kontrol Et:** Gönderilen e-postanın konusunun içe aktarma günlüğüne kaydedildiğini doğrulayın.

    **Temizlik:**

    * **İçe Aktarılan Belgeyi Sil:** E-postadan içe aktarılan belgeyi kaldırın.
    * **E-postayı Sil:** Her şeyi temiz tutmak için gönderilen ve taşınan e-postayı klasörlerden silin.

## Her Testin Ayrıntılı Açıklaması

* **Kurulum ve Başlatma:**
  * **Paylaşılan Verileri Başlat:** Testler için paylaşılan verileri hazırlayın.
* **E-posta Bağlantı Testleri:**
  * **Bağlantı Kimliğini Al:** E-posta sunucusuna bağlanıp bağlanamadığımızı ve bağlantı için bir kimlik alıp alamadığımızı kontrol edin.
  * **Oturum Açma Doğrulaması:** E-posta sunucusunda oturum açmanın düzgün çalıştığından emin olun.
* **Klasör Doğrulama Testleri:**
  * **Hedef Klasörü Kontrol Et:** Hedef klasörün e-posta sunucusunda var olduğundan emin olun.
  * **Klasör Listesini Doğrula:** Sunucudan gelen klasör listesinin beklentilerimizle eşleştiğinden emin olun.
* **E-posta Gönderme ve Kimlik Alma:**
  * **Bir E-posta Gönder:** Belirli bir konu ve ek ile bir test e-postası gönderin.
  * **E-posta Kimliğini Al:** Bu gönderilen e-postanın benzersiz kimliğini gelen kutusundan alın.
* **E-posta Taşıma ve Durum Kontrolü:**
  * **E-postayı Klasöre Taşı:** Test e-postasını gelen kutusundan hedef klasöre taşıyın.
  * **Okunmamış Durumunu Kontrol Et:** Taşındıktan sonra e-postanın okunmamış olarak işaretlendiğinden emin olun.
* **E-posta Getirme ve Yanıt Doğrulama:**
  * **Klasörden E-posta Getir:** E-postayı hedef klasörden sistemimize aktarın.
  * **Getirilen E-postayı Doğrula:** Getirilen e-postanın yanıtta mevcut olduğunu onaylayın.
* **İçe Aktarma Günlüğü Doğrulama:**
  * **İçe Aktarma Günlüğünü Getir:** İçe aktarılan e-postaların günlüğünü alın.
  * **Günlükte E-posta Konusunu Kontrol Et:** Test e-postasının konusunun içe aktarma günlüğünde mevcut olduğundan emin olun.
* **Temizlik:**
  * **İçe Aktarılan Belgeyi Sil:** E-postadan içe aktarılan belgeyi kaldırın.
  * **E-postayı Sil:** Test e-postasını gelen kutusundan ve hedef klasörden silerek her şeyi temiz tutun.
