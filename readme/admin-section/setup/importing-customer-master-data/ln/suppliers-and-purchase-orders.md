# Dobavljači i Narudžbine za Kupovinu

## **Tačka Povezivanja**

Potrebno je da kreirate DocBits API tačku povezivanja kako biste kasnije mogli kreirati protok podataka.

Prvo, u InforOS-u, idite na ION Desk → Poveži → Tačke Povezivanja

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6\_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC\_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Jednom ovde, treba da kreirate novu tačku povezivanja.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs\_Hjw3\_NDT49XG\_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Izaberite API**

Dajte tački povezivanja ime i opis koji opisuje njen karakter i okruženje. Pod karticom Povezivanje, uvezite servisni nalog koji ste kreirali za okruženje sa kojim radite.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT\_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89\_6oJjuq0)

Zatim, pređite na karticu Dokumenti. Treba da dodate sledeće BOD-ove tački povezivanja.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as\_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Ovaj BOD se koristi da signalizira na DocBits-u da je došlo do greške unutar Infor-a. Konfiguracija za ova dva BOD-a treba da izgleda slično sledećem (Naziv API poziva se menja za svaki)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X\_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ\_K6qXbtu04AP67G8jrNwkdj32LCgAhy\_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

Konfiguracija za ovaj BOD treba da izgleda slično sledećem

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4\_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul\_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

Konfiguracija za ovaj BOD treba da izgleda slično sledećem

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Kada su ovi BOD-ovi konfigurisani, možete sačuvati tačku povezivanja pritiskom na ikonu koja se nalazi desno od dugmeta za povratak.

## **Protok Podataka**

Protok podataka će izgledati slično sledećem

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(Razlog za više DocBits API-ja je zbog toga što svaka veza predstavlja različito okruženje, što znači da, zavisno od broja okruženja koje imate, vaš protok podataka može malo da se razlikuje)

Za potrebe ovog objašnjenja koristićemo primer sa četiri odvojena okruženja.

### **LN**

Početak protoka podataka sastoji se od vaše LN aplikacije

### **DocBits API**

Ovde ćete dodati aplikaciju i izabrati DocBits API-e koje ste ranije kreirali

### **Fajlovi**

Konfiguracija treba da izgleda kako sledi

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J\_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU\_TahhNxBugX\_Bnu3QjZsKHX0Pafae-zU)

## **Okidači LN BOD-a**

Kada je sve gore navedeno završeno, treba da odete na Infor LN i pokrenete BOD-ove kako bi različiti master podaci koje trebate za Dobavljače i Narudžbine za Kupovinu stigli u DocBits.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n\_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **Narudžbina za Kupovinu**

Iz gornjeg menija, u levom meniju, izaberite Zajedničko → BOD-Poruke → Objavi BOD-ove → Objavi Transakcione Podatke o Upravljanju Narudžbinama

Izaberite karticu Narudžbina za Kupovinu i označite polje. 

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr\_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B\_\_08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd\_66GAySp3dC1ptYKBaqLqaP1TwJco)
### **Dobavljači**

Sa LN početne stranice, u levom meniju, idite na Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Izaberite karticu PartyMaster i označite polje Supplier → Buy-from ili SupplierPartyMaster.

![](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Pokretanje BOD-a**

Kada su svi ispravni BOD-ovi označeni za objavljivanje, izaberite karticu Options.

Treba izabrati sledeće opcije.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Kada završite, pritisnite dugme PROCESS i BOD-ovi će biti pokrenuti. Pojaviće se poruka na ekranu koja će vas obavestiti da su BOD-ovi pokrenuti.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Ako je uspešno izvršeno, tabele Dobavljača i Narudžbina sada bi trebalo da budu dostupne pod Postavke → Pretraga master podataka.
