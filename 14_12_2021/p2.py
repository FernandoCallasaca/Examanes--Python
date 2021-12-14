def sumatoria(n, p, su = 0):
    if n == 0:
        return su
    else:
        su += p * n
        return sumatoria(n-1, p, su)

n = int(input('Input n: '))
p = int(input('Input p: '))

# Mostramos el resultado
print('Output:', sumatoria(n,p))
    
