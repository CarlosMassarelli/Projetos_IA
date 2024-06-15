"""
Exercício USP Cursera
Calculando Bhascara
"""
import math

# Recebe os coeficientes a, b e c
a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

# Calcula o delta
delta = b**2 - 4*a*c

if delta < 0:
    # Quando não houver raízes reais
    print('esta equação não possui raízes reais')
elif delta == 0:
    # Quando houver apenas uma raiz (raiz dupla)
    raiz = -b / (2*a)
    print('a raiz dupla desta equação é', raiz)
else:
    # Quando houver duas raízes reais distintas
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    # Ordena as raízes em ordem crescente
    if raiz1 > raiz2:
        raiz1, raiz2 = raiz2, raiz1
    print('as raízes da equação são', raiz1, 'e', raiz2)