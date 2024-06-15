"""
Exercício USP Cursera
divisão por 5 ou 3
"""
print('Vamos definir se o número é divisível por 3 e por 5.')
inteiro=int(input('Digite um número inteiro:'))

#verificando divisão por 3 e por 5
resto1=inteiro%5
resto2=inteiro%3

if (resto1 == 0 and resto2 == 0):
    print('FizzBuzz')
else:
    print(inteiro)