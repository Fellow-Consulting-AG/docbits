# Mimarlık

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits**, ION API, ION Desk ve Infor Standart BOD'lar aracılığıyla Infor LN/M3 ile sorunsuz entegre olur. API entegrasyonumuz bize verileri Infor'a aktarma ve Doc**Bits** içinde ana veri doğrulaması yapma imkanı sağlar.

## Verilerin Infor'a Aktarılması

PDF'yi özelliklerle birlikte IDM'ye göndermek için ION API'yi kullanıyoruz ve BOD Sync.CaptureDocument'ı ION Desk'e gönderiyoruz. ION Desk'te, işlenen belge türüne bağlı olarak Sync.CaptureDocument'ı istenilen hedef BOD'lara dönüştürüyoruz. Bu dönüştürülmüş Infor BOD'ları daha sonra LN veya M3'e otomatik olarak aktarılır.

## DocBits'te Ana Veri Doğrulaması

Tedarikçiyi tanımlamak veya satın alma sipariş satırlarını karşılaştırmak/eşleştirmek için, LN/M3'te bir tetikleyici etkinleştiririz ve Sync.RemitToPartyMaster, Sync.SupplierPartyMaster ve Sync.PurchaseOrder BOD'larını Doc**Bits**'e göndeririz. Bu süreci ION Desk'te, veri akışını Doc**Bits**'e belirli bir bağlantı noktasına tanımlayarak yapılandırırız.
