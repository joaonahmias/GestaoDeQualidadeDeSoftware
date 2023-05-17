def paciente_mais_visitas(lista,medico):
    pacientes = []
    contagem = []
    resultado = []
    for elemento in lista:
        if elemento[3]==medico:
            if elemento[1] not in pacientes:
                pacientes.append(elemento[1])
                contagem.append(1)
            else:
                indice = pacientes.index(elemento[1])
                contagem[indice]+=1
    if len(contagem)>0:
        maior = contagem[0]
        indice = 0
        for i in range(len(contagem)):
            if(contagem[i]>maior):
                maior = contagem[i]
        for i in range(len(pacientes)):
            if(contagem[i]==maior):
                resultado.append(pacientes[i])
        return resultado
    else:
        return "Paciente não encontrado"
    
def pacientes_premiados(lista):
    pacientes = []
    consultas = []
    premiados=[]
    for elemento in lista:
        if elemento[1] not in pacientes:
            pacientes.append(elemento[1])
            consultas.append(1)
        else:
            indice = pacientes.index(elemento[1])
            consultas[indice]+=1

    maior = consultas[0]
    for i in range(len(consultas)):
        if consultas[i]>maior:
            maior=consultas[i]
    for i in range(len(pacientes)):
        if consultas[i]==maior:
            premiados.append(pacientes[i])
    return premiados
    




