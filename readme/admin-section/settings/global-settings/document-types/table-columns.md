# Tablo Sütunları

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_overview.png" alt="Docbits Table Columns Overview"><figcaption></figcaption></figure>

#### Genel Bakış

Docbits'teki Tablo Sütunları arayüzü, her belge türü için veri tablolarında görünen sütunları belirtmek için kullanılır. Her sütun, belirli türde verileri (örneğin, dize veya sayısal değerler) tutacak şekilde yapılandırılabilir ve Docbits içinde sıralama, filtreleme ve raporlama işlevleri için önemli olabilir.

#### Temel Özellikler ve Seçenekler

1. **Sütun Yapılandırması**:
* **Sütun Adı**: Veritabanındaki sütunun tanımlayıcısı.
* **Başlık**: Arayüzde görünecek sütun için insan tarafından okunabilir başlık.
* **Sütun Türü**: Sütunun veri türünü tanımlar (örneğin, DİZE, TUTAR), bu da sütunda hangi tür verilerin depolanabileceğini belirler.
* **Tablo Adı**: Sütunun hangi tabloya ait olduğunu belirtir, onu FATURA_TABLOSU gibi belirli bir belge türüne bağlar.
2. **İşlemler**:
* **Düzenle**: Mevcut bir sütunun ayarlarını değiştirin.
* **Sil**: Sütunu tablodan kaldırın, bu verinin artık gerekli olmadığı durumlarda veya belge türünün veri yapısının değiştiği durumlarda faydalıdır.
3. **Yeni Sütunlar ve Tablolar Ekleme**:
* **Yeni Tablo Sütunu Ekle**: Adını, zorunlu olup olmadığını, veri türünü ve ait olduğu tabloyu tanımlayabileceğiniz bir iletişim kutusunu açar.
* **Yeni Tablo Oluştur**: Belirli bir belge türüyle ilişkili verileri depolamak için kullanılacak benzersiz bir adı tanımlayarak yeni bir tablo oluşturmayı sağlar.

<figure><img src="../../../../.gitbook/assets/docbits_create_new_table.png" alt="Docbits Create New Table"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_integrity.png" alt="Docbits Table Columns Integrity"><figcaption></figcaption></figure>

Bu bölüm, Docbits sistemi içinde belgelerden çıkarılan verilerin düzenli ve erişilebilir bir şekilde depolanmasını sağlayarak verilerin yapısal bütünlüğünü ve kullanılabilirliğini korumak için hayati öneme sahiptir.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2493" %}
