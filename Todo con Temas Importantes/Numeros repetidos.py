# modulo para crear la lista
def lista_creada(frase):
    l = []
    for i in list(frase):
        if(i != ' '):
            l.append(i)
    return l

# modulo para sacar repetidos
def numero_repetidos(lista):
    n_repetidos = 0
    lista_repetidos = []
    for i, c in enumerate(lista):
        if (lista.index(c) != i):
            lista_repetidos.append(c)
    
    return len(set(lista_repetidos))

# recibir la frase
frase = str(input('Ingresa la frase: '))
# imprimos la lista
print(lista_creada(frase))
print(numero_repetidos(lista_creada(frase)))
