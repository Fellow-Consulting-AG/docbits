# ZUGFeRD + Swiss QR Code Alan Eşlemesi

## Genel Bakış

ZUGFeRD XML verilerini ve Swiss QR Code'u içeren PDF faturaları işlenirken, DocBits her iki kaynaktan da verileri çıkarır ve bunları akıllıca birleştirir.

## Nasıl Çalışır

1. **ZUGFeRD XML Çıkarma** - DocBits önce gömülü ZUGFeRD XML'den alanları çıkarır
2. **Swiss QR Code Algılama** - barcode-service, Swiss QR kodlarını algılar ve ayrıştırır
3. **Akıllı Birleştirme (Smart Merge)** - Boş alanlar Swiss QR verileriyle doldurulur (değeri olan alanlar korunur)
4. **Denetim İzi (Audit Trail)** - Doğrulama için tam QR kodu verileri `qr_code_data` içinde saklanır

## Alan Eşleme Tablosu

### Swiss QR Code → DocBits Alan Eşlemesi

| Swiss QR Alanı | DocBits Alanı | Açıklama |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | Alacaklının IBAN'ı (örn. CH9300762011...) |
| Amount | `total_amount` | Ödeme tutarı (örn. 1234.56) |
| Currency | `currency` | Para birimi kodu (CHF veya EUR) |
| Reference | `payment_reference` / `esr_reference` | QR referansı veya ESR numarası |
| Creditor.Name | `supplier_name` | Tedarikçi firma adı |
| Creditor.AddressLine1 | `supplier_address` | Adres (sokak) |
| Creditor.PostalCode | `supplier_plz` | Posta kodu |
| Creditor.City | `supplier_city` | Şehir |
| Creditor.Country | `supplier_country` | Ülke kodu (CH) |
| Debtor.Name | `company_name` | Alıcı firma adı |
| Debtor.AddressLine1 | `company_street` | Alıcı adresi |
| Debtor.PostalCode | `company_plz` | Alıcı posta kodu |
| Debtor.City | `company_city` | Alıcı şehri |

## Örnek: Örnek Fatura İşleme

### Giriş Belgesi

*   **PDF**: Gömülü ZUGFeRD 1.0 XML + Swiss QR Code barkodu içeren fatura

### Swiss QR Code'dan Çıkarılan Veriler

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Alan Çıkarma Sonuçları

| Alan | Değer | Kaynak | Yöntem |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Çıkarma Yöntemleri

| Yöntem Kodu | Açıklama |
| :--- | :--- |
| **ED** | Elektronik Belge (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Swiss QR Code barkod çıkarma |
| **OCR** | Optik Karakter Tanıma |
| **ML** | Machine Learning çıkarma |

## Birleştirme Önceliği (Merge Priority)

1.  **ZUGFeRD XML** en yüksek önceliğe sahiptir (yapılandırılmış, güvenilir veriler)
2.  **Swiss QR Code** boş alanları doldurur (ödeme verileri için garanti edilen doğruluk)
3.  **OCR/ML**, elektronik kaynaklarda bulunmayan alanlar için kullanılır

## Desteklenen Swiss QR Code Sürümleri

*   Swiss QR Bill formatı (ISO 20022)
*   QR-IBAN formatı (30, 31 ile başlar)
*   Standart IBAN formatı
*   Yapılandırılmış referanslı/referanssız (QRR, SCOR)

## Sürüm Gereksinimi

Bu özellik **doc2-api sürüm 10.95.6** ve **barcode-service sürüm 1.0.5** veya daha üstünü gerektirir.

### Bileşen Sürümleri (Dev Ortamı)

| Bileşen | Sürüm | Açıklama |
| :--- | :--- | :--- |
| `doc2-api` | 10.95.6 | ZUGFeRD 1.0 çıkarma destekli çekirdek API |
| `barcode-service` | 1.0.5 | Swiss QR Code algılama ve ayrıştırma |
| `auth-service` | 1.48.8 | Kimlik doğrulama hizmeti |

### Geçiş (Migration) Gerekli

ZUGFeRD 1.0 desteği, aşağıdaki Alembic geçişinin uygulanmasını gerektirir:

*   `g2h3i4j5k6l7_add_zugferd_1_0_attribute_values.py` - ZUGFeRD 1.0 için TRANSFORMATION, EXTRACTION_PATHS ve PREVIEW değerlerini ekler

Geçişleri şu komutla çalıştırın:

```bash
alembic upgrade head
```

