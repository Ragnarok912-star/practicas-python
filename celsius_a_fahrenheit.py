import os
import time


print ("Convertidor de celcius a fahrenheit")
print ("-----------------------------------\n")


capturar = int(input("Introduce los grados celcius: "))
os.system('clear')

def convertir(grados_celcius):
    f =  grados_celcius * 1.8 + 32
    return f

print ("Haciendo conversion..")
time.sleep(2.0)
os.system('clear')


print ("Imprimiendo grados...")
time.sleep(2.0)
os.system('clear')

print (f"Grados Fahrenheit: {convertir(capturar)}° Fahrenheit")
