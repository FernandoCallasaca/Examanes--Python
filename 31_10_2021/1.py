def distancia(string):
    n_a = 0
    n_e = 0
    n_i = 0
    n_o = 0
    n_u = 0
    for i in string:
        i = i.lower()
        if(i == 'a'):
            n_a += 1
        elif(i == 'e'):
            n_e += 1
        elif(i == 'i'):
            n_i += 1
        elif(i == 'o'):
            n_o += 1
        elif(i == 'u'):
            n_u += 1
    if(n_o == 2 and n_e > 1):
        return 13
    else:
        if(n_u > 7):
            return n_u
        elif(n_a >= 1 and n_e >= 1 and n_i >= 1 and n_o >= 1 and n_u >= 1):
            return int((n_a + n_e + n_i + n_o + n_u)**(1/2))
        else:
            return (n_a + n_e + 1)**2

def direccion(string):
    d = ''
    for i in string:
        i = i.lower()
        if(i == 'n'):
            d = 'norte'
            break
        elif(i == 's'):
            d = 'sur'
            break
        elif(i == 'e'):
            d = 'este'
            break
        elif(i == 'o'):
            d = 'oeste'
            break
    if(d != ''):
        return d
    else:
        return 'al inframundo'


N = int(input())
L = []
for i in range(N):
    L.append(input())
for j in L:
    dis = distancia(j)
    dire = direccion(j)
    print('Hermes debe moverse {0} metros en direccion {1}'.format(dis, dire))
    
