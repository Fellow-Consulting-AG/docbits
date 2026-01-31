# ZUGFeRD Alan Eşleştirme Genel Bakış

## Giriş

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland), UN/CEFACT Cross Industry Invoice (CII) ve ISO standardı 19005-3 (PDF/A-3) tabanlı bir Alman e-fatura standardıdır. Bir PDF dosyası içinde yapılandırılmış fatura verilerinin değişimine olanak tanır.

DocBits, ZUGFeRD belgelerinden alanları çıkarır ve OAGIS BOD standartlarını kullanarak bunları Infor ERP sistemleri (M3, LN) ile hizalar.

## Desteklenen ZUGFeRD Sürümleri

DocBits, ZUGFeRD standardının birden fazla sürümünü destekler:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Veri Akışı

Bir ZUGFeRD belgesinden ERP sisteminize veri akışı şu adımları izler:

1. **Çıkarma**: DocBits, ZUGFeRD sürümüne bağlı olarak PDF'den gömülü XML verilerini ayrıştırır.
2. **DocBits Alan Eşleştirme**: Çıkarılan veriler standart DocBits alanlarıyla eşleştirilir.
3. **ERP Hizalaması**: DocBits alanları, Infor BOD (Business Object Document) alanlarıyla veya M3/LN'ye özgü API alanlarıyla eşleştirilir.
4. **Dışa Aktarma**: Eşleştirilen veriler Infor sistemine aktarılır.

## Eşleştirme Standartları

Eşleştirme aşağıdaki standartlara dayanmaktadır:
* **UN/CEFACT CII**: ZUGFeRD XML yapısı için temel.
* **OAGIS/OASIS**: Infor BOD'ları için standart.
* **EN 16931**: ZUGFeRD 2.x'in uyumlu olduğu e-faturalama için Avrupa standardı.
