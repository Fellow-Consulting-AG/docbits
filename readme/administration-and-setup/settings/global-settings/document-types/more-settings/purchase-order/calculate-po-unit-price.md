# Berechnung des PO-Einzelpreises

## **Übersicht**

Sie können wählen, den Einzelpreis manuell zu berechnen, indem Sie den Nettobetrag durch die Menge teilen, anstatt ihn automatisch aus dem Dokument zu extrahieren. Dies ist besonders nützlich, wenn der Einzelpreis in der Bestellnummer (in Infor) von dem Preis abweicht, der aus dem Dokument extrahiert wird. Solche Abweichungen können auftreten, wenn ein Rabatt auf den Einzelpreis in der Infor-Bestellnummer angewendet wird, während das Dokument den Rabatt nur auf den Nettobetrag anwendet.

## **Aktivierungsschritte**

1.  Navigieren Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Wählen Sie den gewünschten Dokumenttyp aus und klicken Sie auf **Weitere Einstellungen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Aktivieren Sie im Abschnitt **Bestellnummer** die Option **Berechnung des PO-Einzelpreises**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_3.png)

## Beispiel:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_4.png)

In diesem Fall wird der Einzelpreis (ohne Rabatt) aus dem Dokument extrahiert, während die Bestellnummer in Infor den Einzelpreis mit angewendetem Rabatt speichert. Dies führt zu einer Diskrepanz im Einzelpreis.

Sobald die Einstellung aktiviert ist, wird der Einzelpreis wie folgt neu berechnet:\
**Einzelpreis = Nettobetrag ÷ Menge**\
Dies stellt sicher, dass der Einzelpreis konsistent ist und dem beabsichtigten Wert entspricht.
