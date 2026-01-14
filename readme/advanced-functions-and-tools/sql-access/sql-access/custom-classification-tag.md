# Aangepaste Classificatietag

**Tabelnaam:** `custom_classification_tag`

Deze tabel definieert de tags die worden gebruikt voor aangepaste documentclassificatie.

| Kolomnaam | Gegevenstype | Beschrijving |
| :--- | :--- | :--- |
| `id` | `String` | Unieke identifier voor de classificatietag. |
| `name` | `String` | De naam van de tag (bijv. "Factuur", "Contract", "Bestelling"). |
| `description` | `String` | Een beschrijving van waar de tag voor staat. |
| `created_at` | `DateTime` | Tijdstempel wanneer het record is aangemaakt. |
| `updated_at` | `DateTime` | Tijdstempel wanneer het record voor het laatst is bijgewerkt. |
| `organization_id` | `String` | Identifier voor de organisatie. |
