# Tedarikçiler ve Satın Alma Siparişleri

## **Bağlantı Noktası**

Veri akışını oluşturabilmek için DocBits API bağlantı noktasını oluşturmanız gerekecektir.

InforOS'ta, ION Desk → Bağlan → Bağlantı Noktaları'na gidin

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Buraya geldikten sonra yeni bir bağlantı noktası oluşturmanız gerekecek.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**API Seçimi**

Bağlantı noktasına doğasını ve ortamını açıklayan bir ad ve açıklama verin. Bağlantı sekmesinde, çalıştığınız ortam için oluşturduğunuz hizmet hesabını içe aktarın.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Daha sonra Belgeler sekmesine geçin. Bağlantı noktasına aşağıdaki BOD'ları eklemeniz gerekecek, tedarikçi ve satın alma siparişi ana verileri için hepsi gerekli olmasa da, diğer özellikler uygulanırken faydalı olacaktır.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Şu anda sadece gerekli BOD'lara odaklanacağız, bunlar: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster ve Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData ve Sync.SupplierPartyMaster

Bu iki BOD için yapılandırma aşağıdaki gibi olmalıdır (her biri için API Çağrı Adı değişecektir)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

Bu BOD için yapılandırma aşağıdaki gibi olmalıdır

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Bu BOD'lar yapılandırıldıktan sonra, bağlantı noktasını kaydedebilirsiniz, geri düğmesinin hemen yanındaki simgeye basarak.

## **Veri Akışı**

Veri akışı aşağıdaki gibi görünecektir

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Birden fazla DocBits API'sının olmasının nedeni, her bağlantının farklı bir ortamı temsil etmesidir, bu da sahip olduğunuz ortam sayısına bağlı olarak veri akışınızın biraz farklı olabileceği anlamına gelir)

Bu açıklamanın amacı için dört ayrı ortama sahip olma örneğini kullanacağız.

### **M3**

Veri akışının başlangıcı M3 uygulamanızdan oluşur

### **Filtre**

Filtrenin yapılandırması aşağıdaki gibi görünür

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(Muhasebe birimi kimliği elbette kuruluşunuza özgüdür)

### **DocBits API**

Burada bir uygulama ekleyecek ve daha önce oluşturduğunuz DocBits API'larını seçeceksiniz
### **Dosyalar**

Yapılandırma aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **M3 BOD Tetikleme**

Infor M3 uygulamasına gidin

Ana menüdeyken, Komut + R tuşlarına basarak komut arama kutusunu açın. Daha sonra evs006 yazın ve arayın.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Bu sayfada, SupplierPartyMaster, RemitToPartyMaster ve PurchaseOrder'ı listeye eklemeniz gerekecek.

BOD ismi: SupplierPartyMaster

Tablo: CIDMAS

BOD ismi: RemitToPartyMaster

Tablo: CIDMAS

BOD ismi: PurchaseOrder

Tablo: MPHEAD

Her durumda, bunları listeye eklemek için artı simgesine basmanız gerekecek.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Her BOD'u ekledikten sonra, BOD'un BOD ismine sağ tıklayın ve İlgili → Çalıştır'ı seçin

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

BOD'ları tetikledikten sonra, BOD fiilini Senkronize olarak değiştirmeniz ve BOD'ları tetiklemek için İLERİ'ye basmanız gerekecek.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

BOD'ları tetikledikten sonra, bunu doğrulayan bir bildirim alacaksınız.

Başarılı bir şekilde tamamlandıysa, Tedarikçi ve Satın Alma Siparişi tabloları Artık Ayarlar → Ana Veri Arama altında mevcut olmalıdır.
