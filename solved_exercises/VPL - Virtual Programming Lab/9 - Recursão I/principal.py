def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


def main():
    numero = int(input('Digite um número: '))

    resultado = fibonacci(numero)
    
    print('Resultado: ', resultado)


if __name__ == '__main__':
    main()
