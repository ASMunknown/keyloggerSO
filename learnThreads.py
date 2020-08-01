import threading

# Clase hilo
class HiloContador1(threading.Thread):

    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)

    def run (self):  # run() se utiliza para definir el comportamiento del hilo
          print(str(self.__x))

class HiloSaludador(threading.Thread):

    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)

    def run (self):  # run() se utiliza para definir el comportamiento del hilo
          print(str(self.__x))



HiloContador1(1).start

HiloSaludador(1).start


