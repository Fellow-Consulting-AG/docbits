# DocBits Infor on Premise Customer

To send data to Infor onPremise customer we offer two ways Site2Site with IPsec or [WatchDog](../readme-1/how-to-import-documents/watchdog.md)

For an IPsec (Internet Protocol Security) site-to-site VPN, you need to configure and open the following ports:



1\. UDP port 500: Used for Internet Key Exchange (IKE) phase 1 and phase 2.

2\. UDP port 4500: Used for NAT traversal (NAT-T), allowing VPN traffic to pass through NAT (Network Address Translation) devices.

3\. Protocol 50: Used for Encapsulating Security Payload (ESP) which is responsible for encrypting the data payload.

4\. Protocol 51 (optional): Used for Authentication Header (AH), which provides data integrity and authenticity. Note that AH is less commonly used in modern IPsec implementations.

## Access for to Infor OS&#x20;

Auth: https://inforos.CustomerXYZad.net/&#x20;

Data: https://inforos.CustomerXYZad.net:7443/

