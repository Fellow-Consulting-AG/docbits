# Architektura

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits** doskonale integruje się z Infor LN/M3 za pośrednictwem interfejsu API ION, ION Desk i standardowych BODs Infor. Nasza integracja API pozwala nam eksportować dane do Infor i przeprowadzać walidację danych podstawowych w Doc**Bits**.

## Eksportowanie danych do Infor

Korzystamy z interfejsu API ION do wysyłania pliku PDF z atrybutami do IDM oraz BOD Sync.CaptureDocument do ION Desk. W ION Desk przekształcamy [Sync.CaptureDocument](admin-section/setup/exporting-in-docbits/) na docelowe BODs na podstawie przetwarzanego typu dokumentu. Te przekształcone BODs Infor są następnie automatycznie importowane do LN lub M3.

{% hint style="info" %}
Eksport do [Infor](admin-section/setup/exporting-in-docbits/exporting-to-infor/)&#x20;
{% endhint %}

## Walidacja danych podstawowych w DocBits

Aby zidentyfikować dostawcę lub porównać/dopasować pozycje zamówienia, aktywujemy wyzwalacz w LN/M3, który wysyła BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster i Sync.PurchaseOrder do Doc**Bits**. Proces ten konfigurujemy w ION Desk, definiując przepływ danych do określonego punktu połączenia z Doc**Bits**.

\

{% hint style="info" %}
[Walidacja danych podstawowych](admin-section/setup/importing-customer-master-data/)
{% endhint %}
