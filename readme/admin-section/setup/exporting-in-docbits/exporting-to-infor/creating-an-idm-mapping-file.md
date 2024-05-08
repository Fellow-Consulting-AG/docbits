# IDM Eşleme Dosyası Oluşturma

Elde edildikten sonra dosyayı tercih ettiğiniz uygun dosya düzenleyicinizde açın. Bu adımda, VSCode kullanılacaktır.

## Eşleme Dosyasını Düzenleme

Belge türü kodunun DocBits'teki gibi olduğundan emin olun (örneğin, BOD Eşleme Dosyası'nda alan ayarları URL'sindeki belge türü adıyla eşleşmelidir) ve ayrıca belge türünün adının Infor'daki Belge Yöneticisi (IDM) içinde olduğu gibi olup olmadığını kontrol edin.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**Bilgi**: Belge türünün IDM'deki adının M3\_SupplierInvoice olduğu belirtilmektedir, bu, M3 örneğinden bir örnek olmasından kaynaklanmaktadır. Bu, LN veya M3 kullanıp kullanmadığınıza ve belirli IDM yapılandırmanıza bağlı olarak değişebilir.

Şirket kimliğini kontrol edin ve Entity ID'yi (SF\_MDS\_EntityType) kontrol edin, bu değer BOD Eşleme Dosyasında olduğu gibi olmalıdır.

IndexFieldFromDocBits=IDMAttributeID olmasını sağlayın (alan ayarlarında DocBits'in solunda IDM'in sağında olduğunu Belge Türü → Öznitelikler'de kontrol edin).

### Infor'daki Belge Yöneticisi

Belge Yöneticisine gidin ve dışa aktarmaya çalıştığınız mevcut belge türünün adını seçin, örneğin, Tedarikçi Faturası.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Yukarıdaki simgeye tıklayın ve ardından Yönetim → Belge Türü'ne tıklayın ve ihtiyacınız olan belge türünü listeden bulun

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Aşağıdaki gibi, belge türü adını INFOR'da göreceksiniz

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Bu adın IDM Eşleme Dosyasında nasıl gösterildiğinden emin olun

## Dosyayı DocBits'e Yükleme

Dosya hazır olduğunda, onu DocBits'teki dışa aktarma yapılandırmanıza yükleyin. Bu, Ayarlar → Dışa Aktarım'da mevcuttur. 

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
