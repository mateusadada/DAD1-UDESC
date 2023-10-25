def mdc(numero_1, numero_2, comum):
    if numero_1 % comum == 0 and numero_2 % comum == 0:
        return comum
    else:
        return mdc(numero_1, numero_2, comum - 1)


def main():
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite um número: '))

    resultado = mdc(numero_1, numero_2, numero_2)
    
    print('Resultado: ', resultado)


if __name__ == '__main__':
    main()
