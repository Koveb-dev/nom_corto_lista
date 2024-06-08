import csv


def mensaje_agregar_nombres():
    while True:
        mensaje = str(input(
            '¿Deseas agregar otro nombre? ("si": agrega otro nombre)("no": no agrega): '))
        if mensaje.lower() in ("si", "no"):
            return mensaje
        else:
            print('ERROR! debe ingresar una opción valida, opciones valida("si" o "no")!')


def encontrar_num_pequeno(p_lista_nom):
    if len(p_lista_nom) >= 1:
        nombre_peq = p_lista_nom[0]

    for nombre in p_lista_nom:
        if len(nombre) < len(nombre_peq):
            nombre_peq = nombre
    p_lista_nom.remove(nombre_peq)


def crear_csv_nombres(p_lista_nombres):
    with open('ej3_n_pequeno.csv', "w", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(p_lista_nombres)
