# importamos para sacar numeros aleatorios en un rango
import random

# creamos la lista
numeros = [random.randint(1,20) for _ in range(10)]
# Imprimimos los números
print('NUMEROS GENERADOS')
num = ''
for i in range(len(numeros)):
    if(i!=(len(numeros)-1)):
        num+=str(numeros[i])+', '
    else:
        num+=str(numeros[i])
print(num)
print()

# pedimos que ingrese el número
num_a_buscar = int(input('Ing Numero a buscar: '))

# buscamos y guardamos posiciones
indices_numero = []
for i in range(len(numeros)):
    if numeros[i] == num_a_buscar:
        indices_numero.append(i+1)

# mostramos resultados
print()
print('RESPUESTA')

if(len(indices_numero) == 0):
    print('posicion : No EXISTE')
else:
    ind = ''
    for i in range(len(indices_numero)):
        if(i!=(len(indices_numero)-1)):
            ind+=str(indices_numero[i])+', '
        else:
            ind+=str(indices_numero[i])
    print('posicion :', ind)
