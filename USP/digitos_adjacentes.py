def tem_digitos_adjacentes_iguais(numero):
    """
    Verifica se o número tem dois ou mais dígitos adjacentes iguais e retorna esses dígitos.

    Args:
    numero (float): O número a ser verificado.

    Returns:
    dict: Dicionário com os dígitos como chave e a quantidade de repetições como valor.
    """
    numero_str = str(numero).replace('.', '')  # Converte o número para string e remove os pontos decimais
    digitos_adjacentes = {}

    i = 0
    while i < len(numero_str) - 1:
        if numero_str[i].isdigit():
            count = 1
            while i < len(numero_str) - 1 and numero_str[i] == numero_str[i + 1]:
                count += 1
                i += 1
            if count > 1:
                if numero_str[i] in digitos_adjacentes:
                    digitos_adjacentes[numero_str[i]].append(count)
                else:
                    digitos_adjacentes[numero_str[i]] = [count]
        i += 1

    return digitos_adjacentes

def main():
    try:
        numero = input('Digite um número (inteiro ou float): ')  # Recebe a entrada como string
        numero_float = float(numero)  # Valida a entrada como um número
        digitos_adjacentes = tem_digitos_adjacentes_iguais(numero)

        if digitos_adjacentes:
            print('O número possui os seguintes dígitos adjacentes iguais:')
            for digito in sorted(digitos_adjacentes):
                for count in sorted(digitos_adjacentes[digito]):
                    print(f'{count} --> {digito}')
        else:
            print('O número não possui dígitos adjacentes iguais.')
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
