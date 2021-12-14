def imprimir_combates(N, tipo):
    combatientesSegunTipo = []
    for i in range (0,N):
        # hacemos uso del metodo tipo_campeon de la librería campeones
        if(tipo_campeon(i) == tipo):
            # en caso sea igual ya tenemos un campeon con el mismo tipo
            combatientesSegunTipo.append(i)
    # Hasta aquí tenemos los combatientes del mismo tipo 'tipo'
    # en combatientesSegunTipo

    # Ahora haremos que se peleen y muestre los ganadores
    for i in combatientesSegunTipo:
        for j in combatientesSegunTipo:
            # Aquí vamos a la función combate_campeones de la librería campeones
            resultadoCombate = combate_campeones(i, j)
            ganador = i
            if(resultadoCombate == 1):
                ganador = i
            elif(resultadoCombate == 0):
                ganador = j
            elif(resultadoCombate == -1):
                ganador = i
            print('Campeon',i,'v/s Campeon',j,'-> Gana',ganador)

def mejor_campeon(N, tipo):
    combatientesSegunTipo = []
    listaGanadores = []
    for i in range (0,N):
        if(tipo_campeon(i) == tipo):
            combatientesSegunTipo.append(i)

    # Ahora haremos que se peleen y muestre los ganadores
    for i in combatientesSegunTipo:
        for j in combatientesSegunTipo:
            # Aquí vamos a la función combate_campeones de la librería campeones
            resultadoCombate = combate_campeones(i, j)
            ganador = i
            if(resultadoCombate == 1):
                ganador = i
            elif(resultadoCombate == 0):
                ganador = j
            elif(resultadoCombate == -1):
                ganador = i
            # Agregamos los ganadores a una lista para sacar el mejor
            listaGanadores.append(ganador)
    # Sacamos el mejor de la lista de ganadores
    cambat = combatientesSegunTipo[0]
    ganados = listaGanadores.count(cambat)
    for i in range(1, len(combatientesSegunTipo)):
        if(listaGanadores.count(combatientesSegunTipo[i])>ganados):
            cambat = combatientesSegunTipo[i]
    return cambat
