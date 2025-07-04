# Exportar

## Visión general

La página de Exportar muestra todas las configuraciones de exportación configuradas, incluido si están activas o inactivas. Desde aquí, los usuarios pueden:

* Ver y gestionar las configuraciones de exportación existentes
* Crear nuevas conexiones de exportación (por ejemplo, a **Infor**, **Infor & IDM**, **Webhook** o **SFTP**)
* Editar o eliminar las configuraciones de exportación existentes

## Dónde encontrarlo

Puedes encontrarlo en: **Configuración** → **Procesamiento de documentos** → **Exportar**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6ldlcI2sVUEgDdWb9U4%252Fimage.png%3Falt%3Dmedia%26token%3D8368818d-c899-4bee-ad21-a631d6be5c20\&width=768\&dpr=4\&quality=100\&sign=fbfcbd0c\&sv=2)

## **Usando la página de Exportar**

Cuando abres la página de Exportar, verás una lista de todas las configuraciones de exportación existentes.

Cada fila en la lista muestra:

* **Indicador de estado**
  * **Verde** significa que la exportación está activa
  * **Rojo** significa que la exportación está desactivada
* **Nombre** – el nombre de la configuración de exportación
* **Tipo de documento** – el tipo de documento para el que se ha configurado la exportación
* **Sub-Organización** – si la exportación está limitada a una sub-organización específica
* **Método de exportación** – dónde se enviará el documento (por ejemplo, Infor, IDM, SFTP)
* **Acciones** – botones para **editar, eliminar** o **activar/desactivar** la configuración

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyN87I5gzXxwGoAqC6zMF%252Fimage.png%3Falt%3Dmedia%26token%3D7df9d573-7e57-4ace-99c6-15a83691b926\&width=768\&dpr=4\&quality=100\&sign=6221cb80\&sv=2)

#### **Reglas importantes para la configuración de exportación**

Para cada **tipo de documento** **dentro de una organización o suborganización dada**, se aplican las siguientes reglas:

* Puedes tener **solo una exportación activa de Infor**
* Puedes tener **solo una exportación activa que no sea de Infor** (por ejemplo, Webhook, SFTP)

Sin embargo, es posible tener:

* **Una exportación activa de Infor** _y_ **una exportación activa que no sea de Infor** al mismo tiempo para el mismo tipo de documento
* **Diferentes configuraciones de exportación para diferentes suborganizaciones** — por ejemplo, una exportación de Infor para Sub-Org A y otra exportación de Infor para Sub-Org B

## **Creando una nueva exportación**

Para crear una nueva exportación:

1. Haz clic en el botón **“Nuevo”**.\
   &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FTsHrIAUpe7EqenIzNAaJ%252Fimage.png%3Falt%3Dmedia%26token%3Dd2dbc996-b129-443c-a8df-9927a6f43a36\&width=300\&dpr=4\&quality=100\&sign=8769c331\&sv=2)
2. Selecciona el **Tipo de exportación** que deseas configurar (por ejemplo, Infor, IDM, SFTP).
3. Completa los campos requeridos según el tipo de exportación.
4. Guarda la configuración.

## Opciones de Exportación

#### Webhook

<details>

<summary>Webhook</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCwXUqFdCbRI5lRW49ymw%252Fimage.png%3Falt%3Dmedia%26token%3D798c0f40-6c4a-4650-9320-af2c17634fe9\&width=768\&dpr=4\&quality=100\&sign=15836833\&sv=2)

#### **Descripciones de Campos**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable con todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **URL de Exportación** La URL de destino donde se debe exportar el documento.

</details>

#### SFTP

<details>

<summary>SFTP</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzwUCWTdFETTvuTGl8qAn%252Fimage.png%3Falt%3Dmedia%26token%3D3f94b210-0128-4710-ae69-150a1363ce49\&width=768\&dpr=4\&quality=100\&sign=4ecd353\&sv=2)

#### **Descripciones de Campo**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Nombre de Usuario** El nombre de usuario utilizado para autenticarse en el servidor SFTP.
* **Contraseña** La contraseña correspondiente para la cuenta SFTP. Asegúrese de que la cuenta tenga acceso de escritura a la carpeta especificada.
* **URL del Servidor** El nombre de host o la dirección IP del servidor SFTP de destino.
* **Puerto** El puerto utilizado para conectarse al servidor SFTP.
* **Carpeta** La ruta en el servidor SFTP donde se deben cargar los documentos (por ejemplo, `/incoming/invoices/`). Debe existir y ser escribible.
*   **Archivo XSLT (Opcional)**

    El **archivo XSLT** permite la transformación del formato de exportación predeterminado de DocBits.

    * **Cuándo usar:** Solo si el sistema receptor requiere una estructura diferente o un formato específico que difiere del predeterminado de DocBits.
    * **Déjelo vacío** si el formato de exportación predeterminado cumple con los requisitos.

</details>

#### Exportación de Infor a SFTP

<details>

<summary>Exportación de Infor a SFTP</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FU0W4Qdy7ZlNoCn3E9wX5%252Fimage.png%3Falt%3Dmedia%26token%3D33673a12-55c4-479b-8ca8-b7c95e7a6a89\&width=768\&dpr=4\&quality=100\&sign=4af07f48\&sv=2)

#### **Descripciones de Campos**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable con todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Archivo de Mapeo IDM** Seleccione un archivo de mapeo desde el administrador de archivos. [¿Necesita ayuda para crear uno? Consulte la Guía de Mapeo IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Archivo de Mapeo BOD** Seleccione un archivo de mapeo desde el administrador de archivos. [¿Necesita ayuda para crear uno? Consulte la Guía de Mapeo BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Carpeta** La ruta en el servidor SFTP donde se deben cargar los documentos (por ejemplo, `/incoming/invoices/`). Debe existir y ser escribible.

</details>

#### **SMB**

<details>

<summary>SMB</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6e4B9BWQWgHvcHhduXKb%252Fimage.png%3Falt%3Dmedia%26token%3D09e9534e-9268-4221-bd7b-89b621c80670\&width=768\&dpr=4\&quality=100\&sign=b03835a\&sv=2)

#### **Descripciones de Campo**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportación.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable que lista todos los tipos de documento disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Nombre de Usuario** El nombre de usuario utilizado para conectarse a la carpeta compartida SMB.
* **Contraseña** La contraseña correspondiente para la autenticación SMB.
* **URL del Servidor** La dirección del servidor SMB.
* **Puerto** Número de puerto utilizado para acceder a la carpeta compartida SMB.
* **Carpeta** La ruta de la carpeta dentro de la carpeta compartida SMB donde se deben guardar los documentos (por ejemplo, `/incoming/invoices/`). Debe existir y ser escribible.
*   **Archivo de Mapeo JPL (Opcional)**

    El **archivo JPL** se utiliza para definir una transformación de los datos exportados antes de que se escriban en la carpeta compartida SMB.

    * **Cuándo usar:** Solo cuando los datos del documento exportado necesitan ajustarse para que coincidan con el formato externo o las expectativas del sistema.
    * **Déjelo vacío** si no es necesaria ninguna transformación.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FQ1AtdmTRZr1sGkH6oLwP%252Fimage.png%3Falt%3Dmedia%26token%3D720a4184-3f91-4b70-b3da-b846f3cce030\&width=768\&dpr=4\&quality=100\&sign=dc678c2c\&sv=2)

#### **Descripciones de Campos**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable que lista todos los tipos de documento disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Archivo de Mapeo ION** Selecciona un archivo de mapeo desde el administrador de archivos.
* **Archivo de Mapeo IDM** Selecciona un archivo de mapeo desde el administrador de archivos. [¿Necesitas ayuda para crear uno? Consulta la Guía de Mapeo IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Nube / Alternar On-Prem** Un interruptor para indicar el tipo de implementación de Infor:
  * **Nube**: Selecciona esto si eres cliente de Infor CloudSuite.
  * **On-Prem**: Selecciona esto si Infor es autohospedado.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcYDXwDYH4RSc5vcY4fmr%252Fimage.png%3Falt%3Dmedia%26token%3Da9cfac80-9795-4e8f-a664-e268c9b4856c\&width=768\&dpr=4\&quality=100\&sign=5a4b0bd0\&sv=2)

#### **Descripciones de Campo**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable con todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Archivo de Mapeo ION** Selecciona un archivo de mapeo desde el administrador de archivos.
* **Archivo de Mapeo BOD** Selecciona un archivo de mapeo desde el administrador de archivos. [¿Necesitas ayuda para crear uno? Consulta la Guía de Mapeo BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Nube / Alternar On-Prem** Un interruptor para indicar el tipo de implementación de Infor:
  * **Nube**: Selecciona esto si eres cliente de Infor CloudSuite.
  * **On-Prem**: Selecciona esto si Infor está autohospedado.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FY13EX2xxOKLZzliAAHB0%252Fimage.png%3Falt%3Dmedia%26token%3D94335922-6342-405f-8c6d-29fdf2f31a2e\&width=768\&dpr=4\&quality=100\&sign=c0322806\&sv=2)

#### **Descripciones de Campo**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Tipo de Documento** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Archivo de Mapeo ION** Selecciona un archivo de mapeo desde el administrador de archivos.
* **Archivo de Mapeo IDM** Selecciona un archivo de mapeo desde el administrador de archivos. [¿Necesitas ayuda para crear uno? Consulta la Guía de Mapeo IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Archivo de Mapeo BOD** Selecciona un archivo de mapeo desde el administrador de archivos. [¿Necesitas ayuda para crear uno? Consulta la Guía de Mapeo BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Alternar Nube / Local** Un interruptor para indicar el tipo de implementación de Infor:
  * **Nube**: Selecciona esto si eres cliente de Infor CloudSuite.
  * **Local**: Selecciona esto si Infor está alojado en tu propio servidor.

</details>

### Para clientes de Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4SfGDqhA4KDrPfJ5vcsT%252Fimage.png%3Falt%3Dmedia%26token%3D4833c0dc-af8b-48a1-a977-6cc8ded20277\&width=768\&dpr=4\&quality=100\&sign=6301596\&sv=2)

#### **Descripciones de campos**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de documento** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Archivo de mapeo ION** Seleccione un archivo de mapeo desde el administrador de archivos.
* **Archivo de mapeo IDM** Seleccione un archivo de mapeo desde el administrador de archivos. [¿Necesita ayuda para crear uno? Vea la Guía de Mapeo IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Archivo de mapeo LN** Seleccione un archivo de mapeo desde el administrador de archivos. [¿Necesita ayuda para crear uno? Vea el Ejemplo de Mapeo LN](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAN4T0aQEoogbUA8PUgy9%252Fimage.png%3Falt%3Dmedia%26token%3Da2b91153-858f-4711-abcc-4ed7ad60d49a\&width=768\&dpr=4\&quality=100\&sign=bb6bda83\&sv=2)

#### **Descripciones de Campo**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable que enumera todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Archivo de Mapeo ION** Seleccione un archivo de mapeo del administrador de archivos.
* **Archivo de Mapeo IDM** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Vea la Guía de Mapeo IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Archivo de Mapeo M3** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Vea el Ejemplo de Mapeo M3](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCdoduCkkbnomw3ahZgul%252Fimage.png%3Falt%3Dmedia%26token%3D4e5c7d08-5eaf-4c3e-9918-5cce58d8e3b3\&width=768\&dpr=4\&quality=100\&sign=e984c4e0\&sv=2)

#### **Descripciones de Campo**

* **Título** El nombre de la configuración de exportación. Esto aparecerá en la lista de exportaciones.
* **Sub-Organización** _(opcional)_ Un menú desplegable con todas las sub-organizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la sub-organización elegida.
* **Tipo de Documento** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Archivo de Mapeo ION** Seleccione un archivo de mapeo del administrador de archivos.
* **Archivo de Mapeo IDM** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Vea la Guía de Mapeo IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Archivo de Mapeo M3 toml** Seleccione un archivo de mapeo del administrador de archivos o use la opción seleccionar Toml para usar un toml creado con el administrador de reglas. [¿Necesita ayuda para crear uno? Vea la Guía del Administrador de Reglas](https://docs.docbits.com/administration-and-setup/settings/document-processing/rule-manager)

</details>
