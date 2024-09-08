#Diaz Matias Hernan 35993466
#Trabajo practico carrera de caballos

import threading
import random
import time

def horse(number: int):
    #Caballo que corre hasta la posición 100 de manera random
    #Cuando llega a 100 corta el bucle cambiando el valor de la variable global
    position = 0
    global order
    global winner
    while (position < 100 and winner is None):
        position += random.randint(1,10)
        with lock:
            if winner is None:
                print(f'Caballo N° {number} posicion {position}')
                if(position > 100):
                    winner = number
                    print('--------META--------------')
                    break

def horseCreation(amount):
    threads = []
    for i in range(amount):
        threads.append(threading.Thread(target=horse, args=(i,)))
    return threads

def startRace(horses):
    for i in horses:
        i.start()

def stopRace(horses):
    for i in horses:
        i.join()

def win(bet):
    global winner
    if(bet == winner):
        print('Su caballo gano la carrera')
    else:
        print('Perdio apuesta')
        print(f'El caballo ganador fue el {winner}')

def main():
    amount = int(input('Ingrese cantidad de caballos a correr '))
    bet = int(input('Numero del caballo al que desea apostar '))
    horses = horseCreation(amount)
    startRace(horses)
    stopRace(horses)
    win(bet)
    

#Variable global que miran todos los caballos para saber si siguen corriendo o no
#cambia cuando un caballo llegue a la meta

lock = threading.Lock()
winner = None

main()

#Algunos pocos caballos seguiran corriendo porque cuando cambie la bandera
#ya se encontraran dentro del bucle
#para esto guardo los posibles "ganadores" en un array y el primero que se guardo
#efectivamente fue el primero, ese es el ganador