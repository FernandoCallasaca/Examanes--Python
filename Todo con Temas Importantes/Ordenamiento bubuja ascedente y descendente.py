# importamos para sacar numeros aleatorios en un rango
import random

# creamos la lista
numeros = [random.randint(1,100) for _ in range(10)]
# Imprimimos los números
print('NUMEROS GENERADOS')
num = ''
for i in range(len(numeros)):
    if(i!=(len(numeros)-1)):
        num+=str(numeros[i])+', '
    else:
        num+=str(numeros[i])
print(num)

# separamos la lista en menores y mayores de 50
menores_50 = []
mayores_iguales_50 = []

for i in numeros:
    if(i < 50):
        menores_50.append(i)
    else:
        mayores_iguales_50.append(i)

# ahora aplicamos un algoritmo de ordenamiento
# creamos burbuja
def ordenamiento_burbuja_ascendente(numeros):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(numeros) - 1):
            if numeros[i] > numeros[i + 1]:
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                intercambio = True

def ordenamiento_burbuja_descendente(numeros):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(numeros) - 1):
            if numeros[i] < numeros[i + 1]:
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                intercambio = True
                
# ahora aplicamos el metodo para ordenar
ordenamiento_burbuja_descendente(menores_50)
men = ''
for i in range(len(menores_50)):
    if(i!=(len(menores_50)-1)):
        men+=str(menores_50[i])+', '
    else:
        men+=str(menores_50[i])

ordenamiento_burbuja_ascendente(mayores_iguales_50)
may = ''
for i in range(len(mayores_iguales_50)):
    if(i!=(len(mayores_iguales_50)-1)):
        may+=str(mayores_iguales_50[i])+', '
    else:
        may+=str(mayores_iguales_50[i])

# ahora imprimimos los resultados
print()
print('Respuesta')
print('1-50 :', men)
print('50-100 :', may)
