"""
USP
Função para fazer matrizes
"""
def cria_matriz(num_linhas,num_colunas):
    # cria e retorna uma matriz conforme solicitado
    matriz=[] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha=[] # lista vazia
        for j in range(num_colunas):
            valor=int(input('Digite o elemento ['+ str(i)+']'+str(j)+']: '))
            linha.append(valor)
        
        # adiciona linha à matriz
        matriz.append(linha)

    return imprime_matriz(matriz)

def imprime_matriz(matriz):
    # Função que imprime a matriz de forma formatada
    for linha in matriz:
        print(" ".join(f"{x:>3}" for x in linha))  # Formata os valores com 3 espaços alinhados

def dados_matriz():
    lin = int(input('Digite o número de linhas: '))
    col = int(input('Digite o número de colunas: '))
    return cria_matriz(lin, col)

#matriz = cria_matriz(5,2,30)
#imprime_matriz(matriz)
dados_matriz()