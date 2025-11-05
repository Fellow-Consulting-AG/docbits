# Inkomende e-mails

## Inkomende e-mail activeren voor Documentverwerking

Om te beginnen met het gebruik van inkomende e-mail voor documentverwerking, volg je deze stappen:

1. **Ga naar Instellingen**: Begin met het navigeren naar het **Instellingen** menu van de app.
2. **Selecteer Documentverwerking**: Kies onder instellingen voor **Documentverwerking** om toegang te krijgen tot gerelateerde configuratieopties.
3. **Open Module**: Klik in de sectie Documentverwerking op **Module**.
4. **Scroll naar Documenttype**: Scroll naar beneden totdat je **Documenttype** vindt.
5. **Activeer Inkomende e-mail**: Zoek **Inkomende e-mail** en activeer deze door de schakelaar om te zetten.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_1.png)

## Inkomende e-mail configureren voor Document Importeren

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_2.png)

Nadat je inkomende e-mail hebt geactiveerd, configureer je de instellingen om te bepalen hoe documenten worden geïmporteerd. Zo doe je dat:

1. **Ga terug naar Documentverwerking**: Navigeer in de instellingen naar **Documentverwerking**.
2.  **Selecteer Importeren**: Kies **Importeren** om toegang te krijgen tot de instellingen voor inkomende e-mail.

    Je ziet de volgende opties:

    * **E-mailveld**: Dit veld toont een uniek, door het systeem gegenereerd e-mailadres op basis van je organisatie-ID. Het formaat is `org_id@environment.inbound.docbits.com`. Stuur of stuur e-mails met documenten door naar dit adres voor automatische import.
    * **Document alleen importeren vanuit vooraf gedefinieerde e-mailadressen**: Zet deze optie aan om imports te beperken tot e-mails die alleen van specifieke, vooraf gedefinieerde adressen zijn ontvangen.
    * **Beantwoord deze e-mail als de import niet kan worden uitgevoerd**: Zet deze optie aan als je wilt dat het systeem automatisch reageert wanneer een importpoging mislukt.
3. **Instellingen Opslaan**: Klik op **Opslaan** om de configuraties toe te passen.

## Vooraf gedefinieerde e-mailadressen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_3.png)

Wanneer de optie **Document alleen importeren vanuit vooraf gedefinieerde e-mailadressen** is ingeschakeld, kun je beheren welke e-mailadressen zijn gemachtigd om documenten naar de inkomende e-mail te sturen.

1. **Voer Geautoriseerde E-mails in**: Typ in het veld **Voer e-mail hier in** elk e-mailadres dat je wilt autoriseren.
2. **Toewijzen aan Suborganisatie (Optioneel)**:
   * Als er geen suborganisatie is geselecteerd, wordt het document toegewezen aan de hoofdorganisatie.
   * Als er een suborganisatie is geselecteerd, wordt het document alleen naar die suborganisatie gestuurd.
3. **E-mail Toevoegen**: Klik op **Toevoegen** om elk e-mailadres op te slaan in de lijst met geautoriseerde adressen.
4. **E-mail Verwijderen**: Klik op **Verwijderen** naast de e-mailinvoer om een geautoriseerde e-mail te verwijderen.

Met deze opzet worden documenten van ongeautoriseerde e-mailadressen genegeerd, zodat alleen specifieke bronnen documenten voor import kunnen verzenden.

## **Beantwoord deze e-mail als de import niet kan worden uitgevoerd**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_4.png)

Als je **Beantwoord deze e-mail als de import niet kan worden uitgevoerd** inschakelt, verschijnt er een extra veld waarin je een e-mailadres kunt invoeren. Dit e-mailadres ontvangt een melding als een documentimportpoging mislukt, zodat je op de hoogte blijft van eventuele problemen in het importproces.

1. **Schakel Foutmelding in**: Zet **Beantwoord deze e-mail als de import niet kan worden uitgevoerd** aan.
2. **Voer Melding E-mail in**: Voer in het nieuwe veld het e-mailadres in waar je foutmeldingen wilt ontvangen.

Met deze functie ingeschakeld, zullen mislukte importpogingen een automatische reactie naar het opgegeven e-mailadres triggeren, zodat je snel importproblemen kunt aanpakken.

**Vergeet niet op Opslaan te klikken om je wijzigingen toe te passen na het configureren van alle instellingen.**
