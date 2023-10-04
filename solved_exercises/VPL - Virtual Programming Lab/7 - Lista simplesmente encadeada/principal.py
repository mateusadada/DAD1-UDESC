class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Lista:

    def __init__(self):
        self.inicio = None
        # self.fim = None #PROIBIDO!!!!

    def inserir_inicio(self, valor):
        pass

    def remover_inicio(self):
        pass

    def inserir_final(self, valor):
        pass

    def remover_final(self):
        pass

    def imprimir_tudo(self):
        pass

    def excluir_tudo(self):
        pass

    def inserir_na_posicao(self, posicao, valor):
        pass

    def remover_da_posicao(self, posicao):
        pass

    def imprimir_da_posicao(self, posicao):
        pass


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
        print("7- Inserir na Posicao") #
        print("8- Remover da Posicao") #
        print("9- Imprimir da Posicao") #
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
            pass

        elif opcao == 8:
            pass

        elif opcao == 9:
            pass

        else:
            break
    

if __name__ == "__main__":
    main()
