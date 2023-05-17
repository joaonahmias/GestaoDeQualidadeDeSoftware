def repor_Estoque(lista):
    ProdutosArepor = 0
    for produto in lista:
        if produto[1]<5:
            ProdutosArepor+=1
            
    return  ProdutosArepor

