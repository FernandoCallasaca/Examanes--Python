def escapar_inframundo(lista, posicion, vida):
    if(vida <= 0 or len(lista) == 0):
        if(vida <= 0):
            return 0
        else:
            return vida
    else:
        elemento = lista[posicion]
        sum_digitos = 0
        lugar_enemigo = ''
        for i in elemento:
            if(i.isnumeric()):
                sum_digitos += int(i)
            else:
                lugar_enemigo += i
        if(lugar_enemigo == 'Tartarus' or lugar_enemigo == 'Asphodel' or lugar_enemigo == 'Elysium'):
            vida += sum_digitos
            print('Has superado {0} [{1}] y recuperado {2} de vida ({3})'.format(lugar_enemigo, posicion, sum_digitos, vida))
        else:
            vida -= sum_digitos
            if(vida > 0):
                print('Has derrotado a {0} [{1}], perdiendo {2} de vida ({3})'.format(lugar_enemigo, posicion, sum_digitos, vida))
            else:
                print('Has perdido contra {0} [{1}]'.format(lugar_enemigo, posicion))
            if(lugar_enemigo == 'Hades'):
                if(vida > 0):
                    return vida
                else:
                    return 0
        del(lista[posicion])            
        return escapar_inframundo(lista, sum_digitos, vida)

#lista1 = ['6Rhadamanthus', 'Alect7o', 'Styx4', 'Ha19de3s', 'Ae9acus','Tartaru4s', 'Magae2ra', 'Cerb6eru5s', '7Spart3a', '1Hecate','Eur3yno7mos', 'E3lysium', '1Achlys', 'Asphode0l','19C3orfu7', '5Melinoe', 'Per3sephone', 'Cha3ron', 'Mi9nos','Th4anatos', 'Tisipho2ne', 'Ny0x']
#pos1 = 4
#vida1 = 34

#lista2 = ['1Magaera', 'Elysium3', '1Mete625o4ra', 'Had8es2', 'Achly0s','Eurynomo6s', 'C5haron', 'Minos1', 'N8yx', 'Tart8arus','Thanatos8', '6Styx', 'Asphod5el']
#pos2 = 8
#vida2 = 59

#resultado = escapar_inframundo(lista2, pos2, vida2)
#if(resultado == 0):
#    print('No has logrado escapar de Hades')
#else:
#    print('Has derrotado a Hades y vuelto a Hellas!')
