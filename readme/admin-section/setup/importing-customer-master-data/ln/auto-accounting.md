# Otomatik Muhasebe

## **Önkoşullar**

* İşlevsel LN to DocBits veri akışı
* Doğru yapılandırılmış DocBits ortamı

## **Infor Yapılandırması**

### **ION Masaüstü**

Infor'da, ION Masaüstü uygulamasını açın. Sol sekmeden Connect → Connection Points'e gidin

![](https://lh7-us.googleusercontent.com/tOzuXMmjVxByy-GQHBnNbFgP15YKIR0GNGoqrcqz87S3\_qBeZCvk92FA4PtD6UjLtUGBBKfmMd-W087C6TnORp7qptWzpDIEp4R2BbivWjQAsmStpZ4RcMgCY7s2CIV0AHErRtQDO2ePlMbNJSoIrmg)

Bu, LN'den verilerinizi otomatik muhasebe için gerekli olan iki bağlantı noktasını oluşturacağınız yerdir.

Yeni bir bağlantı noktası oluşturmak için "EKLE" ye tıklayın, aşağıdaki gibi API seçeneğini seçin

![](https://lh7-us.googleusercontent.com/C8l4LJ2WHIoPU7E\_uFhNIo8XakbizRx874hyTdJH9oHIW-PGd5tOhsnc1uJ6TW6P9BUQqmjoMrHL5WwQJ8IUJqufsbPFIdamKR9cF0EnnPOZD-TlJEQQAmcHKzoKrumCDQAexYZOQ1CpN1p\_bAnLNzI)

İki ayrı API bağlantı noktasını yapılandırmanız gerekecek, yani:

* HesapPlânı
* FinalEsnekBoyutlar

#### **HesapPlânı**

HesapPlânı bağlantı noktanızın bağlantı sekmesi aşağıdaki gibi görünmelidir. Bağlantı noktasına uygun bir ad ve açıklama verin, ayrıca oluşturduğunuz Hizmet Hesabını içe aktarın.

![](https://lh7-us.googleusercontent.com/gJ1VStvYQ8cu1HBua2iA1Axo1M\_lXTS0VGYuqqtSDx-mtu-4xQQBjasNsGyiNSgjuYYQ0yYQkJN79\_HJcFF0vTyY4wLZWYIJQHC2oCColX43Va-g-E-KeCRyRQiV6eRDm932eFu6ic7g8OttWULPNUE)

![](https://lh7-us.googleusercontent.com/6zmLNSm7pLiS8dA9VceJv5pxwGpTE8WWZ1nmOt-UJA9qvW0wytcRZXB21jW2xa1BABB1YNNS5uWlxVWgEp4bWU5Rw4li3\_qr9potqxxXTY99V0VQQrp3kz4YyFE4jmibHYAEusc1qRtb8E-x9ilbR8c)

Bu bölüm için bu bağlantı noktası için iki BOD eklemeniz gerekecektir. Bunlar Sync.ChartOfAccounts ve Sync.CodeDefinition olup, bu BOD'ları eklemek için aşağıdakileri yapın:

**Sync.ChartOfAccounts**

* Artı (+) simgesine tıklayın

![](https://lh7-us.googleusercontent.com/aWwQaVreFHJsv5jd8-ZrVt-FAMvt00aO9W3n1KZ2XmUyxtaCGkg6yS6adPOwXJrqRGdFGTDpG4QsXXJG9V6IJeCrWKsKh6SRjl7ZOacLy9-i5K3dA5mWs6Ps6a91K2TNvdUx98OPwEDWWadz3BwaPiQ)

* "API'ye Gönder" i seçin

![](https://lh7-us.googleusercontent.com/uT-PjpDfv7MGB7wwvkYu0M9muSRXtAqMSjk3LKz3xWdtduWHr\_HT1m4ZoETyhP782zOaWBbnEiWxTC9PphoiqogrUNsM5e8PuYutjcwJPqQKAqAlXQMWHOpYru0b7nabzmt\_WqgxEp2Naz2hXViNWzY)

* Sync.ChartOfAccounts BOD'unu arayın

![](https://lh7-us.googleusercontent.com/yQQ92Nn3koBsPG32cPv2Pv9sjdmScGE0WGJ062YSg9q9RDyHnIg-qbh1RA6i7yhfKBeBhgbYEi3uJmR\_z6AdnR9pL49M41hvDoqzvijuPhGm3ZltHExmRtfXdccFc7Ogb44\_Y4gA8VDBXwt5lJsYEW0)

![](https://lh7-us.googleusercontent.com/WcK\_a7Lb61R-5fKGGqzVyR3lAAyyg9jgYunJYC8VNHCsU3Qopvz\_d7EJwXo6RZsbcEos05hv\_sILd-b29Ky4QVz9lNtzvoicT6bBykPKe-WIPPS-OtZ7yXg8VK6MHa5ZzNdqXvR1CUZmnR4WCu3MpSs)

* ION API sekmesine geçin, API adını kopyalayın ve API Çağrısını seçmek için SEÇ düğmesine basarak API Çağrısını arayın

![](https://lh7-us.googleusercontent.com/364Jd0-EBMpWgpgPZukqcjdRlEoGfkgKkB\_U-Y2d87DlB13\_E-ovjnBaeRdPCi4rAMm6Ksc\_MRHAm75y1BPY21HQ12Fjdr6Q0j1YDTBI0Fo5l3LiIHSwL3ITsKbQ-VIBc5aO6O\_DAeKl1z8AUr8xhfo)

* Ürün olarak, ION API'de oluşturduğunuz ortam için oluşturduğunuz API Uç Noktasını seçin. Aşağıdaki API çağrısını arayın, API çağrısını seçin ve TAMAM'a basın.

![](https://lh7-us.googleusercontent.com/NWfGZk5ttI0tWMli1DRZ4SdzC9xHa0LhGR1QbgaeJN1726FYoiqMg1Cb5\_x0TvYu4MlTyJqS9n6c6EfW2veKhcUdvpY-bkK\_uyfRJt6vESmRsVuIx93ipwuffd3YJr3y2sYX5fjFxjRNWEWzH9ojlr8)

* Sonra, İstek Gövdesi sekmesine geçin

![](https://lh7-us.googleusercontent.com/BNwExG0mPZ\_enovlnQh\_SWATS4wDEcOCXuyX98EJza80OxKvrhcFUZ\_l4v88XVBBI-iIjg6eprynpO-zjjNeNsCpgulcUCG8OpGA1SzC-1h\_OyPHTfHlF\_ZsWkpUhT5hz39ruI-TNPo4lelSsvz4jrc)

* Bu BOD için alan eşlemesini yapılandıracağınız yer burasıdır, yapılandırmanız aşağıdakine benzer olmalıdır. Alan eşlemeleri https://docbits.com/doc/field-mappings/ adresinde mevcuttur.

![](https://lh7-us.googleusercontent.com/0O76spiOI\_ZofZiDYRtzuphCzPycktfvxzeEa9MTG3fxeI3bQPjREIyh2sVEwzyGthFzlwdHo1OPifIVpcSMS9yv2WjfIfacCdUQwgvCQu-dXf6aZutRYmrMSCoTFv4mCYtndtLL0-N8NjrlR6oIy-A)

Yukarıdaki adımları tamamladıktan sonra, Sync.ChartOfAccounts BOD'unu başarıyla yapılandırmış olacaksınız. Bir sonraki ve son BOD'u eklemek için ARTI simgesine tıklayın.

**Sync.CodeDefinition (TotalFlexDimensions)**

CodeDefinition bağlantı noktanızın bağlantı sekmesi aşağıdaki gibi görünmelidir. Bağlantı noktasına uygun bir ad ve açıklama verin, ayrıca oluşturduğunuz Hizmet Hesabını içe aktarın.

* "API'ye Gönder" i seçin
* Arama yapın: Sync.CodeDefinition BOD

* ION API sekmesine geçin, API adını kopyalayın ve SEÇ düğmesine basarak API Çağrısını arayın

* Sonra, İstek Gövdesi sekmesine geçin

* Burada bu BOD için alan eşlemesini yapılandıracağınız yerdir, yapılandırmanız aşağıdaki gibi görünmelidir. Alan eşlemeleri https://docbits.com/doc/field-mappings/ adresinde mevcuttur.

Tamamladıktan sonra, Sync.CodeDefinition BOD'u TotalFlexDimensions ana veri tablosu için başarıyla yapılandırmış olacaksınız.

#### **FinalFlexDimensions**

FinalFlexDimensions bağlantı noktanızın bağlantı sekmesi aşağıdaki gibi görünmelidir. Bağlantı noktasına uygun bir ad ve açıklama verin, oluşturduğunuz Hizmet Hesabını içe aktarın.

Bu bölümde bu bağlantı noktası için bir BOD eklemeniz gerekecektir. Bu, Sync.CodeDefinition olacaktır, bu BOD'u eklemek için aşağıdakileri yapın:

CodeDefinition bağlantı noktanızın bağlantı sekmesi aşağıdaki gibi görünmelidir. Bağlantı noktasına uygun bir ad ve açıklama verin, oluşturduğunuz Hizmet Hesabını içe aktarın.

* "API'ye Gönder"i seçin

* Arama yapın: Sync.CodeDefinition BOD

* ION API sekmesine geçin, API adını kopyalayın ve SEÇ düğmesine basarak API Çağrısını arayın
* Sonraki adımda, İstek Gövdesi sekmesine geçin

![](https://lh7-us.googleusercontent.com/LRDKhs2rq92Zef63nYy9NNK6bapmlPKUX10NSrRGBhvhdXIgBRte4sGunmOBUzymgnWnAv1O\_qV0AKsULSXsGT1kvorG0Pl0vQFW0exV2sqyUXhgiBMthRYTQbB10c6oI4P6Z139A8VqZVeg6c2HkZ4)

* İşte bu noktada bu BOD için alan eşleme yapılandırmasını yapacaksınız, yapılandırmanız aşağıdaki gibi görünmelidir. Alan eşlemeleri https://docbits.com/doc/field-mappings/ adresinde mevcuttur.

![](https://lh7-us.googleusercontent.com/bjoXs4ZSra4dgpf2rC8GwA-uB\_Qp6INkdCapR7M03EV7cuqKzeVPWRCq4EHTZVeKpL92sdesL0iuHTHD1Ed5WHpr7Z15XOJMkPBlWgfbapzD4ZjfSre29Ii2SLGOvjs9-85SougBpDGzzTseAcWNVUo)

Yukarıdaki adımları tamamladıktan sonra, Sync.CodeDefinition BOD'unu FinalFlexDimensions ana veri tablosu için başarılı bir şekilde yapılandırmış olacaksınız.

## **Veri Akışları**

Otomatik Muhasebe için iki ayrı veri akışını yapılandırmanız gerekecek:

* HesapPlânı
* FinalEsnekBoyutlar

### **HesapPlânı**

Bu veri akışının genel bir görünümü aşağıdaki gibi görünmektedir (bağlandığınız farklı ortamların sayısına bağlı olarak DocBits API bağlantı noktalarının sayısı değişir).

![](https://lh7-us.googleusercontent.com/xog1wW9zE0PeVF\_SzaVS5qWxR2UuHKVR9cD4n6hxD9IAm\_jqJJHKGMCvmsF4V4bcVhd\_zaepEBrbK6wTd6kd7eqDL2Apwe799ewGo8TwMVrtRPwJcImuRjvWJxmcBiMvTjla0KgoGXhMD6oCeZFvOcM)

#### **LN Şirketi**

![](https://lh7-us.googleusercontent.com/jaFn8KOdu907VI7vx2fkgtJZYiKw37LJ9ySqKWlgm5MLOuUcElJdOCpThwwa2NdE2eJ4iLWdfM\_Nlrkiq0BpIvrZDvyYJng94oZyaOpCIAhF5ZCTwQ0asfceY-KnIjZYrlQ5QsApnvU-hdMp8waQNeA)

Bu bağlantı noktasının yapılandırması, DocBits'e aktarmak istediğiniz ana verilere sahip LN şirketine bağlıdır, sizinki aşağıdakine benzer olmalıdır.

![](https://lh7-us.googleusercontent.com/k28OYp8vkZZcWCKJTiSFZkDE0SlfLgE\_S3o37OhuvNsOR7Tli3xCYzqN3fRTfrlgE9fF9tYkOXCiC7kZeweCGA86wEDEMj0wKRUO7Idba1d8mY-v15uJGpYlkhZEKSlUA83yPvSlp-aRn2e-pYckXyc)

#### **Belge**

![](https://lh7-us.googleusercontent.com/n9ABWRQI8k7SVDk6RsYcvI\_\_r5CWXdMDn49fKkAy3T\_0s3TTJp4aMV5K4hsiGh56YKrxcUaqmUZfj3\_QBSS2eSZ1TAPCoI5-LnJCC-JYv8K5XEOZsJLXX77EKGZCs37qtKiFHD9P9KpW2jhOEX4bu1Y)

Aşağıdaki belgeler veri akışına eklenmelidir:

* Sync.HesapPlânı
* Sync.KodTanımı

![](https://lh7-us.googleusercontent.com/c6Dhk5iR1fJXqjrXsbSMmkIDBl3eaRNoiijw9WMA69HSrXMKqOjMEKtRtqfXbHcy9fQH1etprR2IuZO6xpMBnY6EYuU6cyBCFjHx4yN2KxxRwTqX12TwSsUaF7wFySImLki86BUKRMW-0YKQJfQTWOw)

#### **DocBits (HesapPlânı)**

![](https://lh7-us.googleusercontent.com/JhBa8R1tRR\_GcoBmas\_mJ-QPT3XTNyGAdwh48N7pISM-fRNa3lfuZB7MhAScDbbCtpgGXtxx140w0bcEwgVdtMkGDh6S56uVsm039Z\_8FGA\_FwA2aSvJftr8MeHr3e9WPwRZqugKvRD\_kIVnQdexFek)

Bu, daha önce oluşturduğunuz HesapPlânı API bağlantı noktasını ekleyeceğiniz yerdir, bunun yapılandırması buna benzer olmalıdır

![](https://lh7-us.googleusercontent.com/yyq6JularNBP\_GpUbDLQ-KWu6utcEZefLXcoHboFa6rcmbN1e8QrdLkab9h2QBWuW-V-i7edmqpTWJwtqWg14GKLDnukyLGuljKXue\_XH\_bLmL2dNz5dECDI\_lkg9hO84nFIDyYWYatkzRkxAYyJe6w)

### **FinalEsnekBoyutlar**

Bu veri akışının genel bir görünümü aşağıdaki gibi görünmektedir (bağlandığınız farklı ortamların sayısına bağlı olarak DocBits API bağlantı noktalarının sayısı değişir).

![](https://lh7-us.googleusercontent.com/MQyQxEHmvG0vX4VXSnpntbXBGQBtC5uvMeNXklp-EETOIMLZNOJqwOlZp9xm\_\_Lj--o3bJETADpxgZkajW0H0xOE2Gvib9OeU3BeV-mj4lpKFqPQ8A4fymQJDjTZNI8fzrOxYqa595I0\_C3b8QkoTb0)

#### **LN Şirketi**

Bu bağlantı noktasının yapılandırması, DocBits'e aktarmak istediğiniz ana verilere sahip LN şirketine bağlıdır, sizinki aşağıdakine benzer olmalıdır.

![](https://lh7-us.googleusercontent.com/D25DTQRX3yecDDMmp\_UvmS9b6AWPYue8LdUueurlCTYg0qWw\_SyM0lCx1sn3VSK0m5MOilgmGWJ261YLr1MlTm9G452QyDQXbyN7DXsQpmmINEbVL5g-OIhpYKN14XQk6oEMqwoTgvpLNKS9\_MkU-sk)

![](https://lh7-us.googleusercontent.com/rGMdEdvYixTZ5wmS5ptBiGcxoOT0abpASTeSDzEFH3SSx-G97gSxIniXja2R3erYP4oIxyVezvL7VjqXKcKd5i6caNZHI-1gVIi2jrKfy\_yVFQ5T80n3ZpR1wSiPWCh\_8affNONcGAcuokvN69-Urfg)
#### **Belge**

![](https://lh7-us.googleusercontent.com/WyltkYqwzyofXZpwm\_x1-SiM5MCbvDoKPQ9AVOT6nyxXnqXqQn4G-uM7BO2hNRJii91EODf5mjIwS85eOfJ\_UyATLAWqbXegd54leKsK\_zNlVWQNm79yoyTb\_Ok3605NEOM\_Hu\_ov-yaboAQ26PpmTk)

Aşağıdaki belge veri akışına eklenmesi gerekiyor:

* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/YIvKeqyGUDBZIoi7I6jhTIlUYtsgYEMeKA3h4Xm9KHz5pYWssDuIaq7343RQdEsxMznTNnReWEB2OCqBQGvgzi7HEOVGlX5EqPa2JEO5sC1LpUF-OXvYLO5a7LMbE2h2YY1Bk2rRnNbCjAZqIMuIxGw)

**DocBits (FlexDimensions)**

![](https://lh7-us.googleusercontent.com/zNJteyBB\_TcRKGE7GL3iPPlFaOqbij5ag37NdNW5GcZBz0xMmb9iev8EktCSJDSNkeZPOnCf-5nImxJjn6RIBTg3x8xJrLK-Z0Z48VTXXLPNIO-3NnmDEVVF-9oHteOQWIjCIMhhzKLK7iCL\_jVsfEY)

Bu, daha önce oluşturduğunuz FinalFlexDimensions API bağlantı noktasını eklediğiniz yerdir, bunun için yapılandırma şu şekilde görünmelidir

![](https://lh7-us.googleusercontent.com/ymjxWkOzchUu91ovhE1eE58mSRCyrclNKsNoK48gFcSwKRVuc9Zfy7QZzJ83ATXUWJO4sgPpcNEVPyYZX8dr-sJoEfYKez-WtScX\_hnmOfH-2wBcFKrhxy5wwBUSlKP-ayxcMnCiQ6DKrgqYkfL4xQg)

## **BOD Tetikleme (M3)**

Yukarıdakilerin hepsi tamamlandıktan sonra, Infor LN'ye gidip BOD'leri tetiklemeniz gerekecek, bu sayede Auto Accounting için ihtiyacınız olan çeşitli ana veriler DocBits'e ulaşacaktır.

![](https://lh7-us.googleusercontent.com/OG5eKwuynVhgRagfTwylC2hT6lYMKIgn0ogn1RPShzv7gbE2IO4lC8YzKWDmHa6l6waMREGwVLZmhsCOhUWNrp\_7rkkdrVgo5Z8s84V475UO927BPujEwsX8SY7kRsZBt3R0GUWD13hogj0LdgqNotU)

Yukarıdaki menüden, sol menü sekmesinde, Common → BOD-Messaging → Publish BODs → Publish Financial Master Data'yı seçin. Aşağıdaki menüden, yayınlamak için FlexDimensions ve ChartOfAccounts BOD'larını bulacaksınız.

![](https://lh7-us.googleusercontent.com/KWv\_YZ0BuoZrBvnp2MRzXKRRH1pID7V0iwjCkT4xt7NcbHYoZnFS6wnM\_itC3RzNNGJ95565KynkMFuPb-1NjY0zOGjvlINvVQIrJBcm8daOZa3UiDIB0zBPlt5BS5KavsmYcXHWBQZ9NytMg6NJezs)

Yayınlamak için aşağıdaki BOD'ları seçmek için her kutuyu işaretleyin, tüm bu BOD'ları yayınlamak istediğimiz için başka değişiklikler yapmanıza gerek yoktur, böylece ana veriler DocBits'te tamamlanmış olur.

![](https://lh7-us.googleusercontent.com/cp9CKdRYofwTrRodTNbZDfMmi\_Q23jchyt\_w7hFkGvvoBo89uhSRoKz0uD2cm2M0tLDmrkb6-8qq9z5EfX-ciEmraWqyytxH09jMK8jVVunb8zjK9EkvGhyl07Igoa4sf8hCLvyGnIlHMVjeLzMFrD8)

![](https://lh7-us.googleusercontent.com/cu8PW0WenwC5jBBFa4trAua-d8zYxi60S2syvKHoBoL2Tk9jdQAOQTvUvGZWSR3cpErwDUZ3WHkm4cDCwS1ZhSJyiQltf43\_Re05WddfxQwJ69C3E\_z\_0bMhEwbq3NasV3Q2waKJlfyBk1oIWdVDjps)

Yukarıdaki iki BOD seçildikten sonra, Seçenekler sekmesine gidin

![](https://lh7-us.googleusercontent.com/imBr628dcJJoNBknxVfKjoWindKT\_\_5AzmYDVXIaHF\_n0RWQUSiK07EHH1df0L2xxCOC5z36UQOfsknF4-GwUgZ9tDZcwDosjxChqFft0GGvVo1JAkPpK\_St-GB7NW1RlBgTszID4YQteYiZlFKPuz4)

Seçenekler menüsünde, aşağıdaki seçenekleri seçin ve BOD'ları yayınlamak için İŞLEM'i seçin.

![](https://lh7-us.googleusercontent.com/3LH3Me8kacFfp1QH0VFMIfzQtWyFt12IgRQzcAcJByoPQtjhxDnQKE3EjNLO349WeW2WINoFwwrpQJIOoSXBBM\_tmIecJLJEyLipUHXel5yRw7H98OdfydXJdZcChaHvnnwc86wihiblnthMobZyu\_s)

Bu işlem tamamlandığında, DocBits ortamınızda üç ayrı ana veri tablosunu Master Data Lookup altında görmelisiniz:

* chartofaccounts
* totalflexdimensions
* finalflexdimensions
