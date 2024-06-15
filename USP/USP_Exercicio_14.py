def imprime_n_impares(n):
    """
    Exercício USP Cursera

    Imprime os n primeiros números ímpares naturais.

    Args:
    n (int): A quantidade de números ímpares a ser impressa.
    """
    count = 0
    num = 1
    while count < n:
        print(num)
        num += 2
        count += 1

def main():
    try:
        n = int(input('Digite o valor de n: '))
        if n <= 0:
            print("Por favor, insira um número inteiro positivo.")
        else:
            imprime_n_impares(n)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
