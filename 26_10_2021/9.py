# modulo para calificar equipos
def calificar(lista):
    calificacion = 0
    for i in lista:
        if(i.isnumeric()):
            calificacion += int(i)
    return calificacion


# pedimos el numero de equipos
N = int(input('Grupos: '))

# mayor calificacion
mayor = 0

for i in range(N):
    grupo = list(input('Resultado Grupo '+ str(i) + ' : '))
    calificacion = calificar(grupo)
    if mayor < calificacion:
        mayor = calificacion
print('Calificacion ganador =', mayor)
