# Otomatik Satın Alma Sipariş Verisi Eşleme

Docbits, satın alma sipariş verilerini (PO'lar) gelen fatura belgeleriyle otomatik olarak eşleştirmeyi amaçlayan gelişmiş bir sistemdir. Bu araç, fatura verilerinin ERP sistemleri içinde verimli bir şekilde yönetilmesi ve işlenmesi için özel olarak tasarlanmıştır. Bu belge, Docbits aracılığıyla otomatik eşleştirmenin temellerini açıklar ve başarılı eşleştirme için gerekli belirli kuralları tanımlar.

## **Docbits'te Otomatik Eşleştirmenin Temel İlkeleri**

**Veri Çıkarma:** Docbits, dijitalleştirilmiş fatura belgelerinden ilgili verileri çıkararak süreci başlatır. Genellikle, bu veriler her fatura satırının kalemlerinin numaralarını, miktarlarını ve birim fiyatlarını içerir. Bu çıkarma işleminin hassasiyeti sonraki eşleştirme sürecinin temelini oluşturduğundan önemlidir.

**PO Verileriyle Karşılaştırma:** Çıkarılan veriler, depolanan satın alma siparişlerindeki ilgili bilgilerle karşılaştırılır. Docbits, kalemlerin numaralarının, miktarlarının ve fiyatlarının PO'larla eşleşip eşleşmediğini kontrol eder. Başarılı bir eşleşme için, fatura verilerinin, satın alma siparişlerindeki verilere, belirlenen tolerans eşiklerini dikkate alarak uyması gerekir.

**Otomatik Eşleştirme:** Karşılaştırma sonuçlarına dayanarak, Docbits eşleştirmeyi gerçekleştirir. Sistem, eşleşme kriterlerinin belirlenen tolerans sınırları içinde olup olmadığını doğrular. Bu kriterler karşılandığında, eşleşme başarılı kabul edilir.

**Raporlama:** Eşleştirme sürecini tamamladıktan sonra, Docbits eşleşmelerin durumunu gösteren raporlar oluşturur. Bu raporlar, başarılı eşleşen faturalar hakkında bilgi verir ve uyumsuzlukları belirler.

## **Eşleştirme Kurallarının Tanımı**

**Kalem Numarası:** Faturadaki kalem numarası, satın alma siparişindeki kalem numarasıyla tam olarak eşleşmelidir. Kalem numaralarında sapmalar için tolerans yoktur.

**Miktarlar:** Faturada teslim edilen mal miktarı önceden belirlenmiş bir tolerans aralığında değişebilir. Genellikle, teslim miktarlarındaki küçük farklılıkları hesaba katmak için ±5% tolerans kabul edilebilir.

**Fiyatlar:** Fiyat sapmaları belirlenen bir eşik kadar tolere edilebilir. Genellikle, fiyat farklılıklarını kabul etmek için yaygın bir tolerans ±2% olabilir; bu farklılıklar yuvarlama farklılıklarından veya döviz kurlarındaki dalgalanmalardan kaynaklanabilir.

## **Eşleşme Durumu:**

* **Tam Eşleşme:** Tüm veri noktaları (kalem numarası, miktar ve fiyat) belirlenen tolerans sınırları içindedir.
* **Kısmi Eşleşme:** Bir veya daha fazla veri noktası tolerans sınırlarının dışında sapmalar gösterir, ancak sapmalar minimaldir ve manuel incelemeyi gerektirir.
* **Eşleşme Yok:** Bir veya daha fazla veri noktasında önemli sapmalar vardır ve derhal düzeltme veya daha fazla inceleme gerektirir.

Bu kuralların kesin tanımı ve tolerans sınırlarının belirlenmesi, otomatik eşleştirmenin verimliliği ve manuel müdahalelerin azaltılması için önemlidir. Docbits, bu parametrelerin esnek yapılandırılmasına olanak tanır ve çeşitli işletmelerin ve endüstrilerin ihtiyaçlarını karşılamak için uygundur.