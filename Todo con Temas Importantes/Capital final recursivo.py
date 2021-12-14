def capital_final(ci, n):
    if n == 0:
        return ci
    else:
        return (capital_final(ci, n-1)*1.01)
    
ci = int(input('Ingrese el Capital Inicial: '))
n = int(input('Ingrese el mes en el que quiere saber su capital: '))
  
print('El Capital en el mes ' + str(n) + ' es: ' + str(round(capital_final(ci, n),3)))
