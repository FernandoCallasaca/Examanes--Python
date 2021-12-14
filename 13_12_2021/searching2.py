N = int(input('Ingrese un número entero: '))
while(N < 5):
    N = int(input('Ingrese un número entero: '))

numeros = []
for i in range(5):
    numeros.append(int(input()))

print('Lista:', numeros)

# Pedimos el numero a buscar
n_buscar = int(input('Ingrese número a buscar: '))
while(n_buscar <= 0):
    n_buscar = int(input('Ingrese número a buscar: '))

posicion = -1
# Realizamos la busqueda
primero = 0
ultimo = len(numeros)-1
encontrado = False
while primero<=ultimo and not encontrado:
    puntoMedio = (primero + ultimo)// 2
    if numeros[puntoMedio] == n_buscar:
        encontrado = True
        posicion = puntoMedio
    else:
        if n_buscar < numeros[puntoMedio]:
            ultimo = puntoMedio-1
        else:
            primero = puntoMedio+1

if(encontrado == False):
    lista = [0 for i in range(N)]
    print('No se encontró {0}. -> {1}'.format(n_buscar, lista))
else:
    print('Se encontró ' + str(n_buscar) + ' en la posición ' + str(posicion))
