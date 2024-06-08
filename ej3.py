import time
import os
from funciones import *
nombres = []

while True:
    while True:
        nombre = str(input('Ingrese nombre: '))
        if len(nombre.strip()) >= 3:
            nombres.append(nombre)
            break
        else:
            print('ERROR! debe ingresar un nombre con al menos 3 letras!')
        time.sleep(1)
        os.system('cls')

    mensaje = mensaje_agregar_nombres()

    if mensaje.lower() == "si":
        print('cargando')
        time.sleep(1)
        os.system('cls')
    else:
        break

encontrar_num_pequeno(nombres)

print(nombres)

crear_csv_nombres(nombres)
