def suma_cubos(num):
    num = str(num)
    suma = 0
    for i in num:
        suma += (int(i))**3
    return suma


# pedir numero
num = int(input('Ingrese un numero: '))
while(num%3 != 0):
    num = int(input('Ingrese un numero: '))

suma_c = 0
while(suma_c != 153):
    suma_c = suma_cubos(num)
    print('la suma de cubos de '+ str(num) + ' es: ' + str(suma_c))
    num = suma_c
