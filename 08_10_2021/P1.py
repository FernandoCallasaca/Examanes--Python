# Número de hoyos
N = int(input())
# Iteramos los Hoyos
totalJ1 = 0
totalJ2 = 0

resultado = []

for i in range(N):
    # Leemos los inputs
    # el primer input es la distancia
    distancia = int(input())
    resultado.append('Hoyo ' + str(i+1) + ' - Distancia inicial: ' + str(distancia))
    #print('Hoyo ' + str(i+1) + ' - Distancia inicial: ' + str(distancia))
    # empezamos el ciclo para esa jugada
    # sabiendo que el que juega primero es el jugador
    dj1 = distancia
    dj2 = distancia
    i = 0 # par j1, impar j2
    terminoJ1 = False
    terminoJ2 = False
    # numero de jugadas por hoyo
    puntajeJ1 = 0
    puntajeJ2 = 0
    while(dj1 != 0 or dj2 != 0):
        tiro = int(input())
        if((i%2==0 and terminoJ1==False) or terminoJ2==True):
            resultado.append('J1: ' + str(tiro))
            #print('J1: ' + str(tiro))
            dj1 -= tiro
            dj1 = abs(dj1)
            if(dj1 == 0):
                terminoJ1 = True
            puntajeJ1 += 1
        elif((i%2 != 0 and terminoJ2==False) or terminoJ1==True):
            resultado.append('J2: ' + str(tiro))
            #print('J2: ' + str(tiro))
            dj2 -= tiro
            dj2 = abs(dj2)
            if(dj2 == 0):
                terminoJ2 = True
            puntajeJ2 += 1
        i += 1
    totalJ1 += puntajeJ1
    totalJ2 += puntajeJ2
    resultado.append('Puntaje actual J1: ' + str(totalJ1))
    resultado.append('Puntaje actual J2: ' + str(totalJ2))
    #print('Puntaje actual J1: ' + str(totalJ1))
    #print('Puntaje actual J2: ' + str(totalJ2))
if(totalJ1 > totalJ2):
    resultado.append('Gana J2')
    #print('Gana J2')
elif(totalJ2 > totalJ1):
    resultado.append('Gana J1')
    #print('Gana J1')
else:
    resultado.append('Empate!')
    #print('Empate!')

for i in resultado:
    print(i)

            
