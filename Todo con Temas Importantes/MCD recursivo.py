def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

a = int(input('Por favor ingrese número A: '))
b = int(input('Por favor ingrese número B: '))

print('El máximo común divisor es:', mcd(a,b))
