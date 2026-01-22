# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## Przegląd

W panelu administracyjnym XRechnung spotkasz następujące kluczowe komponenty:

## 1. Transformacja

### Cel

Proces transformacji jest niezbędny do konwersji surowych danych, zazwyczaj w formacie XML, na ustrukturyzowany format spełniający określone wymagania, takie jak generowanie faktury. W przypadku XRechnung odbywa się to głównie za pomocą XSLT (Extensible Stylesheet Language Transformations). XSLT to język zaprojektowany do przekształcania dokumentów XML w inne typy dokumentów, takie jak inny XML, HTML lub zwykły tekst.

### Jak to działa

• Szablon XSLT: Plik XSLT definiuje sposób przetwarzania danych XML i wygląd końcowego wyniku. Stosuje reguły i szablony do wyodrębniania, manipulowania i wyprowadzania danych z dokumentu XML.

• Elementy i atrybuty: Plik XSLT zawiera określone elementy i atrybuty sterujące procesem transformacji. Na przykład \<xsl:value-of> służy do wyodrębnienia wartości określonego węzła z dokumentu XML.

### Możliwości administratora

• Modyfikowanie XSLT:

• Edytowanie istniejących szablonów: Administrator może modyfikować istniejące szablony XSLT, aby zmienić sposób transformacji wejściowych danych XML. Na przykład, jeśli istnieje potrzeba wyodrębnienia dodatkowych informacji z dokumentu XML, administrator może dodać nowe reguły w pliku XSLT.

• Tworzenie nowych wersji: Jeśli wymagane są zmiany, administrator może utworzyć nową wersję szablonu XSLT. Zapewnia to, że poprzednie wersje pozostaną nienaruszone do celów historycznych lub ewentualnego przywrócenia.

### Przykład:

Załóżmy, że szablon XSLT wyodrębnia ID faktury za pomocą:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Jeśli trzeba wyodrębnić nowe pole, takie jak numer referencyjny klienta, administrator może dodać:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Podgląd

### Cel

Funkcja podglądu pozwala administratorom wyświetlić wynik wygenerowany przez transformację XSLT przed jej sfinalizowaniem. Ten krok jest kluczowy dla upewnienia się, że reguły transformacji działają poprawnie, a wynik spełnia wymagane standardy.

### Jak to działa

• Walidacja w czasie rzeczywistym: Funkcja podglądu zapewnia renderowanie w czasie rzeczywistym tego, jak będą wyglądać przetworzone dane po zastosowaniu do rzeczywistego dokumentu (np. faktury). Pomaga to we wczesnym wykrywaniu błędów lub problemów z formatowaniem.

• Korekty: Jeśli podgląd wykazuje rozbieżności lub błędy, korekty można wprowadzić bezpośrednio w pliku transformacji (XSLT).

### Możliwości administratora

• Dostosowywanie podglądu:

• Modyfikowanie ustawień podglądu: Administrator może dostosować, które części transformacji są wyświetlane w podglądzie. Na przykład może skupić się na określonych sekcjach dokumentu lub przetestować nowe reguły dodane do szablonu XSLT.

• Zapisywanie i iteracja: Po wprowadzeniu poprawek podgląd można odświeżyć, aby zobaczyć zmiany. Ten proces iteracyjny pozwala na dopracowanie wyniku aż do osiągnięcia pożądanego efektu.

### Przykład:

Jeśli administrator zauważy, że format daty w podglądzie jest nieprawidłowy (np. wyświetla RRRR-MM-DD zamiast DD-MM-RRRR), może zmodyfikować XSLT, aby poprawnie sformatować datę i natychmiast zobaczyć wynik w podglądzie.

## 3. Ścieżki ekstrakcji

### Cel

Ścieżki ekstrakcji definiują określone ścieżki w strukturze XML lub JSON, z których powinny zostać wyodrębnione dane. Ten proces jest niezbędny do wyizolowania kluczowych informacji w dokumencie, które zostaną użyte w transformacji lub do innych zadań przetwarzania.

### Jak to działa

• XPath i JSONPath: Ścieżki ekstrakcji wykorzystują języki takie jak XPath (dla XML) lub JSONPath (dla JSON) do określenia lokalizacji danych w dokumencie. Ścieżki te są kluczowe dla wskazania systemowi, gdzie dokładnie znaleźć i jak wyodrębnić wymagane informacje.

### Możliwości administratora

• Definiowanie i modyfikowanie ścieżek:

• Modyfikowanie istniejących ścieżek: Administrator może modyfikować ścieżki ekstrakcji, jeśli struktura danych ulegnie zmianie lub jeśli zajdzie potrzeba wyodrębnienia dodatkowych danych. Może to obejmować zmianę wyrażeń XPath lub JSONPath.

• Dodawanie nowych ścieżek: Dla nowych pól lub punktów danych administrator może zdefiniować nowe ścieżki ekstrakcji. Wiązałoby się to z określeniem poprawnej ścieżki w dokumencie XML lub JSON.

### Przykład:

W dokumentcie faktury XML, jeśli ścieżka do ID faktury jest zdefiniowana jako:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

I trzeba dodać nowe pole, takie jak adres wysyłki, administrator może dodać:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```
