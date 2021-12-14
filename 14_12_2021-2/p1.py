import random

# generar números
numeros = [random.randint(1,20) for _ in range(10)]

# Imprimimos los números
print('NUMEROS GENERADOS')
num = ''
for i in range(len(numeros)):
    if(i!=(len(numeros)-1)):
        num+=str(numeros[i])+'-'
    else:
        num+=str(numeros[i])
print(num)

# ahora generamos un diccionario para crear los repetidos
my_dict = dict({})

repetidos = False

for i in numeros:
    if (i in my_dict.keys()):
        my_dict[i] = my_dict[i] + 1
        if(my_dict[i] >= 2):
            repetidos = True
    else:
        my_dict[i] = 1

print()
if(repetidos):
    for key, value in my_dict.items():
        if(value >= 2):
            print('{0}: {1}'.format(key, value))
else:
    print('NO SE REPITEN')
