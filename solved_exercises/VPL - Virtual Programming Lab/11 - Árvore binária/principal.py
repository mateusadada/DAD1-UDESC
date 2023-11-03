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
        if caminho is None:
            caminho = No(dado)
            return caminho

        else:
            if caminho.dado < dado:
                caminho.direita = self.InserirDado(caminho.direita, dado)
                return caminho

            elif caminho.dado > dado:
                caminho.esquerda = self.InserirDado(caminho.esquerda, dado)
                return caminho

            else:
                return caminho

    def ProcurarDado(self, caminho, dado):
        if caminho is not None:
            if dado == caminho.dado:
                print(caminho.dado, end=' ')
                return caminho.dado

            if self.ProcurarDado(caminho.esquerda, dado) == 0:
                return self.ProcurarDado(caminho.direita, dado)

            else:
                return caminho.dado

        return print('0')

    def RemoverDado(self, caminho, dado):
        if caminho is None:
            print('0')
            return None

        elif caminho.dado < dado:
            caminho.direita = self.RemoverDado(caminho.direita, dado)
            return caminho

        elif caminho.dado > dado:
            caminho.esquerda = self.RemoverDado(caminho.esquerda, dado)
            return caminho

        else:
            if (caminho.direita is None) and (caminho.esquerda is None):
                return None
            else:
                return caminho

    def PreOrdem(self, caminho):
        if caminho is not None:
            print(caminho.dado, end=' ')
            self.PreOrdem(caminho.esquerda)
            self.PreOrdem(caminho.direita)

    def EmOrdem(self, caminho):
        if caminho is not None:
            self.EmOrdem(caminho.esquerda)
            print(caminho.dado, end=' ')
            self.EmOrdem(caminho.direita)

    def PosOrdem(self, caminho):
        if caminho is not None:
            self.PosOrdem(caminho.esquerda)
            self.PosOrdem(caminho.direita)
            print(caminho.dado, end=' ')

    def ImprimirRaiz(self):
        if self.raiz is None:
            print('Vazio')
        else:
            print(self.raiz.dado)

    def ImprimirFolhas(self, caminho):
        if caminho is not None:
            self.ImprimirFolhas(caminho.esquerda)
            self.ImprimirFolhas(caminho.direita)
            if (caminho.direita is None) and (caminho.esquerda is None):
                print(caminho.dado, end=' ')

    def ImprimirAltura(self, caminho):
        if caminho is None:
            return -1
        else:
            esquerda = self.ImprimirAltura(caminho.esquerda)
            direita = self.ImprimirAltura(caminho.direita)
        if esquerda > direita:
            return esquerda + 1
        else:
            return direita + 1

    def ApagarTudo(self):
        self.raiz = None

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
