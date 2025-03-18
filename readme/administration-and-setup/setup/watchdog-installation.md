# WatchDog Installation

## Configurer WatchDog dans DocBits

1. **Accéder aux Paramètres de WatchDog**
   * Naviguez vers **Paramètres → Traitement des Documents → WatchDog**.
2. **Dossier Paramètres**
   * Définissez les chemins où WatchDog trouve et traite les documents.
   * Les chemins des dossiers doivent correspondre à ceux créés lors de l'installation :
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
3. **Paramètres Généraux**
   * Sélectionnez les types de documents à traiter en cochant les cases correspondantes.
4. **Configurations d'Exportation**
   * Affiche toutes les exportations configurées pour **traitement sur site**.
   * Affiche l'horodatage de la **dernière connexion réussie** pour chaque configuration.
5. **Télécharger la Configuration**
   * Enregistrez la configuration
   * Téléchargez la configuration

## Guide d'Installation de WatchDog

1. **Créer les Dossiers Requis**
   * Créez un répertoire principal : `C:/WatchDog`
   * À l'intérieur de `C:/WatchDog`, créez les sous-dossiers suivants :\
     <mark style="color:red;">**Remarque**</mark>**: ceux-ci doivent correspondre aux dossiers dans DocBits**
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
2. **Télécharger WatchDog**
   * Téléchargez la dernière version de `WatchDog.exe` depuis :\
     [https://github.com/Fellow-Consulting-AG/ActualWatchdog/releases](https://github.com/Fellow-Consulting-AG/ActualWatchdog/releases)
   * Placez le fichier téléchargé `WatchDog.exe` dans `C:/WatchDog`.
   * Placez le fichier téléchargé `watchdog-config.json` dans `C:/WatchDog`.
   * ouvrez le `watchdog-config.json.` et changez le **config\_path.**
   * Dans cet exemple :
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Installer WatchDog**
   * Ouvrez **Invite de Commande (CMD)** avec **droits d'Administrateur**.
   * Naviguez vers le dossier WatchDog
   *   Exécutez la commande suivante pour installer WatchDog :

       `WatchDog.exe install`
4. **Démarrer le Service WatchDog**
   *   Exécutez la commande suivante dans CMD :

       `WatchDog.exe start`
5. **Définir le Type de Démarrage**
   * Ouvrez **Services** (Appuyez sur `Win + R`, tapez `services.msc`, et appuyez sur **Entrée**).
   * Localisez **WatchDog** dans la liste des services.
   * Double-cliquez pour ouvrir ses propriétés.
   * Définissez le **Type de Démarrage** sur **Automatique (Démarrage Différé)**.
   * Cliquez sur **OK**.
