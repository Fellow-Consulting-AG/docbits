# Dobavljači i Narudžbine

## **Tačka Povezivanja**

Potrebno je da kreirate DocBits API tačku povezivanja kako biste kasnije mogli kreirati protok podataka.

U InforOS-u, idite na ION Desk → Poveži → Tačke Povezivanja

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Ovde ćete morati da kreirate novu tačku povezivanja.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Izaberite API**

Dajte tački povezivanja ime i opis koji opisuju njen karakter i okruženje. Pod karticom Povezivanje, uvezite servisni nalog koji ste kreirali za okruženje sa kojim radite.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Zatim pređite na karticu Dokumenti. Morate dodati sledeće BOD-ove tački povezivanja, iako svi nisu neophodni za master podatke o dobavljačima i narudžbinama, biće korisni kada se implementiraju druge funkcionalnosti poput Automatskog Knjigovodstva.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Za sada ćemo se fokusirati samo na neophodne BOD-ove, a to su: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster i Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData i Sync.SupplierPartyMaster

Konfiguracija za ova dva BOD-a treba da izgleda slično kao na sledećoj slici (Naziv API poziva se menja za svaki)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

Konfiguracija za ovaj BOD treba da izgleda slično kao na sledećoj slici

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Kada su ovi BOD-ovi konfigurisani, možete sačuvati tačku povezivanja pritiskom na ikonu koja se nalazi desno od dugmeta za povratak.

## **Protok Podataka**

Protok podataka će izgledati slično kao na sledećoj slici

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Razlog za više DocBits API-ja je zbog toga što svaka veza predstavlja različito okruženje, što znači da, u zavisnosti od broja okruženja koje imate, vaš protok podataka može malo da se razlikuje)

Za potrebe ovog objašnjenja koristićemo primer sa četiri odvojena okruženja.

### **M3**

Početak protoka podataka sastoji se od vaše M3 aplikacije

### **Filter**

Konfiguracija filtera izgleda ovako

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(ID entiteta za knjigovodstvo naravno mora biti jedinstven za vašu organizaciju)

### **DocBits API**

Ovde ćete dodati aplikaciju i izabrati DocBits API-je koje ste prethodno kreirali
### **Fajlovi**

Konfiguracija treba da izgleda ovako

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **M3 BOD Okidači**

Idite na Infor M3 aplikaciju

Kada ste na glavnom meniju, otkucajte Command + R da biste otvorili polje za pretragu komandne linije. Zatim otkucajte evs006 i pretražite.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Kada se nalazite na ovoj stranici, treba da dodate SupplierPartyMaster, RemitToPartyMaster i PurchaseOrder na listu.

BOD imenica: SupplierPartyMaster

Tabela: CIDMAS

BOD imenica: RemitToPartyMaster

Tabela: CIDMAS

BOD imenica: PurchaseOrder

Tabela: MPHEAD

Za svaki slučaj treba da pritisnete ikonu plus da biste ih dodali na listu.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Kada dodate svaku od BOD-ova, desnim klikom na BOD imenicu BOD-a odaberite Povezano → Pokreni

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Bićete preusmereni na sledeći meni, gde treba da promenite BOD glagol u Sync i zatim pritisnite NEXT da biste okinuli BOD-ove.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Kada okinete BOD-ove, dobićete obaveštenje koje potvrđuje ovo.

Ako je uspešno izvršeno, tabele Dobavljača i Narudžbine za kupovinu sada bi trebalo da budu dostupne pod Postavke → Pretraga master podataka.
