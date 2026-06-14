import os
import time

for t in range(1, 11):
    os.system('clear')

    print ("===============================")
    print (f"      ♻️   Tabla del {t}  ♻️      ")
    print ("===============================\n")

    print ("Imprimiendo tabla. ")
    for i in range(1, 11):
        resultado = t * i
        print (f" ↗️  {t} x {i:2d} = {resultado}")

        time.sleep(0.3)


print ("\n=========================================")
print ("Siguiente tabla en camino... ℹ️")


time.sleep(2.0)

print ("✔️ Fin de la animacion")
os.system('clear')

