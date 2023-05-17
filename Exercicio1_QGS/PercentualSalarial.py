def PercentualSalarial(lista_trabalho_salario):
    salarioTotal=0
    for salario in lista_trabalho_salario:
        salarioTotal+=salario[1]
    lista_trabalho_salarioPercentual=[]
    
    for salario in lista_trabalho_salario:
        if salarioTotal==0:
            lista_trabalho_salarioPercentual.append((salario[0], 0))
        else:
             lista_trabalho_salarioPercentual.append((salario[0], round(salario[1]/salarioTotal,4)))
            
    return lista_trabalho_salarioPercentual


def percentual_renda_media(lista):
    quant_trabalhos = len(lista[0])
    lista_media = []
    for trabalho in range(quant_trabalhos):
        salario_total_mensal = 0
        for mes in lista:
            salario_total_mensal += mes[trabalho][1]
        lista_media.append((lista[0][trabalho][0], salario_total_mensal))
    return PercentualSalarial(lista_media)


