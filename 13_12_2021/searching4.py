peliculas = [
        {'año': 2010, 'nombre': 'Andre Geim y Konstant Novosiólov'},
        {'año': 2011, 'nombre': 'Perlmutter Schimidt y Adam Riess'},
        {'año': 2012, 'nombre': 'Serge Haroche y David Wineland'},
        {'año': 2013, 'nombre': 'Peter Higgs y Francois Englert'},
        {'año': 2014, 'nombre': 'Akasaki Hiroshi Amano y Nakamura'},
        {'año': 2015, 'nombre': 'Takaaki Kajita y Arthur B MacDonald'},
        {'año': 2016, 'nombre': 'Thouless Haldane y Kosterlitz'},
        {'año': 2017, 'nombre': 'Rainer Weiss Barry Barish y Thorne'},
        {'año': 2018, 'nombre': 'Donna Strickland Mouron y Ashkin'},
        {'año': 2019, 'nombre': 'James Peebles Mayor y Queloz'}
    ]

def buscar_peliculas(peliculas, anio):
    # realizamos la busqueda
    result = {}

    primero = 0
    ultimo = len(peliculas)-1
    encontrado = False
    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)// 2
        if peliculas[puntoMedio]['año'] == anio:
            encontrado = True
            result = peliculas[puntoMedio]
        else:
            if anio < peliculas[puntoMedio]['año']:
                ultimo = puntoMedio - 1
            else:
                primero = puntoMedio + 1
    
    # mostramos el resultado
    print('Ganadores:', result['nombre'])

anio = int(input('Ingrese año: '))

# Realizamos la busqueda
buscar_peliculas(peliculas, anio)
