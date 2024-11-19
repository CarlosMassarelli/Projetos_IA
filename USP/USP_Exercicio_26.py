"""
USP
Soma hipotenusa (soma as hipotenusas de um inteiro entre um e o um número dado)...

# Exemplos de uso
print(soma_hipotenusas(25))  # Saída: 105
"""

def e_hipotenusa(h):
    """Verifica se um número é a hipotenusa de um triângulo retângulo."""
    for i in range(1, h):
        for j in range(i, h):  # Para evitar duplicação, começamos j em i
            if i**2 + j**2 == h**2:
                #print ('valor i =',i)
                #print ('valor j =',j)
                #print ('valor h =',h)
                return True
    return False

def soma_hipotenusas(n):
    """Calcula a soma de todas as hipotenusas entre 1 e n."""
    soma = 0
    for h in range(1, n + 1):
        if e_hipotenusa(h):
            soma += h
            #print('valor soma =',soma)

    return soma


