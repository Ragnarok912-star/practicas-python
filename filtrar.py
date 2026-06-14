def capturar(palabra, n):
    filtrar = []

    for i in palabra:
        if len(i) > n:
           filtrar.append(i)

    return filtrar, ban


print ("💥PROGRAMA PARA FILTRAR LONGITUD DE PALABRAS💥")
print ("----------------------------------------------\n")

dato = input("Ingrese una palabra: ")
num = int(input("Ingrese un numero: "))

lista = dato.split()


print (f"Las palabras que superan el rango son: {capturar(lista, num)}")
