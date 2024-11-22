"""
USP
Exercício final...
Verificador de similaridade de textos.

"""

import re

def le_assinatura():
    '''Lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho médio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''Lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''Recebe um texto e devolve uma lista das sentenças dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''Recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''Recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        freq[p] = freq.get(p, 0) + 1
    return len(freq)

def calcula_assinatura(texto):
    '''Recebe um texto e devolve a assinatura do texto'''
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    wal = sum(len(palavra) for palavra in palavras) / len(palavras)  # Tamanho médio de palavra
    ttr = n_palavras_diferentes(palavras) / len(palavras)           # Relação Type-Token
    hlr = n_palavras_unicas(palavras) / len(palavras)               # Razão Hapax Legomana
    sal = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)  # Tamanho médio de sentença
    sac = sum(len(separa_frases(sentenca)) for sentenca in sentencas) / len(sentencas)  # Complexidade de sentença
    pal = sum(len(frase) for frase in frases) / len(frases)         # Tamanho médio de frase

    return [wal, ttr, hlr, sal, sac, pal]

def compara_assinatura(as_a, as_b):
    '''Recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas'''
    return sum(abs(as_a[i] - as_b[i]) for i in range(len(as_a))) / len(as_a)

def avalia_textos(textos, ass_cp):
    '''Recebe uma lista de textos e uma assinatura ass_cp. Devolve o número (1 a n) do texto mais provável de estar infectado por COH-PIAH'''
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas]
    return similaridades.index(min(similaridades)) + 1

def main():
    '''Função principal que orquestra a execução do programa'''
    assinatura_cp = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, assinatura_cp)
    print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH")

if __name__ == "__main__":
    main()

