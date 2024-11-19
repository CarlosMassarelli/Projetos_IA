"""
USP
Função remove repetidos de uma lista...

# Exemplos de uso
lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))  # Saída: [1, 2, 3, 4]

print(remove_repetidos([1, 2, 3, 3, 3, 4]))  # Saída: [1, 2, 3, 4]
"""

def remove_repetidos(lista):
    # Usa set para remover elementos repetidos e sorted para ordenar a lista
    lista_sem_repetidos = sorted(set(lista))
    return lista_sem_repetidos


