# Standart İş Akışı

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits İş akışı Satın alma Sipariş 4"><figcaption></figcaption></figure>

#### İş Akışı Bileşenlerinin Genel Bakışı:

* **AP Fatura E-postası**: Süreç muhtemelen e-posta aracılığıyla alınan bir fatura ile başlar.
* **DocBits**: Bu araç, faturaların yakalanması ve dijitalleştirilmesi gibi ilk belge yönetimi görevleri için kullanılabilir.
* **Finans İncelemesi**: Faturalar, geçerlilikleri ve doğrulukları konusunda kararların alındığı bir finans incelemesinden geçer.

#### İş Akışındaki Adımlar:

1. **İlk İnceleme**:
* Faturalar DocBits kullanılarak alınır ve başlangıçta işlenir.
* Ardından, finans ekibi tarafından incelenir ve eksiksizse iş akışından çıkarılır veya daha fazla işlem için ileri yönlendirilir.
2. **PO'lar ve PO Olmayan Faturalar**:
* İş akışı, PO'ya ilişkin ve PO olmayan faturalar arasında ayrım yapar.
* PO olmayan faturalar, tedarikçi kimliği, miktar, birim fiyat ve madde numarası gibi önceden belirlenmiş kriterlere göre onay veya reddetme için yönlendirilir.
3. **Eşleşme ve Uyuşmama**:
* Faturalar, mal teslimat fişleriyle karşılaştırılarak detayların eşleştiği kontrol edilir (örneğin, tedarikçi kimliği ve miktar).
* Uyuşmazlıklar oluşursa, fatura daha fazla inceleme ve muhtemelen reddetme sürecine tabi tutulur.
4. **Finans ve Alıcı İncelemesi**:
* PO'ya ilişkin faturalar için, alıcı incelemesini içeren detaylı bir eşleştirme süreci yürütülür.
* Satın alma siparişlerinde veya mal teslimat fişlerinde ayarlamalar gerekebilir.
5. **Son Kararlar**:
* Tüm kontrolleri geçen faturalar onaylanır ve finansal sistemlere entegre edilerek kayıt altına alınır.
* Reddedilen faturalar bildirimleri tetikler ve alıcıdan yeni bir fatura istenebilir.
6. **Infor IDM & LN+M3 ile Entegrasyon**:
* Onaylanan faturalar muhtemelen belge yönetimi için Infor'un IDM'sine ve defter notu almak için LN'ye gönderilir.
* Bu entegrasyon, tüm finansal kayıtların güncel olduğundan ve iş akışının sorunsuz bir şekilde daha geniş ERP sistemine beslendiğinden emin olur.

#### Karar Noktaları:

* İş akışı boyunca, bir faturanın onaylanabileceği, reddedilebileceği veya ek bilgi için geri gönderilebileceği çeşitli karar noktaları bulunmaktadır. Gecikmelerden sonra bildirimler gönderilir, böylece zamanında işlem yapılır.

Bu İş Akışları Standart İş Akışına Dahil Edilecektir.
