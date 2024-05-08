# Tedarikçiler ve Satın Alma Siparişleri

## **Bağlantı Noktası**

Veri akışını oluşturabilmek için DocBits API bağlantı noktasını oluşturmanız gerekecektir.

İlk olarak, InforOS'ta ION Desk → Bağlan → Bağlantı Noktaları'na gidin

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6\_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC\_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Buraya geldikten sonra yeni bir bağlantı noktası oluşturmanız gerekecek.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs\_Hjw3\_NDT49XG\_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**API Seçimi**

Bağlantı noktasına doğasını ve ortamını açıklayan bir ad ve açıklama verin. Bağlantı sekmesinde, çalıştığınız ortam için oluşturduğunuz hizmet hesabını içe aktarın.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT\_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89\_6oJjuq0)

Daha sonra, Belgeler sekmesine geçin. Aşağıdaki BOD'leri bağlantı noktasına eklemeniz gerekecek.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as\_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Bu BOD, Infor içinde bir hata oluştuğunu DocBits'e bildirmek için kullanılır. Bu iki BOD için yapılandırma aşağıdaki gibi olmalıdır (Her API Çağrısı Adı değişir)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X\_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ\_K6qXbtu04AP67G8jrNwkdj32LCgAhy\_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

Bu BOD için yapılandırma aşağıdaki gibi olmalıdır

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4\_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul\_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

Bu BOD için yapılandırma aşağıdaki gibi olmalıdır

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Bu BOD'ler yapılandırıldıktan sonra, bağlantı noktasını kaydedebilmek için geri düğmesinin hemen sağındaki simgeye basmanız gerekecektir.

## **Veri Akışı**

Veri akışı aşağıdakine benzer olacaktır

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(Birden fazla DocBits API'si olmasının nedeni, her bağlantının farklı bir ortamı temsil etmesidir, bu da sahip olduğunuz ortam sayısına bağlı olarak veri akışınızın biraz farklı olabileceği anlamına gelir)

Bu açıklamanın amacı için dört ayrı ortama sahip olduğumuzu varsayalım.

### **LN**

Veri akışının başlangıcı LN uygulamanızdan oluşur

### **DocBits API**

Burada bir uygulama ekleyecek ve daha önce oluşturduğunuz DocBits API'lerini seçeceksiniz

### **Dosyalar**

Yapılandırma aşağıdaki gibi olmalıdır

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J\_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU\_TahhNxBugX\_Bnu3QjZsKHX0Pafae-zU)

## **LN BOD Tetikleme**

Yukarıdakilerin hepsi tamamlandıktan sonra, DocBits'e Tedarikçiler ve Satın Alma Siparişleri için gereken çeşitli ana verilerin ulaşabilmesi için Infor LN'e gidip BOD'leri tetiklemeniz gerekecektir.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n\_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **Satın Alma Siparişi**

Yukarıdaki menüden, sol menü sekmesinde, Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data'ya gidin

Satın Alma Siparişi sekmesini seçin ve kutuyu işaretleyin.

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr\_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B\_\_08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd\_66GAySp3dC1ptYKBaqLqaP1TwJco)
### **Tedarikçiler**

LN ana sayfasından, sol menü sekmesinde, Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data yolunu izleyin.

PartyMaster sekmesini seçin ve Supplier → Buy-from veya SupplierPartyMaster kutusunu işaretleyin.

![](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **BOD Tetikleme**

Doğru BOD'ların tümü yayınlanacak şekilde işaretlendikten sonra, Options sekmesini seçin.

Aşağıdaki seçenekler işaretlenmelidir.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Bu adım tamamlandığında, PROCESS düğmesine basın ve BOD'lar tetiklenecektir. Ekranınızda BOD'ların tetiklendiğine dair bir bildirim mesajı görünecektir.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Başarılı bir şekilde tamamlandığında, Tedarikçi ve Satın Alma Siparişi tabloları Artık Ayarlar → Master Data Lookup altında mevcut olmalıdır.

\
