"""
USP
Exercício final...
Melhoramentos no programa de verificação de plágio.
"""

import re

# Funções auxiliares (mantidas do código fornecido)
def le_assinatura():
    '''Lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
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
    texto = input(f"Digite o texto {i} (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f"Digite o texto {i} (aperte enter para sair): ")
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

    wal = sum(len(palavra) for palavra in palavras) / len(palavras)
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    hlr = n_palavras_unicas(palavras) / len(palavras)
    sal = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)
    sac = sum(len(separa_frases(sentenca)) for sentenca in sentencas) / len(sentencas)
    pal = sum(len(frase) for frase in frases) / len(frases)

    return [wal, ttr, hlr, sal, sac, pal]

def compara_assinatura(as_a, as_b):
    '''Recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas'''
    return sum(abs(as_a[i] - as_b[i]) for i in range(len(as_a))) / len(as_a)

def avalia_textos(textos, ass_cp):
    '''Recebe uma lista de textos e uma assinatura ass_cp. Devolve o número (1 a n) do texto mais provável de estar infectado por COH-PIAH'''
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas]
    return similaridades.index(min(similaridades)) + 1

# Novas funções para o menu
def calcula_assinatura_media(textos):
    '''Calcula a assinatura média de um conjunto de textos fornecidos'''
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    assinatura_media = [
        sum(assinatura[i] for assinatura in assinaturas) / len(assinaturas)
        for i in range(len(assinaturas[0]))
    ]
    return assinatura_media

def menu():
    '''Exibe o menu de opções e executa a ação escolhida'''
    while True:
        print("\n--- MENU ---")
        print("1. Calcular valores típicos de assinatura (baseado em textos fornecidos)")
        print("2. Detectar texto infectado com COH-PIAH")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nDigite textos para calcular a assinatura média.")
            textos = le_textos()
            if textos:
                assinatura_media = calcula_assinatura_media(textos)
                print("\nAssinatura média calculada:")
                print(f"Tamanho médio de palavra: {assinatura_media[0]:.4f}")
                print(f"Relação Type-Token: {assinatura_media[1]:.4f}")
                print(f"Razão Hapax Legomana: {assinatura_media[2]:.4f}")
                print(f"Tamanho médio de sentença: {assinatura_media[3]:.4f}")
                print(f"Complexidade média de sentença: {assinatura_media[4]:.4f}")
                print(f"Tamanho médio de frase: {assinatura_media[5]:.4f}")
            else:
                print("Nenhum texto fornecido.")
        elif opcao == "2":
            assinatura_cp = le_assinatura()
            textos = le_textos()
            if textos:
                texto_infectado = avalia_textos(textos, assinatura_cp)
                print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH.")
            else:
                print("Nenhum texto fornecido para análise.")
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
