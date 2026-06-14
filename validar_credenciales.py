contraseña = "okite123"
intento = 0
while intento < 3:
      entrada = input("Ingrese contraseña: ")
      if entrada == contraseña:
         print ("Acesso permitido")
         break
      else :
         print ("Acesso denegado.. intente nuevamente")
         intento  += 1
if intento == 3:
   print ("Acceso bloqueado")
