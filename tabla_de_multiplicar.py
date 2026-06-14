c =1
i =0
while True:
    i += 1
    resultado = c * i
    print (f"{c} x {i} = {resultado}")
    
    if i == 9:
       print (end=".")
       c += 1
       i = 0
    if c == 9:
       break

