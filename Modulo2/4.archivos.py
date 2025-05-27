"""
Archivos en python: .xls, .csv, .json
"""
import json
import os

clientes_file = r"G:\Python\Modulo2\datosreto.json"
bandera = True

menu = """
*******************************************
*    1: Registrar clientes                *
*    2: Eliminar un cliente               *
*    3: Buscar un cliente                 *
*    4: Listar todos los clientes         *
*    5: Listar clientes preferenciales    *
*    6: Salir                             *
*******************************************
"""

# Función para cargar clientes
def cargar_clientes():
    if os.path.exists(clientes_file):
        with open(clientes_file, "r") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []
    return []

# Función para guardar clientes
def guardar_clientes(lista_clientes):
    with open(clientes_file, "w") as archivo:
        json.dump(lista_clientes, archivo, indent=4)

# Ciclo principal
while bandera:
    print(menu)
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("--- Ingrese los datos del cliente ---")
        cedula = input("Ingrese la cedula: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = int(input("Ingrese la edad: "))
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el telefono: ")
        direccion = input("Ingrese la direccion: ")
        preferencial = input("Es cliente preferencial? (s/n): ").lower()

        nuevo_cliente = {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "email": email,
            "telefono": telefono,
            "direccion": direccion,
            "preferencial": preferencial
        }

        clientes = cargar_clientes()
        clientes.append(nuevo_cliente)
        guardar_clientes(clientes)
        print("Cliente registrado.")

    elif opcion == 2:
        print("--- Eliminar un cliente ---")
        cedula = input("Ingrese la cedula del cliente a eliminar: ")
        clientes = cargar_clientes()
        cliente_encontrado = False

        for cliente in clientes:
            if cliente["cedula"] == cedula:
                clientes.remove(cliente)
                cliente_encontrado = True
                break

        if cliente_encontrado:
            guardar_clientes(clientes)
            print("Cliente eliminado.")
        else:
            print("Cliente no encontrado.")

    elif opcion == 3:
        print("--- Buscar un cliente ---")
        cedula = input("Ingrese la cedula del cliente a buscar: ")
        clientes = cargar_clientes()
        encontrado = False
        for cliente in clientes:
            if cliente["cedula"] == cedula:
                print(cliente)
                encontrado = True
                break
        if not encontrado:
            print("Cliente no encontrado.")

    elif opcion == 4:
        print("--- Listado de todos los clientes ---")
        clientes = cargar_clientes()
        for cliente in clientes:
            print(cliente)
        print("--- Fin de la lista ---")

    elif opcion == 5:
        print("--- Listado de clientes preferenciales ---")
        clientes = cargar_clientes()
        for cliente in clientes:
            if cliente["preferencial"] == "s":
                print(cliente)
        print("--- Fin de la lista ---")

    elif opcion == 6:
        print("Gracias por usar el programa.")
        bandera = False
