# Entegrasyon

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## API Anahtarı

* **Anahtar**: Bu, harici uygulamaların Docbits'in API'sine erişmek için kullandığı benzersiz tanımlayıcıdır. Diğer yazılımlardan Docbits'e yapılan istekleri doğrulamak için hayati öneme sahiptir.
* Görüntüleme, yeniden oluşturma veya API anahtarını kopyalama gibi işlemler, belirli ihtiyaçlara ve güvenlik protokollerine bağlı olarak burada gerçekleştirilebilir.

## SSO (Tek Oturum Açma) Hizmet Sağlayıcı Ayarları

* **Varlık Kimliği**: Bu, SSO yapılandırmasında Docbits'in bir hizmet sağlayıcı olarak tanımlayıcısıdır. Docbits'i SSO çerçevesi içinde benzersiz bir şekilde tanımlar.
* **SLO (Tek Oturum Kapatma) URL'si**: SSO oturumlarının eş zamanlı olarak çıkış yapmak için gönderildiği URL.
* **SSO URL'si**: Tek oturum açma işlemi başlatmak için kullanılan URL.
* "Sertifika İndir" ve "Meta Veri İndir" gibi işlemler, SSO entegrasyonunu kurmak ve sürdürmek için gereken güvenlik sertifikalarını ve meta veri bilgilerini elde etmek için mevcuttur.

{% hint style="info" %}
[SSO Kurulumu](../../../setup/sso-configuration.md) bölümüne bakın.
{% endhint %}

## Kimlik Hizmeti Sağlayıcı Ayarları

* **Kiracı Kimliği**: Bu, Docbits'in kullanıldığı şirkete özgü verileri ve erişim yapılandırmalarını yönetmek için kiracı tanımlayıcısı gerektiren bulut hizmetleriyle entegre olduğunda kullanılabilir.
* **Dosya Yükle**: Yöneticinin kimlik sağlayıcı ile entegrasyonu kolaylaştıran yapılandırma dosyalarını veya diğer gerekli dosyaları yüklemesine olanak tanır.
* **Yapılandır**: Değişiklikler yapıldıktan veya yeni yapılandırmalar yüklendikten sonra ayarları uygulamak veya güncellemek için bir düğme.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2488" %}
