p = [1, 2, 1]
q = [4, -17]
r = [-1, 0, 0, -5, 0, 3]
s = [0] * 40 + [5] + [0]*39 + [2]

def grado(p):
    return len(p) - 1

print(grado(p))
print()
print(grado(r))
print()
print(grado(s))
print()

def evaluar(p, x):
    evaluacion = 0
    for i in range(0, len(p)):
        evaluacion += x**i * p[i]
    return evaluacion

print(evaluar(p, 3))
print()
print(evaluar(q, 0.0))
print()
print(evaluar(r, 1.1))
print()
print(evaluar([4,3,1], 3.14))
print()

def sumar_polinomios(p1, p2):
    suma = []
    mayor = len(p1)
    if len(p2) > len(p1):
        mayor = len(p2)

    for i in range(0,mayor):
        sum = 0
        if i < len(p1):
            sum += p1[i]
        if i < len(p2):
            sum += p2[i]
        suma.append(sum)
    return suma

print(sumar_polinomios(p,r))
print()

def derivar_polinomio(p):
    derivada = []
    for i in range(1, len(p)):
        derivada.append(p[i]*i)
    return derivada

print(derivar_polinomio(r))
print()

def multiplicar_polinomio(p1, p2):
    len_p1 = len(p1)
    len_p2 = len(p2)

    if (len_p1 == 1 and len_p2 == 1):
        return [p1[0] * p2[0]]
    elif (len_p1 == 1 and len_p2 > 1):
        return p2
    elif (len_p1 > 1 and len_p2 == 1):
        return p1
    else:
        mayor = len_p1
        if len_p1 < len_p2:
            mayor = len_p2
            
        multiplicacion = []
        for i in range(0,((len_p1 - 1) + (len_p2 - 1)) + 1):
            multiplicacion.append([])
            
        l1 = []
        l2 = []
        if mayor == len(p1):
            l1 = p1
            l2 = p2
        else:
            l1 = p2
            l2 = p1
        
        for i in range(0, len(l2)):
            for j in range(0, len(l1)):
                multiplicacion[j+i].append(l2[i]*l1[j])
                
    resultado = []
    for i in multiplicacion:
        suma = 0
        for j in i:
            suma += j
        resultado.append(suma)
            
    return resultado

print(multiplicar_polinomio(p,q))
print()
print(multiplicar_polinomio(r,q))

    
