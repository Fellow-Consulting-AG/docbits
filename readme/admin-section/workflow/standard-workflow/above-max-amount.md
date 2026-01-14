# Maksimum Tutarın Üzerinde

<figure><img src="../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Fatura 2"><figcaption></figcaption></figure>

Bu başlık, faturanın toplam tutarının onaylayıcının yetkilendirildiği maksimum tutardan büyük olduğu durumları yönetmek üzere tasarlanmış bir kuralı işaret eder.

#### Kural Yapılandırması:

1. **Şu Durumda…**
* **Belge Türü Fatura ise**: Bu koşul, kuralın yalnızca faturalara uygulanmasını sağlar, bu da iş akışını doğru şekilde yönlendirmek için önemlidir.
2. **Ve…**
* **Belge Durumu Onay Bekliyor ise**: Fatura "Onay Bekliyor" durumunda olmalıdır. Bu durum, kuralın hala işlenmekte olan ve henüz tamamlanmamış faturalara uygulandığından emin olmak için önemlidir.
* **İki Alanı Karşılaştır: Toplam Tutar Onaylayıcı Maksimum Tutarından Büyük ise**: Bu koşul, faturanın toplam tutarının bir onaylayıcının işleyebileceği maksimum tutarı aştığını kontrol eder. Bu karşılaştırma, önceden belirlenmiş kriterlere dayalı küçük varyasyonlara izin veren bir tolerans ayarı da içerebilir.

#### Eylem (O zaman…):

* **Next Level Approver alanından kullanıcı atayın, yedek olarak User kullanın**: Fatura belirtilen maksimum tutarı aşıyorsa, otomatik olarak daha yüksek seviyeli bir onaylayıcıya atanır, bu da 'Next Level Approver' alanı tarafından belirtilir. Bu alan dolu değilse veya belirtilen kullanıcı uygun değilse, faturanın gecikmeden incelenmesini sağlamak için bir varsayılan kullanıcı (muhtemelen bir yönetici veya başka bir atanmış personel) yedek olarak kullanılır.

#### Arayüz Öğeleri:

* **Kart Ekle**: Bu seçenek, kurala ek koşullar veya eylemler eklenmesine olanak tanır, karmaşık senaryolarla başa çıkmak için esneklik sağlar.
* **Kaydet**: Bu düğme, kural yapılandırmasını sisteme kaydeder.

#### Bu Kuralın Amacı:

Bu kuralın amacı, belirli finansal eşikleri aşan faturaların uygun yetkilendirme seviyelerine sahip onaylayıcılar tarafından incelenmesini sağlamaktır. Bu, finansal kontrol ve denetimin sürdürülmesine yardımcı olur, harcamaların uygun onay limitlerine sahip personel tarafından incelenmesini sağlayarak, kuruluşu yetkisiz veya uygun olmayan harcamalara karşı korur.

Bu kural, önceki gibi iş akışını otomatikleştirerek manuel çabayı azaltmaya ve kuruluşun finansal politikalarına uyumu artırmaya yardımcı olur. Şirket içinde karmaşık finansal süreçleri yönetmek için iş akışı otomasyonunun etkili bir şekilde nasıl kullanılabileceğinin bir örneğidir.
