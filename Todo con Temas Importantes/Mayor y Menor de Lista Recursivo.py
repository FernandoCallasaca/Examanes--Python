def mayor(numeros):
    if(len(numeros) == 1):
        return numeros[0]
    else:
        if(numeros[0] > numeros[1]):
            numeros[1] = numeros[0]
            return mayor(numeros[1:])
        else:
            return mayor(numeros[1:])

def menor(numeros):
    if(len(numeros) == 1):
        return numeros[0]
    else:
        if(numeros[0] < numeros[1]):
            numeros[1] = numeros[0]
            return menor(numeros[1:])
        else:
            return menor(numeros[1:])

n = int(input('Ingrese el número de elementos de la lista: '))

numeros = [int(input('Ingrese elemento ' + str(i + 1) + ': ')) for i in range(n)]

print('El menor elemento de la lista es', menor(numeros))
print('El mayor elemento de la lista es', mayor(numeros))
