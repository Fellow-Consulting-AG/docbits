# O365 Kiracısı

## Uygulamayı Azure AD'ye Kaydetme

<mark style="color:red;">**Not**</mark>: İzinler bir yöneticiden yetki gerektirebilir.

1. Kimlik bilgilerinizi kullanarak [Azure Portal](https://portal.azure.com/)'ında oturum açın.
2. Azure hizmetlerinden Azure Active Directory'yi (Azure AD olarak da bilinir) bulun ve açın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_1.png" alt=""><figcaption></figcaption></figure>

3. **Yönet** bölümü altında, **Uygulama kayıtları**'nı seçin.

<figure><img src="../../../../.gitbook/assets/o365_tenant_2.png" alt=""><figcaption></figcaption></figure>

4. Uygulama kayıtları ekranında, **+ Yeni kayıt**'a tıklayın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_3.png" alt=""><figcaption></figcaption></figure>

5. **Uygulama kaydet** ekranı görüntülenir. **Ad** alanına Uygulama için kullanıcıya dönük görünen adı girin.

<figure><img src="../../../../.gitbook/assets/o365_tenant_4.png" alt=""><figcaption></figcaption></figure>

6. İhtiyaçlarınıza bağlı olarak aşağıdaki hesap türlerinden birini seçin:

* **Herhangi bir kuruluş dizinindeki hesaplar (Herhangi bir Azure AD dizini - Çok kiracılı) ve kişisel Microsoft hesapları (örneğin Skype, Xbox)**
* **Herhangi bir kuruluş dizinindeki hesaplar (Herhangi bir Azure AD dizini - Çok kiracılı)**

<figure><img src="../../../../.gitbook/assets/o365_tenant_5.png" alt=""><figcaption></figcaption></figure>

7. **Yönlendirme URI'si (isteğe bağlı)** seçeneğini olduğu gibi bırakın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_6.png" alt=""><figcaption></figcaption></figure>

8. Uygulama kaydını tamamlamak için **Kaydet**'e tıklayın. Bu sizi yeni Uygulama ekranına döndürecektir.
9. Uygulama ekranında, **Uygulama (istemci) kimliği**'ni bulun. **DocBits** için e-posta içe aktarımını yapılandırırken kullanılmak üzere kopyalayın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_7.png" alt=""><figcaption></figcaption></figure>

10. Sol panelden **Sertifikalar ve sırlar**'ı seçin:

<figure><img src="../../../../.gitbook/assets/o365_tenant_8.png" alt=""><figcaption></figcaption></figure>

11. **Sertifikalar ve sırlar** ekranında, **İstemci sırları** bölümü altındaki **+ Yeni istemci sırrı** düğmesine tıklayın:

<figure><img src="../../../../.gitbook/assets/o365_tenant_9.png" alt=""><figcaption></figcaption></figure>

12. **İstemci sırrı ekle** iletişim kutusunda, **Ekle** düğmesine tıklayın:

<figure><img src="../../../../.gitbook/assets/o365_tenant_10.png" alt=""><figcaption></figcaption></figure>

Bu sırrı diğerleri arasında tanımlamak için bir açıklama girmeniz önerilir (şu an itibariyle Uygulama başına sınır 2 sırdır).

<figure><img src="../../../../.gitbook/assets/o365_tenant_11.png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Not**</mark>: Bu son kullanma tarihini şirket politikanıza göre seçin. Süresi dolduğunda, yeni bir istemci sırrı oluşturulmalı ve daha önce kullanıldığı her e-posta yapılandırması için belirtilmelidir.

13. Yeni oluşturulan istemci sırrı görünür olacaktır. DocBits için e-posta içe aktarımını yapılandırırken kullanılmak üzere bu istemci sırrını kopyalayın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_12.png" alt=""><figcaption></figcaption></figure>

**Önemli:** İstemci sırrını kopyaladığınızdan emin olun çünkü kapatıldıktan sonra istemci sırrı tekrar görüntülenmeyecektir.

14. Sol panelde **Kimlik Doğrulama**'yı seçin. Bu, sağ tarafta **Kimlik Doğrulama** ekranını sunacaktır.

<figure><img src="../../../../.gitbook/assets/o365_tenant_13.png" alt=""><figcaption></figcaption></figure>

15. **Gelişmiş ayarlar** bölümünde, **Varsayılan istemci türü** için **Evet**'e tıklayın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_14.png" alt=""><figcaption></figcaption></figure>

16. Değişiklikleri onaylamak için **Kaydet**'e tıklayın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_15.png" alt=""><figcaption></figcaption></figure>

17. Sol panelde **API izinleri**'ni seçin. Bu, API izinleri ekranını sunacaktır.

<figure><img src="../../../../.gitbook/assets/o365_tenant_16.png" alt=""><figcaption></figcaption></figure>

18. Varsayılan olarak **Microsoft Graph**'tan **User.Read** izni mevcuttur, bunu olduğu gibi bırakın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_17.png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Not**</mark>: Bu gerekli bir izindir. Bu izin mevcut değilse, **Mail.ReadWrite** izni için aşağıda belirtilen adımlarla izni ekleyin.

19. **+ İzin ekle**'ye tıklayın. Bu, **API izinleri iste** panelini açacaktır.

<figure><img src="../../../../.gitbook/assets/o365_tenant_18.png" alt=""><figcaption></figcaption></figure>

20. **Microsoft Graph**'a tıklayın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_19.png" alt=""><figcaption></figcaption></figure>

21. İki alt kategoriden **Temsilci izinleri**'ni seçin.

<figure><img src="../../../../.gitbook/assets/o365_tenant_20.png" alt=""><figcaption></figcaption></figure>

22. Arama kutusuna **Mail.ReadWrite** yazın. İzin için **Mail.ReadWrite** onay kutusunu seçin.

<figure><img src="../../../../.gitbook/assets/o365_tenant_21.png" alt=""><figcaption></figcaption></figure>

23. Bu, panelin altındaki **İzinleri ekle** düğmesini etkinleştirecektir. **İzinleri ekle**'ye tıklayın.

<figure><img src="../../../../.gitbook/assets/o365_tenant_22.png" alt=""><figcaption></figcaption></figure>

24. Bu, **Mail.ReadWrite** iznini Uygulama için **Yapılandırılmış izinler** listesine ekleyecektir.

<mark style="color:red;">**Not**</mark>: Yönetici izinleri gerekebilir. Yönetici, bu izinleri kullanmak için Uygulamayı yetkilendirmek zorunda kalacaktır. Yetkilendirildikten sonra verilen durum aşağıdaki gibi gösterilecektir:

<figure><img src="../../../../.gitbook/assets/o365_tenant_23.png" alt=""><figcaption></figcaption></figure>
