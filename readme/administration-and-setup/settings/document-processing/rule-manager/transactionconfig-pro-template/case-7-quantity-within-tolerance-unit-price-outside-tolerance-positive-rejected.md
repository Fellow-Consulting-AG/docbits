# Durum 7: Tolerans Dahilinde Miktar, Tolerans Dışında Birim Fiyat (Pozitif Reddedildi)

## Senaryo:

Miktar tolerans dahilindedir, ancak birim fiyat kabul edilebilir aralığı (pozitif tolerans) aşar ve onaylanmamıştır.

## Eylem:

Sistem fatura birim fiyatını reddeder, satın alma siparişiyle eşleşecek şekilde ayarlar ve fazla faturalanan tutarı hesaba katmak için bir borç notu oluşturabilir.

## Örnek:

* **Satın Alma Siparişi (PO):**
  * Miktar: 200 birim
  * Birim Fiyat: 15,00 TL
  * Toplam Tutar: 3.000,00 TL
* **Alınan Fatura:**
  * Miktar: 198 birim (%1 tolerans dahilinde)
  * Birim Fiyat: 17,00 TL (%13,33 pozitif tolerans dışında)
  * Toplam Tutar: 3.366,00 TL
* **Tolerans Seviyeleri:**
  * Miktar Toleransı: ±%2
  * Birim Fiyat Toleransı: ±%1

Miktar (198 birim) kabul edilebilir tolerans aralığında olduğundan ancak birim fiyat (17,00 TL) kabul edilebilir toleransı aştığından ve onaylanmadığından, sistem şunları yapacaktır:

1. **Fatura Birim Fiyatını Reddetme:** Sistem, faturalanan 17,00 TL'lik birim fiyatı kabul etmez.
2. **Birim Fiyatı Ayarlama:** Sistem, birim fiyatı orijinal satın alma siparişi birim fiyatıyla eşleşecek şekilde ayarlar.
   * Düzeltilmiş Birim Fiyat = 15,00 TL (PO'dan)
3. **Düzeltilmiş Toplam Tutarı Hesaplama:** Düzeltilmiş birim fiyatı kullanarak sistem toplam tutarı yeniden hesaplar.
   * **Düzeltilmiş Toplam Tutar = Miktar × Düzeltilmiş Birim Fiyat**
   * **Düzeltilmiş Toplam Tutar = 198 birim × 15,00 TL = 2.970,00 TL**
4. **Borç Notu Oluşturma:** Sistem, fazla faturalandırmadan kaynaklanan farkı hesaba katmak için bir borç notu oluşturur.
   * **Borç Notu Tutarı = Orijinal Fatura Toplamı - Düzeltilmiş Toplam Tutar**
   * **Borç Notu Tutarı = 3.366,00 TL - 2.970,00 TL = 396,00 TL**
   * Bu borç notu, tedarikçi tarafından fazla faturalanan tutarı temsil eder.
5. **Faturayı İşleme:** Sistem, faturayı 2.970,00 TL'lik düzeltilmiş toplam tutarla işler ve fazla faturalandırmayı mahsup etmek için 396,00 TL'lik bir borç notu düzenler.

Bu yaklaşım, her türlü fazla faturalandırmanın düzeltilmesini sağlayarak işlemi satın alma siparişi şartlarıyla uyumlu hale getirir ve işletmenin finansal çıkarlarını korur.
