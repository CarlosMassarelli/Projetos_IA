"""
Exercício USP Cursera
jogo do NIM
"""

def computador_escolhe_jogada(n, m):
    # Computador escolhe a jogada de acordo com a estratégia vencedora
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    return m

def usuario_escolhe_jogada(n, m):
    # Solicita ao usuário uma jogada válida
    jogada_valida = False
    while not jogada_valida:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            jogada_valida = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")
    return jogada

def partida():
    # Solicita ao usuário os valores de n e m
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Decide quem começa
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False

    # Jogo prossegue até que todas as peças sejam retiradas
    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print(f"Você tirou {jogada} peça(s).")
            vez_do_usuario = False
        else:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f"O computador tirou {jogada} peça(s).")
            vez_do_usuario = True
        print(f"Agora restam {n} peça(s) no tabuleiro.\n")

    # Declara o vencedor e retorna o resultado
    if vez_do_usuario:
        print("O computador ganhou!")
        return "computador"
    else:
        print("Você ganhou!")
        return "usuario"

def campeonato():
    # Realiza um campeonato de 3 partidas
    placar_computador = 0
    placar_usuario = 0

    for i in range(1, 4):
        print(f"**** Rodada {i} ****\n")
        vencedor = partida()
        if vencedor == "computador":
            placar_computador += 1
        else:
            placar_usuario += 1

    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

# Início do programa
print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

opcao = int(input())

if opcao == 1:
    print("\nVocê escolheu uma partida isolada!")
    partida()
elif opcao == 2:
    print("\nVocê escolheu um campeonato!")
    campeonato()
