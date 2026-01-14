# Test: E-posta İçe Aktarma ve İşleme Testleri

## Neler Test Ediliyor?

Bu testler, e-posta içe aktarma sistemimizin doğru çalıştığından emin olur. Ana hedefler şunlardır:

1. Ekleri olan **e-postalar gönderin**.
2. **E-postaları alın ve belirli klasörlere taşıyın**.
3. **E-postaların okunmuş veya okunmamış olup olmadığını kontrol edin.**
4. **E-postaları sistemimize aktarın.**
5. Sonrasında e-postaları ve içe aktarılan belgeleri silerek **temizlik yapın**.

## İlgili Adımlar

1. **Kurulum:**
   * **Ortam Ayarlarını Al:** E-posta sunucusu ayrıntılarını ve kimlik bilgilerini ortam değişkenlerinden yükleyin.
   * **E-posta Şifresini Şifrele:** E-posta şifresini güvenli bir şekilde şifreleyin.
2. **E-postaları Gönder ve Yönet:**
   * **E-postaları Gönder:** Belirli konular ve eklerle e-posta göndermek için bir SMTP işlevi kullanın.
   * **E-postaları Taşı:** E-postaları hedef klasöre taşımak için IMAP işlevlerini kullanın.
   * **Klasörleri Listele:** Hedef klasörün var olup olmadığını kontrol edin.
   * **E-postaları Sil:** E-postaları klasörlerden silerek temizleyin.
   * **E-posta Durumunu Kontrol Et:** E-postaların okunmamış veya okunmuş olarak işaretlenip işaretlenmediğini doğrulayın.
3.  **Test Sırası**

    **Başlangıç Kurulumu:**

    * **Bağlantıyı Kontrol Et:** E-posta sunucusuna bağlantıyı doğrulayın ve bağlantı kimliğini alın.
    * **Oturum Açma Testi:** Saklanan kimlik bilgileriyle oturum açmanın çalıştığını onaylayın.
    * **Klasör Kontrolü:** Hedef klasörün e-posta sunucusunda var olduğundan emin olun.

    **E-posta İşlemleri:**

    * **Test E-postalarını Gönder:** Benzersiz konulara sahip üç e-posta gönderin.
    * **E-posta Kimliklerini Al:** Gönderilen e-postaların kimliklerini gelen kutusundan alın.
    * **E-postaları Taşı:** Bu e-postaları gelen kutusundan hedef klasöre taşıyın.
    * **E-posta Durumunu Kontrol Et:** Hedef klasördeki e-postaların okunmamış olarak işaretlendiğinden emin olun.

    **E-posta İçe Aktarma:**

    * **E-postaları Getir:** E-postaları hedef klasörden sistemimize aktarın.
    * **İçe Aktarılan E-postaları Kontrol Et:** İçe aktarılan e-postaların doğru şekilde getirildiğinden ve günlüğe kaydedildiğinden emin olun.

    **Günlük Doğrulama:**

    * **İçe Aktarma Günlüklerini Kontrol Et:** Gönderilen e-postaların konularının içe aktarma günlüklerine kaydedildiğini doğrulayın.

    **Temizlik:**

    * **İçe Aktarılan Belgeleri Sil:** E-postalardan içe aktarılan belgeleri kaldırın.
    * **E-postaları Sil:** Gönderilen ve taşınan e-postaları klasörlerden silerek temizleyin.

### Her Testin Ayrıntılı Açıklaması

* **Kurulum ve Başlatma:**
  * **Paylaşılan Verileri Başlat:** Testler için paylaşılan verileri hazırlayın.
* **E-posta Bağlantı Testleri:**
  * **Bağlantı Kimliğini Al:** E-posta sunucusuna bağlanıp bağlanamadığımızı ve bağlantı için bir kimlik alıp alamadığımızı kontrol edin.
  * **Oturum Açma Doğrulaması:** E-posta sunucusunda oturum açmanın düzgün çalıştığından emin olun.
* **Klasör Doğrulama Testleri:**
  * **Hedef Klasörü Kontrol Et:** Hedef klasörün e-posta sunucusunda var olduğundan emin olun.
  * **Klasör Listesini Doğrula:** Sunucudan gelen klasör listesinin beklentilerimizle eşleştiğinden emin olun.
* **E-posta Gönderme ve Kimlik Alma:**
  * **E-postaları Gönder:** Belirli konular ve eklerle üç test e-postası gönderin.
  * **E-posta Kimliklerini Al:** Bu gönderilen e-postaların benzersiz kimliklerini gelen kutusundan alın.
* **E-posta Taşıma ve Durum Kontrolü:**
  * **E-postaları Klasöre Taşı:** Test e-postalarını gelen kutusundan hedef klasöre taşıyın.
  * **Okunmamış Durumunu Kontrol Et:** Taşındıktan sonra e-postaların okunmamış olarak işaretlendiğinden emin olun.
* **E-posta Getirme ve Yanıt Doğrulama:**
  * **Klasörden E-postaları Getir:** E-postaları hedef klasörden sistemimize aktarın.
  * **Getirilen E-postaları Doğrula:** Getirilen e-postaların gönderilen e-postalarla eşleştiğini onaylayın.
* **İçe Aktarma Günlüğü Doğrulama:**
  * **İçe Aktarma Günlüğünü Getir:** İçe aktarılan e-postaların günlüğünü alın.
  * **Günlükte E-posta Konularını Kontrol Et:** Test e-postalarının konularının içe aktarma günlüğünde mevcut olduğundan emin olun.
* **Temizlik:**
  * **İçe Aktarılan Belgeleri Sil:** E-postalardan içe aktarılan belgeleri kaldırın.
  * **E-postaları Sil:** Test e-postalarını gelen kutusundan ve hedef klasörden silerek her şeyi temiz tutun.
