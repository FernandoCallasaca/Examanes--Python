def extra_intervalo(lista, limite_inf = 0, lim_super = 100):
    lista_intervalo = []
    for i in lista:
        if((i >= limite_inf) and (i <= lim_super)):
            lista_intervalo.append(i)
    return lista_intervalo

# llamamos a la lista
lista = [1, 80, 15 ,30, 25, 90, 110, 105, 180, 200, 10]
print(extra_intervalo(lista, 10, 70))
print()
print(extra_intervalo(lista))
