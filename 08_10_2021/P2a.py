# Leer la actividad
actividades = str(input())

contadorDias = 1
contadorComida = 0

for i in actividades:
    if(i != '!' and i != '?'):
        if(i == 'C'):
            contadorComida += 1
    else:
        if(contadorComida >= 2):
            print('Dia ' + str(contadorDias) + ' come ' + str(contadorComida) + ' veces')
        else:
            if(contadorComida == 1):
                print('Dia ' + str(contadorDias) + ' come ' + str(contadorComida) + ' vez')
            else:
                print('Dia ' + str(contadorDias) + ' no come')
        contadorComida = 0
        contadorDias += 1

