import os
import time

while True:
      os.system('clear')
      print ("Bienvenido al Menu de opciones para tu red 🌍")
      print ("-------------‐-------------------------------\n")

      print ("1. Ver estado de red")
      print ("2. Escanear estado de la red")
      print ("​3. Cambiar configuración IP")
      print ("​4. Salir\n")


      op = input("Ingresa una opcion valida, presiona 4 para salir: ")
      print ("\n")

      match op:
          case "1":
               print ("Estado de red optimo")
               time.sleep(2.0)
          case "2":
               print ("Escaneando red...")
               time.sleep(2.0)
          case "3":
               print ("ip cambiada con exito")
               time.sleep(2.0)
          case "4":
               print ("Saliendo...")
               time.sleep(2.0)
               os.system('clear')
               print ("Bye, vuelve pronto..")
               break
          case _:
               print ("Introduce un numero valido")
               time.sleep(2.0)
