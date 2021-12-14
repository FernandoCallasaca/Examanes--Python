def cantidad_campeones(N, tipo):
    totalCampeones = 0
    for i in range (0,N):
        # hacemos uso del metodo tipo_campeon de la librería campeones 
        tipoCampeon = tipo_campeon(i)
        # preguntamos si la respuesta del metodo es igual al tipo que buscamos
        if(tipoCampeon == tipo):
            # en caso sea igual ya tenemos un campeon con el mismo tipo
            totalCampeones += 1
    return totalCampeones

    
