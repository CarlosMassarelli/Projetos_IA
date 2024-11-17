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
i=0
if valor == 0:
    lista.append(valor)
    valor = 0
    valor=float (input('Digite uma sequência de números quaisquer, quando terminar de digitar, digite 0(zero): '))
else:
    for i in range (len(lista),-1): 
        print (lista [i])
    

