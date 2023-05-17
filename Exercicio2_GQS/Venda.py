def Percentual_Venda_Produto(lista):
    lista_quantidade = []
    lista_id = []
    resultante = []
    total=0
    for produto in lista:
        if produto[1] not in lista_id:
            lista_id.append(produto[1])
            lista_quantidade.append(produto[2])
        else:
            i = lista_id.index(produto[1])
            lista_quantidade[i]+=produto[2]
        total+=produto[2]
    i=0
    for produto in lista_id:
        percentual = round(lista_quantidade[i]/total,4)
        resultante.append((produto,percentual))
        i+=1
    return resultante

def Total_Vendas(lista):
    resultante=0
    for venda in lista:
        resultante+=venda[1]
    return resultante

def Percentual_Crescimento(lista, parametro):
    indice = 0
    for elemento in lista:
        if elemento[0] == parametro:
            valor = elemento[1]
            break
        indice+=1 
    resultado = 0
    if(indice!=0):
       resultado = ((valor-lista[indice-1][1])/lista[indice-1][1])*100
    return resultado 
       

    
    


