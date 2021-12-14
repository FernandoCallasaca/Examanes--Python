# funcion validar contrasenia
def validar_contrasenia(contrasenia):
    # sacamos los caracteres
    caracteres = len(contrasenia)
    if(caracteres >= 6):
        minusculas = 0
        mayusculas = 0
        numeros = 0
        for i in contrasenia:
            if(i.isnumeric()):
                numeros += 1
            else:
                if(i == i.upper()):
                    mayusculas += 1
                elif(i == i.lower()):
                    minusculas += 1
        if((minusculas >= 2) and (mayusculas >= 2) and (numeros >= 2)):
            return 'Correcto'
        else:
            return 'Error'
    else:
        return 'Error'

# pedimos la contrasenia
contrasenia = input('clave: ')

# verificamos si se correcto o es error
verificacion = validar_contrasenia(contrasenia)

# imprimimos el resultado
print('Respuesta:',verificacion)
