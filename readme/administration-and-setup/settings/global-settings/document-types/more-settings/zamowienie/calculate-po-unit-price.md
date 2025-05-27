# Oblicz cenę jednostkową PO

## **Przegląd**

Możesz zdecydować się na ręczne obliczenie ceny jednostkowej, dzieląc kwotę netto przez ilość, zamiast automatycznie wyciągać ją z dokumentu. Jest to szczególnie przydatne, gdy cena jednostkowa w zamówieniu zakupu (w Infor) różni się od ceny wyciągniętej z dokumentu. Takie rozbieżności mogą wystąpić, jeśli rabat jest stosowany do ceny jednostkowej w zamówieniu zakupu Infor, podczas gdy dokument stosuje rabat tylko do kwoty netto.

## **Kroki aktywacji**

1.  Przejdź do **Ustawienia** -> **Ustawienia globalne** -> **Typy dokumentów**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Wybierz żądany typ dokumentu i kliknij **Więcej ustawień**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  W sekcji **Zamówienie zakupu** włącz opcję **Oblicz cenę jednostkową PO**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Przykład:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

W tym przypadku cena jednostkowa (bez rabatu) jest wyciągana z dokumentu, podczas gdy zamówienie zakupu w Infor przechowuje cenę jednostkową z zastosowanym rabatem. Skutkuje to niezgodnością w cenie jednostkowej.

Po aktywacji ustawienia cena jednostkowa zostanie przeliczona w następujący sposób:\
**Cena jednostkowa = Kwota netto ÷ Ilość**\
Zapewnia to, że cena jednostkowa jest spójna i odpowiada zamierzonej wartości.
