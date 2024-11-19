"""
USP
Função inverte a ordem dos elementos de uma lista...


"""
# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para receber os números
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break  # Interrompe o loop se o número for 0
    numeros.append(num)

# Imprime os números em ordem inversa
for num in reversed(numeros):
    print(num)
