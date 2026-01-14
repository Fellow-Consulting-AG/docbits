# Durum 8b, 9b: Tolerans Dışında Miktar (Onaylandı), Tolerans Dışında Birim Fiyat (Onaylandı)

## Senaryo:

Hem miktar hem de birim fiyat tolerans aralığının dışındadır ancak onaylanmıştır.

## Eylem:

Sistem, hem miktar hem de birim fiyat için fatura değerlerini kullanarak işlemi gerçekleştirir ve gerekli ayarlamaları veya kalem masraflarını uygular.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 200 birim
  * Birim Fiyat: 25,00 TL
  * Toplam Tutar: 5.000,00 TL
* **Alınan Fatura:**
  * Miktar: 220 birim (%10 tolerans dışında, onaylanmış)
  * Birim Fiyat: 27,00 TL (%8 tolerans dışında, onaylanmış)
  * Toplam Tutar: 5.940,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%5
  * Birim Fiyat Toleransı: ±%2

Hem miktar (220 birim) hem de birim fiyat (27,00 TL) kabul edilebilir tolerans sınırlarının dışında olmasına rağmen onaylandığı için, sistem şunları yapacaktır:

1. **Onaylanan Miktarı Kabul Etme:** Sistem, tolerans aralığının dışında olmasına rağmen onaylandığı için faturalanan 220 birimlik miktarı kabul eder.
2. **Onaylanan Birim Fiyatı Kabul Etme:** Sistem, tolerans aralığının dışında olmasına rağmen onaylandığı için faturalanan 27,00 TL'lik birim fiyatı kabul eder.
3. **Toplam Tutarı Hesaplama:** Sistem, onaylanan fatura değerlerine göre toplam tutarı hesaplar:
   * **Toplam Tutar = Miktar × Birim Fiyat**
   * **Toplam Tutar = 220 birim × 27,00 TL = 5.940,00 TL**
4. **Gerekli Ayarlamaları veya Kalem Masraflarını Uygulama:** Varsa, sistem kuruluşun onaylanan sapmaları ele alma politikalarına dayanarak ek kalem masrafları veya ayarlamalar uygulayabilir.
5. **Faturayı İşleme:** Sistem, hem miktar hem de birim fiyat için onaylanan değerleri kullanarak faturayı işler ve işlemi 5.940,00 TL'lik toplam tutarla tamamlar.

Bu yaklaşım, esneklik sağlarken doğru finansal kayıtları koruyarak işlemin onaylanan sapmalara göre işlenmesini sağlar.
