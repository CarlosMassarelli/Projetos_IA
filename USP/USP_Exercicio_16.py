def eh_primo(n):
    """
    Exercício USP Cursera

    Verifica se um número é primo.

    Args:
    n (int): O número a ser verificado.

    Returns:
    bool: True se o número for primo, False caso contrário.
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def main():
    try:
        n = int(input('Digite um número inteiro: '))
        if n <= 0:
            print("Por favor, insira um número inteiro positivo.")
        else:
            if eh_primo(n):
                print("primo")
            else:
                print("não primo")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
