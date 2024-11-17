"""
USP
Números primos (identifica quantos números primos tem em um número positivo)...

# Exemplos de uso
print(n_primos(2))    # Saída: 1
print(n_primos(4))    # Saída: 2
print(n_primos(121))  # Saída: 30
"""

def n_primos(n):
    def eh_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    contador = 0
    for i in range(2, n + 1):
        if eh_primo(i):
            contador += 1
    
    return contador      
