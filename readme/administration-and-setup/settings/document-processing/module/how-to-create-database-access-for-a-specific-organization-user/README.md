# Comment Créer un Accès à la Base de Données pour un Utilisateur Spécifique de l'Organisation

### **1. Se Connecter à Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Allez sur la page de connexion de votre application.
2. Saisissez vos identifiants (nom d'utilisateur et mot de passe) pour vous connecter.

### **2. Accéder aux Paramètres** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Une fois connecté, repérez l'icône **Paramètres** (engrenage ⚙️) dans la barre latérale gauche.
2. Cliquez sur **Paramètres** pour ouvrir le panneau de configuration du système.

### **3. Ouvrir le Module de Traitement des Documents** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Dans les **Paramètres**, repérez la section **Traitement des Documents**.
2. Sous **Traitement des Documents**, trouvez et cliquez sur l'option **Module**.
   * Cela ouvrira la page de configuration du module pertinent où vous pourrez procéder à la création de l'utilisateur pour la base de données.

<figure><img src="../../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

### 4. Étapes pour Activer et Accéder à l'Utilisateur de Documents IA et de Base de Données : <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Basculer les Fonctionnalités** :
   * Utilisez les commutateurs sur la droite pour activer ou désactiver des fonctionnalités spécifiques :
     * **Entrepôt de Documents IA** : Activez ceci pour permettre l'accès aux fonctionnalités liées à l'IA.
     * **Accès BD** : Activez ceci pour accorder l'accès à la base de données à l'utilisateur.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

2. **Identifiants de la Base de Données** :
   * Le tableau de bord fournit les détails suivants de connexion à la base de données :
     * **Nom d'utilisateur** : Un nom d'utilisateur unique est affiché.
     * **Mot de passe** : Assurez-vous que le mot de passe est stocké ou copié en toute sécurité.
     * **Base de données** : Est le nom de la Base de Données.
     * **Hôte** : Nom de l'Hôte.
     * **Port** : Est le Port.
     * **Mode SSL :** La connexion nécessite `sslmode=require` pour une communication sécurisée.
3. **Copie des Identifiants** :
   * Utilisez les icônes de copie à côté de chaque champ pour copier rapidement les identifiants pour une utilisation dans votre client de base de données ou votre application.
4. **Connexion via DBeaver :**
   *   Se connecter via Hôte

       * choisissez PostgreSQL

       <figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

       * Remplissez les informations requises

       <figure><img src="../../../../../.gitbook/assets/image (4) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

       * passez à l'onglet SSL et cochez Utiliser SSL. Descendez jusqu'au mode SSL et sélectionnez require

       <figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
   *   Se connecter via URL

       * Remplissez les informations requises :
         - remplacez Hôte par les informations d'hôte fournies
         - remplacez Port par les informations de port fournies
         - remplacez Base de données par les informations de base de données fournies
         - pour Nom d'utilisateur sélectionnez les informations de nom d'utilisateur fournies
         - pour Mot de passe sélectionnez les informations de mot de passe fournies

       <figure><img src="../../../../../.gitbook/assets/image (5) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
5. **Tester la Connexion** :
   * Cliquez sur le bouton **"Tester la Connexion"** pour vous assurer que les identifiants et les détails de connexion sont corrects.
   * Si le test est réussi, procédez à la connexion.
6. **Explorer la Base de Données** :
   * Une fois connecté, naviguez vers la section **schéma** ou **tables** dans votre client de base de données.
   * Vérifiez les tables disponibles.
