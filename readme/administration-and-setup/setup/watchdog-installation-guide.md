# WatchDog Installation Guide

## Configuring WatchDog in DocBits

1. **Access WatchDog Settings**
   * Navigate to **Settings → Document Processing → WatchDog**.\

2. **Folder Settings**
   * Define the paths where WatchDog finds and processes documents.
   *   The folder paths should match those created during installation:

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       <div data-full-width="true"><figure><img src="../../.gitbook/assets/image (405).png" alt=""><figcaption></figcaption></figure></div>
3. **General Settings**
   *   Select the document types to process by checking the corresponding checkboxes\


       <figure><img src="../../.gitbook/assets/Bildschirmfoto 2025-02-19 um 09.15.55.png" alt=""><figcaption></figcaption></figure>
4. **Export Configurations**
   * Displays all configured exports for **on-premise processing**.
   *   Shows the timestamp of the **last successful connection** for each configuration.\


       <figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

## WatchDog Installation Guide

1. **Create Required Folders**
   * Create a main directory: `C:/WatchDog`
   * Inside `C:/WatchDog`, create the following subfolders:
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`\

2. **Download WatchDog**
   * Download the latest version of `WatchDog.exe` from:\
     [ ](https://github.com/Fellow-Consulting-AG/ActualWatchdog/releases)[https://github.com/Fellow-Consulting-AG/ActualWatchdog/releases](https://github.com/Fellow-Consulting-AG/ActualWatchdog/releases)
   * Place the downloaded `WatchDog.exe` file in `C:/WatchDog`.\

3. **Install WatchDog**
   * Open **Command Prompt (CMD)** with **Administrator rights**.
   * Navigate to the WatchDog folder&#x20;
   *   Run the following command to install WatchDog:

       `WatchDog.exe install`
   * The configuration window will open automatically.\

4. **Configure Settings**
   * Navigate to the **Settings tab in the configuration window.**
   * Adjust the settings as needed.
   * Click **Save**.\

5. **Reinstall the Service**
   *   To apply the new settings, rerun the installation command:

       `WatchDog.exe install`\

6. **Start the WatchDog Service**
   *   Run the following command in CMD:

       `WatchDog.exe start`\

7. **Set Startup Type**
   * Open **Services** (Press `Win + R`, type `services.msc`, and press **Enter**).
   * Locate **WatchDog** in the service list.
   * Double-click to open its properties.
   * Set **Startup Type** to **Automatic (Delayed Start)**.
   * Click **OK**.

## Updating the WatchDog

1. **Stop the Service**
   * Open **Command Prompt (CMD)** with **Administrator rights**.
   * Navigate to the WatchDog folder
   *   Run the following command:

       `WatchDog.exe stop`\

2. **Remove the Service**
   *   Execute the following command in CMD:

       `WatchDog.exe remove`\

3. **Reset Configuration**
   * Delete or rename the existing configuration file in `C:/WatchDog`.
   * Re-download `WatchDog.exe` if needed from:\
     [https://github.com/Fellow-Consulting-AG/ActualWatchdog/releases](https://github.com/Fellow-Consulting-AG/ActualWatchdog/releases)
   * Place `WatchDog.exe` in `C:/WatchDog`.\

4. **Reinstall the Service**
   *   Run the installation command:

       `WatchDog.exe install`
   * Enter the configuration settings and click **Save**.
   *   To apply the configuration, run the command again:

       `WatchDog.exe install`\

5. **Start the Service**
   *   Run the following command to start WatchDog:

       `WatchDog.exe start`
