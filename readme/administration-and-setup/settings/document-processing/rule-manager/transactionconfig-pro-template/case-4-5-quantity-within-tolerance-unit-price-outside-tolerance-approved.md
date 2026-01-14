# Durum 4, 5: Tolerans Dahilinde Miktar, Tolerans Dışında Birim Fiyat (Onaylandı)

## Senaryo:

Faturadaki miktar tolerans dahilindedir, ancak birim fiyat kabul edilebilir tolerans aralığının dışındadır. Ancak, birim fiyattaki bu sapma ilgili makamlarca incelenmiş ve onaylanmıştır.

## Eylem:

Sistem, birim fiyatı satın alma siparişiyle eşleşecek şekilde ayarlar ve farkı hesaba katmak için gerekli kalem masraflarını uygular.

## Örnek:

**Satın Alma Siparişi (PO):**

Miktar: <mark style="color:green;">100</mark> birim

Birim Fiyat: 10,00 TL

Toplam Tutar: <mark style="color:purple;">1.000,00 TL</mark>

**Alınan Fatura:**

Miktar: <mark style="color:green;">100</mark> birim (tolerans dahilinde)

Birim Fiyat: <mark style="color:red;">11,00 TL</mark> (%±5 tolerans dışında)

Toplam Tutar: <mark style="color:red;">1.100,00 TL</mark>

**Tolerans Seviyeleri:**

Miktar Toleransı: ±%2

Birim Fiyat Toleransı: ±%5 (beklenen aralık: 9,50 TL ile 10,50 TL arası)

**Onay:**

• 11,00 TL'lik birim fiyat tolerans aralığının dışındadır ancak ilgili departman tarafından manuel olarak onaylanmıştır.

Miktar tolerans dahilinde olduğundan ancak birim fiyat tolerans dışında (fakat onaylanmış) olduğundan, sistem şunları yapacaktır:

1\. **Birim Fiyatı Ayarlama**: Sapma onaylandığı için sistem birim fiyatı PO'nun birim fiyatına geri ayarlar:

• **Düzeltilmiş Birim Fiyat = 10,00 TL**

• **Düzeltilmiş Toplam Tutar = 100 birim × 10,00 TL = 1.000,00 TL**

2\. **Fark İçin Kalem Masrafı Uygulama**: Onaylanan 11,00 TL'lik birim fiyat, PO birim fiyatı olan 10,00 TL'den yüksek olduğundan, sistem bu farkı hesaba katmak için bir kalem masrafı uygular:

• **Kalem Masraf Tutarı = (Onaylanan Fatura Birim Fiyatı - PO Birim Fiyatı) × Miktar**

• **Kalem Masraf Tutarı = (11,00 TL - 10,00 TL) × 100 birim = 100,00 TL**

3\. **Faturayı İşleme**: Sistem faturayı şu şekilde işler:

• **Temel Tutar:** 1.000,00 TL

• **Kalem Masrafı:** 100,00 TL

• **Toplam İşlenen Tutar:** 1.100,00 TL

Bu, tutarlılık için temel PO değerleri korunurken, birim fiyattaki onaylanmış sapmanın ek bir kalem masrafı yoluyla hesaba katılmasını sağlayarak doğru finansal işleme ve kayıt tutma sağlar.
