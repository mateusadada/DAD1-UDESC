def main():
    
    while True:
        print("")
        print("1–  Imprima como saída do programa a frase: 'Olá, Mundo!'")
        print("2–  Leia e imprima seu primeiro nome.")
        print("3–  Leia dois números inteiros.")
        print("4–  Leia dois números inteiros e imprima como saída a soma deles.")
        print("5–  Leia dois números inteiros e imprima apenas o maior.")
        print("6–  Leia um número inteiro e imprima como saída do programa 'PAR' se o número for par e 'ÍMPAR' se o "
              "número for ímpar. ")
        print("7–  Imprima como saída todos os números pares de 0 (zero) até 200 (duzentos).")
        print("8–  Imprima as raízes reais de uma equação de segundo, na forma ax² + bx + c.")
        print("9–  Leia um número inteiro positivo e informe se é um número primo ou não.")
        print("10– Leia um número inteiro (menor de 10 de preferência)  e imprima o cálculo final do seu fatorial.")
        print("11– Leia uma palavra e informe a sua quantidade de caracteres.")
        print("12– Leia um numero inteiro positivo e imprima como saída do programa o seu reverso.")
        print("13– Leia 3 (três) números inteiros positivos e informe se um triângulo construído com essas medidas "
              "seria: Equilátero, Isósceles ou Escaleno.")
        print("14– Leia um número inteiro entre um (1) e dez (10) e gere sua tabuada")
        print("15– Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        
        if opcao == 1:
            print('Olá, Mundo!')
            break

        elif opcao == 2:
            nome = str(input('Digite seu primeiro nome: '))
            print(nome)
            break

        elif opcao == 3:
            numero1 = int(input('Digite um número inteiro: '))
            numero2 = int(input('Digite um número inteiro: '))
            print(numero1, numero2)
            break

        elif opcao == 4:
            numero1 = int(input('Digite um número inteiro: '))
            numero2 = int(input('Digite um número inteiro: '))
            print(numero1 + numero2)
            break

        elif opcao == 5:
            numero1 = int(input('\nDigite um número inteiro: '))
            numero2 = int(input('Digite um número inteiro: '))
            lista = [numero1, numero2]

            print(max(lista))
            break

        elif opcao == 6:
            numero = int(input('Digite um número inteiro: '))

            if numero % 2 == 0:
                print('PAR')
            else:
                print('ÍMPAR')
            break

        elif opcao == 7:
            for value in range(0, 200, 2):
                print(value, end=' ')
            break

        elif opcao == 8:
            a = float(input('a: '))
            b = float(input('b: '))
            c = float(input('c: '))

            raiz1 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
            raiz2 = (- b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

            if raiz1 == raiz2:
                print(int(raiz1))
            else:
                print(int(raiz1), int(raiz2))
            break

        elif opcao == 9:
            numero = int(input('Digite um número inteiro positivo: '))
            contador = 0

            for index in range(numero, 0, -1):
                if numero % index == 0:
                    contador += 1

            if contador > 2 or contador == 0:
                print('NÃO')
            else:
                print('SIM')
            break

        elif opcao == 10:
            numero = int(input('Digite um número inteiro (menor de 10): '))
            total_fatorial = 1

            for index in range(numero, 0, -1):
                total_fatorial *= index
            print(total_fatorial)
            break

        elif opcao == 11:
            palavra = str(input('Digite uma palavra: '))

            print(len(palavra))
            break

        elif opcao == 12:
            numero = input('Digite um número inteiro positivo: ')

            print(numero[::-1])
            break

        elif opcao == 13:
            lado1 = int(input('Digite um número inteiro positivo: '))
            lado2 = int(input('Digite um número inteiro positivo: '))
            lado3 = int(input('Digite um número inteiro positivo: '))

            if lado1 == lado2 == lado3:
                print('Equilátero')
            elif lado1 != lado2 != lado3 != lado1:
                print('Escaleno')
            else:
                print('Isósceles')
            break

        elif opcao == 14:
            numero = int(input('Digite um número (1 a 10): '))

            for value in range(1, 11):
                print(f'{numero} X {value} = {numero * value}')
            break

        else:
            break


if __name__ == "__main__":
    main()
