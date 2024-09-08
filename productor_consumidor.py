#Esquema de UN productor y UN consumidor
#ABABABAB
from threading import Thread,Semaphore
"""

#Crear variable semáforo
p = Semaphore(1) 
q = Semaphore(0)

#Definicion de Funciones
def region_critica(name):
    #El productor llena el buffer y el consumidor lo limpia, si el productor llena el bufer
    #y ya estaba lleno avisa que accede indevidamente ya que no espero al consumidor
    #Analogamente el consumidor no puede vaciar el buffer si ya esta vacio notificando
    #caso contrario.
    global buffer
    if(name == 'productor'):
        if(len(buffer) != 0):
            print('Productor accedio indevidamente a zona critica')  
        buffer.append('prod')
        print (f'Productor {buffer}')
    if(name == 'consumidor'):
        if(len(buffer) == 0):
            print('Consumidor accedio indevidamente a zona critica')  
        buffer.remove('prod')
        print (f'Consumidor {buffer}')

#Definicion de Clase Hilo
class Hilo(Thread):
    def __init__(self,name): #Constructor de la clase
        Thread.__init__(self)
        self.name=name

    def run(self): #Metodo que se ejecutara con la llamada start
        #Si es productor entra y si el semaforo lo permite accede a region critica
        # si no esperara al hilo que pueda acceder como consumidor y cuando salga
        #de la zona critica despetara el semaforo del productor sumando 1 al 
        #contador interno del mismo
        i = 0
        while(i < 10):
            if(self.name == 'productor'):
                p.acquire()
                region_critica(self.name)
                q.release()
                i += 1
            if(self.name == 'consumidor'):
                q.acquire()
                region_critica(self.name)
                p.release()
                i += 1

#Programa Principal
hilos = [Hilo('productor'),Hilo('consumidor')] #Creacion de objetos Hilos
buffer = []
for h in hilos:
    h.start() #Ejecutar todos los hilos

for h in hilos:
    h.join()
#################################################
print()
print()

"""
################################################
#PRODUCTOR CONSUMIDOR PRODUCTOR
#ABCBABCB

#Crear variable semáforo
x = Semaphore(1) 
y = Semaphore(0)
n = Semaphore(1) 
m = Semaphore(0)


#Definicion de Funciones
def region_critica(name):
    #El productor llena el buffer y el consumidor lo limpia, si el productor llena el bufer
    #y ya estaba lleno avisa que accede indevidamente ya que no espero al consumidor
    #Analogamente el consumidor no puede vaciar el buffer si ya esta vacio notificando
    #caso contrario.
    global buffer
    if(name == 'productor'  or name == 'productor2'):
        if(len(buffer) != 0):
            print('Productor accedio indevidamente a zona critica')  
        buffer.append('prod')
        print (f'Productor {name} {buffer}')
    if(name == 'consumidor'):
        if(len(buffer) == 0):
            print('Consumidor accedio indevidamente a zona critica')  
        buffer.remove('prod')
        print (f'Consumidor {buffer}')

#Definicion de Clase Hilo
class NewHilo(Thread):
    def __init__(self,name): #Constructor de la clase
        Thread.__init__(self)
        self.name=name

    def run(self): #Metodo que se ejecutara con la llamada start
        #Si es productor entra y si el semaforo lo permite accede a region critica
        # si no esperara al hilo que pueda acceder como consumidor y cuando salga
        #de la zona critica despetara el semaforo del productor sumando 1 al 
        #contador interno del mismo
        i = 0
        while(i < 10):
            if(self.name == 'productor'):
                n.acquire()
                x.acquire()
                region_critica(self.name)
                i += 1
                y.release()
                m.release()
            
            if(self.name == 'consumidor'):
                y.acquire()
                region_critica(self.name)
                i += 1
                x.release()

            if(self.name == 'productor2'):
                m.acquire()
                x.acquire()
                region_critica(self.name)
                i += 1
                y.release()
                n.release()
        print(f"fin {self.name}")
      
        

#Programa Principal
hilosPPC = [NewHilo('productor'),NewHilo('consumidor'),NewHilo('productor2')] #Creacion de objetos Hilos
buffer = []
for h in hilosPPC:
    h.start() #Ejecutar todos los hilos

for h in hilosPPC:
    h.join()

