# Durum 11a: Tolerans Dışında Miktar (Pozitif Reddedildi), Tolerans Dahilinde Birim Fiyat

## Senaryo:

Faturadaki miktar kabul edilebilir aralığı (pozitif) aşar ve reddedilir, ancak birim fiyat tolerans dahilindedir.

## Eylem:

Sistem, miktarı onaylanan seviyeye ayarlar, birim fiyatı korur ve işlemi gerçekleştirir. Fazla miktar reddedilir ve faturalanmaz.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 100 birim
  * Birim Fiyat: 8,00 TL
  * Toplam Tutar: 800,00 TL
* **Alınan Fatura:**
  * Miktar: 110 birim (%10 tolerans dışında, reddedildi)
  * Birim Fiyat: 8,00 TL (tolerans dahilinde)
  * Toplam Tutar: 880,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%5
  * Birim Fiyat Toleransı: ±%2

Miktar (110 birim) kabul edilebilir tolerans sınırını aştığı için (%10 pozitif sapma) ve onaylanmadığı için, ancak birim fiyat (8,00 TL) tolerans dahilinde olduğundan, sistem şunları yapacaktır:

1. **Fazla Miktarı Reddetme:** Sistem, onaylanan tolerans seviyesini aşan miktarı reddeder.
2. **Miktarı Ayarlama:** Sistem, miktarı satın alma siparişinde belirtilen onaylanan seviyeye uyacak şekilde ayarlar.
   * Onaylanan Miktar = 100 birim (PO'dan)
3. **Birim Fiyatı Koru:** Birim başına 8,00 TL olan birim fiyat tolerans dahilindedir ve değişmeden kalır.
4. **Toplam Tutarı Yeniden Hesapla:** Sistem, onaylanan miktarı ve kabul edilen birim fiyatı kullanarak toplam tutarı hesaplar:
   * **Toplam Tutar = Onaylanan Miktar × Birim Fiyat**
   * **Toplam Tutar = 100 birim × 8,00 TL = 800,00 TL**
5. **Faturayı İşleme:** Sistem, yalnızca onaylanan miktarı ve birim fiyatı yansıtacak şekilde 800,00 TL'lik düzeltilmiş toplam tutarla faturayı işler. 10 birimlik fazla miktar reddedilir ve faturalanmaz.

Bu yaklaşım, tedarikçi fazla miktar için fatura kesmeye çalışsa bile, faturalanan tutarın satın alma siparişinde kararlaştırılan şartlarla uyumlu olmasını sağlar.
