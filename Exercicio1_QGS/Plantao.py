def Plantao(lista_medico_hora):
    if(len(lista_medico_hora)==0):
        return[]
    else:
        resultado=[]
        plantaomaislongo = lista_medico_hora[0][1]
        for plantao in lista_medico_hora:
            if plantao[1]==plantaomaislongo:
                resultado.append(plantao)
            elif plantao[1] > plantaomaislongo:
                resultado=[]
                resultado.append(plantao)
                plantaomaislongo = plantao[1]
            
    return resultado
            

