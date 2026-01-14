# Durum 15: Başlık Masrafı - Tolerans Dışında Birim Başına Masraf (Reddedildi)

## Senaryo:

Birim başına başlık masrafı tolerans dışındadır ve onaylanmamıştır.

## Eylem:

Sistem başlık masrafını satın alma siparişiyle eşleşecek şekilde ayarlar, işlemi buna göre gerçekleştirir ve gerekli notları oluşturur.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Birim Başına Başlık Masrafı: 4,00 TL
  * Miktar: 1.500 birim
  * Toplam Başlık Masrafı Tutarı: 6.000,00 TL
* **Alınan Fatura:**
  * Birim Başına Başlık Masrafı: 5,00 TL (%25 tolerans dışında, reddedildi)
  * Miktar: 1.500 birim
  * Toplam Başlık Masrafı Tutarı: 7.500,00 TL
* **Tolerans Seviyeleri:**
  * Birim Başına Başlık Masrafı Toleransı: ±%5

Birim başına başlık masrafı (5,00 TL) %5'lik kabul edilebilir tolerans aralığını aştığından ve onaylanmadığından, sistem şunları yapacaktır:

1. **Faturalanan Birim Başına Başlık Masrafını Reddetme:** Sistem, sapma tolerans sınırını aştığı için faturalanan 5,00 TL'lik birim başına başlık masrafını kabul etmez.
2. **Birim Başına Başlık Masrafını Ayarlama:** Sistem, birim başına masrafı orijinal satın alma siparişiyle veya onaylanan birim başına masrafla eşleşecek şekilde ayarlar:
   * Düzeltilmiş Birim Başına Başlık Masrafı = 4,00 TL (PO'dan)
3. **Toplam Başlık Masrafı Tutarını Yeniden Hesaplama:** Sistem, düzeltilen birim başına masrafa göre toplam masraf tutarını yeniden hesaplar:
   * **Düzeltilmiş Toplam Başlık Masrafı Tutarı = Miktar × Düzeltilmiş Birim Başına Başlık Masrafı**
   * **Düzeltilmiş Toplam Başlık Masrafı Tutarı = 1.500 birim × 4,00 TL = 6.000,00 TL**
4. **Alacak Notu Oluşturma:** Orijinal fatura toplamı düzeltilmiş toplamdan yüksek olduğu için sistem, fazla faturalanan tutar için bir alacak notu oluşturur:
   * **Alacak Notu Tutarı = Orijinal Fatura Toplamı - Düzeltilmiş Toplam Başlık Masrafı Tutarı**
   * **Alacak Notu Tutarı = 7.500,00 TL - 6.000,00 TL = 1.500,00 TL**
5. **Faturayı İşleme:** Sistem, faturayı 6.000,00 TL'lik düzeltilmiş toplam masraf tutarıyla işler ve fazla faturalanan tutarı hesaba katmak için 1.500,00 TL'lik bir alacak notu düzenler.

Bu yaklaşım, işlemin satın alma siparişinin orijinal şartlarıyla uyumlu olmasını sağlayarak, fazla faturaları düzeltirken doğru finansal işlemeyi sürdürür.
