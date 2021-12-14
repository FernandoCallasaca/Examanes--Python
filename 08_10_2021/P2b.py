# Implementamos la función
# Esta función retorna la cantidad de abejas que comió la lagartija en el día a día
def abejas_comidas(actividades, dieta, dia):
    indiceDieta = 0
    contadorDias = 1
    contadorComida = 0
    for i in actividades:
        if(i != '!' and i != '?'):
            if(i == 'C'):
                contadorComida += 1
        else:
            if(contadorDias == dia):
                if(contadorComida!=0):
                    dietaDIA = dieta[indiceDieta:indiceDieta+contadorComida]
                    numeroAbejas = 0
                    for i in dietaDIA:
                        if(i=='A'):
                            numeroAbejas += 1
                    return numeroAbejas
                else:
                    return 0
            else:
                if(contadorComida!=0):
                    indiceDieta += contadorComida
            contadorComida = 0
            contadorDias += 1
