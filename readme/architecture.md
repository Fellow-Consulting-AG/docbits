# Architektura

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits** doskonale integruje się z Infor LN/M3 za pośrednictwem interfejsu API ION, ION Desk oraz standardowych BODs Infor. Nasza integracja API pozwala nam na eksportowanie danych do Infor oraz przeprowadzanie walidacji danych podstawowych w Doc**Bits**.

## Eksportowanie danych do Infor

Korzystamy z interfejsu API ION do wysyłania pliku PDF z atrybutami do IDM oraz BOD Sync.CaptureDocument do ION Desk. W ION Desk przekształcamy Sync.CaptureDocument na docelowe BODs na podstawie typu przetwarzanego dokumentu. Te przekształcone BODs Infor są następnie automatycznie importowane do LN lub M3.

## Walidacja danych podstawowych w DocBits

Aby zidentyfikować dostawcę lub porównać/zestawić pozycje zamówienia, aktywujemy wyzwalacz w LN/M3, który wysyła BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster oraz Sync.PurchaseOrder do Doc**Bits**. Konfigurujemy ten proces w ION Desk, definiując przepływ danych do określonego punktu połączenia z Doc**Bits**.

\
