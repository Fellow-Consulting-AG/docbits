# Test: FTP İçe Aktarma Bağlantısı

#### Amaç

Bu testler, FTP içe aktarma sistemimizin doğru çalıştığından emin olur. Yeni bir FTP içe aktarma bağlantısı ekleyebildiğimizi, bağlantıyı test edebildiğimizi, etkinleştirip devre dışı bırakabildiğimizi ve sonrasında temizleyebildiğimizi doğrularız.

{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Test Senaryoları

1. **Kurulum:**
   * **Ortam Değişkenleri:** FTP sunucusu bilgileri ve kimlik bilgileri gibi gerekli ayrıntıları ortam değişkenlerinden yükleyin.
2.  **FTP Bağlantı Testleri:**

    **Yeni Bağlantı Ekle:**

    * **Test Yeni FTP İçe Aktarma Bağlantısı Ekle (`test_add_new_ftp_import_connection`):**
      * Verilen kimlik bilgileri ve sunucu ayrıntılarıyla yeni bir FTP içe aktarma bağlantısı ekleyin.
      * **Beklenen Sonuç:** Bağlantı başarıyla eklenmelidir.

    **Bağlantıyı Devre Dışı Bırak:**

    * **Test FTP İçe Aktarma Bağlantısını Devre Dışı Bırak (`test_deactivate_ftp_import_connection`):**
      * Yeni eklenen FTP içe aktarma bağlantısını devre dışı bırakın.
      * **Beklenen Sonuç:** Bağlantı başarıyla devre dışı bırakılmalıdır.

    **Bağlantıyı Test Et:**

    * **Test FTP Bağlantısı (`test_test_ftp_connection`):**
      * FTP içe aktarma bağlantısının FTP sunucusuna başarıyla bağlanıp bağlanamadığını test edin.
      * **Beklenen Sonuç:** Bağlantı başarıyla test edilmelidir.

    **Listede Bağlantıyı Kontrol Et:**

    * **Test Listede FTP Bağlantısını Kontrol Et (`test_check_ftp_connection_in_list`):**
      * Yeni eklenen FTP içe aktarma bağlantısının bağlantı listesinde mevcut olup olmadığını kontrol edin.
      * **Beklenen Sonuç:** Bağlantı listede bulunmalıdır.

    **Bağlantının Devre Dışı Olduğunu Kontrol Et:**

    * **Test FTP Bağlantısının Devre Dışı Olduğunu Kontrol Et (`test_check_ftp_connection_deactivated`):**
      * FTP içe aktarma bağlantısının listede pasif olarak işaretlendiğini doğrulayın.
      * **Beklenen Sonuç:** Bağlantı pasif olmalıdır.

    **Test Klasörü Ekle:**

    * **Test Bağlantıya Test Klasörü Ekle (`test_add_test_folder_to_connection`):**
      * FTP içe aktarma bağlantısına varsayılan bir dizin (test klasörü) ekleyin.
      * **Beklenen Sonuç:** Varsayılan dizin başarıyla eklenmelidir.

    **Bağlantıyı Yeniden Etkinleştir:**

    * **Test FTP İçe Aktarma Bağlantısını Yeniden Etkinleştir (`test_reactivate_ftp_import_connection`):**
      * Daha önce devre dışı bırakılan FTP içe aktarma bağlantısını yeniden etkinleştirin.
      * **Beklenen Sonuç:** Bağlantı başarıyla yeniden etkinleştirilmelidir.

    **Bağlantının Yeniden Etkinleştirildiğini Kontrol Et:**

    * **Test FTP Bağlantısının Yeniden Etkinleştirildiğini Kontrol Et (`test_check_ftp_connection_reactivated`):**
      * FTP içe aktarma bağlantısının listede aktif olarak işaretlendiğini doğrulayın.
      * **Beklenen Sonuç:** Bağlantı aktif olmalıdır.

    **Temizlik:**

    * **Test FTP İçe Aktarmayı Temizle (`test_cleanup_ftp_import`):**
      * Testlerden sonra temizlik yapmak için FTP içe aktarma bağlantısını silin.
      * **Beklenen Sonuç:** Bağlantı başarıyla silinmelidir.

## Her Testin Ayrıntılı Açıklaması

* **Kurulum ve Başlatma:**
  * **Paylaşılan Verileri Başlat:** Testler için paylaşılan verileri hazırlayın.
* **FTP Bağlantı Testleri:**
  * **Yeni Bağlantı Ekle:** Sağlanan kimlik bilgileri ve sunucu ayrıntılarıyla yeni bir FTP içe aktarma bağlantısı ekleyin.
  * **Bağlantıyı Devre Dışı Bırak:** Yeni eklenen FTP içe aktarma bağlantısını devre dışı bırakın.
  * **Bağlantıyı Test Et:** FTP içe aktarma bağlantısının FTP sunucusuna başarıyla bağlanıp bağlanamadığını test edin.
  * **Listede Bağlantıyı Kontrol Et:** Yeni FTP içe aktarma bağlantısının bağlantı listesinde mevcut olduğunu doğrulayın.
  * **Bağlantının Devre Dışı Olduğunu Kontrol Et:** FTP içe aktarma bağlantısının listede pasif olarak işaretlendiğini onaylayın.
  * **Test Klasörü Ekle:** FTP içe aktarma bağlantısına varsayılan bir dizin (test klasörü) ekleyin.
  * **Bağlantıyı Yeniden Etkinleştir:** Daha önce devre dışı bırakılan FTP içe aktarma bağlantısını yeniden etkinleştirin.
  * **Bağlantının Yeniden Etkinleştirildiğini Kontrol Et:** FTP içe aktarma bağlantısının listede aktif olarak işaretlendiğinden emin olun.
  * **Temizlik:** Testlerden sonra temizlik yapmak için FTP içe aktarma bağlantısını silin.
