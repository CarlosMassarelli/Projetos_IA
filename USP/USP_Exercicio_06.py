"""
Exercício USP Cursera
números impares e pares
"""
print('Vamos definir os números digitados.')
inteiro=int(input('Digite um número inteiro:'))
#verificando impar / par
resto=inteiro%2

if resto != 0:
    print('ímpar')
else:
    print('par')
    


"""
if resto != 0:
    print('O número', inteiro,'é impar')
else:
    print('O número', inteiro,'é par')
    
print('Fim!')
"""
