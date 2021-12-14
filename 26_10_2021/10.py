# modulo para hallar la sumatoria
def sumatoria(num = 10):
    s = 0
    for i in range(num + 1):
        s += i
    return s

# pedimos el numero

Input = input('Input: ')
if(Input.isnumeric()):
    print('Output: ' + str(sumatoria(int(Input))))
else:
    print('Output: ' + str(sumatoria()))

