# creamos la funcion recursiva
def sum_pares(numeros, suma = 0):
    if(len(numeros) == 0):
        return suma
    else:
        if(numeros[0] % 2 == 0):
            suma += numeros[0]
            return sum_pares(numeros[1:], suma)
        else:
            return sum_pares(numeros[1:], suma)


# recibimos los numeros separados por coma como cadena
num_cadena = input('Num: ')

# ahora convertimos esa cadena a un arreglo
num = [int(i) for i in num_cadena.split(',')]


# ahora llamamos a la funcion recursiva
suma_pares = sum_pares(num)

# mostramos el resultado
print('Respuesta:', suma_pares)
