# API Inloggegevens

**Tabelnaam:** `api_credentials`

Deze tabel slaat API-inloggegevens op die worden gebruikt voor authenticatie en toegang tot externe services.

| Kolomnaam | Gegevenstype | Beschrijving |
| :--- | :--- | :--- |
| `id` | `String` | Unieke identifier voor de inloggegevens. |
| `name` | `String` | Een beschrijvende naam voor de inloggegevens. |
| `api_key` | `String` | De API-sleutel. |
| `api_secret` | `String` | Het API-geheim (versleuteld opgeslagen). |
| `service_type` | `String` | Het type service waarvoor deze inloggegevens zijn (bijv. "Infor", "Salesforce"). |
| `created_at` | `DateTime` | Tijdstempel wanneer het record is aangemaakt. |
| `updated_at` | `DateTime` | Tijdstempel wanneer het record voor het laatst is bijgewerkt. |
| `organization_id` | `String` | Identifier voor de organisatie waartoe deze inloggegevens behoren. |
