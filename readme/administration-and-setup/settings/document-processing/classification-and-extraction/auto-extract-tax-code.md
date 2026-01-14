# Vergi kodunu otomatik çıkar

## **Nereden Etkinleştirilir**

1. **Ayarlar → Belge İşleme → Sınıflandırma ve Çıkarma** yoluna gidin.
2. **Vergi kodunu otomatik çıkar**'ı etkinleştirin.

<figure><img src="../../../../.gitbook/assets/auto_extract_tax_code_1.png" alt=""><figcaption></figcaption></figure>

## **Ne İşe Yarar?**

* Etkinleştirildiğinde, sistem **Doğrulama Ekranındaki** **vergi kodu alanını otomatik olarak doldurur**—bir **vergi kodu alanının** ayarlanmış olması koşuluyla.

<figure><img src="../../../../.gitbook/assets/auto_extract_tax_code_2.png" alt=""><figcaption></figcaption></figure>

* Vergi kodunu belirlemek için kullanılan mantık aşağıdaki tabloda özetlenmiştir.

<table data-full-width="true"><thead><tr><th>Fatura Belge türü</th><th></th><th>Vergi Kodu</th><th>Veya Metin alanında</th><th>PO numarası</th><th>Tedarikçi ülkesi</th><th>Kural</th></tr></thead><tbody><tr><td>Maliyet Faturası</td><td>Vergi tutarı ile</td><td>NAGDH</td><td>LD + % (en yüksek ABS tutarına yuvarlanmış)</td><td>boş</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesi olduğunda</td></tr><tr><td>Maliyet Faturası</td><td>Vergi tutarı olmadan</td><td>NAGD0</td><td>LD + % (en yüksek ABS tutarına yuvarlanmış)</td><td>boş</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesi olduğunda</td></tr><tr><td>Maliyet Faturası</td><td>Vergi tutarı olmadan</td><td>EUDH</td><td>ED 0 %</td><td>boş</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesinden farklı olduğunda ve ülke tablosunda (tcmcs010) AB ülkesi olduğunda</td></tr><tr><td>Sipariş faturası</td><td>Vergi Tutarı ile</td><td>NAHGH</td><td>IG + % (en yüksek ABS tutarına yuvarlanmış)</td><td>Boş değil</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesi olduğunda</td></tr><tr><td>Sipariş faturası</td><td>Vergi Tutarı Olmadan</td><td>NAHG0</td><td>IG + % (en yüksek ABS tutarına yuvarlanmış)</td><td>Boş değil</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesi olduğunda</td></tr><tr><td>Sipariş faturası</td><td>Vergi Tutarı ile</td><td>EUGH</td><td>ED 0 %</td><td>Boş değil</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesinden farklı olduğunda ve ülke tablosunda (tcmcs010) AB ülkesi olduğunda</td></tr><tr><td>Maliyet Faturası</td><td>Vergi tutarı olmadan</td><td>IMGD</td><td>ID 0 %</td><td>boş</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesinden farklı olduğunda ve ülke tablosunda (tcmcs010) AB üyesi olmadığında</td></tr><tr><td>Sipariş faturası</td><td>Vergi Tutarı ile</td><td>IMHG</td><td>IG 0 %</td><td>Boş değil</td><td>Vergi Kimliğinin ilk 2 hanesi olabilir <br>veya tedarikçinin adres ülkesi tccom120.cadr  -->  tccom130.cadr alanı tcom130.ccty</td><td>Ülke şirket ülkesinden farklı olduğunda ve ülke tablosunda (tcmcs010) AB üyesi olmadığında</td></tr></tbody></table>
