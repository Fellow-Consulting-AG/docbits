# Automatsko knjigovodstvo

## **Preduslovi**

* Funkcionalan protok podataka između M3 i DocBits
* Ispravno konfigurisan DocBits okruženje

## **Infor Konfiguracija**

U Infor-u, otvorite aplikaciju ION Desk. Na levoj kartici, idite na Connect → Connection Points

&#x20;

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt\_gRkqLxkF5CC\_CNGpVRzrNs7rfF1msK320\_J02g)

Ovde ćete kreirati tačku povezivanja potrebnu za uvoz podataka iz M3 koji su potrebni za Automatsko knjigovodstvo.

Kliknite na “+ADD” da biste kreirali novu tačku povezivanja, izaberite opciju API kao što je prikazano ispod

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG\_g946\_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

Treba da konfigurišete API tačku povezivanja nazvanu:

* ChartOfAccounts

### **ChartOfAccounts**

Kartica povezivanja za vašu tačku povezivanja ChartOfAccounts treba da izgleda slično kao što je prikazano ispod. Dajte tački povezivanja odgovarajuće ime i opis, kao i uvezite Servisni nalog koji ste kreirali.

![](https://lh7-us.googleusercontent.com/p-jly6\_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK\_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh\_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-LQmI6E)

Treba da dodate dva BOD-a u ovoj sekciji za ovu tačku povezivanja. To su Sync.ChartOfAccounts i Sync.CodeDefinition, da biste dodali ove BOD-ove uradite sledeće:

#### **Sync.ChartOfAccounts**

* Kliknite na ikonu PLUS (+)

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj\_Gl-wU8QePGV4Wr3\_78OK22nUY35dfCQhUPQIp\_qkdHN0wr7V-VY)

* Izaberite “Send to API”

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo\_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq\_JNhDqxc-SI5HtZh\_Z\_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Potražite BOD Sync.ChartOfAccounts

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-\_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7\_Yp2KDtsohRQkNtIgr1VutFbR8mTkT\_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds\_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Prebacite se na karticu ION API, kopirajte ime API-ja i potražite API poziv pritiskom na dugme SELECT

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074\_nsHzirJUgBfkBkQ8Ydp\_WjImf2bx3pDnLPE)

* Kod proizvoda, izaberite API Endpoint koji ste kreirali za okruženje sa kojim radite, a koji ste kreirali u ION API. Potražite sledeći API poziv, izaberite API poziv i pritisnite OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p\_wwE\_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM\_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* Zatim, prebacite se na karticu Request Body

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq\_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* Ovde ćete konfigurisati mapiranje polja za ovaj BOD, vaša konfiguracija treba da izgleda kao na slici. Mapiranja polja su dostupna ovde.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB\_69KP8Ukh\_0NhATYBxvrS\_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Kada završite sa gore navedenim koracima, uspešno ste konfigurisali BOD Sync.ChartOfAccounts. Kliknite na ikonu PLUS da biste dodali sledeći i poslednji BOD.
#### **Sync.CodeDefinition**

Kartica za povezivanje vaše tačke povezivanja CodeDefinition trebalo bi da izgleda slično kao što je prikazano ispod. Dajte tački povezivanja odgovarajuće ime i opis, kao i uvoz Servisnog naloga koji ste kreirali.

* Izaberite "Pošalji na API"

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG\_URcRGgv\_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD\_zLy2W\_iMQ0I77cY\_Bs)

* Potražite Sync.CodeDefinition BOD

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ\_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg\_N\_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Prebacite se na karticu ION API, kopirajte ime API-ja i potražite API poziv pritiskom na dugme SELECT

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf\_YMVkXjhTkvnGwLzwH\_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* Zatim pređite na karticu Telo zahteva

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU\_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW\_yE\_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* Ovde ćete konfigurisati mapiranje polja za ovaj BOD, vaša konfiguracija treba da izgleda kao što je prikazano ispod. Mapiranja polja su dostupna ovde.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1\_omw22GRKONfB-zc8ikn\_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW\_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Kada završite sa gore navedenim koracima, uspešno ste konfigurisali Sync.CodeDefinition BOD za tabelu master podataka M3FlexDimensions.

## **Protok podataka**

Potrebno je da konfigurišete sledeći protok podataka za Auto računovodstvo:

* PlanRačuna

### **PlanRačuna**

Pregled ovog protoka podataka izgleda kako je prikazano ispod (broj tačaka povezivanja DocBits API-ja na kraju zavisi od broja različitih okruženja koje konfigurišete).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **M3 Kompanija**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0\_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3\_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

Konfiguracija ove tačke povezivanja zavisi od M3 kompanije koja sadrži master podatke koje želite da uvezete u DocBits, vaša bi trebalo da izgleda slično kao što je prikazano ispod.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X\_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx\_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC\_YumwpS9Q)

### **Dokumenti**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw\_vM-uPApJ02QdxvCmX27bwAW\_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

Sledeći dokumenti treba da budu dodati u protok podataka:

* Sync.PlanRačuna
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo\_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD\_Pys8jAydydJgbsK8)
### **Filter**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ_fDPiY)

Za drugu rutu protoka podataka (prema usmeravanju u protoku podataka), primenjujemo filter sa sledećom konfiguracijom.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6_IIzTVYF_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc_L7URD7AbEq_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP_JNMGkxvmiEnPJ_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-_nhMGl1zdEHfUKK56owelabcG-6gM1S_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/Npm92rS_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

Ovde dodajete tačku konekcije API-ja ChartOfAccounts koju ste prethodno kreirali, konfiguracija za ovo treba da izgleda slično ovome

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj_FqdsaFxaRhQyk6_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2_UtYe4dVii0JbM)

## **Pokretanje BOD-a**

Kada završite sve gore navedeno, treba da odete na Infor M3 i pokrenete BOD-ove kako bi različiti master podaci koje trebate za Auto računovodstvo stigli u DocBits.

Počnite pritiskom na Command + r, da otvorite meni za unos, unesite "evs006" i pritisnite enter.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I_6_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

Biće vam prikazan sledeći meni

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT_vLrkVUlFd_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

Da biste dodali različite BOD-ove, treba da unesete BOD imenice i imena tabela za svaki BOD pojedinačno.

![](https://lh7-us.googleusercontent.com/5gVWRDm_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

BOD-ovi koje treba dodati su:

* ChartOfAccounts
* CodeDefinition
* CodeDefinitionAccountingDimension

Da biste dodali novi BOD, nakon unosa BOD Imenice i Imena Tabele, pritisnite ikonu PLUS označenu ispod

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io_5GZGfzSQ2qt_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg_hAMSfs_NJa6zYBMpoyTVs)

BOD imenice i imena tabela su sledeća.

**ChartOfAccounts**

* BOD Imenica: ChartOfAccounts
* Ime Tabele: FCHACC

**CodeDefinition**

* BOD Imenica: CodeDefinitionAccountingDimension
* Ime Tabele: FCHACC

### **Objavljivanje BOD-ova**

Nakon dodavanja svakog BOD-a, desnim klikom na dodati BOD, izaberite Povezano, a zatim Pokreni.

![](https://lh7-us.googleusercontent.com/225-ujyGzG_RJOXgbx8NOh_4s-Sn_o80b_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

Bićete preusmereni na ovaj ekran.

Promenite BOD Glagol u "sync" i pritisnite DALJE.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Kada pritisnete DALJE, dobićete obaveštenje koje ukazuje da je proces objavljivanja BOD-a počeo.
### **CostingElement**

Da biste uvezli tabelu m3costingelement u DocBits, morate uraditi sledeće.

Sa M3 početne stranice, otkucajte Command + r i pretražite "PPS280" prompt.

Izaberite bilo koju liniju koja vam se prikaže. Na sledećem meniju, izaberite TOOLS i "Export to Excel"

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m\_blJ\_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI\_anUNvmACFyx\_ssgxaqWq25vLt\_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Izaberite "Export all Rows" i zatim pritisnite EXPORT.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis\_zELtCIfpmkIUKgasfrdfNW-dr\_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP\_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Kada preuzmete fajl, moraćete da izmenite excel fajl pre konvertovanja u CSV fajl.

Treba da otvorite excel fajl, izgledaće slično kao što je prikazano ispod.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp\_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO\_Z34c8\_f0cNMX-9lp0lT5wOZoH1QUCgE)

Iz ovog excel lista potrebne su vam samo prve 2 kolone, izmenite excel list tako da krajnji rezultat izgleda kao što je prikazano ispod.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C\_\_nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM\_xUXbqmzBtiQZstnpEYj1dUSbs\_IkAydlhBfdmcc)

Kada završite sa tim, sačuvajte fajl kao CSV.

Kada imate CSV fajl, idite na sledeću veb stranicu. Ovo zavisi od toga koju okolinu koristite:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Ovde ćete ručno učitati tabelu CostingElement putem API-ja. Kliknite na dugme Authorise.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O\_mxN5bSVp40jYfgsVJcE\_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Ovde ćete morati da unesete API ključ sa vaše DocBits okoline. Ovo se nalazi u Postavkama pod Integracija.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq\_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf\_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i\_gvBPuE8CvfwRpX-ZIlb\_g)

Kada završite, potražite API pod nazivom master\_data\_lookup/import\_data i popunite potrebne informacije. Kada završite, kliknite na EXECUTE da biste pokrenuli API.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

Ako je sve urađeno ispravno, tabela M3CostingElement sada bi trebalo da bude u vašoj DocBits okolini. Auto računovodstvo za M3 sada je konfigurisano za vašu okolinu.
