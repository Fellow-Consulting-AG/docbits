# Barkod Çıkarımları

**Barkod Çıkarımları**, belgelerdeki çeşitli barkod türlerinin otomatik olarak tanınmasını ve veri olarak çıkarılmasını sağlar.

## Desteklenen Formatlar

DocBits aşağıdaki barkod türlerini destekler:
* Code 128
* Code 39
* EAN-13
* EAN-8
* UPC-A
* UPC-E
* Interleaved 2 of 5
* QR Kodları (Standart)

## Yapılandırma

1. **Etkinleştir**: Barkod çıkarımını açmak için anahtarı kullanın.
2. **Çıkarılacak Alanlar**: Barkod verilerinin hangi belge alanlarına (örneğin Fatura Numarası, Takip Numarası) eşleneceğini belirleyin.
3. **Filtreleme**: Gerekirse, yalnızca belirli desenlere uyan barkodları işlemek için düzenli ifadeler (Regex) kullanın.

<figure><img src="../../../../../../.gitbook/assets/module_barcode_extraction.png" alt=""><figcaption></figcaption></figure>
