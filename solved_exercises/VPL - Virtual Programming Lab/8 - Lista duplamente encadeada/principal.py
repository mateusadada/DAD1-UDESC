class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, valor):
        novoNo = No(valor)
        novoNo.proximo = self.inicio
        if self.inicio is None:
            self.fim = novoNo
        else:
            self.inicio.anterior = novoNo

        self.inicio = novoNo

    def remover_inicio(self):
        if self.inicio is None:
            print('Erro')
        else:
            self.inicio = self.inicio.proximo
            if self.inicio is not None:
                self.inicio.anterior = None
            else:
                self.fim = None

    def inserir_final(self, valor):
        novoNo = No(valor)
        if self.inicio is None and self.fim is None:
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo
            novoNo.proximo = None
            novoNo.anterior = self.fim
            self.fim = novoNo

    def remover_final(self):
        if self.inicio is None and self.fim is None:
            print('Vazia')
        else:
            self.fim.anterior.proximo = None
            self.fim = self.fim.proximo

    def imprimir_tudo(self):
        if self.inicio is None:
            print('Vazio')
        else:
            auxiliar = self.inicio
            while auxiliar is not None:
                print(auxiliar.dado, end=' ')
                auxiliar = auxiliar.proximo

    def excluir_tudo(self):
        self.inicio = None
        self.fim = None

    def inserir_na_posicao(self, posicao, valor):
        if self.inicio is None or posicao == 0:
            self.inserir_inicio(valor)
        else:
            atual = self.inicio
            for p in range(posicao):
                if atual is not None:
                    atual = atual.proximo
            novoNo = No(valor)
            novoNo.proximo = atual
            novoNo.anterior = atual.anterior.proximo
            atual.anterior.proximo = novoNo
            atual.anterior = novoNo

    def remover_da_posicao(self, posicao):
        if posicao == 0:
            self.remover_inicio()
        else:
            auxiliar = self.inicio
            posicao_atual = 0
            while auxiliar is not None:
                if posicao_atual == posicao:
                    auxiliar.anterior.proximo = auxiliar.proximo
                    auxiliar.proximo.anterior = auxiliar.anterior
                auxiliar = auxiliar.proximo
                posicao_atual += 1

    def imprimir_da_posicao(self, posicao):
        auxiliar = self.inicio
        posicao_atual = 0
        while auxiliar is not None:
            if posicao_atual == posicao:
                print(auxiliar.dado)
                return
            auxiliar = auxiliar.proximo
            posicao_atual += 1


def main():
    L1 = Lista()

    while True:
        print("")
        print("1- Inserir Inicio")
        print("2– Remover Inicio")
        print("3- Inserir Final")
        print("4- Remover Final")
        print("5- Imprimir Tudo")
        print("6- Excluir Tudo")
        print("7- Inserir na Posicao")
        print("8- Remover da Posicao")
        print("9- Imprimir da Posicao")
        print("10- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())

        if opcao == 1:
            L1.inserir_inicio(str(input('Digite um valor: ')))

        elif opcao == 2:
            L1.remover_inicio()

        elif opcao == 3:
            L1.inserir_final(str(input('Digite um valor: ')))

        elif opcao == 4:
            L1.remover_final()

        elif opcao == 5:
            L1.imprimir_tudo()

        elif opcao == 6:
            L1.excluir_tudo()

        elif opcao == 7:
            posicao = int(input('Digite uma posição'))
            valor = str(input('Digite um valor'))
            L1.inserir_na_posicao(posicao, valor)

        elif opcao == 8:
            L1.remover_da_posicao(int(input('Digite uma posição: ')))

        elif opcao == 9:
            L1.imprimir_da_posicao(int(input('Digite uma posição: ')))

        else:
            break


if __name__ == "__main__":
    main()
