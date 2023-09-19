class Fila:

    def __init__(self):
        self.minhaFila = []
        self.inicio = str
        self.fim = str

    def imprimir_tudo(self):
        return self.minhaFila

    def enfileirar(self, value):
        self.minhaFila.append(value)
        self.fim = value
        if len(self.minhaFila) == 1:
            self.inicio = value

    def desenfileirar(self):
        if len(self.minhaFila) == 0:
            return print('Erro')
        else:
            self.minhaFila.pop(0)
            if len(self.minhaFila) == 0:
                self.fim = 'Vazio'
                self.inicio = 'Vazio'
            else:
                self.inicio = self.minhaFila[0]

    def imprimir_inicio(self):
        return self.inicio

    def imprimir_fim(self):
        if len(self.minhaFila) == 0:
            return 'Vazio'
        else:
            return self.fim

    def excluir_tudo(self):
        self.minhaFila.clear()
        self.minhaFila = []
        self.inicio = 'Vazio'
        self.fim = 'Vazio'


def main():
    f1 = Fila()

    while True:
        print("")
        print("1- Enfileirar")
        print("2– Desenfileirar")
        print("3- Imprimir inicio")
        print("4- Imprimir fim")
        print("5- Imprimir tudo")
        print("6- Excluir tudo")
        print("7- Sair")
        print("")
        print("Opção: ", end='')
        opcao = int(input())

        if opcao == 1:
            f1.enfileirar(str(input('Digite o que deseja enfileirar: ')))
            pass

        elif opcao == 2:
            f1.desenfileirar()

        elif opcao == 3:
            print(f1.imprimir_inicio())

        elif opcao == 4:
            print(f1.imprimir_fim())

        elif opcao == 5:
            if len(f1.minhaFila) == 0:
                print('Vazio')
            else:
                for value in f1.imprimir_tudo():
                    print(value, end=' ')

        elif opcao == 6:
            f1.excluir_tudo()

        else:
            break


if __name__ == "__main__":
    main()
