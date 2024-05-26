---
description: How to configure PowerBI
---

# PowerBI

1.  ODBC Driver Installation

    * You'll need the ODBC driver for ClickHouse to create a bridge to PowerBI. Head over to the ClickHouse official website or GitHub page to download and install the latest ODBC driver for ClickHouse. Just follow the setup wizard.

    <div align="left">

    <figure><img src="../../.gitbook/assets/1 (17).png" alt=""><figcaption></figcaption></figure>

    </div>
2. Configuring the ODBC Data Source
   * Open your ODBC Data Source Administrator from the Control Panel. Yes, that old thing still has its uses.
   * Go to the "System DSN" tab and hit "Add". Scroll through the list and find the ClickHouse ODBC driver you just installed. Give it a click.
   * Now, you get to fill in the blanks. Name your data source something memorable, put in your ClickHouse server details, and any other info required. Credentials, server address, port—make sure you get these right.
3. PowerBI Time!
   * Fire up PowerBI Desktop. Feeling the power yet?
   * Choose "Get Data" from the homepage or the ribbon—your call. Then, you’re aiming for "ODBC" under the database category. Hit "Connect".
   * You'll see a list of data sources. Find the name of the ODBC data source you christened earlier and select it. Then, proceed to "Connect".
4. Navigating the Navigator
   * After a moment of digital wizardry, you’ll see the Navigator pane. Here’s where you pick the tables or views you want to play with in PowerBI. Select what you need, then hit "Load" if you're ready to roll or "Transform Data" if you want to tweak things first.
5. Querying and Visualizing
   * With your data now in PowerBI, the world (or at least your data world) is your oyster. Use Power Query Editor for any heavy lifting on data transformation.
   * Dive into creating visuals. Drag fields onto the canvas, explore different visualization types, and tweak to your heart’s content. You know, make it pretty and insightful.
6. Refreshing Your Data
   * Remember, if your ClickHouse data changes, you’ll want those updates in PowerBI. You can set up scheduled refreshes in PowerBI Service to keep things up-to-date. Just make sure your PowerBI Desktop file is published to PowerBI Service, and configure the refresh settings there.

