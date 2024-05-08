# Grupos y Permisos

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.26.22.png" alt=""><figcaption></figcaption></figure>

#### Componentes de la Sección de Grupos y Permisos

1. **Activar/Desactivar Grupos y Permisos**: Un interruptor que permite al administrador del sistema habilitar o deshabilitar el uso de grupos y permisos en toda la plataforma. Cuando se desactiva, el sistema puede recurrir a un modelo de control de acceso menos granular.
2. **Lista de Grupos**: Muestra la lista de grupos de usuarios disponibles dentro de la organización. Cada grupo se puede configurar con permisos específicos. Los administradores pueden agregar nuevos grupos haciendo clic en el botón "+ Nuevo".
3. **Tabla de Permisos**:

- Se muestra una vez que se selecciona un grupo o se está configurando un nuevo grupo.
- Enumera todos los tipos de documentos reconocidos por el sistema (por ejemplo, FACTURA, NOTA DE CRÉDITO, NOTA DE ENTREGA).
- Para cada tipo de documento, hay casillas de verificación para diferentes permisos:
  - **Ver**: Permiso para ver el documento.
  - **Actualizar**: Permiso para modificar el documento.
  - **Eliminar**: Permiso para eliminar el documento del sistema.
  - **Primera Aprobación**: Permiso para realizar la aprobación inicial del documento.
  - **Segunda Aprobación**: Permiso para realizar un segundo nivel de aprobación (si corresponde).

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.26.33.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2486" %}
