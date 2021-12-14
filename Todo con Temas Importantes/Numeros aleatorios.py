# para sacar numeros aleatorios importamos la libreria random
import random

# creamos la lista con numeros aleatorios de 10 numeros
lista_aleatorios = [random.randint(1, 10) for i in range(10)]

print('Lista 1:')
print(lista_aleatorios)

# creamos la 2da lista multiplos de 3 y 5
lista_multiplos = [i for i in lista_aleatorios if ((i % 3 == 0) or (i % 5 == 0))]

# ahora eliminamos los duplicados
lista_multiplos = list(set(lista_multiplos))

print('Lista 2:')
print(lista_multiplos)
