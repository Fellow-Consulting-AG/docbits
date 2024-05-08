# Maliyet Faturası - Dışa Aktarım

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.53.28.png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın özellikle maliyet faturalarını yönetmek için yapılandırıldığını ve dışa aktarma eylemini içerdiğini belirtir, muhtemelen raporlama, daha fazla işlem veya diğer sistemlerle entegrasyon için.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, kuralın yalnızca fatura olarak kategorize edilen belgeler için tetiklendiğinden emin olur, fatura yönetiminin özgünlüğünü korur.
2. **Ve…**
* **Belge Alanı Fatura Alt Türü Eşittir Maliyet Faturası ise**: Bu, kuralın yalnızca belirli bir alandaki belgede açıkça "Maliyet Faturası" olarak işaretlenen faturalara uygulandığını belirtir. Bu, diğer fatura türlerinden ayırt etmeye yardımcı olur.
* **Belge Durumu Bekleyen İkinci Onay ise**: Fatura "Bekleyen İkinci Onay" durumunda olmalıdır. Bu, faturanın zaten bir ilk onaydan geçtiğini ve ikinci, muhtemelen son, bir incelemeyi beklediğini gösterir.

#### Eylem (O zaman…):

* **Dışa Aktarmayı Başlat**: Fatura belirtilen koşulları karşıladığında (maliyet faturası olması ve ikinci onayda beklemesi), "Dışa Aktarmayı Başlat" eylemi gerçekleştirilir. Bu, fatura verilerinin finansal analiz, raporlama veya uyumluluk amaçları için başka bir sisteme gönderilmesini içerebilir.

#### Bu Kuralın Amacı:

* **İş Akışı Verimliliği**: Bu kural, maliyet faturalarının işlemlerinin manuel müdahale olmadan gerekli onay aşamalarından geçirilerek otomatikleştirilmesine yardımcı olur, finansal operasyonların hızını ve doğruluğunu artırır.
* **Kontrol ve Uyumluluk**: İkinci bir onay gerektirerek, sistem maliyet faturalarının detaylı bir şekilde incelendiğini sağlayan bir kontrol mekanizmasını zorlar, finansal denetimi artırır.
* **Entegrasyon ve Raporlama**: Dışa aktarma eylemi, faturalar tamamen onaylandığında, bunların başka sistemlere entegre edilebileceğini ve daha fazla işlem veya analiz için kritik olan finansal raporlama ve denetimler için önemli olduğunu önerir.

Bu tür kural, çeşitli fatura türleriyle uğraşan ve her türün belirli protokollere göre ele alındığından emin olmak isteyen organizasyonlar için hayati önem taşır. Hataların riskini azaltır ve iç kontroller ve harici düzenlemelere uyumu sağlar.
