# Erstellen eines Datenbankzugriffs für einen bestimmten Organisationsbenutzer

### **1. Einloggen bei Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Gehen Sie zu Ihrer Anmeldeseite.
2. Geben Sie Ihre Anmeldedaten (Benutzername und Passwort) ein, um sich anzumelden.

### **2. Zugriff auf die Einstellungen** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Sobald Sie eingeloggt sind, suchen Sie das Symbol **Einstellungen** (Zahnrad ⚙️) in der linken Seitenleiste.
2. Klicken Sie auf **Einstellungen**, um das Systemkonfigurationspanel zu öffnen.

### **3. Öffnen des Moduls Dokumentenverarbeitung** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Suchen Sie in den **Einstellungen** den Bereich **Dokumentenverarbeitung**.
2. Klicken Sie unter **Dokumentenverarbeitung** auf die Option **Modul**.
   * Dies öffnet die entsprechende Modulkonfigurationsseite, auf der Sie mit der Erstellung des Datenbankbenutzers fortfahren können.

<figure><img src="../../../../../../.gitbook/assets/docbits_db_access_creation.png" alt="Docbits Db Access Creation"><figcaption></figcaption></figure>

### 4. Schritte zum Aktivieren und Zugreifen auf den KI-Dokumenten- und Datenbankbenutzer: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Funktionen umschalten**:
   * Verwenden Sie die Schalter auf der rechten Seite, um bestimmte Funktionen zu aktivieren oder zu deaktivieren:
     * **KI Dokumenten-Warehouse**: Schalten Sie dies ein, um den Zugriff auf KI-bezogene Funktionen zu ermöglichen.
     * **DB-Zugriff**: Schalten Sie dies ein, um dem Benutzer Datenbankzugriff zu gewähren.

<figure><img src="../../../../../../.gitbook/assets/image (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

2. **Datenbank-Zugangsdaten**:
   * Das Dashboard stellt die folgenden Datenbankverbindungsdetails bereit:
     * **Benutzername**: Ein eindeutiger Benutzername wird angezeigt.
     * **Passwort**: Stellen Sie sicher, dass das Passwort sicher gespeichert oder kopiert wird.
     * **Datenbank**: Ist der Name der Datenbank.
     * **Host**: Hostname.
     * **Port**: Ist der Port.
     * **SSL-Modus:** Die Verbindung erfordert `sslmode=require` für eine sichere Kommunikation.
3. **Kopieren der Zugangsdaten**:
   * Verwenden Sie die Kopiersymbole neben jedem Feld, um die Zugangsdaten schnell für die Verwendung in Ihrem Datenbank-Client oder Ihrer Anwendung zu kopieren.
4. **Verbindung über DBeaver:**
   *   Verbinden über Host

       * Wählen Sie PostgreSQL

       <figure><img src="../../../../../../.gitbook/assets/image (2) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

       * Füllen Sie die erforderlichen Informationen aus

       <figure><img src="../../../../../../.gitbook/assets/image (4) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

       * Wechseln Sie zum SSL-Tab und aktivieren Sie "SSL verwenden". Gehen Sie nach unten zum SSL-Modus und wählen Sie "require".

       <figure><img src="../../../../../../.gitbook/assets/image (3) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
   *   Verbinden über URL

       * Füllen Sie die erforderlichen Informationen aus:
         - ersetzen Sie Host durch die bereitgestellten Host-Informationen
         - ersetzen Sie Port durch die bereitgestellten Port-Informationen
         - ersetzen Sie Datenbank durch die bereitgestellten Datenbank-Informationen
         - wählen Sie für Benutzername die bereitgestellten Benutzername-Informationen
         - wählen Sie für Passwort die bereitgestellten Passwort-Informationen

       <figure><img src="../../../../../../.gitbook/assets/image (5) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
5. **Verbindung testen**:
   * Klicken Sie auf die Schaltfläche **"Verbindung testen"**, um sicherzustellen, dass die Zugangsdaten und Verbindungsdetails korrekt sind.
   * Wenn der Test erfolgreich ist, fahren Sie mit der Verbindung fort.
6. **Datenbank erkunden**:
   * Sobald Sie verbunden sind, navigieren Sie zum Bereich **Schema** oder **Tabellen** in Ihrem Datenbank-Client.
   * Überprüfen Sie die verfügbaren Tabellen.
