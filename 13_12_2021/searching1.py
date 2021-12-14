actores = [{"actor": "Felipe", "nacionalidad": "peruana", "pelicula": "loco por mary"},
           {"actor": "Gorilon", "nacionalidad": "brasilera", "pelicula": "asesinos locos"},
           {"actor": "Grecia", "nacionalidad": "cubana", "pelicula": "salvando al soldado Jacinto"},
           {"actor": "Teresita", "nacionalidad": "venezolana", "pelicula": "tres y dos son ocho"}]

# pedimos que actor buscar
actor = input('Ingrese nombre de actor a buscar: ')
print()

def buscar_actores(actores, actor):
    # realizamos la busqueda
    result = {}

    primero = 0
    ultimo = len(actores)-1
    encontrado = False
    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)// 2
        if actores[puntoMedio]['actor'] == actor:
            encontrado = True
            result = actores[puntoMedio]
        else:
            if actor < actores[puntoMedio]['actor']:
                ultimo = puntoMedio - 1
            else:
                primero = puntoMedio + 1
    
    print('Resultado:')
    print('nombre:', result['actor'])
    print('nacionalidad:', result['nacionalidad'])
    print('película:', result['pelicula'])

buscar_actores(actores, actor)

