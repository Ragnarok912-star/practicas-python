import os
import time


def medicion(colorfibra, señal):
    equipos_online = 0
    for color, potencia in zip(colorfibra, señal):
        if float(potencia) >= -25.1:
            print(f"Analizando señal de hilo {color} es de {potencia} dBm, la   señal es buena")
            equipos_online += 1
            time.sleep(1)
            os.system("clear")

        else :
            print(f"Analizando señal de hilo {color} es de {potencia} dBm, la   señal es mala")
            time.sleep(1)
            os.system("clear")
    print("Imprimiendo total de equipos online...")
    time.sleep(2)
    os.system("clear")
    print (f"Total de equipos online: {equipos_online}")

colorfibra = ["rojo", "verde", "azul", "amarillo"]
señal = [-20.5, -30.2, -25.0, -26.5]
medicion(colorfibra, señal)