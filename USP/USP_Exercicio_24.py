"""
USP
Desenho com #, agora com espaços...
"""
# Recebe as dimensões do retângulo
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# Laços aninhados para desenhar o retângulo
for i in range(altura):
    if i == 0 or i == altura - 1:
        # Imprime a primeira e a última linha com '#'
        print("#" * largura)
    else:
        # Imprime as linhas intermediárias com borda e espaços no meio
        print("#" + " " * (largura - 2) + "#")

