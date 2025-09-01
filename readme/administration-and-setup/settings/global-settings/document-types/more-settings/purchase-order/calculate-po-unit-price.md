# Oblicz cenę jednostkową zamówienia

## **Przegląd**

Możesz wybrać automatyczne obliczanie **ceny jednostkowej** poprzez podzielenie **całkowitej kwoty** przez **ilość**, a następnie pomnożenie przez wartość **cena jednostkowa za**, zamiast bezpośredniego wyciągania ceny jednostkowej z dokumentu. Jest to szczególnie przydatne, gdy cena jednostkowa w zamówieniu zakupu (w Infor) różni się od ceny wyciągniętej z dokumentu. Takie rozbieżności mogą wystąpić, jeśli rabat jest stosowany do ceny jednostkowej w zamówieniu zakupu Infor, podczas gdy dokument stosuje rabat tylko do kwoty netto.

## **Kroki aktywacji**

1.  Przejdź do **Ustawienia** -> **Ustawienia globalne** -> **Typy dokumentów**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Wybierz pożądany typ dokumentu i kliknij na **Więcej ustawień**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  W sekcji **Zamówienie zakupu** włącz opcję **Oblicz cenę jednostkową zamówienia**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_3.png)

## Przykład:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_4.png)

W tym przypadku cena jednostkowa (bez rabatu) jest wyciągana z dokumentu, podczas gdy zamówienie zakupu w Infor przechowuje cenę jednostkową z zastosowanym rabatem. Skutkuje to niezgodnością w cenie jednostkowej.

Po aktywacji ustawienia cena jednostkowa zostanie przeliczona w następujący sposób:\
&#xNAN;**`Cena jednostkowa = Całkowita kwota ÷ Ilość * Cena jednostkowa za`**\
Zapewnia to, że cena jednostkowa jest spójna i odpowiada zamierzonej wartości.
