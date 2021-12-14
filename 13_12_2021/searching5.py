# pedimos que ingrese su usuario

usuario = input('Usuario: ')
clave = input('Clave: ')
print('CORRECTO')

# pregutamos si desea cambiar de clave
respuesta = True

# creamos un arreglo con todos las claves
claves = [clave]

while(respuesta):
    pregunta = input('Desea cambiar clave[S/N]: ')
    respuesta = True if pregunta == 'S' else False
    if(respuesta):
        usuario = input('Usuario: ')
        clave = input('Clave: ')
        if(clave in claves):
            print('ERROR')
        else:
            claves.append(clave)
            print('CORRECTO')
if(respuesta == False):
    print('FIN')
