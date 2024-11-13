# Architecture

Cliente en la cloud:

<figure><img src="../.gitbook/assets/architecture1.avif" alt=""><figcaption></figcaption></figure>

En las instalaciones:

<figure><img src="../.gitbook/assets/architecture2.avif" alt=""><figcaption></figcaption></figure>

Doc**Bits** se integra sin problemas con Infor LN/M3 a través de ION API, ION Desk y BODs estándar de Infor. Nuestra integración API nos permite exportar datos a Infor y realizar la validación de datos maestros en Doc**Bits**.

## Exportando Datos a Infor

Utilizamos la ION API para enviar el PDF con atributos a IDM y el BOD Sync.CaptureDocument a ION Desk. En ION Desk, transformamos el Sync.CaptureDocument a los BODs de destino deseados según el tipo de documento que se esté procesando. Estos BODs de Infor transformados se importan automáticamente a LN o M3.

{% hint style="info" %}
Exportar a [Infor](../setup/exporting-in-docbits/exporting-to-infor/)
{% endhint %}

## Validación de Datos Maestros en DocBits

Para identificar al proveedor o comparar/igualar líneas de órdenes de compra, activamos un disparador en LN/M3 que envía los BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster y Sync.PurchaseOrder a Doc**Bits**. Configuramos este proceso en ION Desk definiendo el flujo de datos a un punto de conexión específico a Doc**Bits**.

<figure><img src="../.gitbook/assets/architecture3.avif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Validación de Datos Maestros](../setup/importing-customer-master-data/)
{% endhint %}
