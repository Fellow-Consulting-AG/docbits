# Zasady i Obliczenia

Na tej stronie możesz znaleźć, które kolumny są dopasowane, zasady, którymi się kierują, oraz jak wykonywane są obliczenia.

## Które kolumny są dopasowywane?

Proces dopasowywania zamówień zakupu dopasowuje tylko określone kolumny. Poniższa lista przedstawia, które kolumny są dopasowane, jeśli są dostępne. Jeśli nie ustawiono [tolerancji](rules-and-calculations.md#akceptuj-tolerancje), kolumny będą dopasowane tylko wtedy, gdy będą dokładnym (100%) dopasowaniem.

* [Ilość](rules-and-calculations.md#ilosc) (Ilość | Ilość odebrana | Ilość otwarta dostawy odebranej)
* Cena jednostkowa
* Numer zamówienia zakupu
* Numer przedmiotu/ID przedmiotu dostawcy
* Obiecana data dostawy

## Ilość

Masz trzy opcje dopasowania ilości.

* Ilość
* Ilość odebrana
* Ilość otwarta dostawy odebranej

Możesz ustawić tę opcję w **Ustawienia → Ustawienia globalne → Typy dokumentów → Więcej ustawień → Zamówienie zakupu → Zamówienie zakupu**

## Akceptuj tolerancje

Możesz określić, że określona tolerancja jest akceptowalna podczas procesu dopasowywania. Domyślnie tylko dokładne (100%) dopasowania są uważane za ważne. Aby uzyskać więcej informacji, zobacz [szczegółową dokumentację](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Wyłącz statusy

Możesz wykluczyć określone linie z pewnymi statusami z dopasowania. Aby uzyskać więcej informacji, zapoznaj się z [szczegółową dokumentacją](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md).

## Obliczenia

Poniżej tabeli zawierającej informacje wyciągnięte z Twojego dokumentu, możesz znaleźć proste obliczenia, aby zweryfikować, czy całkowite rezerwacje się zgadzają.

<figure><img src="../../../.gitbook/assets/po_rules.png" alt="" width="423"><figcaption></figcaption></figure>

### Zarejestrowane rezerwacje:

To jest obliczane na podstawie zarejestrowanego numeru zamówienia zakupu przy użyciu następującego wzoru:

```
Zarejestrowane rezerwacje = CENA JEDNOSTKOWA * ILOŚĆ (na podstawie zamówienia zakupu)
```

### Dopasowana całkowita kwota:

To jest obliczane na podstawie kwoty wyciągniętej z dokumentu przy użyciu następującego wzoru:

```
 Dopasowana całkowita kwota = CENA JEDNOSTKOWA * ILOŚĆ (na podstawie dokumentu)
```

### **Opłaty:**

W tej sekcji zostaną dodane wszelkie obowiązujące opłaty, jeśli są obecne.

### Niezrealizowana kwota:

Wynikowa różnica jest wyświetlana tutaj i jest obliczana w następujący sposób:

```
Niezrealizowana kwota = Zarejestrowane rezerwacje - Dopasowana całkowita kwota - Opłaty
```
