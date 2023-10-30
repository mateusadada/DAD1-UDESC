from collections import deque


class No:
    def __init__(self, dado):
        self.dado = dado
        self.direita = None
        self.esquerda = None
        

class Arvore:
    def __init__(self):
        self.raiz = None

    def InserirDado(self, caminho, dado):
        pass

    def ProcurarDado(self, caminho, dado):
        pass

    def RemoverDado(self, caminho, dado):
        pass

    def PreOrdem(self, caminho):
        pass

    def EmOrdem(self, caminho):
        pass

    def PosOrdem(self, caminho):
        pass

    def ImprimirRaiz(self):
        pass

    def ImprimirFolhas(self, caminho):
        pass

    def ImprimirAltura(self, caminho):
        pass

    def ApagarTudo(self):
        pass

############################################################## 
    # Código para imprimir a árvore
    def print_tree(self, root):
        res = []
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    row.append("#")
                    continue
                row.append(node.dado)
                q.append(node.esquerda)
                q.append(node.direita)
            res.append(row)
        rows = len(res)
        base = 2 ** rows
        for r in range(rows):
            for v in res[r]:
                print("." * base, end="")
                print(v, end="")
                print("." * (base - 1), end="")
            print("|")
            base //= 2     
###############################################################

        
def main():
    arv = Arvore()
    
    while True:
        print("")
        print("1- Inserir número")
        print("2– Procurar número")
        print("3- Excluir número")
        print("4– Imprimir PreOrdem")
        print("5- Imprimir EmOrdem")
        print("6- Imprimir PosOrdem")
        print("7- Imprimir raiz")
        print("8- Imprimir folhas")
        print("9- Imprimir altura")
        print("10- Excluir todos os números")
        print("11- Sair")
        print("Opção: ")
        opcao = int(input())

        if opcao == 1:
            arv.raiz = arv.InserirDado(arv.raiz, int(input("Digite: ")))

        elif opcao == 2:
            arv.ProcurarDado(arv.raiz, int(input("Digite: ")))

        elif opcao == 3:
            arv.RemoverDado(arv.raiz, int(input("Digite: ")))

        elif opcao == 4:
            arv.PreOrdem(arv.raiz)

        elif opcao == 5:
            arv.EmOrdem(arv.raiz)

        elif opcao == 6:
            arv.PosOrdem(arv.raiz)

        elif opcao == 7:
            arv.ImprimirRaiz()

        elif opcao == 8:
            arv.ImprimirFolhas(arv.raiz)

        elif opcao == 9:
            print(arv.ImprimirAltura(arv.raiz))

        elif opcao == 10:
            arv.ApagarTudo()

        else:
            arv.print_tree(arv.raiz)
            break
    
    
if __name__ == "__main__":
    main()
    