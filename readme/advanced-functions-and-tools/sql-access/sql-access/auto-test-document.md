# Auto Test Document

**Tabelnaam:** `auto_test_document`

Deze tabel slaat informatie op over documenten die worden gebruikt voor geautomatiseerde testdoeleinden.

| Kolomnaam | Gegevenstype | Beschrijving |
| :--- | :--- | :--- |
| `id` | `String` | Unieke identifier voor het testdocument. |
| `name` | `String` | Naam van het testdocument. |
| `file_path` | `String` | Pad naar het opgeslagen documentbestand. |
| `expected_results` | `JSON` | JSON-object met de verwachte extractieresultaten voor validatie. |
| `last_run_status` | `String` | Status van de laatste testrun (bijv. "Geslaagd", "Mislukt"). |
| `created_at` | `DateTime` | Tijdstempel wanneer het record is aangemaakt. |
| `updated_at` | `DateTime` | Tijdstempel wanneer het record voor het laatst is bijgewerkt. |
| `organization_id` | `String` | Identifier voor de organisatie. |
