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
