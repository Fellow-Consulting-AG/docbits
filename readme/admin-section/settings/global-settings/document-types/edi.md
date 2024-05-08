# EDI

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.49.21.png" alt=""><figcaption></figcaption></figure>

#### Przegląd

W DocBits, ustawienia EDI zapewniają narzędzia do definiowania i zarządzania strukturą oraz formatem komunikatów EDI odpowiadających różnym typom dokumentów, takim jak faktury czy zamówienia zakupu. Ustawienia umożliwiają dostosowanie komunikatów EDI do standardów i wymagań określonych dla różnych partnerów handlowych i branż.

#### Główne funkcje i opcje

1. **Elementy konfiguracji EDI**:
* **Deskryptor struktury**: Definiuje podstawową strukturę dokumentu EDI, w tym kolejność segmentów, pola obowiązkowe i kwalifikatory niezbędne do poprawności dokumentu EDI.
* **Transformacja**: Określa transformacje stosowane do konwersji danych dokumentu na sformatowany komunikat EDI. Zazwyczaj obejmuje określenie odwzorowań pól dokumentu na segmenty i elementy EDI.
* **Podgląd**: Umożliwia administratorom zobaczenie, jak będzie wyglądał komunikat EDI po transformacji, co pomaga zapewnić dokładność przed transmisją.
* **Ścieżki ekstrakcji**: Pokazuje ścieżki używane do wyodrębnienia wartości z dokumentu, które są następnie używane do wypełnienia komunikatu EDI.
2. **Edytor XSLT**:
* Służy do edycji i walidacji XSLT (eXtensible Stylesheet Language Transformations) używanych w procesie transformacji. XSLT to potężny język zaprojektowany do transformacji dokumentów XML na inne dokumenty XML lub inne formaty, takie jak HTML, tekst czy nawet inne struktury XML.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.49.59.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2499" %}
