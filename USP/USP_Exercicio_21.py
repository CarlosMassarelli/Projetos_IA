"""
Fatorial USP
"""
print("Vamos ver o fatorial de um número qualquer!")
n=int(input('Digite um número inteiro: '))
f=n
while n>=0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial*n
        n=n-1
    print('O valor do fatorial de ',f,' é ',fatorial)
    n=int(input('Digite um número inteiro: '))
    f=n


