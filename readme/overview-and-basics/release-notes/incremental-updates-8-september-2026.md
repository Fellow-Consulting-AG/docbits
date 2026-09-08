# Hotfixovi 8. septembar 2026.

> Usklađivanje narudžbenica: šta se promenilo sa hotfixovima implementiranim 8. septembra 2026. Donje ponašanje je aktivno u razvojnom okruženju i stiže na stage, sandbox i produkciju sa sledećim nadogradnjama.

## Usklađivanje narudžbenica

- **Usklađivanje opstaje nakon čuvanja.** Usklađivanje narudžbenice koje je pravilo transformacije ranije tiho odbacivalo pri svakom čuvanju (pravila koja rekonstruišu stavke linija) sada se čuva sve dok pravilo proizvodi iste linije. Kada pravilo zaista zameni usklađene linije, dokument beleži pravilo i ekran ga imenuje.
- **Usklađivanje se ponovo pokreće pri čuvanju.** Kada se broj narudžbenice na dokumentu promeni — ili kada ga popune master podaci nakon obrade, a još nije izvršeno usklađivanje — čuvanje odmah usklađuje dokument. Postojeće usklađivanje nikada nije prepisano čuvanjem.
- **Ekran prikazuje zašto nema usklađivanja.** Ekran za usklađivanje narudžbenica prikazuje jednu rečenicu iznad oblasti narudžbenice: nema broja narudžbenice, narudžbenica nije pronađena u ERP-u, još nije tražena, učitana ali nije povezana, nijedna linija se ne poklapa, nema tabele, kolone tabele nisu mapirane, nema otvorenih linija. Kandidati koji su odloženi su navedeni sa razlogom (na primer broj fakture koji je pročitan u kolonu narudžbenice).
- **Odbijeno usklađivanje nikada nije prijavljeno kao sačuvano.** Ako server ne zadrži usklađivanje, ekran ga vraća, označava dokument kao ne sačuvan i prijavljuje odbijanje sa razlogom umesto "sačuvano".
- **Istorija usklađivanja prikazuje pravila transformacije.** Istorija usklađivanja dokumenta sada ima korak _Transformation rules_ pre prve faze usklađivanja, sa listom pravila koja su pokrenuta i da li je neko od njih odbacio usklađivanje. Administratorima je dostupan link ka pravilu.
- **Cena po jedinici narudžbenice iz neto iznosa.** Sa uključenom opcijom _Calculate PO unit price_, cena se sada prvo izvodi iz **neto** iznosa stavke narudžbenice, a iz ukupnog iznosa samo ako nema neto iznosa. Narudžbenice iz Infora nose porez u ukupnom iznosu stavke; fakture sa neto cenama ranije su se prikazivale kao "unit price under-matched" tačno za stopu poreza. Izračunata cena se osvežava pri svakom usklađivanju, tako da postojeći dokumenti imaju koristi bez ponovnog učitavanja narudžbenice.
- **Brojevi faktura se više ne mešaju sa brojevima narudžbenica.** Kandidat iz kolone stavke ili ranijeg pretraživanja koji je jednak broju fakture dokumenta se odlaže.

## Dokumentacija

- Nova stranica [Transformation Rules](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md).
- [Purchase Order Matching Rules](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) sada pokriva tipove pravila, uslove aktivacije, rezervna pravila, podrazumevani skup pravila, tipove tolerancije i efektivne kolone.
- [Calculate PO unit price](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/calculate-po-unit-price.md) opisuje izračunavanje neto iznosa.
- [Purchase Order Matching Screen](../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) objašnjava poruke "zašto nema usklađivanja" i istoriju usklađivanja.