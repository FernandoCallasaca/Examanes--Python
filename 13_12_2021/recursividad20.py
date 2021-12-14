def mayorListaRec(d):
    if(len(d) == 1):
        return d[0]
    else:
        if(d[0] > d[1]):
            d[1] = d[0]
            return mayorListaRec(d[1:])
        else:
            return mayorListaRec(d[1:])

lista = [5,4,1,8,6,2,3]

print('Mayor:', mayorListaRec(lista))
