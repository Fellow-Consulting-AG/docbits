# Watchdog

**Instalación y Configuración**

Después de descargar el archivo WatchDog.exe, busca Símbolo del sistema → Ejecutar como administrador en tu dispositivo Windows.

![](https://lh7-us.googleusercontent.com/a2kmyk7eD7HqZfPiLWmvSGFnpzg9oHejHe5TpE6gFwErFyJYYBB5BZjqopwr-cEqmlMvaW8-PgARZUGI9KMKHSkz-lU\_C\_w6aHrVA4Wqhwo8WBSqnBfVvCpSckqLu4PwUriGs1MxbKHBBkuQ2pPaVRM)

Una vez abierto, llama al archivo escribiendo la ruta donde se encuentra el archivo WatchDog.exe en tu dispositivo como se muestra a continuación

![](https://lh7-us.googleusercontent.com/W\_jDgPVTtpEW96jR0w\_ibnZGY2CVwF2nAN0nEjMW3liw10bgPGlADiVR\_lWyEAlfGYRD--gSQMdEqboRlMW5TAEP6Ao3GOW-hP3tQimA58K9Uh-WNZf7i06YYNqk5\_EgKERYkjMzPx1Xd56qH2Pw8wA)

Escribe install después de la ruta del archivo y presiona ENTER en tu teclado

![](https://lh7-us.googleusercontent.com/vZQxNIh\_wY2SFTznxNTboFOSePmEMqXQMWbhsSoO45B\_mIh\_6C-yjfJ4SPleBIIV4p943XBN1E-3HJBgFXRRABVfDX9Ey-dnb9c5KYaNleOmE5x1ocK32zLQ4luc71rmcbv7V\_dQ8pEtH\_WoWZkN0fg)

Deberías recibir el siguiente mensaje de error ya que iniciará la aplicación en modo UI y aún no hay configuración presente.

![](https://lh7-us.googleusercontent.com/HmudHszeaiAj3xIlb1Oz1IXPh3Kz1JovUvPjkr9UI7EwSGbGWRK7xVhUNwc9LGlt3t1RRVR0l7DFLfG\_Ob2b8Yxd4DffLb27Hv3z22tzf9LqDVTn577CFV-4Bzs2P\_vTsGDJvtNzf8XW0wPiaWLDj2o)

La aplicación se abrirá automáticamente después de la instalación. En la parte superior, navega a Einstellungen (Configuración) y aquí verás 2 secciones separadas.

**Configuración de carpetas (Ordner Einstellungen)**

![](https://lh7-us.googleusercontent.com/8uSWIY8EJKPrKj9Zk5buY\_ByE9fu2oE7mJ-shG1VB2n7QWyVLAfDfUFdj-Jv3hBq2ncf2Ls1Wh3Lm7Kf-TFqet7yFso2S6srnZev-yzVdKjUxtCMTt2IUtWvUwUU0LMGktA8ioBfIkkZGqG4f53yYHM)

Aquí configurarás las rutas de archivo donde los documentos serán leídos y procesados. La ruta de lectura será para los documentos que deseas que WatchDog extraiga y procese, mientras que la ruta procesada se usará para indicar qué documentos del folder de lectura fueron extraídos y procesados.

**Configuración general (Allgemeine Einstellungen)**

![](https://lh7-us.googleusercontent.com/mTUxSXPBZi\_TTtVEQbGQXyXNonkIuganpTjqaamkB7C7zZ7Qaodvf9Sl8nXjnp6ZpYNf8XOwvuk-MYYEyGkFcKB-SqC9lklBXehC-3jMI7G12tXqfa6ROWywPBFE4fy-p-DcuLo3QdZXy-1rjSzlu9s)

Aquí configurarás tu aplicación DocBits con WatchDog. Deberás ingresar tu entorno de DocBits, clave API y el tipo de documento (como se indica arriba). Para agregar más de un tipo de documento, separa los nombres de los tipos de documento con una coma (FACTURA,NOTA-DE-ENTREGA,ORDEN-DE-COMPRA, etc.)

Si se ingresa una configuración inválida para alguno de los campos, recibirás un mensaje de error como el siguiente.

![](https://lh7-us.googleusercontent.com/BIOMuVCPUojfwPVr-cJukzvoBdWdtxzj5XCXocWlZwbaXwkTpb4u5Gk84vKu-\_Z5UxvZ2cq0asHs4aFRLklBrUOKA19d2R4nqsxyZjd3iJlh3y97f07OfzEyv6jl7JpnorANzdPIgyZfqwmCEYZOlek)

Una vez completado, regresa al área de Símbolo del sistema y vuelve a ejecutar el archivo WatchDog.exe y esta vez se instalará correctamente debido a que las configuraciones ahora están presentes.

![](https://lh7-us.googleusercontent.com/GqtwbyvQjjNb1u9DY\_Eww2woOdK1nYMm0oRMFxEGWSP9oSYN51eu1kkWiDzenz1rHGLvYG-ocwosOK2bTM6ruXTI5co05kjV2HPGI-8TgEIBTVCPpTrvs37SKMk9eBWY0KEj9vCCyPeqXYgCVD0DDXw)

Para iniciar la aplicación en modo UI, ejecuta el siguiente comando

![](https://lh7-us.googleusercontent.com/LELZuaiuL8ukiKPE-pbezsOZAICffXxAomx6gSe0vOvYaIdkr8Sr7X2znc\_Lb3G76bh11X6kGPizWzoA05L-nBwUcJV8NNLUgQuGOf0TyICmhyL4syhnZFGu82JP0a3dORlQXz9MnTA\_f-8b6oy8v6g)

Si solo deseas iniciar la aplicación, ejecuta este comando en su lugar.

![](https://lh7-us.googleusercontent.com/yHiO-x4CPGIjC9hRx6o-Wr5lAYiwjGi0vNBp3faB91OYIqm8TTZcz3SVDgjSmq\_7TN11aVCsNHoHV5sR0FHsA5DJqxJ74z3lAmXoaDkkMutl7yXj4fCoabX-9SwfsWJwOaooiVZhCvOKFXvJOCBicEA)

**Inicio Automático**

Para configurar la aplicación WatchDog de manera que se inicie automáticamente al encender tu sistema.

Simplemente abre "Servicios" en la configuración de tu máquina Windows.

![](https://lh7-us.googleusercontent.com/IEqq96LGZ9lBz2E0ApDrTz5huYutY7G1DecXLwhkdIF0pS235RN9HIqcehuJvXv5tyLdOnobhM\_VNeMFA7tnMhwvWCnFRU5G14cHWN1swA4ZYF1rjvKzZtFMaCK2MDsPebvIz3MejDwjiYEiQ-\_BQyg)

Busca WatchDog en los servicios locales y abre el servicio (doble clic en la entrada)

![](https://lh7-us.googleusercontent.com/qOtVCqR-zytJw2zifnjHmW\_s5Hl6ijJt72d3PRI\_euZU0H3wA-QD69mSFOnyDEnCVJXblEeA\_Zbh5iQsyPa8gPJ85TY8wz-Ir0aMd2SWoKizKw1G4yi9jOmtxZG7-9EZbOvborv45OASD6zSa6lLbAk)

En el menú anterior tendrás las siguientes opciones para el inicio automático:

* Selecciona Automático, el servicio se iniciará al arrancar
* Inicio automático (Inicio diferido), esto esperará 2 minutos después del arranque para iniciar el servicio
