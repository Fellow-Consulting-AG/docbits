# LN Yapılandırması

## Ön Koşullar

Aşağıdakileri oluşturdunuz:

* Bir ION API Uç Noktası
* Bir ION API Dosyası
* Bir BOD Eşleme Dosyası
* Bir IDM Eşleme Dosyası

## Eşleme Dosyalarını İçe Aktar

Veri akışını kurmadan önce eşleme dosyalarını InforOS'a içe aktarmanız gerekmektedir

ION Desk'te → Bağlan ve Eşlemeleri açın

![](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k)

İçe aktarma simgesine tıklayın

![](https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Buradan, SyncCaptDoc_SyncSuppInv, SyncSupplierInvoice_LoadSupplierInvoice ve LoadSupplierInvoice_ProcessSupplierInvoice gibi ihtiyacınız olan çeşitli eşleme dosyalarını seçmeniz gerekmektedir.
* Tüm eşleme dosyalarını içe aktardıktan sonra, Eşleme gösterge tablosundaki her birinin karesindeki onay simgesine tıklayarak her birini onayladığınızdan emin olun.

## DocBits'ten LN'ye

Bir sonraki adım, Veri Akışını ION Desk'te kurmaktır, ION Desk uygulamasına gidin ve Veri Akışı → + EKLE → Belge Akışı'ını seçin

![](https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Daha sonra bu sayfayı göreceksiniz, burada DocBits'ten M3'e bilgi akışını oluşturacaksınız

![](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Bir LN veri akışı aşağıda gösterildiği gibi görünecektir (her bir yol belirli bir belge türü için olduğundan birden fazla yol bulunmaktadır, bu açıklamada fatura veri akışına odaklanacağız).

![](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U)

Zincirin tüm parçaları üst bölümden sürüklenip bırakılır

Zincirde, DocBits ve LN her ikisi de Uygulamalardır, aralarında veriyi bir sonraki veri akışı bölümü tarafından anlaşılabilir bir forma dönüştüren ve bilgiyi ihtiyaç duyulan yere veya amaçlandığı yere gönderen eşlemeler bulunmaktadır.

![](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### DocBits Uygulaması

"DocBits" gibi uygun bir ad verin, ardından artı işaretini seçin ve önceden oluşturduğunuz bağlantı noktasını (örneğin DocBits_Export veya benzeri) arayın ve üzerine tıklayın.

Bu bağlantı noktasını oluşturmak için, ION Desk'e gidin → Bağlan → Bağlantı Noktaları

![](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

"+ Ekle" yi seçin

![](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos)

"IMS aracılığıyla API Gateway"i seçin ve aşağıdaki bilgileri doldurun

![](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

ION API Client ID'si, "ci" değeri altında oluşturduğunuz ION API Dosyasında bulunmaktadır.

Belge sekmesine geçin ve Sync.CaptureDocument BOD'u DocBits bağlantı noktasına ekleyin

![](https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg)

Ardından bağlantı noktasını kaydedin, sol üst köşedeki disk simgesine basarak

Veri akışınıza erişmek için ION Desk'in Veri Akışı bölümüne geri dönün. DocBits uygulamanız aşağıda gösterildiği gibi olmalıdır.

![](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)
### Eşleme 1

İlk eşleme düğümü aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Eşleme 2

İkinci eşleme düğümü aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### LN Uygulaması

INFOR'da zaten uygun LN şirketi için oluşturulmuş bir LN veya benzeri adlı bağlantı noktası olmalı, bu nedenle DocBits Uygulaması'nı seçmek için "+" işaretine tıklayarak aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BOD'lar

![](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

Aşağıdaki yapılandırmalar aşağıdaki gibi görünmelidir:

#### İlk

![](https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### İkinci

![](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Üçüncü

![](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw)

Son simge belge veya bilgi taşımadığından boş olmalıdır.

Tüm gerekli düğümleri veri akışına ekledikten sonra, veri akışını etkinleştirmek için bu düğmeye basın

![](https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
