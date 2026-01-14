# İş Akışı Örneği: Koşullu Dışa Aktarma Tetikleyici



<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_7.png" alt="DocBits İş akışı Satın alma Sipariş 7"><figcaption></figcaption></figure>

Bu iş akışı, bir dışa aktarma işleminin ne zaman başlatılması gerektiği koşullarını belirler. Belirtilen tüm kriterleri karşılayan belgelerin yalnızca dışa aktarma işlemi için işlenmesini sağlar, veri bütünlüğünü artırır ve iş kurallarıyla uyumu sağlar.

### Ne Zaman:

* Sistemdeki bir belge dışa aktarma uygunluğu için değerlendirildiğinde.

### Mantık:

1. **Belge Türü Kontrolü**
* Belge belirli bir türde olmalıdır (örneğin, "Fatura" veya "Fiş"). Dışa aktarma işlemi için uygun olan belge türünü belirtin.
2. **Durum Doğrulaması**
* Belgenin mevcut durumu önceden belirlenmiş kriterleri karşılamalıdır (örneğin, "Onaylandı" veya "Dışa Aktarmaya Hazır"), bu durum belgenin daha fazla işleme hazır olduğunu gösterir.
3. **Bağlamsal Koşullar**
* Belgenin ayrıntılarının belirli gereksinimlerle uyumlu olduğundan emin olmak için ek kontroller yapılır. Bu kontroller, sipariş onayları veya satın alma siparişlerindeki bilgilerin doğrulanmasını içerebilir. Karşılanması gereken belirli koşulları belirtin. Örneğin:
* Sipariş onayında listelenen tüm kalemlerin satın alma siparişindeki kalemlerle eşleşmesi.
* Sipariş onayındaki toplam tutarın satın alma siparişindeki toplam tutarla eşleşmesi.
* Sipariş onayında belirtilen teslimat tarihlerinin satın alma siparişindeki tarihlerle uyumlu olması.

### Sonrasında:

#### Eylem:

* **Dışa Aktarmayı Başlat**
* Yukarıdaki tüm koşullar karşılanıyorsa, sistem belge için dışa aktarma işlemini otomatik olarak başlatır.
* Bu, bir dışa aktarma dosyası oluşturmayı, verileri harici bir sisteme göndermeyi veya başka bir uygulamada bir iş akışını tetiklemeyi içerebilir.

#### Uygulama Örneği:
```yaml
rules:
- description: "Conditional Export Trigger"
conditions:
- type: "DocumentType"
criteria: "<SpecifyDocumentType>"
- type: "Status"
criteria: "<SpecifyStatus>"
- type: "DetailMatch"
criteria:
- "ItemMatch"
- "AmountMatch"
- "DateMatch"
actions:
- operation: "StartExport"
```

