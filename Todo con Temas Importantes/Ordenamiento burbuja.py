# ordenamiento burbuja
def ordenamiento_burbuja(valores, j):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(valores) - 1):
            if valores[i][j] > valores[i + 1][j]:
                valores[i], valores[i + 1] = valores[i + 1], valores[i]
                intercambio = True

datos = [
        ['Sol', 0.000016, -26.73],
        ['Sirio', 8.6, -1.47],
        ['Canopus', 310, -0.72],
        ['Rigil Kentaurus', 4.4, -0.27],
        ['Arturo', 37, -0.04],
        ['Vega', 25, 0.03],
        ['Rigel', 770, 0.12],
        ['Procyon', 11, 0.34],
        ['Achernar', 140, 0.5],
    ]

a_ordenar = input('Ordenar por la columna: ')
j = -1

for i in datos:
    if(a_ordenar == 'nombre'):
        j = 0
    elif(a_ordenar == 'distancia'):
        j = 1
    elif(a_ordenar == 'magnitud'):
        j = 2

# ordenamos
ordenamiento_burbuja(datos, j)

# Mostramos los resultados
print('Nombre, distancia, magnitud')
for i in datos:
    print(str(i)[1:-1])
