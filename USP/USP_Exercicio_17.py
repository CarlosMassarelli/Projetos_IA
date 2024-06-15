def tem_digitos_adjacentes_iguais(numero):
    """
    Exercício USP Cursera

    Verifica se o número possui ao menos um dígito com um dígito adjacente igual a ele.

    Args:
    numero (int): O número a ser verificado.

    Returns:
    bool: True se existir um dígito adjacente igual, False caso contrário.
    """
    numero_str = str(abs(numero))  # Converte o número para string e usa o valor absoluto
    for i in range(len(numero_str) - 1):
        if numero_str[i] == numero_str[i + 1]:
            return True
    return False

def main():
    try:
        numero = int(input('Digite um número inteiro: '))
        if tem_digitos_adjacentes_iguais(numero):
            print("sim")
        else:
            print("não")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
