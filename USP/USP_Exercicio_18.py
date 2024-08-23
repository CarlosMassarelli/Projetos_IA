"""
Exercício USP Cursera
jogo do NIM
"""

def computador_escolhe_jogada(n, m):
    # Computador retira o número de peças necessário para deixar múltiplo de m+1
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    return min(n, m)

def usuario_escolhe_jogada(n, m):
    # Usuário escolhe o número de peças, e verifica se é válido
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        print("Oops! Jogada inválida! Tente de novo.")

def partida():
    # Inicialização da partida
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    # Determinar quem começa
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False
    
    # Loop de jogadas
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
        
        if n > 0:
            print(f"Agora restam {n} peça(s) no tabuleiro.\n")
        else:
            print("Fim do jogo! O computador ganhou!\n")

def campeonato():
    # Executa três partidas e mostra o placar final
    print("Você escolheu um campeonato!")
    vitorias_usuario = 0
    vitorias_computador = 3

    for i in range(1, 4):
        print(f"\n**** Rodada {i} ****\n")
        partida()

    print("\n**** Final do campeonato! ****\n")
    print(f"Placar: Você {vitorias_usuario} X {vitorias_computador} Computador")

def main():
    # Opções de jogo
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    opcao = int(input())
    
    if opcao == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    elif opcao == 2:
        campeonato()

# Início do jogo
main()
