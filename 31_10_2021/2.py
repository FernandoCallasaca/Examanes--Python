import random
#from olimpo.py import clasificacion
# libreria olimpo.py
# funcion clasificacion(nombre) = retorno un string que corresponde
# a la categoria que se encuentra('Olimpo', 'Olimpo fruna', 'Semi Dios', 'Mortal ')

def contar_letras_repetidas(string):
    string = string.lower()
    letras_repetidas = 0
    for i, l in enumerate(string):
        if(string.index(l) == i):
            if(string.count(l) > 1):
                letras_repetidas += string.count(l)
    if(letras_repetidas != 0):
        return letras_repetidas
    else:
        return 1
    
def calcular_poder(nombre, lugar):
    clasi = clasificacion(nombre)
    habilidad_de_combate_enemigo = 0
    if (clasi == 'Olimpo'):
        habilidad_de_combate_enemigo = 5
    elif (clasi == 'Olimpo fruna'):
        habilidad_de_combate_enemigo = 3
    elif (clasi == 'Semi Dios'):
        habilidad_de_combate_enemigo = 2
    elif (clasi == 'Mortal'):
        habilidad_de_combate_enemigo = 0
    aleatoriedad = random.randint(0, 2)
    buff = 1
    if(nombre == 'Zeus' and lugar == 'Olimpo'):
        buff = 10
    elif(nombre == 'Poseidon' and lugar == 'Mar'):
        buff = 8
    elif(nombre == 'Hades' and lugar == 'Infierno'):
        buff = 7
    elif(nombre == 'Ares'):
        buff = 15
    conocimiento_lugar = contar_letras_repetidas(lugar)

    return ((habilidad_de_combate_enemigo + aleatoriedad)*buff)/conocimiento_lugar
        
entrada = input()
L = entrada.split(';')
nombre = L[0]
lugar = L[1]

print('El poder de {0} en {1} es {2}'.format(nombre, lugar, calcular_poder(nombre, lugar)))
