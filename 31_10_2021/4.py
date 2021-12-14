def ataque_ares(lista_tropa, odio_del_turno, arma_ares):
    # lista_tropa = listadao de tropas = lista
    # odio_del_turno = float
    # arma_ares = str
    puntaje_ares = calcular_puntaje_ares(arma_ares)
    n = round(odio_del_turno*len(lista_tropa))
    para_borrar = []
    if(n == 0):
        print('Ha reinado la paz en Atenas (por ahora)')
    else:
        for i in range(n):
            aldeano = lista_tropa[i].split(',')
            nombre_aldeano = aldeano[0]
            puntos_vida_aldeano = int(aldeano[1])
            fuerza_aldeano = int(aldeano[2])

            puntaje_aldeano = calcular_puntaje_aldeano(nombre_aldeano)
            
            if(puntaje_ares > puntaje_aldeano):
                puntos_vida_aldeano -= fuerza_aldeano
                print('Ares ha atacado al aldeano {0} y ha quedado con {1} puntos de vida'.format(nombre_aldeano, puntos_vida_aldeano))
            elif(puntaje_ares <= puntaje_aldeano):
                puntos_vida_aldeano += fuerza_aldeano
                print('El aldeano {0} ha probado la inmortalidad y ahora tiene {1} puntos de vida'.format(nombre_aldeano, puntos_vida_aldeano))

            if(puntos_vida_aldeano <= 0):
                # sale de la lista
                para_borrar.append(i)
                print('Se ha reportado el descenso del aldeano {0}'.format(nombre_aldeano))
        for i in range(len(para_borrar)):
            if(i != 0):
                del(lista_tropa[para_borrar[i]-1])
            else:
                del(lista_tropa[para_borrar[i]])
    return lista_tropa
                
def calcular_estado_atenas(lista_tropa, estado_actual_atenas):
    nuevo_estado_atenas = 0
    promedio = 0
    for i in lista_tropa:
        aldeano = i.split(',')
        puntos_vida_aldeano = int(aldeano[1])
        promedio += puntos_vida_aldeano
    promedio = round(promedio / len(lista_tropa))
    if(promedio > 100):
        nuevo_estado_atenas = estado_actual_atenas + promedio
    elif(promedio <= 100):
        nuevo_estado_atenas = estado_actual_atenas - promedio
    elif(promedio == 0):
        nuevo_estado_atenas = 0
    return nuevo_estado_atenas




