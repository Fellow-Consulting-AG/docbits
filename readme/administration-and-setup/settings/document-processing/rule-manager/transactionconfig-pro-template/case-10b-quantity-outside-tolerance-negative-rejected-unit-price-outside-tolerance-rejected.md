# Durum 10b: Tolerans Dışında Miktar (Negatif Reddedildi), Tolerans Dışında Birim Fiyat (Reddedildi)

## Senaryo:

Hem miktar hem de birim fiyat tolerans dışındadır ve hiçbiri onaylanmamıştır.

## Eylem:

Sistem fatura verilerini reddeder, değerleri satın alma siparişiyle eşleşecek şekilde ayarlar ve gerekli borç veya alacak notlarını oluşturur.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 150 birim
  * Birim Fiyat: 30,00 TL
  * Toplam Tutar: 4.500,00 TL
* **Alınan Fatura:**
  * Miktar: 140 birim (-%6,67 tolerans dışında, reddedildi)
  * Birim Fiyat: 33,00 TL (%10 tolerans dışında, reddedildi)
  * Toplam Tutar: 4.620,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%5
  * Birim Fiyat Toleransı: ±%2

Hem miktar (140 birim) hem de birim fiyat (33,00 TL) kabul edilebilir tolerans sınırlarının dışında olduğundan ve hiçbiri onaylanmadığından, sistem şunları yapacaktır:

1. **Fatura Verilerini Reddetme:** Sistem, tolerans sınırlarından sapmaları nedeniyle faturalanan miktarı veya birim fiyatı kabul etmez.
2. **Miktarı Ayarlama:** Sistem, miktarı orijinal satın alma siparişi miktarıyla eşleşecek şekilde ayarlar.
   * Düzeltilen Miktar = 150 birim (PO'dan)
3. **Birim Fiyatı Ayarlama:** Sistem, birim fiyatı orijinal satın alma siparişi birim fiyatıyla eşleşecek şekilde ayarlar.
   * Düzeltilen Birim Fiyat = 30,00 TL (PO'dan)
4. **Toplam Tutarı Yeniden Hesapla:** Sistem, düzeltilen miktar ve birim fiyatı kullanarak toplam tutarı yeniden hesaplar:
   * **Düzeltilmiş Toplam Tutar = Düzeltilen Miktar × Düzeltilen Birim Fiyat**
   * **Düzeltilmiş Toplam Tutar = 150 birim × 30,00 TL = 4.500,00 TL**
5. **Borç Notu Oluşturma:** Orijinal fatura toplamı düzeltilmiş toplamdan yüksek olduğu için sistem, fazla faturalanan tutar için bir borç notu oluşturur.
   * **Borç Notu Tutarı = Orijinal Fatura Toplamı - Düzeltilmiş Toplam Tutar**
   * **Borç Notu Tutarı = 4.620,00 TL - 4.500,00 TL = 120,00 TL**
6. **Faturayı İşleme:** Sistem, faturayı 4.500,00 TL'lik düzeltilmiş toplam tutarla işler ve fazla faturalanan tutarı mahsup etmek için 120,00 TL'lik bir borç notu düzenler.

Bu yaklaşım, finansal işlemin satın alma siparişi şartlarına uyacak şekilde düzeltilmesini sağlayarak doğru ve adil faturalama uygulamalarını sürdürür.
