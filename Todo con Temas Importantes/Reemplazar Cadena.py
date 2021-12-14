# Pedimos la cadena
cadena = input('CADENA: ')

cadena_reemplazada = ''
# reemplazamos la cadena
for i in cadena:
    if(i=='a'):
        cadena_reemplazada += '1'
    elif(i=='e'):
        cadena_reemplazada += '2'
    elif(i=='i'):
        cadena_reemplazada += '3'
    elif(i=='o'):
        cadena_reemplazada += '4'
    elif(i=='u'):
        cadena_reemplazada += '5'
    elif(i=='A'):
        cadena_reemplazada += '6'
    elif(i=='E'):
        cadena_reemplazada += '7'
    elif(i=='I'):
        cadena_reemplazada += '8'
    elif(i=='O'):
        cadena_reemplazada += '9'
    elif(i=='U'):
        cadena_reemplazada += '0'
    else:
        cadena_reemplazada += i

print('RESPUESTA:',cadena_reemplazada)
