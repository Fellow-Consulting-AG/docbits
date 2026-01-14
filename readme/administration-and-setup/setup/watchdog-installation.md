# WatchDog Installation

## Configuring WatchDog in DocBits

1. **Access WatchDog Settings**
   * Navigate to **Settings → Document Processing → WatchDog**.\

2.  **Folder Settings**

    * Define the paths where WatchDog finds and processes documents.
    * The folder paths should match those created during installation:
      * `C:/WatchDog/Read`
      * `C:/WatchDog/Processed`

    <div data-full-width="true"><figure><img src="../../.gitbook/assets/image (405).png" alt=""><figcaption></figcaption></figure></div>

    * <mark style="color:red;">**Note**</mark>**:  It is recommended to use local paths. These should match the folders in the DocBits Installation**
3. **General Settings**
   *   Select the document types to process by checking the corresponding checkboxes\
       \


       <figure><img src="../../.gitbook/assets/image (1) (4).png" alt=""><figcaption></figcaption></figure>
   * **Barcode Divider:** When turned on enables the barcode dividing.
   * **DocBits Operator:** When enabled opens a chrome browser in the background for the DocBits Operator.
   *   **Export destination:** Sets the export destination.&#x20;

       * **Infor:** Documnets get exported to Infor.
       * **Enaoi Export:** Documents get exported to a defined folder that can be configured below.&#x20;

       <figure><img src="../../.gitbook/assets/image (1) (4) (1).png" alt=""><figcaption></figcaption></figure>

       * <mark style="color:red;">**Note:**</mark> **For XSLT configuration, please consult your project manager.**
4. **Export Configurations**
   * Displays all configured exports for **on-premise processing**.
   *   Shows the timestamp of the **last successful connection** for each configuration.\




       <figure><img src="../../.gitbook/assets/image (425).png" alt=""><figcaption></figcaption></figure>
5.  **bod\_mapping Configuration (Optional)**

    * <mark style="color:red;">**Required Fields:**</mark> Before adding custom metadata mappings, you **must** define the following two values:
      * **`file_name`**&#x20;
      * **`pdf_path`**&#x20;
    * Click **Add Row** to define metadata mappings.\


    <figure><img src="../../.gitbook/assets/image (426).png" alt=""><figcaption></figcaption></figure>

    * **Value:** Specifies the field name for the metadata.
    * **Path:** The XPath expression pointing to the XML data that should be assigned to the field.
    * **Trashcan Icon:** Used to delete a secific row. \

6. **Download the Configuration**&#x20;
   * Save the configuration&#x20;
   *   Download the configuration\


       <figure><img src="../../.gitbook/assets/image (427).png" alt=""><figcaption></figcaption></figure>

## WatchDog Installation Guide

1. **Create Required Folders**
   * Create a main directory: `C:/WatchDog`
   * Inside `C:/WatchDog`, create the following subfolders:
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Note**</mark>**:  It is recommended to use local paths. These should match the folders in the DocBits Configuration**
2. **Download WatchDog**
   * Download the latest version of `WatchDog.exe` from:\
     [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Place the downloaded `WatchDog.exe` file in `C:/WatchDog`.
   * Place the downloaded `watchdog-config.json` file in `C:/WatchDog`.
   * open the `watchdog-config.json.`  and change the **config\_path.**&#x20;
   * In this example:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`\

3. **Install WatchDog**
   * Open **Command Prompt (CMD)** with **Administrator rights**.
   * Navigate to the WatchDog folder&#x20;
   *   Run the following command to install WatchDog:

       `WatchDog.exe install`\

4. **Start the WatchDog Service**
   *   Run the following command in CMD:

       `WatchDog.exe start`\

5. **Set Startup Type**
   * Open **Services** (Press `Win + R`, type `services.msc`, and press **Enter**).
   * Locate **WatchDog** in the service list.
   * Double-click to open its properties.
   * Set **Startup Type** to **Automatic (Delayed Start)**.
   * Click **OK**.

