# İş Akışı Belgeleri

**İş Akışı Belgeleri**

Genel bir bakışı korumak için iş akışlarına farklı başlıklar verebilirsiniz, böylece bu iş akışının hangi görevle ilgili olduğunu hemen bilebilirsiniz.

Yeni bir İş Akışı Oluştur: + İŞ AKIŞI EKLE'ye tıklayın

![](<../../.gitbook/assets/0 (1).png>)

Bu iş akışlarını (Test 1,2,3) kullanarak şirketteki doğru çalışana çeşitli belgeleri otomatik olarak atayabilirsiniz.

![](<../../.gitbook/assets/1 (1).png>)

Fatura veya diğer belgeler belirli bir toplam tutarı aştığında önceden gözden geçirme ve onay gerektiren durumlarda, bu belgeler hemen doğru kişiye atanabilir.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

**Test 1:              Mantık Kartı**

Ne Zaman:             **Atanan:**                    Amier Haider

Ve:                **Belge türü:**        Fatura

O zaman:              **Belgeyi Ata:**   Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2:              Mantık Kartı**

Ne Zaman:              **Atanan:**                    Amier Haider

Ve:                 **Belge türü:**        Teslimat Notu

O zaman:               **Belgeyi Ata:**   James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3:             Mantık Kartı**

**Ne Zaman:**             **Atanan:**                    Amier Haider

**Ve:**                **Belge türü:**        Sipariş Onayı

**O zaman:**              **Belgeyi Ata:**   Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)





Ayrıca, belgenin tek bir kişiye atanmadığı durumlarda, belgeyi baştan belirli bir çalışana atamak da mümkündür.

<figure><img src="../../.gitbook/assets/image (25).png" alt="" width="375"><figcaption></figcaption></figure>





Bir belgenin ne olması gerektiğini daha kolay anlamak için bu iş akışında gelen belgeler için durumu ayarlayabilirsiniz. Bu iş akışı, örneğin bekleyen bir onay olup olmadığını hemen görmeyi mümkün kılar.

**Test 4:             Mantık Kartı**

**Ne Zaman:**             **Belge türü:**         Teslimat Notu

**Ve:**                **Atanan:**                     Amier Haider

**O zaman:**              **Durumu Değiştir:**         Onay Bekliyor

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)



**Test 5:                Mantık Kartı**

Ne Zaman:                **Belge türü:**           Fatura

Ve:                   **Atanan:**                       Stefan Reppermund

O zaman:                 **Durumu Değiştir:**           İkinci Onay Bekliyor

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)





Fatura veya diğer belgeler belirli bir toplam tutarı aştığında ve önceden gözden geçirme ve onay gerektirdiğinde, bu belgeler hemen doğru kişiye atanabilir.

![](<../../.gitbook/assets/11 (1).png>)



**Test 6:                    Mantık Kartı**

Ne Zaman:                   **Atanan:**                   Amier Haider

Ve:                      Docfield        **toplam\_miktar**     şu kadar      **500**'den büyük olduğunda

O zaman:                    **Belgeyi Ata:**   Asad Usman Khan

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)



Ayrıca, atanan kişinin belgenin durumunu hemen görebilmesi ve belgenin ne olduğunu ve bundan sonra ne yapılması gerektiğini görebilmesi için durumu iş akışına girebilirsiniz.



**Test 7:                 Mantık Kartı**

**Ne Zaman:** **Atanan:**                     Amier Haider

**Ve:**                   Docfield           **toplam\_miktar**      şu kadar        **500**'den büyük olduğunda

**O zaman:**                 **Belgeyi Ata:**     Asad Usman Khan

&#x20;                            **Durumu Değiştir:**          Onay Bekliyor

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>





Örneğin, bir belgeden belirli veya önemli bilgiler eksikse, ancak önemli ve işleme alınması gereken bilgiler varsa, bu belgelerin hemen alıcıya ve bir yedek (yerine geçen) kişiye iletilmesi için iş akışını kurabilirsiniz.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>



**Test 9:**

Bu mantık kartlarıyla tasarlanan İş Akışı, sipariş onayında belirtilen miktarın, birim fiyatın veya indirimin, satın alma siparişindeki karşılık gelen rakamlarla eşleşip eşleşmediğini otomatik olarak doğrulamak üzere tasarlanmıştır. Bu doğrulama, sipariş edilen ve tedarikçinin teslim etmeyi onayladığı şey arasında tutarlılık ve doğruluk sağlar.

Bu belgelere belirli bir durum verebilir veya belirli bir çalışana atayabilirsiniz.

<div align="center">

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

</div>

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

**Mantık Kartı: Miktar veya Birim Fiyat veya İndirim Eşleşmesi**

Bu mantık kartı, sipariş onayında belirtilen miktarın, birim fiyatın veya indirimin, satın alma siparişindeki karşılık gelen rakamlarla eşleşip eşleşmediğini otomatik olarak doğrulamak üzere tasarlanmıştır. Bu doğrulama, sipariş edilen ve tedarikçinin teslim etmeyi onayladığı şey arasında tutarlılık ve doğruluk sağlar.



**Tetikleme Koşulu**

Mantık, sipariş onayında orijinal satın alma siparişine göre aşağıdaki koşullardan herhangi biri karşılandığında etkinleştirilir:

* **Miktar**: Sipariş edilen ürün miktarı, tedarikçi tarafından onaylanan miktarla eşleşir.
* **Birim Fiyat**: Kabul edilen her bir ürün fiyatı, tedarikçinin onayıyla eşleşir.
* **İndirim**: Uygulanan indirimler, satın alma siparişi ile sipariş onayı arasında tutarlıdır.



* **Karşılaştırma Parametrelerini Tanımlayın**: Mantık kartının eşleşmeyi kontrol edeceği belirli alanları (miktar, birim fiyat, indirim) ayarlayın.
* **Doğrulamayı Otomatikleştirin**: Bir sipariş onayı alındığında sistemde bu detayları otomatik olarak karşılaştırmak için yapılandırın.
* **Uyarıları Özelleştirin**: Farklılıkların ele alınması için iş akışını belirleyin, manuel inceleme için uyarıları özelleştirin.

Bu mantık kartı, sipariş onayının detaylarının orijinal satın alma siparişiyle uyumlu olduğundan emin olmak için hayati önem taşır, tedarik döngüsünün bütünlüğünü korur.



**Test 10:**

Ek ücretler için farklı bir hesaplama yapmanız gerekiyorsa veya bunları yalnızca bazı öğelerde kullanıyorsanız, genel tablo hesaplama kartlarını kullanabilirsiniz, bazıları ayrıca düzenli ifadelere göre filtreleme yapmanıza olanak tanır.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Yukarıda, 01, 06, 9, 001 veya 000 ile başlayan öğe numaraları için bir filtre ile MTZ için bir hesaplama örneği bulunmaktadır.



Yeni sütunlara bağlı hesaplamaları içeren hesaplamaları manuel olarak ayarlamak, ayrı bir iş akışına bölmeyi önerir. Hesaplama işlemine devam etmek için Çalıştırma İş Akışı kartını kullanabilirsiniz.

**İş Akışını Çalıştır**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Bu kart ile, belgenin iş akışının koşullarını karşıladığında ve mevcut iş akışının önceki ardından kartlarından sonra çalıştırılacak bir iş akışının adını belirtebilirsiniz. Çalışabilir, etkin iş akışlarını önceliklendirirken, belge belirli iş akışlarının koşullarını karşılarsa devre dışı bırakılmış iş akışlarını da çalıştırmanıza olanak tanır.
### **Mevcut bir sütuna hesaplanmış ek ücretler eklemek** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Eğer tüm ek ücretleri indirim sütununa negatif bir indirim olarak eklemek istiyorsanız, hesaplama kartını kullanabilirsiniz. Bu sütunda girişler olabilir, bunu karttaki değişkenlerden biri olarak ayarlayabilir, MTZ'yi çıkarabilir ve sonucu tekrar bu sütuna ekleyebilirsiniz. Boş alanlar varsa (sadece bazı öğeler için ek ücretler) hesaplaması için 0 olarak kabul edilecektir.

**Kullanıcıyı DocBits'te sipariş onayını yetkilendirmesi konusunda bilgilendirin**

Ek ücretleri hesaplama işleminden sonra belirli bir kullanıcıyı sipariş onayını yetkilendirmesi için bilgilendirmek isteyebilirsiniz. Bunun için bildirim kartını kullanabilirsiniz.

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

Ayarlarınıza bağlı olarak, kullanıcıya DocBits'te yeni bir görev atanır ve isteğe bağlı olarak yeni görevlerinden haberdar etmek için bir e-posta alırlar.
