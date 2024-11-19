"""
Fatorar USP
Fatoração de número inteiro positivo.
"""
def eh_primo(n):
    # Verifica se o número é menor que 2, nesse caso não é primo
    if n < 2:
        return False
    # Verifica se o número tem divisores além de 1 e ele mesmo
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita um número do usuário
n=int(input('Digite um número inteiro positivo: '))

# Verifica se o número é primo e exibe o resultado
if eh_primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo. Então vamos fatorar!")

fator=2
multiplicidade=0
while n>1:
    while n % fator==0:
        multiplicidade +=1
        n /= fator
    if multiplicidade>0:
        print('fator= ',fator,'multiplicidade= ',multiplicidade)
    fator +=1
    multiplicidade=0
