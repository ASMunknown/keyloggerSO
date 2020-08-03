# KeyloggerSO

Programa que captura todo el contenido ingresado por teclado y lo envía a un servidor web para su alojamiento.

# Método de uso


Deberá iniciarse el programa desde el intérprete de Python

```bash
$ python main.py
```

(Opcionalmente) Deberá levantarse un servidor para que almacene los datos recibidos, para pruebas elaboramos uno, así mismo se ejecuta con Python. 

```bash
$ python api/server.py
```

# Funcionamiento
#### Keylogger

1.- El proceso principal (mainProcess) crea tres hilos y los ejecuta. <br>
2.- El primer hilo creado es el Keylogger, el cual ejecuta el proceso key_recorder en un bucle infinito. Dicho proceso abre (o crea) un archivo con la fecha y hora actual y registra las pulsaciones que realice el usuario en el teclado. Por cada minuto se creará un archivo diferente.<br>
3.- El segundo hilo será para hacer el upload a un servidor web cada 60 segundos. Para ello usamos un petición del tipo GET para enviar la información.<br>
4.- El tercer hilo realiza las consultas de las características del ordenador de la víctima y lo envía al servidor. Este se ejecuta una vez y termina.<br>


#### Servidor web

El servidor web elaborado está a la escucha de peticiones tipo GET en las siguientes direcciones. <br>
1.- index.html: El cual presentará las frecuencias de las teclas presionadas por la víctima, además de las características del ordenador del mismo. <br>
2.- upload/data: Este recibirá información (data) y lo almacenará en sus archivos. El archivo que se espera almacenar será uno indicando todas las teclas pulsadas para luego hallar la frecuencia de pulsaciones de cada tecla. <br>
3.- uploadSysInfo/data: Este recibirá la información del sistema y la almacenará para luego ser mostrada en la pantalla principal (index.html). <br>


# Librerías que se necesitan instalar
1.- pynput <br>
2.- Flask (Para el servidor)<br>


# Disclaimer
Este software ha sido elaborado únicamente con fines educativos.