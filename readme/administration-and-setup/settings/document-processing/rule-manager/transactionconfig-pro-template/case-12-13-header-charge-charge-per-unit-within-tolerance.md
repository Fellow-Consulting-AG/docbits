# Tolerans Dahilinde Birim Başına Masraf

## Senaryo:

Birim başına başlık masrafı, satın alma siparişine kıyasla kabul edilebilir tolerans aralığı içindedir.

## Eylem:

Sistem başlık masrafını fatura edildiği gibi gerçekleştirir, ayarlama yapmadan uygular.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Birim Başına Başlık Masrafı: 3,50 TL
  * Miktar: 1.200 birim
  * Toplam Başlık Masrafı Tutarı: 4.200,00 TL
* **Alınan Fatura:**
  * Birim Başına Başlık Masrafı: 3,55 TL (%1,43 tolerans dahilinde)
  * Miktar: 1.200 birim
  * Toplam Başlık Masrafı Tutarı: 4.260,00 TL
* **Tolerans Seviyeleri:**
  * Birim Başına Başlık Masrafı Toleransı: ±%2

Birim başına başlık masrafı (3,55 TL) satın alma siparişine kıyasla %2'lik kabul edilebilir tolerans aralığında olduğundan, sistem şunları yapacaktır:

1. **Birim Başına Başlık Masrafını Kabul Etme:** Sistem, tanımlanan tolerans sınırı içinde kaldığı için faturalanan 3,55 TL'lik birim başına başlık masrafını kabul eder.
2. **Başlık Masrafını İşleme:** Sistem, faturalanan birim başına masraf ve miktara göre toplam başlık masrafı tutarıyla faturayı işler:
   * **Toplam Başlık Masrafı Tutarı = Miktar × Birim Başına Başlık Masrafı**
   * **Toplam Başlık Masrafı Tutarı = 1.200 birim × 3,55 TL = 4.260,00 TL**
3. **Faturayı Tamamlama:** Sistem, faturayı olduğu gibi kabul ederek herhangi bir ayarlama yapmadan işlemi gerçekleştirir.

Bu yaklaşım, başlık masrafları kabul edilebilir tolerans aralığında kaldığında işlemlerin sorunsuz ve verimli bir şekilde işlenmesini sağlayarak gereksiz reddetmeleri veya gecikmeleri önler.
