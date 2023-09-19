class Lista:

    def __init__(self):
        self.minhaLista = []
        self.inicio = None
        self.fim = None

    def imprimir_tudo(self):
        if len(self.minhaLista) == 0:
            print('Vazio')
        else:
            for value in self.minhaLista:
                print(value, end=' ')

    def inserir_inicio(self):
        valor = str(input('Inserir qual valor? '))
        self.minhaLista.insert(0, valor)
        self.inicio = self.minhaLista[0]
        self.fim = self.minhaLista[len(self.minhaLista) - 1]

    def remover_inicio(self):
        if len(self.minhaLista) == 0:
            print('Erro')
        else:
            self.minhaLista.pop(0)

            if len(self.minhaLista) == 0:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.minhaLista[0]
                self.fim = self.minhaLista[len(self.minhaLista) - 1]

    def inserir_final(self):
        valor = str(input('Inserir qual valor? '))
        self.minhaLista.append(valor)
        self.inicio = self.minhaLista[0]
        self.fim = self.minhaLista[len(self.minhaLista) - 1]

    def remover_final(self):
        if len(self.minhaLista) == 0:
            print('Erro')
        else:
            self.minhaLista.pop()

            if len(self.minhaLista) == 0:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.minhaLista[0]
                self.fim = self.minhaLista[len(self.minhaLista) - 1]

    def excluir_tudo(self):
        self.minhaLista.clear()
        self.inicio = None
        self.fim = None

    def inserir_na_posicao(self):
        index = int(input('Inserir em qual posição? '))
        value = str(input('Qual o valor? '))
        self.minhaLista.insert(index, value)
        self.inicio = self.minhaLista[0]
        self.fim = self.minhaLista[len(self.minhaLista) - 1]

    def remover_da_posicao(self):
        posicao = int(input('Remover de qual posição? '))

        if posicao < 0 or posicao >= len(self.minhaLista):
            print('Posição inválida!')
        elif len(self.minhaLista) == 0:
            print('Erro')
        else:
            self.minhaLista.remove(self.minhaLista[posicao])

            if len(self.minhaLista) == 0:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.minhaLista[0]
                self.fim = self.minhaLista[len(self.minhaLista) - 1]

    def imprimir_da_posicao(self):
        posicao = int(input('Imprimir de qual posição? '))

        if posicao < 0 or posicao >= len(self.minhaLista):
            print('Posição inválida!')
        elif len(self.minhaLista) == 0:
            print('Erro')
        else:
            print(self.minhaLista[posicao])

    def calcular_determinante(self):
        for index in range(9):
            self.minhaLista.append(int(input(f'{index + 1}º posição: ')))

        linha1 = self.minhaLista[0] * self.minhaLista[4] * self.minhaLista[8]
        linha2 = self.minhaLista[1] * self.minhaLista[5] * self.minhaLista[6]
        linha3 = self.minhaLista[2] * self.minhaLista[3] * self.minhaLista[7]
        linha4 = (self.minhaLista[6] * self.minhaLista[4] * self.minhaLista[2]) * - 1
        linha5 = (self.minhaLista[7] * self.minhaLista[5] * self.minhaLista[0]) * - 1
        linha6 = (self.minhaLista[8] * self.minhaLista[3] * self.minhaLista[1]) * - 1

        print(linha1 + linha2 + linha3 + linha4 + linha5 + linha6)


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
        print("10- Calcular determinante")
        print("11- Sair")
        print("")
        print("Opção: ", end='')
        opcao = int(input())

        if opcao == 1:
            L1.inserir_inicio()

        elif opcao == 2:
            L1.remover_inicio()

        elif opcao == 3:
            L1.inserir_final()

        elif opcao == 4:
            L1.remover_final()

        elif opcao == 5:
            L1.imprimir_tudo()

        elif opcao == 6:
            L1.excluir_tudo()

        elif opcao == 7:
            L1.inserir_na_posicao()

        elif opcao == 8:
            L1.remover_da_posicao()

        elif opcao == 9:
            L1.imprimir_da_posicao()

        elif opcao == 10:
            L1.calcular_determinante()
            break

        else:
            break
    

if __name__ == "__main__":
    main()
