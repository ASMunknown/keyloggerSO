# KeyloggerSO

Programa que captura todo el contenido ingresado por teclado y lo envía a un servidor web para su alojamiento.

# Método de uso
======
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
1.- El proceso principal (mainProcess) crea dos hilos y los ejecuta.
2.- El primer hilo creado es el Keylogger, el cual ejecuta el proceso key_recorder en un bucle infinito. Dicho proceso abre (o crea) un archivo con la fecha y hora actual y registra las pulsaciones que realice el usuario en el teclado. Por cada minuto se creará un archivo diferente.
3.- El segundo hilo será para hacer el upload a un servidor web, para ello usamos un petición del tipo GET para enviar la información.


#### Servidor web
1.- En desarrollo


# Librerías que se necesitan instalar
1.- pynput <br>
2.- Flask (Para el servidor)<br>


# Disclaimer
Software elaborado unicamente con fines educativos.