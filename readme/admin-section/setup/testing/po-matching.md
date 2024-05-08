# PO Eşleme

PO Eşleme yapılandırmanızı test etmek söz konusu olduğunda, INFOR'da bir Satın Alma siparişi oluşturmanız gerekecek ve INFOR'un DocBits ile senkronize olup olmadığını kontrol etmek için LN/M3'de bir Satın Alma siparişi oluşturmanız gerekecek. 

## INFOR'da Satın Alma Siparişi Oluşturma

* LN: [LN Kılavuzu](https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf)
* M3: [M3 Kılavuzu](https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html)

Satın alma siparişinizi oluşturduktan sonra, Ayarlar → Ana Veri Arama'ya gidin ve oluşturduğunuz PO'nun satın alma siparişi numarasını arayın, çünkü şimdi bu numaranın DocBits'te satın alma siparişi ana verilerinizde görünmesi gerekmektedir.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Benzersiz PO numaranızı burada görmelisiniz, bu DocBits ve INFOR'un doğru şekilde senkronize olduğu anlamına gelir.

Şimdi, oluşturduğunuz satın alma siparişinin miktarı ve birim fiyatlarıyla eşleşen faturanızı yükleyin. Belgeyi doğrulayın ve doğrulama ekranında PO Eşleme'yi seçin.

PO ve fatura kalemleri otomatik olarak eşleşmelidir, ardından sadece dışa aktarma seçeneğini seçin ve belgenin herhangi bir hata olmadan dışa aktarılıp aktarılmadığını kontrol edin. Bir dışa aktarma hatasıyla karşılaşırsanız, DocBits destek ekibine yardım etmeleri için bir destek talebi oluşturun. DocBits içinde bir destek talebi nasıl oluşturulacağını bilmiyorsanız, yardım için DocBits Genel Bakış belgemize başvurun.
