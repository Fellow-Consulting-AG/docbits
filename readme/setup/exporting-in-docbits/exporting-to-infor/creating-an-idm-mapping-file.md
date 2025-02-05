# Tworzenie pliku mapowania IDM



Po uzyskaniu, otwórz plik w wybranym edytorze plików. W tym przewodniku użyjemy VSCode.

### Edytuj plik mapowania

Sprawdź, czy kod typu dokumentu jest taki sam jak w DocBits (jak w przypadku pliku mapowania BOD, powinien odpowiadać nazwie typu dokumentu w URL ustawień pola) oraz sprawdź nazwę typu dokumentu, jak powinna być w Menedżerze Dokumentów (IDM) w Infor.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FWHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc\&width=768\&dpr=4\&quality=100\&sign=5bb93fe7\&sv=2)

**FYI**: Mówi, że nazwa typu dokumentu w IDM to M3\_SupplierInvoice, ponieważ jest to przykład z instancji M3. Może to się zmienić w zależności od tego, czy używasz LN czy M3, a także od Twojej konkretnej konfiguracji IDM.

Sprawdź identyfikator firmy oraz identyfikator podmiotu (SF\_MDS\_EntityType), ta wartość powinna być taka sama, jak w pliku mapowania BOD.

Upewnij się, że IndexFieldFromDocBits=IDMAttributeID (sprawdź, czy DocBits po lewej stronie w ustawieniach pola odpowiada IDM po prawej stronie w Typie Dokumentu → Atrybuty).

### Eksport pliku XML i EDI

Aby wyeksportować oryginalny plik XML/EDI wraz z wygenerowanym PDF, musisz zmodyfikować plik mapowania IDM w konfiguracji eksportu. Najpierw zaktualizuj sekcję **Static\_Values**, dodając prefiks pliku i rozszerzenie. Następnie zdefiniuj rzeczywiste mapowanie, aby zapewnić poprawną konfigurację eksportu.

Jeśli eksport faktur do IDM jest już skonfigurowany, wygenerowany PDF powinien być już uwzględniony w eksporcie. Jeśli nie potrzebujesz pliku XML, możesz pominąć następną część. Jeśli jednak potrzebujesz pliku XML, wykonaj poniższe kroki.

#### Aktualizacja wartości statycznych:

Znajdź pole **Static\_Values** i dodaj następujące:

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Następnie dodaj następujące wpisy poniżej **SV\_ACLString**:

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Po tym dodaj rzeczywiste mapowanie, upewniając się, że typ dokumentu eksportu odpowiada typowi dostawcy IDM.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### Mapowanie XML

Dodaj następujące mapowanie na końcu pliku:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Uwaga: Upewnij się, że **export\_doc\_type** jest ustawione na typ faktury IDM. W tym przykładzie jest ustawione na **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### Mapowanie EDI

Dodaj następujące mapowanie na końcu pliku:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Uwaga: Upewnij się, że **export\_doc\_type** jest ustawione na typ faktury IDM. W tym przykładzie jest ustawione na **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Menedżer Dokumentów w Infor

Przejdź do Menedżera Dokumentów i wybierz nazwę aktualnego typu dokumentu, który próbujesz wyeksportować, na przykład, Faktura dostawcy.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Kliknij powyższy ikonę, a następnie kliknij Administracja → Typ dokumentu i znajdź typ dokumentu, którego potrzebujesz na liście

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Jak pokazano poniżej, zobaczysz nazwę typu dokumentu tak, jak jest w INFOR

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Upewnij się, że tak jest pokazana nazwa w pliku mapowania IDM

### Prześlij plik do DocBits

Po przygotowaniu pliku, prześlij go do swojej konfiguracji eksportu w DocBits. Jest to dostępne w Ustawienia → Eksport.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
