import json
"""
Crear un programa que permita registrar clientes con la siguiente informacion:
Cedula, nombre, apellido, edad, email, teelfono, direccion
Guardarl la informacion en un diccionario
el program debe permitir:
    1. Registrar clientes
    2. Elimiar un cliente
    3. Buscar un cliente
    4. Listar todos los clientes
    5. Listar clientes preferenciales
    6. Salir

reto: Realizar el programa dentro de un archivo json
"""
import json

clientes = "G:\Python\Modulo2\datosreto.json"
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

while bandera == True:
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
        cliente = {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "email": email,
            "telefono": telefono,
            "direccion": direccion,
            "preferencial": preferencial
        }
        with open(clientes, "w") as archivo:
            json.dump(cliente, archivo, indent=4)
            print("Cliente registrado")
    elif opcion == 2:
        print("--- Eliminar un cliente ---")
        cedula = input("Ingrese la cedula del cliente a eliminar: ")
        with open(clientes, "r") as archivo:
            clientes = json.load(archivo)

        # 2. Buscar y eliminar el cliente
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["cedula"] == cedula:
                clientes.remove(cliente)
                cliente_encontrado = True
                break

        # 3. Guardar los cambios si se eliminó
        if cliente_encontrado:
            with open(clientes, "w") as archivo:
                json.dump(clientes, archivo, indent=4)
            print("Cliente eliminado.")
        else:
            print("Cliente no encontrado.")
    elif opcion == 3:
        print("--- Buscar un cliente ---")
        cedula = input("Ingrese la cedula del cliente a buscar: ")
        if cedula in clientes:
            print(f"** Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Email: {email}, Telefono: {telefono}, Direccion: {direccion}, Preferencial: {preferencial}")
        else:
            print("Cliente no encontrado")
    elif opcion == 4:
        print("--- Listado de clientes ---")
        for cedula, cliente in clientes.items():
            print(f"** Cedula: {cedula}, Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Email: {email}, Telefono: {telefono}, Direccion: {direccion}, Preferencial: {preferencial}")
            print("--- Fin de la lista ---")
    elif opcion == 5:
        print("--- Listado de clientes preferenciales ---")
        for cedula, cliente in clientes.items():
            if cliente["preferencial"] == "s":
                print(f"** Cedula: {cedula}, Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Email: {email}, Telefono: {telefono}, Direccion: {direccion}, Preferencial: {preferencial}")
                print("--- Fin de la lista ---")
    elif opcion == 6:
        print("Gracias por usar el programa")
        bandera = False