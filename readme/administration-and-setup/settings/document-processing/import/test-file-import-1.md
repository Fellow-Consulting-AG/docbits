# Test: Dosya İçe Aktarma 1

## Amaç

Bu testler, dosya içe aktarma sistemimizin doğru çalıştığından emin olmak için tasarlanmıştır. Özellikle PDF ve TIFF dosyalarının sisteme içe aktarılmasını test ederek, bunların başarıyla işlendiğinden ve saklandığından emin oluruz.

#### Test Kurulumu ve Temizliği

* **Kurulum:**
  * Her testten önce, bir kurulum mesajı günlüğe kaydederiz.
  * **Temizlik:** Her testten sonra, test kullanıcısı tarafından oluşturulan belgeleri veritabanından silerek, artık verilerin sonraki testleri etkilememesini sağlamak için temizlik yaparız.

#### Test Senaryoları

1. **PDF Dosyası İçe Aktar:**
   * **Test PDF İçe Aktar (`test_import_pdf`):**
     * Sisteme bir PDF dosyası (`FellowBananaInvoice.pdf`) içe aktarın.
     * **Beklenen Sonuç:** Dosya başarıyla içe aktarılmalı ve bir belge kimliği döndürmelidir.
2. **TIFF Dosyası İçe Aktar:**
   * **Test TIFF İçe Aktar (`test_import_tiff`):**
     * Sisteme bir TIFF dosyası (`TIFF_FILE.TIF`) içe aktarın.
     * **Beklenen Sonuç:** Dosya başarıyla içe aktarılmalı ve bir belge kimliği döndürmelidir.

## Her Testin Ayrıntılı Açıklaması

* **Kurulum ve Temizlik:**
  * **Günlüğe Kaydetme:** Her test için bir kurulum ve temizlik mesajı günlüğe kaydedilir.
  * **Veritabanı Temizliği (`clean_documents`):** Temiz bir durumu korumak için test kullanıcısı tarafından oluşturulan belgeleri veritabanından siler.
*   **Dosya İçe Aktarma Testleri:**

    **PDF Dosyası İçe Aktar:**

    * **Kullanıcıyı Yükle:** Test kullanıcısını yükleyin.
    * **Dosya Yolu:** PDF dosyasının yolunu belirtin (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Dosyayı İçe Aktar:** PDF dosyasını içe aktarmak için `FileImporter` sınıfını kullanın.
    * **Yanıtı Kontrol Et:** Yanıtın bir başarı mesajı ve bir belge kimliği içeren bir liste olduğundan emin olun.

    **TIFF Dosyası İçe Aktar:**

    * **Kullanıcıyı Yükle:** Test kullanıcısını yükleyin.
    * **Dosya Yolu:** TIFF dosyasının yolunu belirtin (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Dosyayı İçe Aktar:** TIFF dosyasını içe aktarmak için `FileImporter` sınıfını kullanın.
    * **Yanıtı Kontrol Et:** Yanıtın bir başarı mesajı ve bir belge kimliği içeren bir liste olduğundan emin olun.

## Kod Yapısı

* **Logger:** Kurulum, temizlik ve test yürütme sırasında hata ayıklama mesajlarını günlüğe kaydetmek için kullanılır.
* **Database Helper:** Temizlik için sonuç döndürmeden sorguları çalıştırır.
* **File Importer:** Dosyaların sisteme içe aktarılmasını yönetir.
* **Fixtures:** Testler için kurulum ve temizliği yönetmek üzere `set_up` fikstürü.
* **Testler:**
  * `test_import_pdf`: Bir PDF dosyasının içe aktarılmasını test eder.
  * `test_import_tiff`: Bir TIFF dosyasının içe aktarılmasını test eder.

#### Özet

Bu testler, dosya içe aktarma işlevimizin hem PDF hem de TIFF dosyaları için beklendiği gibi çalıştığından emin olur. Bu yaklaşımı izleyerek, dosyaların doğru şekilde içe aktarıldığını ve sistemin farklı dosya türlerini sorunsuz bir şekilde işleyebildiğini doğrularız.
