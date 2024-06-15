"""
Exercício USP Cursera
retorna o número da dezena do valor digitado
"""

numero = int(input("Digite um número inteiro:"))

# Calcula o dígito das dezenas

digito_dezenas = (numero // 10) % 10

print(f"O dígito das dezenas é {digito_dezenas}")