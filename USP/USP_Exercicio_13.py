def fatorial(n):
    """
    Exercício USP Cursera

    Calcula o fatorial de um número natural n.

    Args:
    n (int): Um número natural.

    Returns:
    int: O fatorial de n.
    """
    # abordagem recursiva > tempo e limitado pelas chamadas < complexidade
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
# abordagem iterativa < tempo e ilimitado >complexidade
'''
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

'''
def main():
    try:
        n = int(input('Digite o valor de n: '))
        if n < 0:
            print("Por favor, insira um número natural (não-negativo).")
        else:
            resultado = fatorial(n)
            print(resultado)
#            print(f'O fatorial de {n} é {resultado}.')

    except ValueError:
        print("Por favor, insira um número natural válido.")

if __name__ == "__main__":
    main()
