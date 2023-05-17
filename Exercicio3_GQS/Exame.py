def Exames_alterados(lista, exame, valorEsperado):
    alterados = 0
    total_exame=0
    for elemento in lista:
        if elemento[1] == exame:
            if elemento[3] > valorEsperado:
                alterados+=1
            total_exame+=1
    resultado = 0
    if total_exame!=0:
        resultado = (alterados*100)/total_exame
    return resultado
    
def Quantidade_exames_medico(lista,medico):
    exames=0
    for elemento in lista:
        if elemento[0]==medico:
            exames+=1
    return exames