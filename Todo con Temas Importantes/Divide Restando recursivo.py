def divide_restando(dividendo, divisor, contador = 0):
    if(divisor == 0):
        return 'No se puede dividir entre 0'
    else:
        if((dividendo - divisor) < divisor):
            return contador + 1
        else:
            dividendo = dividendo - divisor
            contador += 1
            return divide_restando(dividendo, divisor, contador)

# ejemplo
print(divide_restando(200, 7))
