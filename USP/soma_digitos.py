def soma_dos_digitos(numero):
    """
    Calcula a soma dos dígitos de um número inteiro.
    
    Args:
    numero (int): O número do qual queremos calcular a soma dos dígitos.
    
    Returns:
    int: A soma dos dígitos do número.
    """
    total = 0
    while numero > 0:
        digito = numero % 10
        total += digito
        numero //= 10
    return total

def main():
    print('Vamos calcular a soma dos dígitos de um número inteiro qualquer!')
    try:
        numero = int(input('Digite um número inteiro qualquer: '))
        resultado = soma_dos_digitos(abs(numero))  # Usa valor absoluto para lidar com números negativos
        print('A soma dos dígitos deste número é igual a:', resultado)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
    

    
    
     