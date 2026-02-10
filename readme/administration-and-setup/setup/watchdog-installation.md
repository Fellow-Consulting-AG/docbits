# WatchDog Installation

## Configuring WatchDog in DocBits

For detailed configuration instructions, please refer to the [WatchDog Configuration](watchdog-configuration.md) page.

## WatchDog Installation Guide

1. **Create Required Folders**
   * Create a main directory: `C:/WatchDog`
   * Inside `C:/WatchDog`, create the following subfolders:
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Note**</mark>**: It is recommended to use local paths. These should match the folders in the DocBits Configuration**
2. **Download WatchDog**
   * Download the latest version of `WatchDog.exe` from: [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Place the downloaded `WatchDog.exe` file in `C:/WatchDog`.
   * Place the downloaded `watchdog-config.json` file in `C:/WatchDog`.
   * open the `watchdog-config.json.` and change the **config\_path.**&#x20;
   * In this example:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Install WatchDog**
   * Open **Command Prompt (CMD)** with **Administrator rights**.
   * Navigate to the WatchDog folder&#x20;
   *   Run the following command to install WatchDog:

       `WatchDog.exe install`
4. **Start the WatchDog Service**
   *   Run the following command in CMD:

       `WatchDog.exe start`
5. **Set Startup Type**
   * Open **Services** (Press `Win + R`, type `services.msc`, and press **Enter**).
   * Locate **WatchDog** in the service list.
   * Double-click to open its properties.
   * Set **Startup Type** to **Automatic (Delayed Start)**.
   * Click **OK**.
