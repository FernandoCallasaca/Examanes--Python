def mayor(lista):
    mayor = lista[0]
    for i in lista:
        if mayor < i:
            mayor = i
    return mayor

def menor(lista):
    menor = lista[0]
    for i in lista:
        if menor > i:
            menor = i
    return menor


# programa principal
nro1 = int(input('Ingrese el nro 1: '))
nro2 = int(input('Ingrese el nro 2: '))
nro3 = int(input('Ingrese el nro 3: '))
nro4 = int(input('Ingrese el nro 4: '))
nro5 = int(input('Ingrese el nro 5: '))

# creamos la lista
lista = [nro1, nro2, nro3, nro4, nro5]

# sacamos el mayor y el menor
mayor = mayor(lista)
menor = menor(lista)

# imprimimos el promedio de mayor y menor
print((mayor+menor)/2)
