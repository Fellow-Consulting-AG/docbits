# Durum 8a, 9a: Tolerans Dışında Miktar (Onaylandı), Tolerans Dahilinde Birim Fiyat

## Senaryo:

Faturadaki miktar kabul edilebilir toleransın dışındadır ancak onaylanmıştır, birim fiyat ise tolerans dahilinde kalmaktadır.

## Eylem:

Sistem, faturadaki onaylanan miktarı ve birim fiyatı kabul eder ve işlemi buna göre gerçekleştirir.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 150 birim
  * Birim Fiyat: 12,00 TL
  * Toplam Tutar: 1.800,00 TL
* **Alınan Fatura:**
  * Miktar: 160 birim (%6,67 tolerans dışında ancak onaylanmış)
  * Birim Fiyat: 12,00 TL (tolerans dahilinde)
  * Toplam Tutar: 1.920,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%5
  * Birim Fiyat Toleransı: ±%2

Miktar (160 birim) kabul edilebilir tolerans sınırını aşmasına rağmen onaylandığı için ve birim fiyat (12,00 TL) kabul edilebilir aralıkta olduğundan, sistem şunları yapacaktır:

1. **Onaylanan Miktarı Kabul Etme:** Sistem, normal tolerans aralığının dışında olmasına rağmen miktarın onaylandığını kabul eder.
2. **Birim Fiyatı Kabul Etme:** 12,00 TL'lik birim fiyat kabul edilebilir tolerans dahilindedir, bu nedenle fatura edildiği gibi kabul edilir.
3. **İşlemi Gerçekleştirme:** Sistem, onaylanan miktar ve birim fiyatı kullanarak toplam tutarı hesaplar:
   * **Toplam Tutar = Miktar × Birim Fiyat**
   * **Toplam Tutar = 160 birim × 12,00 TL = 1.920,00 TL**
4. **Faturayı Tamamlama:** Sistem, onaylanan miktarı ve kabul edilen birim fiyatı yansıtacak şekilde 1.920,00 TL'lik toplam tutarla faturayı işler.

Bu yaklaşım, sistemin birim fiyatın beklenen aralıkta kalmasını sağlarken miktardaki onaylanmış sapmalara uyum sağlamasına olanak tanıyarak sorunsuz işlem yürütülmesini kolaylaştırır.
