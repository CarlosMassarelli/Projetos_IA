"""
    Exercício USP Cursera    
    
    Função fatorial
    
    Args:
    x e y (float): Dois números.

    Returns:
    float: A soma dos dois números

    # aprendendo sobre funções
"""

def fatorial(n):
    fat = 1
    while (n>1):
        fat = fat*n
        n=n-1
    return fat

def testa_fatorial():
    assert fatorial(0) == 1        
    print('testei antes e está ok')
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print('Não funciona para 0')
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print('Não funciona para 1')
    if fatorial(2) == 2:
        print('Funciona para 2')
    else:
        print('Não funciona para 2')

def numero_binomial(n,k):
    return fatorial(n) / (fatorial(k)*fatorial(n-k))

    
print(testa_fatorial())

print(fatorial(5))

print(numero_binomial(5,6))