# recibimos la lista
lista = [float(x) for x in input('Ingrese la lista: ')[1:-1].split(',')]

def suma_numeros(numeros, suma = 0, indice = 0):
    if indice >= len(numeros):
        return suma
    else:
        suma += numeros[indice]
        indice += 1
        return suma_numeros(numeros, suma, indice)

#ejemplo: [3, 5, 0, 1] = 9
# [1.2 , 1.0 , 1.0 , 1.0 , 1.0]

suma = suma_numeros(lista)
print('La suma total es', suma)
