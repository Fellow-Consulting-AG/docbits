---
description: How to configure PowerBI
---

# PowerBI

This guide walks you through connecting **ClickHouse** to **Power BI Desktop** using the **ODBC driver**. It covers driver installation, ODBC configuration, Power BI integration, and setting up data refresh.

#### 1. Install the ClickHouse ODBC Driver

* Download the latest **ClickHouse ODBC Driver** from:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Run the installer and follow the setup wizard.

#### 2. Configure the ODBC Data Source

* Open **ODBC Data Source Administrator (64-bit)** via Control Panel or Windows Search.
* Go to the **System DSN** tab and click **Add**.
* Select **ClickHouse ODBC Driver** from the list and click **Finish**.
*   Fill in the required fields. You can find the necessary information in:

    **DocBits** → **Settings** → **Document Processing** → **Module** → **AI Dashboard** → **ClickHouse Direct Access**

    <figure><img src="../.gitbook/assets/image (440).png" alt=""><figcaption></figcaption></figure>

    **Required Fields:**

    * **Name**: A name for the connection (e.g., `ClickHouse_Prod`)
    * **Description**: A short description for your reference (optional)
    * **Host**: Copy the host value from DocBits
    * **Port**: Copy the port value from DocBits
    * **Database**: Copy the database name from DocBits
    * **Username**: Copy the username from DocBits
    * **Password**: Copy the password from DocBits

#### 3. Connect ClickHouse to Power BI

* Open **Power BI Desktop**.
*   Select **Get Data** → **ODBC** → **Connect**.\


    <figure><img src="../.gitbook/assets/Screenshot 2025-05-19 163621.png" alt=""><figcaption></figcaption></figure>
*   From the DSN list, select your configured source (e.g., `ClickHouse_Prod`).\


    <figure><img src="../.gitbook/assets/Screenshot 2025-05-19 163823.png" alt=""><figcaption></figcaption></figure>
* Click **OK**. Enter credentials again if prompted.

#### 4. Load and Transform Data

* In the **Navigator** pane, browse and select the tables or views to import.
* Choose:
  * **Load**: to import directly
  *   **Transform Data**: to open Power Query for data shaping\


      <figure><img src="../.gitbook/assets/Screenshot 2025-05-19 164134.png" alt=""><figcaption></figcaption></figure>

#### 5. Visualize Your Data

* Use the report canvas to build visualizations.
* Drag fields, add slicers, choose chart types, and use **DAX** expressions as needed.
* &#x20;Leverage **Power Query Editor** to clean or pivot your ClickHouse data before building visuals.
* PowerBI documentation:  [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Enable Scheduled Refresh (Optional)

<mark style="color:red;">**Note:**</mark> **Requires Power BI Pro or Premium + Gateway**

* To keep your reports in sync with ClickHouse:
* Publish your `.pbix` file to **Power BI Service**.
* Install the **Power BI Gateway** (Standard mode) on a machine with network access to ClickHouse.
* In Power BI Service:
  * Go to your dataset → **Settings** → **Scheduled Refresh**
  * Map your DSN and provide credentials
* More informations [here](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).&#x20;

#### 7. Example Dashboards & Data Views&#x20;

<div><figure><img src="../.gitbook/assets/Screenshot 2025-05-13 at 12.23.07.png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/Screenshot 2025-05-13 at 12.23.17.png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/Screenshot 2025-05-13 at 12.23.26.png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/Screenshot 2025-05-13 at 12.23.34.png" alt=""><figcaption></figcaption></figure></div>
