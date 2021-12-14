peliculas = [
        {"titulo": "Shrek", "año": 2001},
        {"titulo": "El viaje de Chihiro", "año": 2002},
        {"titulo": "Buscando a Nemo", "año": 2003},
        {"titulo": "Los Increíbles", "año": 2004},
        {"titulo": "Wallace y Gromit", "año": 2005},
        {"titulo": "Happy Feet", "año": 2006},
        {"titulo": "Ratatouille", "año": 2007},
        {"titulo": "WALL-E", "año": 2008},
        {"titulo": "Up", "año": 2009},
        {"titulo": "Toy Story 3", "año": 2010},
        {"titulo": "Rango", "año": 2011},
        {"titulo": "Valiente", "año": 2012},
        {"titulo": "Frozen", "año": 2013},
        {"titulo": "Grandes Héroes", "año": 2014},
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
    print('Pelicula:', result['titulo'])

anio = int(input('Ingrese año: '))

# Realizamos la busqueda
buscar_peliculas(peliculas, anio)

