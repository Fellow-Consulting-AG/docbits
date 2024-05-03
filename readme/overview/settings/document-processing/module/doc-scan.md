# Doc Scan

**Download Scanner Software**

Click Scan Document on the DocBits Dashboard.

![](https://lh7-us.googleusercontent.com/6IJkuLCmE8lwi-zfw6M36vtDaxAMZHhxBQlNyd6\_vQhFdty6etnXe1THTuEm2\_nn468VsXv3yyebeLTFbGeoOCwArDVlto5O7Aa4XRzw5OfnUEABaKFprecs9bBz3hEpK9m8fL5CNE04pdJ4NvRL-Cw)

As your scanner is not installed yet, you’ll get the following message.

![](https://lh7-us.googleusercontent.com/vG0ySeIyP25Vl7tFwx7UAAME31dvJH7p5kRDavTTv-LrRnCw6Nr5HagWbZrgMQaf0oQ5GNYzi8u-d-Wc1wkT5kWmvFgepJtJUQc4T7PdarGcLnuh90iTT6cMtZ3jQZy5\_BQE4sD\_uTAne03kNPlIe2s)

Depending on which operating system you use, press the appropriate button to download.

Open the installation file and you will see the following.

![](https://lh7-us.googleusercontent.com/hsu0QFcM2zv\_hl2IiRz8Pv-oFXa\_Ry4ePaVR-cJBGgq43KoMu0gxLv1NTyRbvJuV0VDT0zUPGa3Im2H64z4lAORWxza2KOqQ9TWz8ssAi\_fECA-ZIgJORh26ZEbI2rRC0YybCAhHBpx86c\_CTPo-35o)

Click on \`Continue\`, accept the Software License Agreement with \`Agree\` and continue to install the software.

Installing this software requires 33,6 MB of space. You can change the install location before clicking \`Install\` in the next step. As soon as the following screen is displayed you’re almost done.

![](https://lh7-us.googleusercontent.com/WO3PB9qvbVEkisdrUg8Oeo-RzyPwHyVqhyc3bPTztkqMCHmFxhYeGrytaz0LV7qbaTu7I4ZEwBd5JBM04uzt02z-AmTqKOcH2dKZ3ZIgkW8-ln0vJD2nM9EBbQFjpsN\_zbCGBLqXnuX1PlxR3vCR1pA)

Open web browser to test if the app works by entering: https://local.polydocs.io:12500/

If you see this message on the screen, you must first configure some settings in your FritzBox network settings if you are using one.

![](https://lh7-us.googleusercontent.com/voqEnkxI\_zXA-LcIwmKyMp5se3aWVt4uZgsF\_Ee4lI6Q6K2ShKhjoVED8sxZIOZO-7MV8HobTFsIb4IKUiMItedsHgWAh95KLJtW15LHsHsbDbZ9EOM8pkzdh9KhWB03l3EwCc5ArVDaIqmvUjCyd38)

When you see this screen you are ready to click on DocBits.

![](https://lh7-us.googleusercontent.com/ZBuNGMvyVsJhzJ0dqV083BtdJQgfzk4T5CoBS69hjHGuPMh5KirmHdHZpDNww\_HIyaiEn8AsWitMx-Km3EQvnlG0bK8stXnbM6rIyOjmUvAVVRi7xNjDzZ9mPj7JYuRASSPPAJGcFXRnGC1SoztRer4)

You will be redirected to the DocBits login page where you can enter your credentials to access your dashboard.

![](https://lh7-us.googleusercontent.com/CnLDyP06o\_IUz2XlWNo5IxOMi\_5-xC2oaiVgJ0T6ajayKv3CkNbv87G8yFDKSTAUEqhJFXZTkYQEICdUH3BJCybrAOH5c6r5geaoYw6dP0oI0By6DDkAyK81Xkl-mQcJLA78gH5lqPrX7F6AlNhvODs)

All you have to do now is activate Doc Scan in the settings under Modules.

![](https://lh7-us.googleusercontent.com/AVin99r2CWGZI73c-w87UyHkWGf9-IQAQ2oA8TiYwJKzOm6mXregJ5ttuGzi5jrbhNLhaT32EVvWEbK7-nK2m2TYYuGp2UB6UgPeXTzJeOVNes6qHrO1oidvmh93IKa8bw5RU6UVUD80HAsCkW92PJM)

**FritzBox Network Settings**

If you get the following error after installing and calling up the url https://local.polydocs.io:12500/, the reasons are:

* DNS resolution of private IP addresses is not possible.
* DNS resolution for domain names that refer to private IP addresses in the FRITZ!Box home network is not possible via the FRITZ!Box. This means that server services in the FRITZ!Box home network cannot be accessed via the domain name.

You may see one of the following error messages:

* “DNS timed out”
* “DNS request timed out”

For security reasons, the FRITZ!Box suppresses DNS responses that refer to IP addresses in your own home network. This is a security feature of the FRITZ!Box to protect against so-called DNS rebinding attacks.

If you use a FritzBox, you must first make the following settings in the FritzBox menu:

* In the FRITZ!Box user interface, click on \`Heimnetz\`.
* \`Heimnetz\` Click in the menu \`Netzwerk\`.
* Click on the tab \`Netzwerkeinstellungen\`.

In the Hostname exceptions \`DNS-Rebind-Schutz section\`, enter local.polydocs.io for which DNS rebind protection should not apply. Confirm with \`Übernehmen\`

Uninstall Doc2Scan Service Manager

Run the following command to uninstall Doc2Scan Manager:

sudo bash /Library/doc2scan/uninstall.sh

DocScan is compatible with a variety of scanners, to see the full list of compatible scanners, visit: https://docbits.com/doc/settings/modules/doc-scan/

\
