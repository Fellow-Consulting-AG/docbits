# Durum 10a: Tolerans Dışında Miktar (Negatif Reddedildi), Tolerans Dahilinde Birim Fiyat

## Senaryo:

Miktar kabul edilebilir aralığın altındadır (negatif tolerans) ve onaylanmamıştır, ancak birim fiyat tolerans dahilindedir.

## Eylem:

Sistem, miktarı onaylanan seviyeye uyacak şekilde ayarlar ve birim fiyatı tutarlı tutar. İşlem buna göre gerçekleştirilir.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 150 birim
  * Birim Fiyat: 20,00 TL
  * Toplam Tutar: 3.000,00 TL
* **Alınan Fatura:**
  * Miktar: 140 birim (-%6,67 tolerans dışında, reddedildi)
  * Birim Fiyat: 20,00 TL (tolerans dahilinde)
  * Toplam Tutar: 2.800,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%5
  * Birim Fiyat Toleransı: ±%2

Miktar (140 birim) kabul edilebilir tolerans sınırının altında olduğundan (-%6,67'lik negatif sapma) ve onaylanmadığından, ancak birim fiyat (20,00 TL) tolerans dahilinde olduğundan, sistem şunları yapacaktır:

1. **Düşük Miktarı Reddetme:** Sistem, onaylanan tolerans aralığının dışında olduğu için düşük miktarı kabul etmez.
2. **Miktarı Ayarlama:** Sistem, miktarı satın alma siparişinde belirtilen onaylanan seviyeye uyacak şekilde ayarlar.
   * Onaylanan Miktar = 150 birim (PO'dan)
3. **Birim Fiyatı Koru:** Birim başına 20,00 TL olan birim fiyat tolerans dahilindedir ve değişmeden kalır.
4. **Toplam Tutarı Yeniden Hesapla:** Sistem, onaylanan miktar ve kabul edilen birim fiyatı kullanarak toplam tutarı hesaplar:
   * **Toplam Tutar = Onaylanan Miktar × Birim Fiyat**
   * **Toplam Tutar = 150 birim × 20,00 TL = 3.000,00 TL**
5. **Faturayı İşleme:** Sistem, onaylanan miktarı ve birim fiyatı yansıtacak şekilde 3.000,00 TL'lik düzeltilmiş toplam tutarla faturayı işler. Tedarikçinin tam onaylanan miktar için fatura kesmesi beklenir.

Bu yaklaşım, finansal işlemin satın alma siparişinin şartlarıyla uyumlu olmasını sağlar ve doğru finansal kayıtları korurken eksik faturalandırmayı önler.
