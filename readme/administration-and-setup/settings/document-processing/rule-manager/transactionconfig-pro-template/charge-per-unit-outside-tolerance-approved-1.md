# Masraf Kalemi - Tolerans Dışında Birim Başına Masraf (Onaylandı)

## Senaryo:

Birim başına masraf tolerans dışındadır ancak onaylanmıştır.

## Eylem:

Sistem birim başına masrafı kabul eder ve onaylanan masrafları uygular, işlemi buna göre gerçekleştirir.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Birim Başına Masraf: 4,50 TL
  * Miktar: 1.000 birim
  * Toplam Masraf Tutarı: 4.500,00 TL
* **Alınan Fatura:**
  * Birim Başına Masraf: 5,00 TL (%11,11 tolerans dışında, onaylanmış)
  * Miktar: 1.000 birim
  * Toplam Masraf Tutarı: 5.000,00 TL
* **Tolerans Seviyeleri:**
  * Birim Başına Masraf Toleransı: ±%5

Birim başına masraf (5,00 TL) %5'lik kabul edilebilir tolerans aralığının dışında olmasına rağmen onaylandığı için, sistem şunları yapacaktır:

1. **Onaylanan Birim Başına Masrafı Kabul Etme:** Sistem, tolerans sınırını aşmasına rağmen onaylandığı için faturalanan 5,00 TL'lik birim başına masrafı kabul eder.
2. **İşlemi Gerçekleştirme:** Sistem, onaylanan birim başına masrafı ve miktarı kullanarak faturayı işler:
   * **Toplam Masraf Tutarı = Miktar × Onaylanan Birim Başına Masraf**
   * **Toplam Masraf Tutarı = 1.000 birim × 5,00 TL = 5.000,00 TL**
3. **Faturayı Tamamlama:** Sistem, 5.000,00 TL'lik toplam tutarı yansıtacak şekilde onaylanan masraflarla işlemi gerçekleştirir.

Bu yaklaşım, sistemin masraflardaki onaylanmış sapmalara uyum sağlamasına olanak tanıyarak esneklik sağlarken doğru finansal kayıtları sürdürür.
