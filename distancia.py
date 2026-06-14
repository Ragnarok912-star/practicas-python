import os
import time

def medir (dist):
    if dist > 1000:
       print ("Para este tipo de distancias, es recomendado usar fibra monomodo")
       time.sleep(2.0)
       os.system('clear')
       print ("Fin del pregrama")
       return True

    else :
       print ("Para este tipo de  distancias menor a 1000 kilometros, es recomendado utilizar fibra multimodo o cable de red cat.7E para exteriores")
       time.sleep(2.0)
       os.system('clear')
       print ("Fin del programa")
       return False


entrada = int(input("Introduce la distancia, para escoger tipo de tendido: "))
medir(entrada)
