
nom = ["Ana","Pedro","Juan","Carlos"]
ed = [57,89,12,18]
for n,e in zip(nom,ed):
    print(f"Nombre: {n} tiene {e} Años")
    


capitales = {"España":"Madrid", "Colombia": "Bogot D.C"}

for capital in capitales.values():
    print(capital)

for pais, capi in capitales.items():
    print (f"Pais: {pais} capital:, {capi}")


for long in range(6):
    print(long)

#tablas de multiplicar 

num = 1 
num2 = 0


while True:
    num2 += 1
    r = num * num2 
    print (f"{num} x {num2} = {r}")

    if num2 == 10:
       num += 1
       num2 = 0
       print ("\n")
    if num == 30:
       break
       
