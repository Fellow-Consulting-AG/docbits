# Eingehende E-Mails

## Aktivierung von Eingehenden E-Mails für die Verarbeitung von Dokumenten

Um Eingehende E-Mails für die Verarbeitung von Dokumenten zu verwenden, folgen Sie diesen Schritten:

1. **Gehe zu Einstellungen**: Beginnen Sie, indem Sie zum **Einstellungen**-Menü der App navigieren.
2. **Wählen Sie Verarbeitung von Dokumenten**: Wählen Sie unter den Einstellungen **Verarbeitung von Dokumenten**, um auf die zugehörigen Konfigurationsoptionen zuzugreifen.
3. **Öffnen Sie Module**: Klicken Sie im Abschnitt Verarbeitung von Dokumenten auf **Module**.
4. **Scrollen Sie zu Dokumenttyp**: Scrollen Sie nach unten, bis Sie **Dokumenttyp** finden.
5. **Aktivieren Sie Eingehende E-Mail**: Finden Sie **Eingehende E-Mail** und aktivieren Sie sie, indem Sie den Schalter umlegen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_1.png)

## Konfigurieren von Eingehenden E-Mails für den Dokumentenimport

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_2.png)

Nachdem Sie die Eingehende E-Mail aktiviert haben, konfigurieren Sie die Einstellungen, um zu steuern, wie Dokumente importiert werden. So geht's:

1. **Gehe zurück zur Verarbeitung von Dokumenten**: Navigieren Sie in den Einstellungen zu **Verarbeitung von Dokumenten**.
2.  **Wählen Sie Import**: Wählen Sie **Import**, um auf die Einstellungen für Eingehende E-Mails zuzugreifen.

    Sie sehen die folgenden Optionen:

    * **E-Mail-Feld**: Dieses Feld zeigt eine eindeutige, systemgenerierte E-Mail-Adresse basierend auf Ihrer Organisations-ID an. Das Format ist `org_id@environment.inbound.docbits.com`. Senden oder leiten Sie E-Mails mit Dokumenten an diese Adresse weiter, um einen automatisierten Import zu ermöglichen.
    * **Dokument nur aus vordefinierter(n) E-Mail(s) importieren**: Aktivieren Sie diese Option, um Importe auf E-Mails zu beschränken, die nur von bestimmten, vordefinierten Adressen empfangen werden.
    * **Antworten Sie auf diese E-Mail, wenn der Import nicht möglich ist**: Aktivieren Sie diese Option, wenn Sie möchten, dass das System automatisch antwortet, wenn ein Importversuch fehlschlägt.
3. **Einstellungen speichern**: Klicken Sie nach der Konfiguration dieser Optionen auf **Speichern**, um sie anzuwenden.

## Vordefinierte E-Mail(s)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_3.png)

Wenn die Option **Dokument nur aus vordefinierter(n) E-Mail(s) importieren** aktiviert ist, können Sie verwalten, welche E-Mail-Adressen berechtigt sind, Dokumente an die Eingehende E-Mail zu senden.

1. **Geben Sie autorisierte E-Mails ein**: Geben Sie im Feld **E-Mail hier eingeben** jede E-Mail-Adresse ein, die Sie autorisieren möchten.
2. **Zuweisen zu Unterorganisation (Optional)**:
   * Wenn keine Unterorganisation ausgewählt ist, wird das Dokument der Hauptorganisation zugewiesen.
   * Wenn eine Unterorganisation ausgewählt ist, wird das Dokument nur an diese Unterorganisation weitergeleitet.
3. **E-Mail hinzufügen**: Klicken Sie auf **Hinzufügen**, um jede E-Mail zur Liste der autorisierten Adressen zu speichern.
4. **E-Mail löschen**: Um eine autorisierte E-Mail zu entfernen, klicken Sie auf **Löschen** neben dem E-Mail-Eintrag.

Mit diesem Setup werden Dokumente von nicht autorisierten E-Mail-Adressen ignoriert, sodass nur bestimmte Quellen Dokumente zum Import senden können.

## **Antworten Sie auf diese E-Mail, wenn der Import nicht möglich ist**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_4.png)

Wenn Sie **Antworten Sie auf diese E-Mail, wenn der Import nicht möglich ist** aktivieren, erscheint ein zusätzliches Feld, in das Sie eine E-Mail-Adresse eingeben können. Diese E-Mail-Adresse erhält eine Benachrichtigung, wenn ein Dokumentenimportversuch fehlschlägt, sodass Sie über Probleme im Importprozess informiert bleiben.

1. **Aktivieren Sie die Fehlermeldung**: Aktivieren Sie **Antworten Sie auf diese E-Mail, wenn der Import nicht möglich ist**.
2. **Geben Sie die Benachrichtigungs-E-Mail ein**: Geben Sie im neuen Feld die E-Mail-Adresse ein, an die Sie Fehlermeldungen erhalten möchten.

Mit dieser aktivierten Funktion wird jeder fehlgeschlagene Importversuch eine automatische Antwort an die angegebene E-Mail auslösen, sodass Sie Importprobleme schnell angehen können.

**Vergessen Sie nicht, nach der Konfiguration aller Einstellungen auf Speichern zu klicken, um Ihre Änderungen anzuwenden.**
