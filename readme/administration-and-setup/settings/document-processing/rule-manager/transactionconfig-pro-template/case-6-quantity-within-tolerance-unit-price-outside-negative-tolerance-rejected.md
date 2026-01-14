# Durum 6: Tolerans Dahilinde Miktar, Negatif Tolerans Dışında Birim Fiyat (Reddedildi)

## Senaryo:

Miktar tolerans dahilindedir, ancak birim fiyat kabul edilebilir aralığın altındadır (negatif tolerans) ve onaylanmamıştır.

## Eylem:

Sistem birim fiyatı reddeder, satın alma siparişiyle eşleşecek şekilde ayarlar ve fark için bir alacak notu oluşturur. Gerektiğinde ek başlık masrafları uygulanabilir.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 100 birim
  * Birim Fiyat: 10,00 TL
  * Toplam Tutar: 1.000,00 TL
* **Alınan Fatura:**
  * Miktar: 100 birim (%0 tolerans dahilinde)
  * Birim Fiyat: 9,00 TL (-%10 negatif tolerans dışında)
  * Toplam Tutar: 900,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%2
  * Birim Fiyat Toleransı: ±%1

Miktar (100 birim) kabul edilebilir tolerans aralığında olduğundan ancak birim fiyat (9,00 TL) kabul edilebilir toleransın altında olduğundan ve onaylanmadığından, sistem şunları yapacaktır:

1. **Birim Fiyatı Reddetme:** Sistem, faturalanan 9,00 TL'lik birim fiyatı kabul etmez.
2. **Birim Fiyatı Ayarlama:** Sistem, birim fiyatı orijinal satın alma siparişi birim fiyatıyla eşleşecek şekilde ayarlar.
   * Düzeltilmiş Birim Fiyat = 10,00 TL (PO'dan)
3. **Düzeltilmiş Toplam Tutarı Hesaplama:** Düzeltilmiş birim fiyatı kullanarak sistem toplam tutarı yeniden hesaplar.
   * **Düzeltilmiş Toplam Tutar = Miktar × Düzeltilmiş Birim Fiyat**
   * **Düzeltilmiş Toplam Tutar = 100 birim × 10,00 TL = 1.000,00 TL**
4. **Alacak Notu Oluşturma:** Sistem, faturadaki yanlış toplam tutar ile düzeltilmiş toplam tutar arasındaki fark için bir alacak notu oluşturur.
   * **Alacak Notu Tutarı = Orijinal Fatura Toplamı - Düzeltilmiş Toplam Tutar**
   * **Alacak Notu Tutarı = 900,00 TL - 1.000,00 TL = -100,00 TL**
   * Alacak notu, eksik faturalandırmayı etkili bir şekilde tersine çevirecektir.
5. **Faturayı İşleme:** Sistem, faturayı 1.000,00 TL'lik düzeltilmiş toplam tutarla işler ve eksik faturalanan birim fiyatı hesaba katmak için 100,00 TL'lik alacak notunu uygular.

Bu yaklaşım, yanlış ve daha düşük bir fiyat fatura edildiğinde bile fiyatlandırmanın satın alma siparişi şartlarıyla uyumlu olmasını sağlar.
