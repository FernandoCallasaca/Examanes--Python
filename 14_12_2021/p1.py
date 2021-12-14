nota = 0
suma = 0
cantidad = 0
menor_11 = 0
mayor_igual_11 = 0

i = 1
while nota != -1:
    nota = int(input('Nota ' + str(i) + ': '))
    if(nota != -1):
        cantidad += 1
        i += 1
        suma += nota
        if(nota < 11):
            menor_11 += 1
        else:
            mayor_igual_11 += 1

# creamos el diccionario
my_dict = {'Cantidad Notas': cantidad, 'Mayores a 11': mayor_igual_11,
           'Menores a 11': menor_11, 'Promedio': suma/cantidad}

# mostramos el resultado
print('Salida:{0}'.format(my_dict))
