import math

print('Vamos calcular a raiz real de Bhaskara ...')
print('Digite os valores para calcularmos as raízes, precisamos de 3 valores:')
a = int(input('O primeiro valor será: '))
b = int(input('O segundo valor será: '))
c = int(input('O terceiro valor será: '))

# Calculando delta
delta = b**2 - 4*a*c

if delta > 0:
    print('Como o valor de delta é maior que zero, teremos duas raízes.')
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print('Portanto, o gráfico da função encontrará o eixo x em dois pontos, em', raiz1, 'e', raiz2)
elif delta == 0:
    print('Como o valor de delta é igual a zero, teremos uma raiz.')
    raiz = -b / (2*a)
    print('Portanto, o gráfico da função encontrará o eixo x em um ponto, em', raiz)
else:

