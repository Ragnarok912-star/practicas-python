import os
import time

def medir(ips):
    equi_online = 0
    
    for ip in ips:
        print(f"Haciendo ping a la ip {ip}...")
        time.sleep(1.5)
        
        # Al cumplir la condición, lo de abajo lleva 4 espacios extra a la derecha
        if int(ip.split('.')[-1]) % 2 == 0:
            equi_online += 1 

    # Fuera del bucle for para que se ejecute solo al final de revisar todas las IPs
    print("Equipos en linea: ", equi_online)

ips = ["192.168.1.80", "192.168.1.5", "192.168.1.2"]
medir(ips)
