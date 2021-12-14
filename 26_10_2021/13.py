def varidarango(ri, rf, numero):
    return ((numero >= ri) and (numero <= rf))


# pido cantidad de numeros validos
validos = int(input('Ingrese cantidad de numeros validos esperados: '))
inicio = int(input('Ingrese rango de inicio: '))
fin = int(input('Ingrese rango de fin: '))


i = 0
sum_validos = 0

while(i < validos):
    num = int(input('Ingrese numero 1: '))
    if(varidarango(inicio, fin, num)):
        i += 1
        sum_validos += num
    else:
        print("Ingrese numero dentro del rango: [{0} - {1}]".format(inicio, fin))

print('El promedio es: ' + str(sum_validos / validos))
    
