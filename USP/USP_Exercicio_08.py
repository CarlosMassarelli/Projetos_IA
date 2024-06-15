"""
Exercício USP Cursera
divisão por 5
"""
print('Vamos definir se o número é divisível por 5.')
inteiro=int(input('Digite um número inteiro:'))
#verificando divisão por 5
resto=inteiro%5

if resto != 0:
    print(inteiro)
else:
    print('Buzz')