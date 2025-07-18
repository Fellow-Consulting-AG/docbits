# E-mails entrants

## Activation des E-mails entrants pour le Traitement des documents

Pour commencer à utiliser les e-mails entrants pour le traitement des documents, suivez ces étapes :

1. **Allez dans Paramètres** : Commencez par naviguer vers le menu **Paramètres** de l'application.
2. **Sélectionnez Traitement des documents** : Sous les paramètres, choisissez **Traitement des documents** pour accéder aux options de configuration associées.
3. **Ouvrez le Module** : Dans la section Traitement des documents, cliquez sur **Module**.
4. **Faites défiler jusqu'au Type de document** : Faites défiler vers le bas jusqu'à ce que vous trouviez **Type de document**.
5. **Activez E-mail entrant** : Trouvez **E-mail entrant** et activez-le en basculant l'interrupteur.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_1.png)

## Configuration de l'E-mail entrant pour l'Importation de documents

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_2.png)

Après avoir activé l'e-mail entrant, configurez les paramètres pour contrôler comment les documents sont importés. Voici comment :

1. **Retournez au Traitement des documents** : Dans les paramètres, naviguez vers **Traitement des documents**.
2.  **Sélectionnez Importer** : Choisissez **Importer** pour accéder aux paramètres des e-mails entrants.

    Vous verrez les options suivantes :

    * **Champ E-mail** : Ce champ affiche une adresse e-mail unique, générée par le système, basée sur l'ID de votre organisation. Le format est `org_id@environment.inbound.docbits.com`. Envoyez ou transférez des e-mails avec des documents à cette adresse pour une importation automatisée.
    * **Importation de documents uniquement à partir d'e-mails prédéfinis** : Activez cette option pour restreindre les importations aux e-mails reçus uniquement d'adresses spécifiques et prédéfinies.
    * **Répondre à cet e-mail si l'importation ne peut être effectuée** : Activez cette option si vous souhaitez que le système réponde automatiquement lorsqu'une tentative d'importation échoue.
3. **Sauvegarder les paramètres** : Après avoir configuré ces options, cliquez sur **Sauvegarder** pour les appliquer.

## E-mail(s) prédéfini(s)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_3.png)

Lorsque l'option **Importation de documents uniquement à partir d'e-mails prédéfinis** est activée, vous pouvez gérer quelles adresses e-mail sont autorisées à envoyer des documents à l'e-mail entrant.

1. **Entrez les E-mails autorisés** : Dans le champ **Mettre l'e-mail ici**, tapez chaque adresse e-mail que vous souhaitez autoriser.
2. **Attribuer à une sous-organisation (facultatif)** :
   * Si aucune sous-organisation n'est sélectionnée, le document sera attribué à l'organisation principale.
   * Si une sous-organisation est sélectionnée, le document sera dirigé uniquement vers cette sous-organisation.
3. **Ajouter un E-mail** : Cliquez sur **Ajouter** pour sauvegarder chaque e-mail dans la liste des adresses autorisées.
4. **Supprimer un E-mail** : Pour retirer un e-mail autorisé, cliquez sur **Supprimer** à côté de l'entrée de l'e-mail.

Avec cette configuration, les documents provenant d'adresses e-mail non autorisées seront ignorés, garantissant que seules des sources spécifiques peuvent envoyer des documents pour importation.

## **Répondre à cet e-mail si l'importation ne peut être effectuée**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_4.png)

Si vous activez **Répondre à cet e-mail si l'importation ne peut être effectuée**, un champ supplémentaire apparaît où vous pouvez entrer une adresse e-mail. Cette adresse e-mail recevra une notification si une tentative d'importation de document échoue, vous permettant de rester informé de tout problème dans le processus d'importation.

1. **Activer la notification d'échec** : Activez **Répondre à cet e-mail si l'importation ne peut être effectuée**.
2. **Entrez l'E-mail de notification** : Dans le nouveau champ, entrez l'adresse e-mail où vous souhaitez recevoir les notifications d'échec.

Avec cette fonctionnalité activée, toute tentative d'importation échouée déclenchera une réponse automatique à l'e-mail spécifié, vous aidant à résoudre rapidement les problèmes d'importation.

**Après avoir configuré tous les paramètres, n'oubliez pas de cliquer sur Sauvegarder pour appliquer vos modifications.**
