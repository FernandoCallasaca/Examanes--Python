import math

lista1 = [12, 9, 28, 11, 2, 35]
lista2 = [2, 8, 95, 12]
lista3 = [24, 81, 64, 35, 67, 18, 94]

# creamos este modulo ya que a veces el round no redondea bien
# los numeros que terminan en  0.5

def round_probado(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def promedio(lista1, lista2, lista3):
    len_l1 = len(lista1)
    len_l2 = len(lista2)
    len_l3 = len(lista3)
    
    prom = []
    
    mayor = len_l1
    if len_l2 > len_l1:
        mayor = len_l2
    if len_l3 > mayor:
        mayor = len_l3

    for i in range(0, mayor):
        sum = 0
        cont = 0
        if(i < len_l1):
            sum += lista1[i]
            cont += 1
        if(i < len_l2):
            sum += lista2[i]
            cont += 1
        if(i < len_l3):
            sum += lista3[i]
            cont += 1
        prom.append(round_probado(sum / cont))

    return prom

print(promedio(lista1, lista2, lista3))


    
