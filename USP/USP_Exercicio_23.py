"""
USP
Desenho com #
"""

# Recebe as dimensões do retângulo
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# Laços aninhados para desenhar o retângulo
for i in range(altura):  # Loop externo para as linhas (altura)
    for j in range(largura):  # Loop interno para as colunas (largura)
        print("#", end="")  # Imprime o caractere '#' sem quebrar a linha
    print()  # Quebra a linha após cada linha completa do retângulo
