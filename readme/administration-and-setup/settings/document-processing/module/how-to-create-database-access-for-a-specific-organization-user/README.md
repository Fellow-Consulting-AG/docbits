# Cómo Crear Acceso a la Base de Datos para un Usuario Específico de la Organización

### **1. Iniciar sesión en Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Vaya a la página de inicio de sesión de su aplicación.
2. Ingrese sus credenciales (nombre de usuario y contraseña) para iniciar sesión.

### **2. Acceder a la Configuración** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Una vez conectado, localice el icono de **Configuración** (engranaje ⚙️) en la barra lateral izquierda.
2. Haga clic en **Configuración** para abrir el panel de configuración del sistema.

### **3. Abrir el Módulo de Procesamiento de Documentos** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. En la **Configuración**, localice la sección **Procesamiento de Documentos**.
2. En **Procesamiento de Documentos**, busque y haga clic en la opción **Módulo**.
   * Esto abrirá la página de configuración del módulo correspondiente donde podrá proceder con la creación del usuario para la base de datos.

<figure><img src="../../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

### 4. Pasos para Habilitar y Acceder al Usuario de Documentos de IA y Base de Datos: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Alternar Funciones**:
   * Utilice los interruptores a la derecha para habilitar o deshabilitar funciones específicas:
     * **Almacén de Documentos de IA**: Active esto para habilitar el acceso a las funciones relacionadas con la IA.
     * **Acceso a BD**: Active esto para otorgar acceso a la base de datos al usuario.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

2. **Credenciales de la Base de Datos**:
   * El panel proporciona los siguientes detalles de conexión a la base de datos:
     * **Nombre de usuario**: Se muestra un nombre de usuario único.
     * **Contraseña**: Asegúrese de que la contraseña se almacene o copie de forma segura.
     * **Base de datos**: Es el nombre de la Base de Datos.
     * **Host**: Nombre del Host.
     * **Puerto**: Es el Puerto.
     * **Modo SSL:** La conexión requiere `sslmode=require` para una comunicación segura.
3. **Copiar Credenciales**:
   * Utilice los iconos de copiar junto a cada campo para copiar rápidamente las credenciales para su uso en su cliente de base de datos o aplicación.
4. **Conexión a través de DBeaver:**
   *   Conectar a través de Host

       * elija PostgreSQL

       <figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

       * Complete la información requerida

       <figure><img src="../../../../../.gitbook/assets/image (4) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

       * cambie a la pestaña SSL y marque Usar SSL. Desplácese hacia abajo hasta el modo SSL y seleccione require

       <figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
   *   Conectar a través de URL

       * Complete la información requerida:
         - reemplace Host con la información de host proporcionada
         - reemplace Puerto con la información de puerto proporcionada
         - reemplace Base de datos con la información de base de datos proporcionada
         - para Nombre de usuario seleccione la información de nombre de usuario proporcionada
         - para Contraseña seleccione la información de contraseña proporcionada

       <figure><img src="../../../../../.gitbook/assets/image (5) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
5. **Probar la Conexión**:
   * Haga clic en el botón **"Probar Conexión"** para asegurarse de que las credenciales y los detalles de la conexión sean correctos.
   * Si la prueba es exitosa, proceda a conectar.
6. **Explorar la Base de Datos**:
   * Una vez conectado, navegue a la sección **esquema** o **tablas** en su cliente de base de datos.
   * Verifique las tablas disponibles.
