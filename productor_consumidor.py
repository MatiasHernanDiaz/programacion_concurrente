#Esquema de UN productor y UN consumidor
#ABABABAB
from threading import Thread,Semaphore
import time 
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

"""
################################################
#1. Describir en pseudocódigo una solución al problema de productor-consumidor, para el caso de 2 productores y 1 consumidor, 
#todos sobre un mismo buffer. Escribir todas las aclaraciones que sean necesarias.
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
        j = 0
        while(i < 10 and j < 20):
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
                j += 1
                x.release()

            if(self.name == 'productor2'):
                m.acquire()
                x.acquire()
                region_critica(self.name)
                i += 1
                y.release()
                n.release()
        print(f"fin {self.name}")
        exit()
      
        

#Programa Principal
hilosPPC = [NewHilo('productor'),NewHilo('consumidor'),NewHilo('productor2')] #Creacion de objetos Hilos
buffer = []
for h in hilosPPC:
    h.start() #Ejecutar todos los hilos

for h in hilosPPC:
    h.join()

"""
"""
# 2. En pseudocódigo, usando semáforos, resolver el problema del "rendez-vous" (o encuentro). 
# Consiste en tener dos procesos, tales que uno de ellos mientras ejecuta deberá alcanzar un punto 
# (o marca) dentro de su código, y lo mismo con otro proceso. El primero de ambos que llegue a la marca correspondiente 
# deberá quedarse esperando a que el otro proceso llegue a su marca, y recién en el momento en que el otro haya llegado, 
# ambos podrán continuar ejecutando su código a partir de allí. Escribir o discutir luego una solución análoga del 
# rendez-vous para para 3 o más procesos, cada uno con su código y su marca dada. (Opcionalmente, implementarlo en 
# Python u otro lenguaje, imprimiendo mensajes que informen cuando los procesos lleguen a las marcas dadas. 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            En este caso, dentro del código podrían utilizar algún paquete o clase existente que implemente semáforos...)

# Creación de los semáforos con valor inicial en 0
x = Semaphore(0)
y = Semaphore(0)

def proceso_1():
    print("Proceso 1: ejecutando primera parte")
    time.sleep(1)  # Simula trabajo
    print("Proceso 1: alcanzó el punto de encuentro")
    
    # Notificar al proceso 2 que proceso 1 llegó al punto de encuentro
    x.release()
    
    # Esperar a que proceso 2 llegue al punto de encuentro
    y.acquire()
    
    print("Proceso 1: ambos procesos llegaron, continuando ejecución")

def proceso_2():
    print("Proceso 2: ejecutando primera parte")
    time.sleep(2)  # Simula trabajo
    print("Proceso 2: alcanzó el punto de encuentro")
    
    # Notificar al proceso 1 que proceso 2 llegó al punto de encuentro
    y.release()
    
    # Esperar a que proceso 1 llegue al punto de encuentro
    x.acquire()
    
    print("Proceso 2: ambos procesos llegaron, continuando ejecución")

# Crear hilos para los procesos
t1 = Thread(target=proceso_1)
t2 = Thread(target=proceso_2)

# Iniciar los hilos
t1.start()
t2.start()

# Esperar que los hilos terminen
t1.join()
t2.join()

#Si quisiera tener mas procesos deberia agregar mas semaforos y que condicionen
#de manera cruzada al resto de los procesos para que esperen a todos. una vez que todos
#llegen se despiertan los semaforos y continuan

"""