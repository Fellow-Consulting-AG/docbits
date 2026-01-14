# Durum 11b: Tolerans Dışında Miktar (Pozitif Reddedildi), Tolerans Dışında Birim Fiyat (Reddedildi)

## Senaryo:

Miktar kabul edilebilir aralığı (pozitif) aşar ve reddedilir, birim fiyat da tolerans dışındadır ve reddedilir.

## Eylem:

Sistem, miktarı ve birim fiyatı satın alma siparişindeki onaylanan seviyelerle eşleşecek şekilde ayarlar, fazlalıkları reddeder ve işlemi gerçekleştirir.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 200 birim
  * Birim Fiyat: 50,00 TL
  * Toplam Tutar: 10.000,00 TL
* **Alınan Fatura:**
  * Miktar: 220 birim (%10 tolerans dışında, reddedildi)
  * Birim Fiyat: 55,00 TL (%10 tolerans dışında, reddedildi)
  * Toplam Tutar: 12.100,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%5
  * Birim Fiyat Toleransı: ±%2

Hem miktar (220 birim) hem de birim fiyat (55,00 TL) kabul edilebilir tolerans sınırlarını aştığı ve hiçbiri onaylanmadığı için, sistem şunları yapacaktır:

1. **Fazla Miktarı Reddetme:** Sistem, faturalanan 220 birimlik miktarı kabul etmez ve orijinal satın alma siparişine uyacak şekilde ayarlar.
   * Düzeltilmiş Miktar = 200 birim (PO'dan)
2. **Fatura Birim Fiyatını Reddetme:** Sistem, faturalanan 55,00 TL'lik birim fiyatı kabul etmez ve orijinal satın alma siparişine uyacak şekilde ayarlar.
   * Düzeltilmiş Birim Fiyat = 50,00 TL (PO'dan)
3. **Toplam Tutarı Yeniden Hesapla:** Sistem, düzeltilen miktar ve birim fiyatı kullanarak toplam tutarı hesaplar:
   * **Düzeltilmiş Toplam Tutar = Düzeltilmiş Miktar × Düzeltilmiş Birim Fiyat**
   * **Düzeltilmiş Toplam Tutar = 200 birim × 50,00 TL = 10.000,00 TL**
4. **Faturayı İşleme:** Sistem, fazla miktarı ve daha yüksek birim fiyatı reddederek 10.000,00 TL'lik düzeltilmiş toplam tutarla faturayı işler.

Bu yaklaşım, işlemin satın alma siparişinin orijinal şartlarıyla uyumlu olmasını sağlar, onaylanmamış sapmaları reddederken tutarlı fiyatlandırma ve miktar kontrollerini sürdürür.
