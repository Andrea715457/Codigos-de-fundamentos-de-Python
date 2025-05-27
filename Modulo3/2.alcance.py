"""
El alcnce o scope ene l contexto en el que se define una variable 
las vaeriables locales con accesibles dentro de la funcion
las variables globales son accebles dentro y fuera de la funcion

el alcance se refiere a la region del programa donde un espacio de nombres es directamente accecibles

local: la variable se busca primero en el espacio de nombres local
enclosing (intermedio): Si no se encuentra, se busca en los espacios los nombres de culaquier
Global: si se encuentra en los dos anteriores, se busca en el espacio de nombres global.
Buitlt-in: finalmente, si no se encuentra en ninguno de los anterioes, se busca en el espacio
"""

variable_global="soy una variable global"

def funcion():
    variable_local="soy una variable local"
    print(variable_global)
    print(variable_local)

funcion()

#scope de una varible global
contador = 0
def incrementar():
    contador = 10
    contador += 1
    return contador

print(incrementar())
print(contador)

contador = 0
def incrementar():
    global contador
    contador += 1
    return contador

print(incrementar())
print(contador)

#Constantes
PI = 3.14
print(PI)

#ambito globla y local (enclosing)
def funcion_exterior():
    variable_exterior="Variable exterior"

    def funcion_interior():
        variable_interior="Variable interior"
        print(variable_exterior)
        print(variable_interior)


    funcion_interior()

funcion_exterior()

lista = [1,2,3,4,5,6,7,8,9,10]
for valor in lista:
    numero = valor * 10
    print(valor)
