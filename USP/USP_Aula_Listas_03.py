"""
USP
Trabalhando com listas e entendendo variáveis
"""

a = "cesta"
objeto = "cesta"
print(id(a))       # Mostra o endereço de memória do objeto "cesta"
print(id(objeto))  # Mesmo endereço que `a`

objeto = str("cesta")  # Cria explicitamente um novo objeto
print(id(objeto) == id(a))  # Agora será `False`

a is objeto

a = [10,15,20]
print('endereço de a = ',id(a)) 
print('endereço de a[0] = ',id(a[0])) 
type(a)
objeto = [10,15,20]
print('endereço de objeto = ',id(objeto))
type(objeto)
print('endereço de objeto[0] = ',id(objeto[0]))

import copy

# Estrutura original
original = [[1, 2], [3, 4]]

# Cópia superficial
shallow_copy = original.copy()

# Cópia profunda
deep_copy = copy.deepcopy(original)

# Alterando o original
original[0][0] = 100

print("Original:", original)         # [[100, 2], [3, 4]]
print("Shallow Copy:", shallow_copy) # [[100, 2], [3, 4]]  (aponta para os mesmos objetos internos)
print("Deep Copy:", deep_copy)       # [[1, 2], [3, 4]]    (totalmente independente)

original = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original)

# Comparando identidades
print('endereço de original = ',id(original))       # Endereço de memória do objeto original
print('endereço de deep_copy = ',id(deep_copy))      # Endereço de memória da cópia profunda (diferente)
print('endereço de original[0] = ',id(original[0]))    # Endereço da primeira sublista original
print('endereço de deep_copy[0] = ',id(deep_copy[0]))   # Endereço da primeira sublista na cópia (diferente)

"""
Pythônico

Uma forma de escrever
"""

# Nomes que não ajudam
def p(a):
    i = 0
    while i < len(a):
        if a[i] != a[len(a) - i - 1]:
            return False
        i = i + 1
    return True
        
# Nomes que ajudam a entender intuitivamente o problema
def eh_palindromo(palavra):
    letra = 0
    while letra < len(palavra):
        if palavra[letra] != palavra[len(palavra) - letra - 1]:
            return False
        letra = letra + 1
    return True

# Exercícios
lista1 = ["carro", "barco"]
lista2 = [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]]
lista3 = ["carro", "barco", "carro", "barco", "carro", "barco"]
lista1[1] = "metrô"

print(lista1)
print(lista2)
print(lista3)

print('próxima lista')
lista1 = ["carro", "barco"]
lista2 = [lista1] * 3
lista3 = lista1 * 3
lista1[1] = "metrô"

print(lista1)
print(lista2)
print(lista3)