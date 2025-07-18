# Correos electrónicos entrantes

## Activando Correos Electrónicos Entrantes para Procesamiento de Documentos

Para comenzar a usar correos electrónicos entrantes para el procesamiento de documentos, sigue estos pasos:

1. **Ve a Ajustes**: Comienza navegando al menú de **Ajustes** de la aplicación.
2. **Selecciona Procesamiento de Documentos**: En los ajustes, elige **Procesamiento de documentos** para acceder a las opciones de configuración relacionadas.
3. **Abre Módulos**: En la sección de Procesamiento de documentos, haz clic en **Módulos**.
4. **Desplázate hasta Tipo de Documento**: Desplázate hacia abajo hasta que encuentres **Tipo de Documento**.
5. **Activa Correos Electrónicos Entrantes**: Encuentra **Correos Electrónicos Entrantes** y actívalo cambiando el interruptor.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_1.png)

## Configurando Correos Electrónicos Entrantes para Importar Documentos

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_2.png)

Después de activar los correos electrónicos entrantes, configura los ajustes para controlar cómo se importan los documentos. Así es como:

1. **Regresa a Procesamiento de Documentos**: En los ajustes, navega a **Procesamiento de documentos**.
2.  **Selecciona Importar**: Elige **Importar** para acceder a los ajustes de correos electrónicos entrantes.

    Verás las siguientes opciones:

    * **Campo de Correo Electrónico**: Este campo muestra una dirección de correo electrónico única generada por el sistema basada en el ID de tu organización. El formato es `org_id@environment.inbound.docbits.com`. Envía o reenvía correos electrónicos con documentos a esta dirección para la importación automatizada.
    * **Importar Documento Sólo Desde Correo(s) Predefinido(s)**: Activa esta opción para restringir las importaciones a correos electrónicos recibidos solo de direcciones específicas y predefinidas.
    * **Responda a este Correo Electrónico Si No Se Puede Realizar la Importación**: Activa esta opción si deseas que el sistema responda automáticamente cuando falle un intento de importación.
3. **Guardar Ajustes**: Después de configurar estas opciones, haz clic en **Guardar** para aplicarlas.

## Correo(s) Electrónico(s) Predefinido(s)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_3.png)

Cuando la opción **Importar Documento Sólo Desde Correo(s) Predefinido(s)** está habilitada, puedes gestionar qué direcciones de correo electrónico están autorizadas para enviar documentos al correo electrónico entrante.

1. **Ingresa Correos Electrónicos Autorizados**: En el campo **Poner correo electrónico aquí**, escribe cada dirección de correo electrónico que deseas autorizar.
2. **Asignar a Suborganización (Opcional)**:
   * Si no se selecciona ninguna suborganización, el documento se asignará a la organización principal.
   * Si se selecciona una suborganización, el documento se dirigirá solo a esa suborganización.
3. **Agregar Correo Electrónico**: Haz clic en **Agregar** para guardar cada correo electrónico en la lista de direcciones autorizadas.
4. **Borrar Correo Electrónico**: Para eliminar un correo electrónico autorizado, haz clic en **Borrar** junto a la entrada del correo electrónico.

Con esta configuración, los documentos de direcciones de correo electrónico no autorizadas serán ignorados, asegurando que solo fuentes específicas puedan enviar documentos para importación.

## **Responda a este correo electrónico si no se puede realizar la importación**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_4.png)

Si habilitas **Responda a este correo electrónico si no se puede realizar la importación**, aparecerá un campo adicional donde puedes ingresar una dirección de correo electrónico. Esta dirección de correo electrónico recibirá una notificación si algún intento de importación de documento falla, permitiéndote estar informado de cualquier problema en el proceso de importación.

1. **Habilitar Notificación de Fallo**: Activa **Responda a este correo electrónico si no se puede realizar la importación**.
2. **Ingresa Correo Electrónico de Notificación**: En el nuevo campo, ingresa la dirección de correo electrónico donde te gustaría recibir notificaciones de fallos.

Con esta función habilitada, cualquier intento de importación fallido desencadenará una respuesta automática al correo electrónico especificado, ayudándote a abordar rápidamente los problemas de importación.

**Después de configurar todos los ajustes, no olvides hacer clic en Guardar para aplicar tus cambios.**
