# DocBits Infor on Premise Customer

To send data to Infor onPremise customer we offer two ways Site2Site with IPsec or [WatchDog](../../end-user-and-partner-section/end-user-section/how-to-import-documents/watchdog.md)

Sending Data to Infor On-Premise Customer

To send data to an Infor on-premise customer, we offer two ways: Site-to-Site VPN with IPsec.

## IPsec (Internet Protocol Security) Site-to-Site VPN Configuration

### For an IPsec site-to-site VPN, you need to configure and open the following ports:

1\. UDP port 500: Used for Internet Key Exchange (IKE) phase 1 and phase 2.

2\. UDP port 4500: Used for NAT traversal (NAT-T), allowing VPN traffic to pass through NAT (Network Address Translation) devices.

## Accessing Infor OS

• Authentication URL: https://inforos.CustomerXYZad.net/

• Data URL: https://inforos.CustomerXYZad.net:7443/

## Summary:

For setting up an IPsec site-to-site VPN, ensure the above ports and protocols are configured and open.

Use the provided URLs to access Infor OS for authentication and data.



