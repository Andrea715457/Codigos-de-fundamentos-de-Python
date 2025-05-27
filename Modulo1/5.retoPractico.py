"""
RETO: SIMULAR UN MAQUINA EXPENDEDORAS DE ALIMENTOS

    1. Ingresar el dinero
    2. Consultar el producto
    3. Comprar el producto
    5. Devolver el cambio
    5. Salir

"""

#variables globales
dinero = 0
papas_limon = 3000
cocacola = 4000
chocolatina = 2500
papas_pollo = 3000


print("Bienvenido a la maquina expendedora de comida")
menu_inicio = """
******************************************
*    1. Ingresar el dinero               *
*    2. Consultar el producto            * 
*    3. Comprar el producto              *
*    4. Devolver el cambio               *
*    5. Salir                            *
******************************************
"""
menu_comida = """
******************************************
*    1. Papas de limon                   *
*    2. Cocacola 400pet                  * 
*    3. Chocolatina Jet                  *
*    4. Papas de pollo                   *
******************************************
"""

bandera = True
while (bandera == True):
    print(menu_inicio)
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        dinero = int(input("Ingrese la cantidad de dinero: "))
        print(f"Ah ingresado {dinero} pesos")
    elif (opcion == 2):
        print(menu_comida)
        opcion_comida = int(input("Ingrese la opcion que de comida a consultar: "))
        if (opcion_comida == 1):
            print(f"Las papas de limon tiene un costo de {papas_limon} pesos")
        elif (opcion_comida ==2):
            print(f"Las Cocacola 400pet tiene un costo de {cocacola} pesos")
        elif (opcion_comida ==3):
            print(f"Las Chocolatina Jet  tiene un costo de {chocolatina} pesos")
        elif (opcion_comida ==4):
            print(f"Las Papas de pollo tiene un costo de {papas_pollo} pesos")
        else:
            print(f"Opcion invalida")
    elif (opcion == 3):
        print(menu_comida)
        opcion_producto = int(input("Ingrese el producto que desea comprar: "))
        if (opcion_producto == 1):
            if (dinero >= papas_limon):
                dinero -= papas_limon
                print(f"¡¡Cocacola comprada!!, su cambio es {dinero} pesos")
            else:
                print("Dinero insuficiente")
        if (opcion_producto == 2):
            if (dinero >= cocacola):
                dinero -= cocacola
                print(f"¡¡Cocacola comprada!!, su cambio es {dinero} pesos")
            else:
                print("Dinero insuficiente")
        if (opcion_producto == 3):
            if (dinero >= chocolatina):
                dinero -= chocolatina
                print(f"¡¡Cocacola comprada!!, su cambio es {dinero} pesos")
            else:
                print("Dinero insuficiente")
        if (opcion_producto == 4):
            if (dinero >= papas_pollo):
                dinero -= papas_pollo
                print(f"¡¡Cocacola comprada!!, su cambio es {dinero} pesos")
            else:
                print("Dinero insuficiente")
    elif (opcion == 4):
        print(f"Dinero devuelto, {dinero} pesos")
    elif (opcion == 5):
        print("Gracias por su compra")
        bandera = False
    else:
        print("Opcion invalida intente de nuevo")
