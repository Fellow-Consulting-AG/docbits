# Batch Instantie

**Tabelnaam:** `batch_instance`

Deze tabel volgt instanties van batchverwerkingstaken.

| Kolomnaam | Gegevenstype | Beschrijving |
| :--- | :--- | :--- |
| `id` | `String` | Unieke identifier voor de batchinstantie. |
| `batch_job_id` | `String` | Identifier voor de batchtaakdefinitie. |
| `status` | `String` | Huidige status van de batch (bijv. "In behandeling", "Bezig", "Voltooid", "Mislukt"). |
| `start_time` | `DateTime` | Tijdstempel wanneer de batch begon. |
| `end_time` | `DateTime` | Tijdstempel wanneer de batch eindigde. |
| `total_records` | `Integer` | Totaal aantal records dat in deze batch moet worden verwerkt. |
| `processed_records` | `Integer` | Aantal records dat succesvol is verwerkt. |
| `failed_records` | `Integer` | Aantal records dat niet kon worden verwerkt. |
| `log` | `Text` | Gedetailleerd logboek van de batchuitvoering. |
| `created_at` | `DateTime` | Tijdstempel wanneer het record is aangemaakt. |
| `updated_at` | `DateTime` | Tijdstempel wanneer het record voor het laatst is bijgewerkt. |
| `organization_id` | `String` | Identifier voor de organisatie. |
