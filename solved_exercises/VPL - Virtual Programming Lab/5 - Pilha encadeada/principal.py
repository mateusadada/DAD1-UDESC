#1- Incluir uma nova letra na pilha (não imprimir nada)
#2- Excluir a letra do topo da pilha (ou em caso de pilha vazia, imprimir "Erro")
#3- Imprimir a letra do topo da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
#4- Imprimir todas as letras da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
#5- Excluir todas as letras da pilha (não imprimir nada)


class No:

    def __init__(self, dado):
        self.dado = dado
        self.anterior = None

class Pilha:

    def __init__(self):
        self.minhaPilha = None
        self.topo = None


def main():
    
    p1 = Pilha()
    
    while True:
        #opcao = int(input("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: "))
        #print("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: ")
        print("")
        print("1- Empilhar")
        print("2– Desempilhar")
        print("3- Imprimir topo")
        print("4- Imprimir tudo")
        print("5- Excluir tudo")
        print("5- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        else:
            break
    

if __name__ == "__main__":
    main()