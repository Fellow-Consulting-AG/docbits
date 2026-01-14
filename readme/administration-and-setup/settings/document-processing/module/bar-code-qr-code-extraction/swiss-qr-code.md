# İsviçre QR Kodu

**İsviçre QR Kodu** (QR-fatura), İsviçre'deki ödeme işlemleri için standartlaştırılmış bir formattır. DocBits, bu kodları otomatik olarak tanıyabilir ve ilgili ödeme bilgilerini çıkarabilir.

## Özellikler

* **Otomatik Tanıma**: Belge üzerindeki İsviçre QR kodunu otomatik olarak algılar.
* **Veri Çıkarımı**: QR kodundan aşağıdaki bilgileri çıkarır:
    * Alacaklı Bilgileri (IBAN, Ad, Adres)
    * Ödeme Referansı
    * Tutar
    * Para Birimi (CHF veya EUR)
    * Borçlu Bilgileri (varsa)
    * Ek Bilgiler

## Yapılandırma

1. **Etkinleştir**: İsviçre QR kodu işlemeyi etkinleştirmek için anahtarı açın.
2. **Eşleme**: Çıkarılan verilerin DocBits içindeki hangi alanlara (örneğin Tutar, Para Birimi, Referans No) aktarılacağını yapılandırın.

<figure><img src="../../../../../../.gitbook/assets/module_swiss_qr.png" alt=""><figcaption></figcaption></figure>
