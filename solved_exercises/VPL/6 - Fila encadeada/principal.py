class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, valor):
        novoNo = No(valor)
        if self.inicio is None:
            self.inicio = novoNo
        else:
            self.fim.proximo = novoNo

        self.fim = novoNo

    def desenfileirar(self):
        if self.inicio is None:
            print('Erro')
        else:
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = self.inicio

    def imprimir_inicio(self):
        if self.inicio is None:
            print('Vazio')
        else:
            print(self.inicio.dado)

    def imprimir_fim(self):
        if self.fim is None:
            print('Vazio')
        else:
            print(self.fim.dado)

    def imprimir_tudo(self):
        if self.inicio is None and self.fim is None:
            print('Vazio')
        else:
            auxiliar = self.inicio
            while auxiliar is not None:
                print(auxiliar.dado, end=' ')
                auxiliar = auxiliar.proximo

    def excluir_tudo(self):
        while self.inicio is not None:
            self.inicio = self.inicio.proximo
        self.fim = self.inicio


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
        print("Opção: ")
        opcao = int(input())

        if opcao == 1:
            f1.enfileirar(str(input('Digite um valor para enfileirar: ')))

        elif opcao == 2:
            f1.desenfileirar()

        elif opcao == 3:
            f1.imprimir_inicio()

        elif opcao == 4:
            f1.imprimir_fim()

        elif opcao == 5:
            f1.imprimir_tudo()

        elif opcao == 6:
            f1.excluir_tudo()

        else:
            break
    

if __name__ == "__main__":
    main()
