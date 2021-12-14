def puntaje(lista, ganado = 3, empatado = 1):
    puntos = 0
    for i in lista:
        if(i == 'G'):
            puntos += ganado
        elif(i == 'E'):
            puntos += empatado
    return puntos

lista = ['G', 'G', 'P', 'P', 'E', 'G']
print(puntaje(lista, 5, 2))
print()
print(puntaje(lista))
        
