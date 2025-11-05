# Bereken PO-eenheidsprijs

## **Overzicht**

U kunt ervoor kiezen om de **eenheidsprijs** automatisch te berekenen door het **totaalbedrag** te delen door de **hoeveelheid**, en dit vervolgens te vermenigvuldigen met de **eenheidsprijs per** waarde, in plaats van de eenheidsprijs rechtstreeks uit het document te halen. Dit is bijzonder nuttig wanneer de eenheidsprijs in de inkooporder (in Infor) verschilt van de prijs die uit het document is gehaald. Dergelijke discrepanties kunnen ontstaan als er een korting op de eenheidsprijs in de Infor inkooporder wordt toegepast, terwijl het document de korting alleen op het netto bedrag toepast.

## **Activatiestappen**

1.  Navigeer naar **Instellingen** -> **Globale instellingen** -> **Documenttypen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Selecteer het gewenste documenttype en klik op **Meer instellingen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  In de sectie **Inkooporder**, schakel de optie **Bereken PO-eenheidsprijs** in.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_3.png)

## Voorbeeld:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_4.png)

In dit geval wordt de eenheidsprijs (zonder korting) uit het document gehaald, terwijl de inkooporder in Infor de eenheidsprijs met de toegepaste korting opslaat. Dit resulteert in een mismatch in de eenheidsprijs.

Zodra de instelling is geactiveerd, zal de eenheidsprijs als volgt worden herberekend:\
&#xNAN;**`Eenheidsprijs = Totaalbedrag ÷ Hoeveelheid * Eenheidsprijs per`**\
Dit zorgt ervoor dat de eenheidsprijs consistent is en overeenkomt met de bedoelde waarde.
