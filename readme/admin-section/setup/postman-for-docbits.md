# DocBits için Postman

Bu kılavuz, Postman aracılığıyla DocBits organizasyonunuza HTTP istekleri nasıl yapacağınızı gösterecektir. Kullanımı kolaydır ve organizasyon yöneticileri için çok faydalıdır.

## Kurulum

İlk olarak, Postman'ı sisteminize indirin ve oturum açın/kaydolun.

Şimdi HTTP isteklerinin Postman'da nasıl çalıştığını öğrenmek için adım adım kılavuzu takip edin.

Postman'da Yetkilendirme

HTTP isteklerinizi oluşturmadan önce, bunları yetkilendirmek için DocBits'ten API anahtarınızı girmeniz gerekmektedir.

* \`Authorization\` sekmesine tıklayın ve yetkilendirme türü olarak \`API Key\`i seçin.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Değerleri doldurun. \`Key\` alanına "X-API-key" yazın ve API Anahtarınızı değer olarak girin (DocBits Ayarlar menüsünde Entegrasyon altında bulunur). \`Header\`'a eklemek için Ekle'yi seçin.

&#x20;

* Şu şekilde görünmelidir:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### DocBits API

https://api.polydocs.io adresinde mevcuttur

* Sağ üst köşede Yetkilendir'e tıklayın

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* API Anahtarınızı girin ve \`Authorize\`a tıklayarak onaylayın

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Postman'de Yeni Bir Çalışma Alanı Oluşturma

* Çalışma Alanlarına tıklayın ve yeni bir çalışma alanı oluşturun (istediğiniz şekilde adlandırabilirsiniz)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Bu çalışma alanına kimin erişebileceğini belirleyen görünürlüğü seçmelisiniz.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Seçiminizi yaptıktan sonra \`Çalışma Alanı Oluştur\`’a tıklayın ve uygulamanın sol tarafındaki Koleksiyonları seçerek HTTP istekleriniz için yeni bir koleksiyon oluşturun.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

Bu koleksiyona birden fazla HTTP isteği ekleyebilirsiniz. Bunun için koleksiyonun 3 noktasına tıklayın ve \`İstek Ekle\`’yi seçin.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## "GET" Yöntemi Örneği

GET yöntemi, kullanıcılar, alt-organizasyonlar, işlenmiş belgeler ve çok daha fazlası hakkında bilgi almak için çok faydalıdır.

* HTTP isteğinizde GET yöntemini seçin.
* Yukarıda açıklandığı gibi kendinizi yetkilendirin.
* https://api.polydocs.io adresini açın ve Polydocs URL'sinin arkasına işlevin yolunu ekleyin. Örneğin:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Şimdi bu bağlantıyı Postman'daki GET yönteminin yanındaki metin kutusuna yapıştırın.

\`Gönder\`e tıklayın ve organizasyonunuzdaki her kullanıcı hakkında tüm bilgileri almalısınız.

## "POST" Yöntemi Örneği

POST yöntemi genellikle kullanıcı veya organizasyon oluşturmak için kullanılır. Bu yöntem bilgileri veritabanına ekler.

Kullanıcı Oluştur

* POST Yöntemini seçin.
* Yukarıda açıklandığı gibi kendinizi yetkilendirin.
* https://api.polydocs.io adresini açın ve Polydocs URL'sinin arkasına işlevin yolunu ekleyin. Bu durumda:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Şimdi bu bağlantıyı Postman'daki POST yönteminin yanındaki metin kutusuna yapıştırın.
* HTTP isteğinizde \`Body\` sekmesini seçin ve adı yanında kırmızı bir yıldız olan her kimlik için anahtarları ve değerleri girin.

Bittiğinizde, şu şekilde görünmelidir:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Yönetici hesabı oluşturmak istiyorsanız, \`is\_admin\` değerini true olarak ayarlayın.

Son olarak, \`Gönder\`e tıklayın ve belirlediğiniz tüm kimlikleri yanıtın altında görebilirsiniz. Bu, kullanıcının oluşturulduğu anlamına gelir.
### Belge Yükleme

Belge yüklemek için POST yöntemini de kullanabilirsiniz.

* POST Yöntemini seçin.
* Yukarıda açıklandığı gibi kendinizi yetkilendirin.
* https://api.polydocs.io adresini açın ve Polydocs URL'sinin arkasına işlevin yolunu ekleyin.&#x20;

Bu durumda:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Şimdi bu bağlantıyı Postman'deki POST yönteminin yanındaki metin kutusuna yapıştırın.
* HTTP isteğinizde `Body` sekmesini seçin ve `form-data`'yı seçin.

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Dosyayı `KEY` alanına girin, burada gizli Dosya açılır menüsünü bulacaksınız. `Dosya` seçin ve `Dosyaları Seç`e tıklayarak dosyanızı seçebileceğiniz `VALUE` alanına geçin.

`Gönder`e tıkladığınızda yanıtta "success": true görmelisiniz.

Bu şöyle görünmelidir:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## "SİLME" Yöntemi örneği

SİLME yöntemi, örneğin kullanıcıları, kuruluşları vb. silmek için kullanılır.

* SİLME Yöntemini seçin
* Yukarıda açıklandığı gibi kendinizi yetkilendirin.
* https://api.polydocs.io adresini açın ve Polydocs URL'sinin arkasına işlevin yolunu ekleyin.

&#x20;Örneğin:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Şimdi bu bağlantıyı Postman'deki SİLME yönteminin yanındaki metin kutusuna yapıştırın.
* URL'nin sonundaki {user\_id} yerine silmek istediğiniz gerçek kullanıcı kimliğini yazın. (Kullanıcı kimliğini GET yöntemini kullanarak alabilirsiniz).
* Eğer URL'ye kullanıcı kimliğini eklediyseniz, bunun için bir vücut anahtarı ve değeri eklemenize gerek yoktur.
* `Gönder`e tıkladığınızda yanıtta "success": true görmelisiniz.

&#x20;Bu şöyle görünmelidir:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## "KOYMA" Yöntemi örneği

KOYMA yöntemi genellikle kullanıcı veya kuruluş verilerini güncellemek için kullanılır. Anlamak ve kullanmak çok kolaydır.

* KOYMA Yöntemini seçin.
* Yukarıda açıklandığı gibi kendinizi yetkilendirin.
* https://api.polydocs.io adresini açın ve Polydocs URL'sinin arkasına işlevin yolunu ekleyin.

&#x20;Örneğin:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Şimdi bu bağlantıyı Postman'deki KOYMA yönteminin yanındaki metin kutusuna yapıştırın.
* URL'nin sonundaki {user\_id} yerine güncellemek istediğiniz gerçek kullanıcı kimliğini yazın. (Kullanıcı kimliğini GET yöntemini kullanarak alabilirsiniz).

## Bir Kullanıcının E-posta Adresini Değiştirme

* Vücut kısmına "email"i anahtar olarak girin ve yeni e-posta adresini değer olarak girin.
* Sonra sadece `Gönder`e basın ve yanıtta "success"ı görmelisiniz.
