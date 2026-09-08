# Izračunavanje jedinične cene PO

## **Pregled**

Možete izabrati da se **jedinična cena** svake stavke narudžbenice automatski izračunava na osnovu **iznosa** i **količine** stavke, umesto da se koristi jedinična cena koja je došla sa narudžbenicom. Ovo je posebno korisno kada se jedinična cena u narudžbenici (u Infor ERP / SAP) razlikuje od cene na dokumentu. Takve razlike mogu nastati ako je na jediničnu cenu u narudžbenici primenjen popust, dok dokument primenjuje popust samo na neto iznos.

## **Koraci za aktivaciju**

1.  Idite na **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Izaberite željeni tip dokumenta i kliknite na **More Settings**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  U sekciji **Purchase Order**, omogućite opciju **Calculate PO Unit Price**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Kako se cena izračunava

Kada je podešavanje aktivirano, jedinična cena stavke narudžbenice se izračunava kao:

**`Unit Price = Line Amount ÷ Quantity × Unit Price Per`**

gde se **iznos stavke** bira na sledeći način:

| Stavka narudžbenice sadrži                                                              | Korišćeni iznos stavke                |
| ---------------------------------------------------------------------------------------- | -------------------------------------- |
| **neto iznos** (`extended_amount`) koji je veći od 0 i ne prelazi ukupan iznos stavke    | neto iznos                            |
| nema neto iznosa, ili je neto iznos veći od ukupnog iznosa stavke                        | ukupan iznos stavke (`total_amount`)  |
| nema pozitivnog iznosa, ili nema pozitivne količine                                     | ništa se ne izračunava, cena PO ostaje |

Zašto neto iznos dolazi prvi: ERP feedovi (Infor BODs) šalju neto iznos stavke kao `extended_amount` i nose **poreze i takse dodatno** u `total_amount`. Deljenjem oporezovanog ukupnog iznosa sa količinom dobija se bruto jedinična cena, i svaki račun koji je cenjen neto tada izgleda kao da je _jedinična cena niža_ iako je ispravan. Primer iz stvarne stavke narudžbenice: količina 9, neto iznos 879.84, ukupno 954.63 (porez 8.5%) — cena zasnovana na neto iznosu je 97.76 i poklapa se sa računom; cena zasnovana na ukupnom iznosu bi bila 106.07.

Neto iznos koji je **veći** od ukupnog iznosa stavke ne može biti neto iznos, pa se u tom slučaju koristi ukupni iznos. `Unit Price Per` vrednost 0 ili prazno računa se kao 1.

{% hint style="info" %}
Izračunata cena se upisuje u snapshot narudžbenice koji se čuva na dokumentu, i **ponovo se izračunava svaki put kada se dokument uskladi** (Auto PO Match, ručno usklađivanje, usklađivanje pri čuvanju). Dokument koji je usklađen pre promene podešavanja stoga preuzima novu cenu pri sledećem usklađivanju — nije potrebno ponovo učitavanje narudžbenice.
{% endhint %}

## Primer:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

U ovom slučaju, jedinična cena (bez popusta) se izvlači iz dokumenta, dok narudžbenica u ERP-u čuva jediničnu cenu sa primenjenim popustom. To dovodi do neusaglašenosti u jediničnoj ceni. Sa aktiviranim podešavanjem, jedinična cena se uzima iz iznosa stavke i količine, tako da se obe strane slažu.

## Povezana podešavanja

* [Purchase Order Matching Rules](purchase-order-matching-rules.md) — pravila porede **efektivnu** jediničnu cenu, koja je ova izračunata cena kada je podešavanje uključeno.
* [Purchase Order Tolerance Settings](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — koliko cena na računu može odstupati od izračunate cene.