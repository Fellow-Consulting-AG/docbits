# Arquitectura

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits** se integra perfectamente con Infor LN/M3 a través de la API ION, ION Desk y los BODs estándar de Infor. Nuestra integración de API nos permite exportar datos a Infor y realizar validación de datos maestros en Doc**Bits**.

## Exportar Datos a Infor

Utilizamos la API ION para enviar el PDF con atributos a IDM y el BOD Sync.CaptureDocument a ION Desk. En ION Desk, transformamos el Sync.CaptureDocument a los BODs de destino deseados basados en el tipo de documento que se está procesando. Estos BODs de Infor transformados se importan automáticamente a LN o M3.

## Validación de Datos Maestros en DocBits

Para identificar al proveedor o comparar/igualar las líneas de orden de compra, activamos un desencadenante en LN/M3 que envía los BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster y Sync.PurchaseOrder a Doc**Bits**. Configuramos este proceso en ION Desk definiendo el flujo de datos a un punto de conexión específico a Doc**Bits**.
