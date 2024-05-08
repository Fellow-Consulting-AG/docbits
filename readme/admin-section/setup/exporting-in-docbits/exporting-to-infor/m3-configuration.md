# M3 Yapılandırması

## Ön Koşullar

Aşağıdakileri oluşturdunuz:

* Bir ION API Uç Noktası
* Bir ION API Dosyası
* Bir BOD Eşleme Dosyası
* Bir IDM Eşleme Dosyası

## Eşleme Dosyalarını İçe Aktar

Veri akışını kurmadan önce eşleme dosyalarını InforOS'a içe aktarmanız gerekmektedir.

ION Desk'te → Bağlan'a gidin ve Eşlemeleri açın

![](https://lh7-us.googleusercontent.com/EV8z6b_W9tjTgML0j3qJAYHCTYLd4N5yLrArdIECftYpMOCRTRJ_a7eADEzljFM4XHxMUJ6Nx9Z6EN3Hmzote5F0HrM5zd4p1BS0NYicUWDnkhQFX-_3MGbblEYi6x2a1K25SclYYttgW3cWQbOjvfQ)

İçe aktar simgesine tıklayın

![](https://lh7-us.googleusercontent.com/agBHtjNitneogoZsSG1791QAARbvesv9eSriAkw0HL9Fy372Ty6SmQG1sKJjOYZCuE0SnGT3agHAFRJYjgGNxJrN1CMJj9L-fSPhNmXxN78iDKqrrdgEVYFHxsNwy9XLiUFpBCQ1wnWlwyeFH08DsWI)

Buradan, ihtiyacınız olan çeşitli eşleme dosyalarını seçmeniz gerekmektedir: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice ve LoadSupplierInvoice\_ProcessSupplierInvoice.

Tüm eşleme dosyalarını içe aktardıktan sonra, Eşleme gösterge tablosundaki her birinin karesindeki onay simgesine tıklayarak her birini onayladığınızdan emin olun.

## DocBits'ten M3'e

Bir sonraki adım, Veri Akışını ION Desk'te kurmaktır, ION Desk uygulamasına gidin ve Veri Akışı → + EKLE → Belge Akışı'ını seçin

![](https://lh7-us.googleusercontent.com/Kkro7w2LPfnwf-JPMmPI2DzrSRNEi_F9aWW02KDtBvAZz_R7j9DZ71Nqw3ETPSQqDuxBzJ1TU8Uuzz5jU9rOO_tvDBf9abVF-FDSxln_pjr-HMRdYBnGMwgcM6hg-pC2B7FgdBkXibivMB4PptvZ6fk)

Daha sonra bu sayfayı göreceksiniz, burada DocBits'ten M3'e bilgi akışını oluşturacaksınız

![](https://lh7-us.googleusercontent.com/K0B1lC_KLO5RZqGqAltp6JnZZ1sfZG4wg-i_nxZCnLjML33yvViRUHOInK3iHYbzbV4I0uqDY8JpsZMxssD8bbJy24A1zKr9PfQEyqVxewx_L87RCIwzn5MDRjMqgx4X42vkKthbyz--5DDe1H0rvHQ)

Bir M3 veri akışı aşağıda gösterildiği gibi görünecektir (3 ayrı ortam için kullanıldığından 3 DocBits uygulaması ve API'si bulunmaktadır).

![](https://lh7-us.googleusercontent.com/6Oy_UBzYNml-7_sayDEKhqYF92yDzlUNzmGLQSWZOfDT-avvfg3oNUnv_DtXNSP0XF43D-zgIizIuTrCXl6ockLU2uQLYFJna72fzL5BP-T89xjF4oWz2eAz9w0hsoVieyTpgSw_Prvj--89Kc4Kqoo)

Zincirin tüm parçaları üst bölümden sürüklenip bırakılır

Zincirde, DocBits ve M3 hem Uygulamalar iken aralarında veriyi bir sonraki tren bölümü tarafından anlaşılabilir bir forma dönüştüren ve bilgiyi ihtiyaç duyulan yere veya amaçlandığı yere gönderen eşlemeler bulunmaktadır.

![](https://lh7-us.googleusercontent.com/1kjgKNmIQ-NbM_JukcPsj7qmyiMB9b693ixg6Dh1kOlZ6NKgBXViYwn0MNUBHt0WKKWf_1gpRvxgqjIaqpqcy-SyXoYjhJLt3m_bv7wbVADzqHRsx8TYXWyIQO82X-Ixfl5b7iI7nxTRkw06sX3xsBM)

### DocBits Uygulaması

Uygun bir ad verin, örneğin "DocBits", ardından artı işaretini seçin ve önceden oluşturduğunuz bağlantı noktasını arayın, örneğin DocBits_Export veya benzeri ve üzerine tıklayın.

Bu bağlantı noktasını oluşturmak için ION Desk → Bağlan → Bağlantı Noktaları'na gidin

![](https://lh7-us.googleusercontent.com/8qsMIUKMrgmcYqqJPL2zF4GVeHuvSHvn8Z7dfonRuvKFPcXmN4hx2PIrXko4lvW7ayD7s2VRFOMvWkQSxfAH5tTuhg0XhzYmSzlsgnowWRw8GmQC2y5BjcS9X2MjDzLSutgoHg2VN59kCYRunMSxkIY)

"+ Ekle" yi seçin

![](https://lh7-us.googleusercontent.com/-3-3TzgEQppYmX64-clxjp1JBjNz9fsA2FDPqirgNF0wL8DsDJACzUBuSw5wBL2k9JanqvMzAG352CWafOdtjhMfZalJnBFVSjaWA1AszhCjKtCsTvLUUqq1WwMfF-PqL-u7LRo4TPbj4fP2_j48240)

"IMS aracılığıyla API Gateway"i seçin ve aşağıdaki bilgileri doldurun

![](https://lh7-us.googleusercontent.com/wImUEi9mXiQjW5O6mp7_IrKk4CTaHFs903DJ6TXqUEcjGq45TnUWdusFTGH1jzpBPP_TC7rokyjrkYWmh3emSKBQs05qYbO80TO87De0C5OveVURykQMCLFRRYakEMoFHpoeXzxH5QIbKJdjxujeY98)

ION API İstemci Kimliği, "ci" değeri ile bulunan ION API Dosyanızda bulunur. 

Belge sekmesine geçin ve Sync.CaptureDocument BOD'u DocBits bağlantı noktasına ekleyin

![](https://lh7-us.googleusercontent.com/ga1q0Uwdi2GNwuiz22NvDtCzGL0krSkBPLsEVxE-mtoMV7CtEU8TPO0PhF40oB9NB9iv7DCJi9niLnsKjpqarWJsgGRdc1W0pFl9rTDm7i2_BSLj3JOrzR7iclPdqOdpztgCxWZG2Teg1gWljaMUq2E)

Ardından bağlantı noktasını kaydedin, üst sol köşedeki disk simgesine basarak

Veri akışınıza erişmek için ION Desk'in Veri Akışı bölümüne geri dönün. DocBits uygulamanız aşağıda gösterildiği gibi görünmelidir.

![](https://lh7-us.googleusercontent.com/fBzKL6RU0XvGpn1cKFZIyAp2amKonBWc8ilbAq5u_r867xywWWAD7EjP-g-wjlwUsrG4Wz0lS6Ujdnu8P3vc8Q3FbtbRR4qSBmbSLoICfX-aHITMDdHp07bESefC9TuUUUQiHGb1j00HNtB_7A3iDFs)
### Eşleme 1

İlk eşleme düğümü aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/F9AcE4V-s9vs-0kRz8BcCtdHUUQoaooyK3GqOj8pAQWuvIguoUO-tJx7WBEW6\_GmzwNsJp8VUYezGCiLPXvPhEynac3FPh\_NJOvqs1SXtMIUsF5\_HjWmcvY3VC-eZsjG0ZE8HmsKsFhocadr96drSbY)

### Eşleme 2

İkinci eşleme düğümü aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/8M\_V2BtkOGyqV-828ct5c2QvSs5n5\_RtLjlH717kspZwlgtfjbz6tpOJCCXDelruBenMjxsJPqncQ5hUw2bQkM3ya7\_WrVyEBz3UnaU-C9oVOWB8nNtXA20RBYgO3EBMon2TfgpefY0lSPBzF9NoTeU)

### Eşleme 3

Üçüncü eşleme düğümü aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/x9QUHTgQrNaeKnTeMIUflkWjcBr2c3LgsYe2BZBjv01hXiEkvsLtU0GzYt5KppcE12ZqxWeBJ1kbLOC6qA3yKHhujCZt3sFpDNE5yERkHHMJJEjFl0jJE90nQ-iXeMLbR-Bk6G0NIL8AqG3U48Seiuc)

### M3 Uygulaması

INFOR'da zaten M3 veya benzeri adıyla oluşturulmuş bir bağlantı noktası olmalı, bu nedenle DocBits Uygulaması'nı seçmek için "+" işaretine tıklayarak aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/JTXIN5QxidvFJyjegxSw8kA7yVfHfuypxi5yX21CsSlGtOVgykc52U2r0077-cKqNhc0B4zSSZotlipFesmLo371kho3wUSRPzmwEir-stbxyZV1PwCDXkq6qJMm4PNXt\_wGarDMixGIU0tu-eAqV5Y)

### DocBits API

Bu API'yi ilk olarak bir bağlantı noktası olarak oluşturmanız gerekecek, bunu şu şekilde yapabilirsiniz:

ION Desk → Bağlan → Bağlantı Noktaları

![](https://lh7-us.googleusercontent.com/VOXW6LixmcKjHW0CTOO5L8fK6r-4k3jqk0AnoR6DEVoGgJMbx65hS3yKSgMWItypdz4Ha82T-bKCN0aMv34gif-b0Aw7zpDFPBK9G-K6x9\_csrM9xyKcpmWam15tKqO1\_rwKtMsJ2CSoWqdpLxCD5tA)

"+ Ekle" yi tıklayın ve API'yi seçin

![](https://lh7-us.googleusercontent.com/c1RAUNoA3YBhvf6FLJ\_L3ouyZwHK-3bBRU83eL3oAQXjG6SjWEO9O-gDKPItPm8AI\_YhadaCZU-GxY-qUXNuQMiRiKUhBYUtJ8kOFVg\_YYpzJDSoJ68NYSaEtHBSyyfnq0VbHUdWY1e8lBQ0j\_G5xvI)

Doldurmanız gereken bilgiler aşağıdaki gibi görünmelidir

![](https://lh7-us.googleusercontent.com/h2KU6pKeKl9wX8oyul0KmbL\_kg-iPQJpBqbf29l64ED2e-Z4tNj8-m4hBN\_4SSiNPf2TrE92TD4H0-0AZ0eWxMFmDV22IdPlU9NO4XlQF9k0Swg0X3Sm1HMsSPvWi7Q1HUr8uy8j3aDRheFxZqZ2Gbc)

Belge sekmesine geçin ve aşağıdaki yapılandırmayı ekleyin

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_api\_docs1-1024x279.png)

**Acknowledge.SupplierInvoice**

Bu BOD için yapılandırma aşağıdaki gibidir

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_11.png)

Yukarıdaki menüde "API'ye Gönder" seçeneğini seçtiğinizden emin olun.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_2-1024x338.png)

Son olarak, istek gövdesini de aşağıdaki gibi değiştirdiğinizden emin olun.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_3-1024x260.png)

Diğer BOD'lar için bu işlemi tekrarlayın, her yapılandırma aşağıda gösterilmiştir.

**Sync.PurchaseOrder**

Bu BOD için yapılandırma aşağıdaki gibidir

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_2-1024x359.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_3-1024x297.png)

**Sync.RemitToPartyMaster**

Bu BOD için yapılandırma aşağıdaki gibidir

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_1-1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_2-1024x351.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_3-1024x299.png)

**Sync.SupplierPartyMaster**

Bu BOD için yapılandırma aşağıdaki gibidir

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_2.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_3-1024x295.png)

### BOD'lar

![](https://lh7-us.googleusercontent.com/zaDSnm844wXqyefN58Y1DvuJOnMaoOrYQ\_12Z5ZSng8-TPy38Th2ZPdAD6hyIYCOvBKGPDSvGpTmtBPq4K5IwyGtsKyMvk-CKOuY-hzD-RL7UrsG39qLN7m3\_IDcDS66KeIQF5e70OWlHO1cbVvQUXM)

Aşağıdaki yapılandırmalar aşağıdaki gibi görünmelidir:
#### İlk

![](https://lh7-us.googleusercontent.com/5gLpbQEYYW90dVLkSc5V60LeToMe2wcOcHHtwTdIdT0o0Gktu8T_7i7zfNikjgETM3QmzAsJAknlEGeB0W0YFLLi56g2PKPwyr2zPcHaKdu8XJWHgaC1u4--_CHNYfd1wQ__3kZpv1_PwyZty3JEyak)

#### İkinci

![](https://lh7-us.googleusercontent.com/xbWTcP8hYA72Ijt7_IV6l-9jKeSalbRPvTn7aNVcnWYMQcD2RDjM-EzKpBKjSIKF_-r8BaxmmCo9uz6-E-vC9flKb4toU3SH24EPLgbXc-VcfJeDdJKglf5P6WV6XYZg0cZVWAoyvS8qgtuR6ZqJYlI)

#### Üçüncü

![](https://lh7-us.googleusercontent.com/F8wVWXuHkLLW2kuu_7Dxe9LhyYdm04tl__Sp6FjeTyk_JFUzhCIUhVlKS_cq3I3FP_h2ksV4zEJHFC_KXK6sSZ5iz5yhTFZcPnH1HS_RvZb2Nr-UXYQ1H316UMoj6eRv6wMn3wHX842B5WVfPHVnJ74)

#### Dördüncü

![](https://lh7-us.googleusercontent.com/myhi9y2sCvS5ZFkIJa5ysLbu7p0X6CYqbiuJ3sQ5-O-2QWlfAseunjwhXK0kakmAofplm0zmh_H1Np7bA559w0-jdurQUsZwYF9CyKYSKSeGnQaIit0HQ5iN-3Xv8CIC-5nk6mMj3JTDS97SlzbsOFE)

#### Beşinci

![](https://lh7-us.googleusercontent.com/c-5iaUhhx0swH-mQfXE5Mdwe4J0skGt7mst4kJdOpjL3Uat329TZmKM5Af-lGQWmcmBht-ib_aUj4dVG7GaUAHHULjly3jxsR8MJNnLDcu5eZB268Vy-dXPxHmkVB8dMZTRhU5SUB59AREurJlW-K6o)

Son simge boş olmalı çünkü herhangi bir belge veya bilgi taşımıyor.

Tüm gerekli düğümleri veri akışına ekledikten sonra, veri akışını etkinleştirmek için bu düğmeye basın (veri akışını diske kaydederek kaydedin düğmesine basarak). 

![](https://lh7-us.googleusercontent.com/WIecHktG7e5dbVScLbR8hUcZUdCEWXBW4xWDEuq0IqTMmguA_Ih_oRymvpk6CzowWFG5TTSCPIH-68ICnPSOPxeZksc-n4bmpvuH8dvHuHFU1DlppGRno3PKjCSJiK12p9bNlo_9cN2t9Ps3nbqF3xE)
