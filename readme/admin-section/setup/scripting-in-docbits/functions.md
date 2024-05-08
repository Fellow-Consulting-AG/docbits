# Fonksiyonlar

**İşlevsel Belgeler**

Bu modül, belge verilerini manipüle etmek ve belge alanlarıyla ilgili çeşitli işlemleri gerçekleştirmek için fonksiyonlar içerir.

## **Fonksiyonlar**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Açıklama: Belge verisinde bir alanın değerini ayarlar.
* Parametreler:
* `document_data` (dict): Alan bilgilerini içeren belge verisi.
* `field_name` (str): Ayarlanacak alanın adı.
* `value`: Alana ayarlanacak değer.
*   Örnek:

`set_field_value(document_data, "name", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Açıklama: Belge verisinde bir tarih alanının değerini ayarlar.
* Parametreler:
* `document_data` (dict): Alan bilgilerini içeren belge verisi.
* `field_name` (str): Ayarlanacak tarih alanının adı.
* `value`: Ayarlanacak tarih değeri ISO formatında (örn. "2020-12-31").
*   Örnek:

`set_date_value(document_data, "date_of_birth", "1990-05-15")`
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Açıklama: Belge verisinde bir tutar alanının değerini ayarlar.
* Parametreler ve örnek kullanımı `set_field_value` ile benzerdir.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Açıklama: Belge verisinde bir alanın 'is\_required' özniteliğini ayarlar.
* Parametreler ve örnek kullanımı `set_field_value` ile benzerdir.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Açıklama: Belge verisinde bir alanın 'force\_validation' özniteliğini ayarlar.
* Parametreler ve örnek kullanımı `set_field_value` ile benzerdir.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Açıklama: Belge verisinde bir alanın özel özniteliğini ayarlar.
* Parametreler:
* `attribute_name` (str): Ayarlanacak özniteliğin adı.
* `value`: Özniteliğe ayarlanacak değer.
*   Örnek:

`set_field_attribute(document_data, "address", "is_verified", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Açıklama: Belge verisinden bir alanın değerini alır.
* Parametreler ve örnek kullanımı `set_field_value` ile benzerdir.
8. ### **create\_new\_field(field\_name, value="")**
* Açıklama: Belirtilen ad ve değere sahip yeni bir alan oluşturur.
* Parametreler:
* `field_name` (str): Oluşturulacak alanın adı.
* `value`: Alan için başlangıç değeri (varsayılan olarak boş bir dizedir).
*   Örnek:

`create_new_field("address", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
* Açıklama: Belge verisinden bir alanı siler.
* Parametreler ve örnek kullanımı `set_field_value` ile benzerdir.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Açıklama: Belirtilen Kimlikle bir belgenin durumunu günceller.
* Parametreler:
* `doc_id` (str): Güncellenecek belgenin Kimliği.
* `user`: Güncellemeyi yapan kullanıcı (kullanıcı Kimliği veya UserAuthentication nesnesi).
* `org_id`: Belgenin ait olduğu kuruluşun Kimliği.
* `status` (str): Belgenin yeni durumu.
* `message`: Durum güncellemesi ile ilişkilendirilen isteğe bağlı ileti.
* `doc_classification_class`: İsteğe bağlı belge sınıflandırma sınıfı.
*   Örnek:

`update_document_status_with_doc_id("123456", user, org_id, "approved", "Belge onaylandı")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Açıklama: Sağlayıcının belirtilen kriterlere göre geçerli olup olmadığını kontrol eder.
* Parametreler:
* `user` (UserAuthentication): Doğrulanmış kullanıcı.
* `filter_data_json`: Sağlayıcıyı doğrulamak için filtre kriterleri.
* `sub_org_id`: Filtreleme için isteğe bağlı alt-organizasyon Kimliği.
*   Örnek:

`is_supplier_valid(user, {"name": "Tedarikçi A.Ş."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Açıklama: Belge verisinde bir alanı geçersiz olarak işaretler.
* Parametreler:
* `document_data` (dict): Alan bilgilerini içeren belge verisi.
* `field_name` (str): Geçersiz olarak işaretlenecek alanın adı.
* `message` (str): Alan için doğrulama iletişi.
* `code` (isteğe bağlı): Doğrulama için hata kodu (varsayılan olarak None).
*   Örnek:

`set_field_as_invalid(document_data, "email", "Geçersiz e-posta formatı", "EPOSTA_FORMATI_GECERSIZ")`
13. ### **compare\_values(value1, value2)**
* Açıklama: Çeşitli veri tiplerini ele alarak iki değeri eşitlik açısından karşılaştırır.
* Parametreler:
* `value1`: Karşılaştırılacak ilk değer.
* `value2`: Karşılaştırılacak ikinci değer.
*   Örnek:

`compare_values(10, "10")`
