class Pilha:
    minhaPilha = None
    topo = None

    def __init__(self):
        self.minhaPilha = list()
        self.topo = str

    def infixo_prefixo(self, expressao):
        expressao = expressao.split(" ")

        PilhaOperadores = []
        PilhaNumeros = []

        while len(expressao) != 0:
            PilhaNumeros.append(expressao.pop())
            if len(expressao) == 0:
                break
            PilhaOperadores.append(expressao.pop())

        while len(PilhaNumeros) != 0:
            PilhaOperadores.append(PilhaNumeros.pop())

        for i in PilhaOperadores:
            print(i, end=' ')

    def Infixo_Posfixo(self, expressao):
        expressao = expressao.split(' ')
        PilhaOperador = []
        PilhaNumeros = []
        Resultados = []

        while len(expressao) != 0:
            PilhaNumeros.append(expressao.pop())
            if len(expressao) == 0:
                break
            PilhaOperador.append(expressao.pop())

        Resultados.append(PilhaNumeros.pop())
        Resultados.append(PilhaNumeros.pop())
        Resultados.append(PilhaOperador.pop())

        while len(PilhaNumeros) != 0:
            Resultados.append(PilhaNumeros.pop())
            Resultados.append(PilhaOperador.pop())

        for i in Resultados:
            print(i, end=' ')

    def Calcular_Posfixo(self, expressao):
        expressao = expressao.split(' ')
        resultado = 0
        pilha = []

        while len(expressao) != 0:
            pilha.append(expressao.pop())

        numero1 = int(pilha.pop())
        numero2 = int(pilha.pop())
        operador = pilha.pop()

        if operador == '+':
            resultado = numero1 + numero2
        else:
            pass

    def calcular_prefixo(self, expressao):
        expressao = expressao.split()
        resultado = 0
        pilha_operadores_invertidos = []
        pilha_operadores = []
        pilha_numeros = []

        # separa os operadores e números em duas pilhas
        while len(expressao) > 0:
            for value in expressao[::-1]:
                if value in '+-':
                    pilha_operadores_invertidos.append(expressao.pop())
                else:
                    pilha_numeros.append(expressao.pop())

        # reorganiza a lista dos operadores
        while len(pilha_operadores_invertidos) > 0:
            pilha_operadores.append(pilha_operadores_invertidos.pop())

        # verifica se tem sinal na pilha e, se positivo, faz a conta e adiciona na pilha_numeros/resultado
        while len(pilha_operadores) > 0:
            if pilha_operadores[-1] == '+':
                resultado = int(pilha_numeros.pop()) + int(pilha_numeros.pop())
                pilha_numeros.append(resultado)
                pilha_operadores.pop()
            else:
                resultado = int(pilha_numeros.pop()) - int(pilha_numeros.pop())
                pilha_numeros.append(resultado)
                pilha_operadores.pop()

        return print(resultado)

    def calcular_posfixo(self, expressao):
        expressao = expressao.split()
        resultado = 0
        pilha_operadores = []
        pilha_numeros = []

        # separa os operadores e números em duas pilhas
        while len(expressao) > 0:
            for value in expressao[::-1]:
                if value in '+-':
                    pilha_operadores.append(expressao.pop())
                else:
                    pilha_numeros.append(expressao.pop())

        # verifica se tem sinal na pilha e, se positivo, faz a conta e adiciona na pilha_numeros/resultado
        while len(pilha_operadores) > 0:
            if pilha_operadores[-1] == '+':
                resultado = int(pilha_numeros.pop()) + int(pilha_numeros.pop())
                pilha_numeros.append(resultado)
                pilha_operadores.pop()
            else:
                resultado = int(pilha_numeros.pop()) - int(pilha_numeros.pop())
                pilha_numeros.append(resultado)
                pilha_operadores.pop()

        return print(resultado)


def main():

    p1 = Pilha()
    p2 = Pilha()

    while True:
        # opcao = int(input("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: "))
        # print("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: ")
        print("")
        print("1- Empilhar")
        print("2- Desempilhar")
        print("3- Imprimir topo")
        print("4- Imprimir tudo")
        print("5- Apagar tudo")
        print("6- Converter INFIXO para PREFIXO")
        print("7- Converter INFIXO para POSFIXO")
        print("8- Calcular INFIXO")
        print("9- Calcular PREFIXO")
        print("10- Calcular POSFIXO")
        print("11- Sair")
        print("")
        print("Opção: ", end='')
        opcao = int(input())

        if opcao == 1:
            p1.topo = str(input('Digite algo para empilhar: '))
            p1.minhaPilha.append(p1.topo)

        elif opcao == 2:
            p1.minhaPilha.pop()
            p1.topo = p1.minhaPilha[-1]

        elif opcao == 3:
            print(p1.topo)

        elif opcao == 4:
            for value in p1.minhaPilha[::-1]:
                print(value)

        elif opcao == 5:
            p1.minhaPilha.clear()
            p1.topo = str

        elif opcao == 6:
            p2.infixo_prefixo(input('Digite a expressão INFIXO: '))
            break

        elif opcao == 7:
            p2.Infixo_Posfixo(input('Digite a expressão INFIXO: '))
            break

        elif opcao == 8:
            print(eval(input('Digite a expressão: ')))
            break

        elif opcao == 9:
            p2.calcular_prefixo(str(input('Digite a expressão PREFIXO: ')))
            break

        elif opcao == 10:
            p2.calcular_posfixo(str(input('Digite a expressão POSFIXO: ')))
            break

        else:
            break


if __name__ == "__main__":
    main()
