# Aangepast Classificatiedocument

**Tabelnaam:** `custom_classification_document`

Deze tabel slaat documenten op die zijn gebruikt voor het trainen van aangepaste classificatiemodellen.

| Kolomnaam | Gegevenstype | Beschrijving |
| :--- | :--- | :--- |
| `id` | `String` | Unieke identifier voor het classificatiedocument. |
| `name` | `String` | Naam van het document. |
| `file_path` | `String` | Pad naar het opgeslagen documentbestand. |
| `classification_tag_id` | `String` | Identifier voor de tag waarmee dit document is geclassificeerd. |
| `is_training_sample` | `Boolean` | Geeft aan of dit document wordt gebruikt als trainingsvoorbeeld. |
| `created_at` | `DateTime` | Tijdstempel wanneer het record is aangemaakt. |
| `updated_at` | `DateTime` | Tijdstempel wanneer het record voor het laatst is bijgewerkt. |
| `organization_id` | `String` | Identifier voor de organisatie. |
