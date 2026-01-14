# Durum 1, 2, 3: Tolerans Dahilinde Miktar ve Birim Fiyat

## Senaryo:

Faturadaki hem miktar hem de birim fiyat, satın alma siparişine kıyasla kabul edilebilir bir tolerans aralığı içindedir.

## Eylem:

Sistem fatura değerlerini kabul eder ve sağlanan miktar ve birim fiyata göre toplam tutarı hesaplar.

## Örnek:

**Satın Alma Siparişi (PO):**

Miktar: 100 birim

Birim Fiyat: 10,00 TL

Toplam Tutar: 1.000,00 TL

**Alınan Fatura:**

Miktar: 101 birim (%1 tolerans dahilinde)

Birim Fiyat: 10,05 TL (%0,5 tolerans dahilinde)

Toplam Tutar: 1.015,05 TL

**Tolerans Seviyeleri:**

Miktar Toleransı: ±%2

Birim Fiyat Toleransı: ±%1

Miktar (101 birim) ve birim fiyat (10,05 TL) satın alma siparişine kıyasla kabul edilebilir tolerans seviyeleri içinde olduğundan, sistem şunları yapacaktır:

1. **Fatura Değerlerini Kabul Etme:** Faturadaki miktar ve birim fiyat, tanımlanan tolerans sınırları içinde kaldıkları için geçerli kabul edilir.

2. **Toplam Tutarı Hesaplama:** Toplam tutar, kabul edilen değerler kullanılarak hesaplanır:

• Toplam Tutar = Miktar × Birim Fiyat

• Toplam Tutar = 101 birim × 10,05 TL = 1.015,05 TL

3. **Faturayı İşleme:** Fatura 1.015,05 TL tutarıyla işlenir ve finansal kayıtlar buna göre güncellenir.

Bu yaklaşım, kabul edilebilir tolerans seviyeleri içinde kalan küçük tutarsızlıkların fatura reddine veya ödeme gecikmelerine yol açmamasını sağlayarak finansal süreci kolaylaştırır.
