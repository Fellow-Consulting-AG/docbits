# Automatische Erfassung des Steuercodes

### **Wo es aktiviert werden kann**

* Gehe zu **Einstellungen → Dokumentenverarbeitung → Klassifizierung und Extraktion**.
* Aktiviere **Automatische Steuercode-Erfassung**.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FNFjemAlDwyst2ChlvSYC%2Fimage.png?alt=media\&token=14b2e7bf-6a38-4f1e-8fc4-a282b8aef6b7)

### **Was macht es?**

* Wenn aktiviert, füllt das System das **Steuercode-Feld** im **Validierungsbildschirm** automatisch aus, vorausgesetzt, dass ein **Steuercode-Feld** eingerichtet ist.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2Fud4AaaVUJKnxLjJKn78y%2FiScreen%20Shoter%20-%20Google%20Chrome%20-%20250214111226.jpg?alt=media\&token=f8e2571f-1160-4125-b29a-5e2ee3d9bbb3)

*   Die Logik zur Bestimmung des Steuercodes ist in der folgenden Tabelle aufgeführt.

    Kommentar

<table data-full-width="true"><thead><tr><th>Invoice Document type</th><th></th><th>Tax Code</th><th>Or in Text field</th><th>PO number</th><th>Country of supplier</th><th>Rule</th></tr></thead><tbody><tr><td>Cost Invoice</td><td>With Tax amount</td><td>NAGDH</td><td>LD + % (rounded to highest ABS amount)</td><td>empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is company country</td></tr><tr><td>Cost Invoice</td><td>Without Tax amount</td><td>NAGD0</td><td>LD + % (rounded to highest ABS amount)</td><td>empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is company country</td></tr><tr><td>Cost Invoice</td><td>Without Tax amount</td><td>EUDH</td><td>ED 0 %</td><td>empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is different from company country and EU country in country table (tcmcs010)</td></tr><tr><td>Order invoice</td><td>With Tax Amount</td><td>NAHGH</td><td>IG + % (rounded to highest ABS amount)</td><td>Not empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is company country</td></tr><tr><td>Order invoice</td><td>Without Tax Amount</td><td>NAHG0</td><td>IG + % (rounded to highest ABS amount)</td><td>Not empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is company country</td></tr><tr><td>Order invoice</td><td>With Tax Amount</td><td>EUGH</td><td>ED 0 %</td><td>Not empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is different from company country and EU country in country table (tcmcs010)</td></tr><tr><td>Cost Invoice</td><td>Without Tax amount</td><td>IMGD</td><td>ID 0 %</td><td>empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is different from company country and is not an EU member in the country table (tcmcs010)</td></tr><tr><td>Order invoice</td><td>With Tax Amount</td><td>IMHG</td><td>IG 0 %</td><td>Not empty</td><td>Can be the 2 first digits of the TaX  Id <br>or country of address of supplier tccom120.cadr  -->  tccom130.cadr field tcom130.ccty</td><td>When country is different from company country and is not an EU member in the country table (tcmcs010)</td></tr></tbody></table>
