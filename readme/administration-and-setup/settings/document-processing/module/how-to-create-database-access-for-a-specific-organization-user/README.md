# Belirli Bir Organizasyon Kullanıcısı İçin Veritabanı Erişimi Nasıl Oluşturulur

Bu kılavuz, belirli bir organizasyon kullanıcısı için DocBits veritabanına erişim izni verme adımlarını açıklar. Bu, özel raporlama veya veri analizi amacıyla doğrudan veritabanı erişimine ihtiyaç duyan ileri düzey kullanıcılar veya yöneticiler için gereklidir.

## Adım Adım Kılavuz

1.  **Modül Ayarlarına Git**:
    **Ayarlar** -> **Belge İşleme** -> **Modül**'e gidin.

2.  **Veritabanı Erişim Bölümünü Bul**:
    **Belirli Bir Organizasyon Kullanıcısı İçin Veritabanı Erişimi Oluştur** başlıklı bölümü bulun.

3.  **Kullanıcı Seç**:
    Açılır menüden, veritabanı erişimi vermek istediğiniz kullanıcıyı seçin.

4.  **İzinleri Yapılandır**:
    Kullanıcıya verilecek izin düzeyini (örneğin Salt Okunur, Okuma/Yazma) belirleyin.

5.  **Erişim Oluştur**:
    **Oluştur** düğmesine tıklayın. Sistem, kullanıcı için gerekli veritabanı kimlik bilgilerini oluşturacaktır.

6.  **Kimlik Bilgilerini Paylaş**:
    Oluşturulan kimlik bilgilerini (Kullanıcı Adı, Şifre, Ana Bilgisayar, Port, Veritabanı Adı) güvenli bir şekilde kullanıcıyla paylaşın.

<figure><img src="../../../../../../.gitbook/assets/module_db_access.png" alt=""><figcaption></figcaption></figure>

## Önemli Notlar

* **Güvenlik**: Veritabanı kimlik bilgilerini yalnızca güvenilir kullanıcılarla paylaşın.
* **IP Kısıtlaması**: Güvenliği artırmak için, veritabanı erişimini belirli IP adresleriyle sınırlamayı düşünün.
* **Erişimi İptal Et**: Bir kullanıcının erişimine artık ihtiyaç duyulmadığında, bu bölümden erişimi iptal edebilirsiniz.
