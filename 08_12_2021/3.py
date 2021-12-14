refineria = [
        [3000, 7000, 2000],
        [4000, 500, 600]
    ]

componente = [
        [10, 5, 35],
        [15, 4, 31],
        [18, 2, 30]
    ]

def totales_anuales(a, b):
    total = []
    for ele in b:
        subtotal = []
        aux = 0
        for i in ele:
            suma = 0
            for j in range(0, len(a)):
                suma += i*a[j][aux]
            aux += 1
            subtotal.append(suma)
        total.append(subtotal)
    return total
            
print(totales_anuales(refineria, componente))            
print()

def maximo_alquitran(a, b):
    # primero sacamos el alquitran
    alquitran = b[1]

    al_r1 = 0
    al_r2 = 0
    
    for i in range(0, len(a[0])):
        al_r1 += a[0][i]*alquitran[i]

    for i in range(0, len(a[1])):
        al_r2 += a[1][i]*alquitran[i]

    return al_r1, al_r2
        
print(maximo_alquitran(refineria, componente))
print()

def que_matriz_es_componente(a,b):
    if len(a) == 3:
        return a
    else:
        return b

print(que_matriz_es_componente(componente, refineria))
