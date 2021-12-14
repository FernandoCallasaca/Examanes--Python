def binario(N):
    b = []
    while N >= 1:
        b.append(N%2)
        N = N // 2
    return b

# ingresar el numero

numero = input('Input: ')  
if(numero == ''):
    print('Output: ', str(binario(8)))
else:
    while (numero.isnumeric() == False or int(numero) >= 9):
        print('Por favor inténtelo nuevamente')
        numero = input('Input: ')
    print(binario(int(numero)))
