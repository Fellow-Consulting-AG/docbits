# Auto Boekhouding

**Tabelnaam:** `auto_accounting`

Deze tabel bevat regels en configuraties voor automatische boekhoudprocessen.

| Kolomnaam | Gegevenstype | Beschrijving |
| :--- | :--- | :--- |
| `id` | `String` | Unieke identifier voor de auto-boekhoudregel. |
| `name` | `String` | Naam van de regel. |
| `criteria` | `JSON` | JSON-object dat de criteria definieert waaraan moet worden voldaan om deze regel toe te passen. |
| `action` | `JSON` | JSON-object dat de actie definieert die moet worden ondernomen wanneer aan de criteria is voldaan (bijv. toewijzen aan specifieke GL-rekening). |
| `priority` | `Integer` | Prioriteit van de regel (lagere nummers worden eerst verwerkt). |
| `active` | `Boolean` | Geeft aan of de regel actief is. |
| `created_at` | `DateTime` | Tijdstempel wanneer het record is aangemaakt. |
| `updated_at` | `DateTime` | Tijdstempel wanneer het record voor het laatst is bijgewerkt. |
| `organization_id` | `String` | Identifier voor de organisatie. |
