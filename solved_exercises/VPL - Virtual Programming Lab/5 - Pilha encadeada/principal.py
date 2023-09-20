# 1- Incluir uma nova letra na pilha (não imprimir nada)
# 2- Excluir a letra do topo da pilha (ou em caso de pilha vazia, imprimir "Erro")
# 3- Imprimir a letra do topo da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
# 4- Imprimir todas as letras da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
# 5- Excluir todas as letras da pilha (não imprimir nada)


class No:

    def __init__(self, dado):
        self.dado = dado
        self.anterior = None


class Pilha:

    def __init__(self):
        self.topo = None

    def empilhar(self, valor):
        novoNo = No(valor)
        novoNo.anterior = self.topo
        self.topo = novoNo

    def imprimir_tudo(self):
        if self.topo is None:
            print('Vazio')
        else:
            auxiliar = self.topo
            while auxiliar is not None:
                print(auxiliar.dado)
                auxiliar = auxiliar.anterior

    def imprimir_topo(self):
        if self.topo is None:
            print('Vazio')
        else:
            print(self.topo.dado)

    def desempilhar(self):
        if self.topo is None:
            print('Erro')
        else:
            self.topo = self.topo.anterior

    def apagar_tudo(self):
        while self.topo is not None:
            self.topo = self.topo.anterior


def main():
    
    p1 = Pilha()
    
    while True:
        # opcao = int(input("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: "))
        # print("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: ")
        print("")
        print("1- Empilhar")
        print("2– Desempilhar")
        print("3- Imprimir topo")
        print("4- Imprimir tudo")
        print("5- Excluir tudo")
        print("5- Sair")
        print("Opção: ", end='')
        opcao = int(input())
        print("")

        if opcao == 1:
            p1.empilhar(str(input('Digite um valor: ')))

        elif opcao == 2:
            p1.desempilhar()

        elif opcao == 3:
            p1.imprimir_topo()

        elif opcao == 4:
            p1.imprimir_tudo()

        elif opcao == 5:
            p1.apagar_tudo()

        else:
            break
    

if __name__ == "__main__":
    main()
