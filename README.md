# Como hacer una página de internet con python

La finalidad de este proyecto es elaborar mediante una plataforma  denominada Python una página virtual cuyo propósito es crear cualquier contenido , para esta manera facilitar el intercambio de información utilizando IOT(internet de las cosas).

## Para Empezar

Estas instrucciones le proporcionarán una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y pruebas.

### Prerrequisitos

Qué cosas necesita para instalar el software y cómo hacerlo.

    python3
    pip
    flask

### Instalación

Para empezar tenemos que verificar que tenemos python instalado para eso usamos la siguiente línea de codigo.

    python3 -V

La consola debería regresar algo como esto.

    Python 3.5.2

Luego tenemos que asegurarnos de que tenemos pip instalado para esto usamos el comando.

    pip3 -V

La consola debería regrear.

    pip 19.2.3 from /home/usuario/.local/lib/python3.5/site-packages/pip (python 3.5)

Si esto no ocurre toca instalar pip con la siguiente linea de comando.

    sudo apt install python3-pip

Ahora vamos a instalar flask para esto usamos.

    pip3 install flask

Si obtiene un error debe agregar --user despues de install.

Con esto ya deberiamos estar listos para correr nuestro primer codigo de flask.

## Ejecución de Pruebas

Si entramos a el archivo [hello_flask](hello_flask.py) y editamos la dirección ip a la que nos da el ifconfig ya podemos probrar nuestra pagina.

    sudo python3 hello_flask.py

Debería aparecer algo así en la consola

    Serving Flask app "hello_flask" (lazy loading)
    Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    Debug mode: on
    Running on "aqui va tu ip" (Press CTRL+C to quit)
    Restarting with stat
    Debugger is active!
    Debugger PIN: xxx-xxx-xxx

abrimos nuestro explorador de preferencia e ingresamos la ip y debería aparecer el mensaje "Bienvenidos a Digitales 3".

## Autores

-   **Manuel Lopez**
-   **Andres Castillo**
-   **Camilo Duarte**
