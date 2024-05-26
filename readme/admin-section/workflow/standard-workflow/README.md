# Standardni radni tok

<figure><img src="../../../.gitbook/assets/DocBits-APWorkflow-Gronbach.drawio (1).svg" alt=""><figcaption></figcaption></figure>

#### Pregled komponenti radnog toka:

* **AP Invoice Email**: Proces verovatno počinje sa računom primljenim putem e-pošte.
* **DocBits**: Ovaj alat može biti korišćen za početne zadatke upravljanja dokumentima kao što su snimanje i digitalizacija računa.
* **Pregled finansija**: Računi prolaze kroz pregled finansija gde se donose odluke o njihovoj validnosti i tačnosti.

#### Koraci u radnom toku:

1. **Početni pregled**:
* Računi se primaju i početno obrađuju korišćenjem DocBits-a.
* Zatim ih pregleda finansijski tim kako bi se osiguralo da budu uklonjeni iz toka rada ako su kompletni, ili gurnuti dalje na dalju obradu.
2. **PO vs Non-PO računi**:
* Tok rada razlikuje između PO-povezanih i ne-PO računa.
* Ne-PO računi se rutiraju na daljnje odobrenje ili odbijanje na osnovu unapred definisanih kriterijuma poput ID dobavljača, količine, jedinične cene i broja stavke.
3. **Povezivanje i nepodudarnosti**:
* Računi se proveravaju u odnosu na potvrde o prijemu robe kako bi se osiguralo da se detalji podudaraju (poput ID dobavljača i količine).
* U slučaju nepodudarnosti, račun je predmet daljeg pregleda i eventualnog odbijanja.
4. **Pregled finansija i kupca**:
* Za PO-povezane račune, sprovodi se detaljan proces povezivanja koji uključuje pregled kupca.
* Moguće su izmene narudžbenica ili potvrda o prijemu robe.
5. **Konačne odluke**:
* Računi koji prođu sve provere odobravaju se i integrišu u finansijske sisteme radi vođenja evidencije.
* Odbijeni računi pokreću obaveštenja, i kupac može zatražiti novi račun.
6. **Integracija sa Infor IDM & LN+M3**:
* Odobreni računi verovatno se šalju Infor IDM-u za upravljanje dokumentima i LN-u za beleženje u glavnoj knjizi.
* Ova integracija osigurava da su svi finansijski zapisi ažurirani i da se radni tok besprekorno uklapa u širi ERP sistem.

#### Tačke odlučivanja:

* Tokom radnog toka, postoje različite tačke odlučivanja gde račun može biti odobren, odbijen ili vraćen radi dodatnih informacija. Obaveštenja se šalju nakon kašnjenja, osiguravajući pravovremenu obradu.

Ovi radni tokovi biće uključeni u Standardni radni tok
