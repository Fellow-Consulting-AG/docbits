# Arhitektura

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits** se besprekorno integriše sa Infor LN/M3 putem ION API-ja, ION Desk-a i Infor Standard BOD-ova. Naša API integracija nam omogućava da izvozimo podatke u Infor i vršimo validaciju osnovnih podataka u Doc**Bits**-u.

## Izvoz podataka u Infor

Koristimo ION API da pošaljemo PDF sa atributima u IDM i BOD Sync.CaptureDocument u ION Desk. U ION Desk-u, transformišemo [Sync.CaptureDocument](admin-section/setup/exporting-in-docbits/) u željene ciljne BOD-ove na osnovu tipa dokumenta koji se obrađuje. Ovi transformisani Infor BOD-ovi zatim automatski se uvoze u LN ili M3.

{% hint style="info" %}
Izvoz u [Infor](admin-section/setup/exporting-in-docbits/exporting-to-infor/)&#x20;
{% endhint %}

## Validacija osnovnih podataka u DocBits-u

Da bismo identifikovali dobavljača ili uporedili/poklopili linije porudžbine, aktiviramo okidač u LN/M3 koji šalje Sync.RemitToPartyMaster, Sync.SupplierPartyMaster i Sync.PurchaseOrder BOD-ove u Doc**Bits**. Ovaj proces konfigurišemo u ION Desk-u definisanjem protoka podataka ka određenoj tački povezivanja sa Doc**Bits**-om.

\

{% hint style="info" %}
[Validacija osnovnih podataka](admin-section/setup/importing-customer-master-data/)
{% endhint %}
