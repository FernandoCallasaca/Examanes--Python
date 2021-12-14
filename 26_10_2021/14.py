def isDivisible11(num):
    num = str(num)
    sum_par = 0
    sum_impar = 0
    for i, n in enumerate(num):
        if(i%2 == 0):
            sum_par += int(n)
        else:
            sum_impar += int(n)
    if((sum_par - sum_impar) == 0):
        return('SI')
    else:
        return('NO')

# pedimos el numero
num = int(input('Ingrese un numero: '))

if(isDivisible11(num) == 'SI'):
    print('El número SI es divisible por 11')
else:
    print('El número NO es divisible por 11')
