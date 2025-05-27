"""
Documentación y anotaciones de tipo
la documentacion de tipo se utiliza para documentar los tipo de datos
y las anotaciones de tipo se utilizan para indicar que una varible tipos
"""

def suma(numero1:int, numero2:int)->int:
    """
    La funcion suma recibe dos numeros enteros y retorna la suma de los dos numeros
    """
    return numero1+numero2

print(suma(5, 10))
print(suma.__doc__)
help(suma)

#definir una funcion qu eclacule un salario
def calcular_salario(salario_base:float, horas_extras:int, horas_faltantes:int)->float:
    """
    La funcion calcular salario recibe el salario diario y los dias trabajados
    y retorna el salario total
    """
    salario_total = salario_base + (horas_extras * 10) - (horas_faltantes * 5)
    return salario_total

print(calcular_salario(400, 10, 5))
print(calcular_salario.__doc__)

def restar(numero1:int, numero2:int)->int:
    """
    La funcion restar recibe dos numeros enteros y retorna la resta de los dos numeros
    """
    return numero1-numero2

print(restar(1,2))
