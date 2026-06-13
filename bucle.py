
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
