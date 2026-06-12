#bucle for#

#recorrer listas 

#frutas = ["manzana","pera","uva"]
#for c  in frutas:
#    print(c)

#imprimir un rango
#for cont in range(10):
#    print(cont)

#rango con inicio fin, y paso 
#for cont in range(0,10,1):
#   print(cont)


#frutas = ["manzana","pera","uva"]

#for f,index  in enumerate(frutas):
#   print(index,f)

#total = 0
#for num in range(1,10):
#   total += num
#   print(total)


for num in range(2, 111):
    if num == 1:
        break      # sale del bucle cuando num es 7
    if num % 2 == 0:
        continue   # salta los números pares
    print(num)     # imprime solo números impares hasta 6

