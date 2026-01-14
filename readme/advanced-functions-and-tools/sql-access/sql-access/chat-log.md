# Chat Log

**Tabelnaam:** `chat_log`

Deze tabel slaat chatlogs op van interacties binnen het systeem, zoals ondersteuningschats of AI-interacties.

| Kolomnaam | Gegevenstype | Beschrijving |
| :--- | :--- | :--- |
| `id` | `String` | Unieke identifier voor de chatlogvermelding. |
| `session_id` | `String` | Identifier voor de chatsessie. |
| `user_id` | `String` | Identifier voor de gebruiker die betrokken is bij de chat. |
| `message` | `Text` | De inhoud van het chatbericht. |
| `sender_type` | `String` | Type afzender (bijv. "Gebruiker", "Systeem", "AI"). |
| `timestamp` | `DateTime` | Tijdstempel wanneer het bericht is verzonden. |
| `organization_id` | `String` | Identifier voor de organisatie. |
