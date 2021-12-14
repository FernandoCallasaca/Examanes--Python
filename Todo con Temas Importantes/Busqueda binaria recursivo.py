numeros = [10,9,8,7,6,5,4,3,2,1]

def buscar_recursivo(numeros, n):
    if(len(numeros) == 0):
        return False
    else:
        puntoMedio = len(numeros) // 2
        if numeros[puntoMedio] == n:
            return True
        else:
            if n > numeros[puntoMedio]:
                return buscar_recursivo(numeros[:puntoMedio], n)
            else:
                return buscar_recursivo(numeros[puntoMedio:], n)

# Ejemplos
print(buscar_recursivo(numeros, 18))
print()
print(buscar_recursivo(numeros, 10))
