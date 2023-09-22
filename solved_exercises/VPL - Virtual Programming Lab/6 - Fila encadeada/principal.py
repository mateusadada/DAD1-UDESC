class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

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
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            pass
        else:
            break
    

if __name__ == "__main__":
    main()