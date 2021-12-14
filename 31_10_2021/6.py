# numero de arenas
N = int(input())

lista_arenas = []
for i in range(N):
    lista_arenas.append(input())
    
llave = input()

vida = int(input())

# sacamos en cuantas arenas esta la llave

juego_final = []

for arena in lista_arenas:
    rondas = 0
    for j in range(len(arena)-len(llave)):
        if(arena[j:len(llave)+j]==llave):
            rondas += 1
    if(rondas > 0):
       juego_final.append([arena, rondas])

# ingresamos los titanes

for i, j in enumerate(juego_final):
    nombre_titan = input()
    vida_titan = int(input())
    juego_final[i].extend([nombre_titan, vida_titan])

# ========================== empezamos el juego
for i in juego_final:
    arena = i[0]
    rondas = i[1]
    titan = i[2]
    vida_titan = i[3]
    print('> Me he encontrado con {0}\n'.format(titan))
    for j in range(rondas):
        if(vida_titan <= 0 or vida <= 0):
            break
        print('>> Ronda {0}\n'.format(j+1))
        for xo in arena:
            print('Mi vida actual es {0}'.format(vida))
            print('La vida de {0} es {1}'.format(titan, vida_titan))
            if(xo.lower() == 'x'):
                print('>>> {0} me ataco y perdi vida\n'.format(titan))
                vida -= 1
            else:
                dano_causado = calcular_dano_a_titan(vida)
                #dano_causado = 10 # este dato de prueba
                print('>>> Le cause {0} de dano a {1}\n'.format(dano_causado, titan))
                vida_titan -= dano_causado
            if(vida_titan <= 0 and vida > 0):
                print('{0} derrotado con exito!\n'.format(titan))
                break
            elif(vida <= 0):
                print('Te ha derrotado {0}\n'.format(titan))
                break
        if(vida_titan > 0 and vida > 0 and j == (rondas - 1)):
            print('{0} ha escapado de ti con {1} de vida!\n'.format(titan, vida_titan))
                
if(vida <= 0):
    print('Has perdido la batalla contra los titanes y las titanides :(')
else:
    print('Has ganado la titanomaquia y con ello has ganado el favor de Zeus y todos los olimpicos')
    
# Datos de Prueba
"""
1
XXOOOXOOOX
XOOO
20
Oceano
30
"""

"""
2
OXOXOOXOOX
OXXOOXXOXX
OXO
17
Crio
72
"""

"""
5
XXOXXXOXOO
XOXXOXOXXO
OOXXOOXOOO
OOOOOXXXXO
OXXOOXOOXO
XOXX
27
Cronos
16
Japeto
40
"""
