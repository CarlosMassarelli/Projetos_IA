"""
USP
Criando listas
"""
def ehPrimo(x):
    fator=2
    if x == 2:
        return True
    while x % fator != 0 and fator <=x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

limite = int(input('limite máximo: '))
n=2
lista=[]
while n < limite:
    if ehPrimo(n):
        print(n, end=', ')
        lista.append(n)
    n += 1
print('/n')
print(lista)
print(len(lista))


valor=float (input('Digite uma sequência de números quaisquer, quando terminar de digitar, digite 0(zero): '))
while valor != 0:
    lista.append(valor)
    valor = 0
    valor=float (input('Digite uma sequência de números quaisquer, quando terminar de digitar, digite 0(zero): '))
tam=len(lista)-1
while tam>=0:
    print(lista[tam], end=', ')
    tam -=1
    

