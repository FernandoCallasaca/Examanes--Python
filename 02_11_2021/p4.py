# funcion para agregar las minusculas
def agregar_minusculas(cadena):
    minusculas = []
    for i in cadena:
        if(i.isnumeric() == False):
            if(i == i.lower()):
                minusculas.append(i)
    return minusculas

# funcion para agregar numeros
def agregar_numeros(cadena):
    numeros = []
    for i in cadena:
        if(i.isnumeric()):
            numeros.append(i)
    return numeros

# pedimos la cadena
cadena = input('Cadena: ')

# Imprimimos las minusculas
minusculas = agregar_minusculas(cadena)
cadena_min = ''
for i in minusculas:
    cadena_min += i
print('Lista1:', cadena_min)

# Imprimimos los numeros
numeros = agregar_numeros(cadena)
cadena_num = ''
for i in numeros:
    cadena_num += i
print('Lista2:', cadena_num)
