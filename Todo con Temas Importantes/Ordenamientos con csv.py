# ============ Pregunta 1 ============
# Creamos el diccionario
pokemones = dict({})

with open('./pokemon.csv', "r") as archivo:
    # Omitimos el encabezado
    next(archivo, None)
    for linea in archivo:
        # Remover salto de línea
        linea = linea.rstrip()
        # Ahora convertimos la línea a arreglo con split
        lista = linea.split(";")
        # Sacamos los valores
        clave = int(lista[1])
        nombre = lista[0]
        puntos_ataque = int(lista[2])
        puntos_defensa = int(lista[3])
        puntos_velocidad = int(lista[4])
        habilidad = lista[5]
        # creamos el valor(diccionario) de nuestro diccionari principal
        valor = dict({})
        valor['nombre'] = nombre
        valor['puntos_ataque'] = puntos_ataque
        valor['puntos_defensa'] = puntos_defensa
        valor['puntos_velocidad'] = puntos_velocidad
        valor['habilidad'] = habilidad
        # ahora agregamos a nuestro diccionario principal
        pokemones[clave] = valor
print(pokemones)
print()
        
# ============ Pregunta 2 ============ 
def buscar_dato_pokemon(pokemones, id, valor):
    result = ""
    # preguntamos si existe en el diccionario el id
    if(id in pokemones.keys()):
        result = pokemones[id][valor]
    else:
        result = 'Pokémon no encontrado'
    return result

print(buscar_dato_pokemon(pokemones, 3, 'puntos_ataque'))
print()

# ============ Pregunta 3 ============
def pokemon_rapido(pokemones):
    result = ()
    
    mayor = 0
    id_pok = -1
    for key,value in pokemones.items():
        if(value['puntos_velocidad']>mayor):
            mayor = value['puntos_velocidad']
            id_pok = key
    result = (pokemones[id_pok]['nombre'], pokemones[id_pok]['puntos_velocidad'])

    return result

print(pokemon_rapido(pokemones))
print()

# ============ Pregunta 4 ============

def merge(left, right):
    merged_list = []
    # SU SOLUCION EMPIEZA AQUI
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    # SU SOLUCION TERMINA AQUI
    return merged_list

def merge_sort(lista):
    # SU SOLUCION EMPIEZA AQUI
    longitud = len(lista)

    if longitud == 1:
        return lista
    
    mitad = longitud // 2
    
    left = merge_sort(lista[:mitad]) # debe implementar el valor correcto de left
    right = merge_sort(lista[mitad:]) # debe implementar el valor correcto de right

    # SU SOLUCION TERMINA AQUI
    return merge(left, right)

def nombre_ascendente(pokemones):
    result = []
    # SU SOLUCION EMPIEZA AQUI
    nombres = []
    my_dict = {}
    for key,value in pokemones.items():
        nombres.append(pokemones[key]['nombre'])
        my_dict[pokemones[key]['nombre']] = key
    nombres = merge_sort(nombres)
    for i in nombres:
        result.append((i, my_dict[i]))
    # SU SOLUCION TERMINA AQUI
    return result

print(nombre_ascendente(pokemones))
print()

# ============ Pregunta 5 ============

def busqueda_habilidad(nombre_a_buscar, nombres_ordenados, pokemones):
    result = {}
    # SU SOLUCION EMPIEZA AQUI
    primero = 0
    ultimo = len(nombres_ordenados)-1
    encontrado = False
    id_pok = -1
    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)// 2
        if nombres_ordenados[puntoMedio][0] == nombre_a_buscar:
            encontrado = True
            id_pok = nombres_ordenados[puntoMedio][1]
        else:
            if nombre_a_buscar < nombres_ordenados[puntoMedio][0]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1
    if(encontrado):
        result[id_pok] = pokemones[id_pok]
    else:
        result[-1] = 'No encontrado'
    # SU SOLUCION TERMINA AQUI
    return result

print(busqueda_habilidad('Squirtle1',nombre_ascendente(pokemones), pokemones))
print()
