class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Lista:

    def __init__(self):
        self.inicio = None
        # self.fim = None #PROIBIDO!!!!

    def inserir_inicio(self, valor=''):
        novoNo = No(valor)
        novoNo.proximo = self.inicio
        self.inicio = novoNo

    def remover_inicio(self):
        if self.inicio is None:
            print('Erro')
        else:
            self.inicio = self.inicio.proximo

    def inserir_final(self, valor):
        novoNo = No(valor)
        if self.inicio is None:
            self.inicio = novoNo
        else:
            auxiliar = self.inicio
            while auxiliar.proximo is not None:
                auxiliar = auxiliar.proximo
            auxiliar.proximo = novoNo

    def remover_final(self):
        if self.inicio is None:
            print('Vazio')
        else:
            if self.inicio.proximo is None:
                self.inicio = None
            else:
                auxiliar = self.inicio
                while auxiliar.proximo.proximo is not None:
                    auxiliar = auxiliar.proximo
                auxiliar.proximo = None

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

    def inserir_na_posicao(self, posicao, valor):
        novoNo = No(valor)
        if posicao == 0:
            self.inserir_inicio(valor)
        else:
            contador = 1
            auxiliar = self.inicio
            while auxiliar is not None:
                if contador == posicao:
                    novoNo.proximo = auxiliar.proximo
                    auxiliar.proximo = novoNo
                    return
                contador += 1
                auxiliar = auxiliar.proximo
        self.inserir_final(valor)

    def remover_da_posicao(self, posicao):
        if posicao == 0:
            if self.inicio is not None:
                self.remover_inicio()
            else:
                print('Erro')
        else:
            contador = 1
            auxiliar = self.inicio
            while auxiliar.proximo is not None:
                if contador == posicao:
                    auxiliar.proximo = auxiliar.proximo.proximo
                contador += 1
                auxiliar = auxiliar.proximo

    def imprimir_da_posicao(self, posicao):
        if posicao == 0:
            if self.inicio is not None:
                print(self.inicio.dado)
            else:
                print('Vazio')
        else:
            contador = 1
            auxiliar = self.inicio
            while auxiliar.proximo is not None:
                auxiliar = auxiliar.proximo

                if contador == posicao:
                    print(auxiliar.dado)
                    return
                contador += 1


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
