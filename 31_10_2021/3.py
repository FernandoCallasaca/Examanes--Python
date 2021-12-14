def decodificar_cetaceo(frase_cetacea):
    frase_cetacea = frase_cetacea.lower()
    traduccion = ''
    for i, l in enumerate(frase_cetacea):
        if(i>0):
            if(l.isnumeric()):
                if(frase_cetacea[i-1].isnumeric() == False):
                    traduccion += ' '
            else:
                if(l != frase_cetacea[i-1]):
                    traduccion += l
        else:
            traduccion += l
    return traduccion

frase = input()       
#print(decodificar_cetaceo('ggggrRRRRieEegggGGGooOooO6>5oOooiikoOOoOos'))
print(decodificar_cetaceo(frase))
