"""
Exercício USP Cursera
Calculando a distância entre 2 pontos
"""
import math

# Recebe 4 números como entrada
x1 = float(input('Digite a coordenada x do primeiro ponto: '))
y1 = float(input('Digite a coordenada y do primeiro ponto: '))
x2 = float(input('Digite a coordenada x do segundo ponto: '))
y2 = float(input('Digite a coordenada y do segundo ponto: '))

# Calcula a distância entre os dois pontos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Verifica a distância e imprime o resultado adequado
if distancia >= 10:
    print('longe')
else:
    print('perto')