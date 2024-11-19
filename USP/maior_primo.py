def e_primo(k):
    """
    Exercício USP Cursera

    verifica se um número é primo

    Args:
    k (int): O número a ser verificado.

    Returns:
    retorna True/False.
    """
    if k < 2:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

def maior_primo(n):
    """
    Exercício USP Cursera

    tras o maior primo

    Args:
    n (int): O número a ser verificado.

    Returns:
    retorna o número.
    """
    for num in range(n, 1, -1):
        if e_primo(num):
            return num
        
