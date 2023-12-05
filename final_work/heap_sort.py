# Código adaptado de https://brilliant.org/wiki/heap-sort/
# Modificações: alterado os nomes das variáveis para o PT-BR; adicionado "PRINTs" para mostrar o processo;
# incluído observações.

# terciário
def max_heapify(arvore, heap_tamanho, i):
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    maior = i
    if esquerda < heap_tamanho and arvore[esquerda] > arvore[maior]:
        maior = esquerda

    if direita < heap_tamanho and arvore[direita] > arvore[maior]:
        maior = direita

    if maior != i:
        arvore[i], arvore[maior] = arvore[maior], arvore[i]
        max_heapify(arvore, heap_tamanho, maior)


# secundário
def construir_heap(arvore):
    heap_tamanho = len(arvore)
    for i in range(heap_tamanho, -1, -1):
        max_heapify(arvore, heap_tamanho, i)


# principal
def heapsort(arvore):
    heap_tamanho = len(arvore)
    construir_heap(arvore)
    print(f'Árvore organizada: \033[33m{arvore}\033[m\n')  # árvore organizada antes de ordenar
    for i in range(heap_tamanho - 1, 0, -1):
        arvore[0], arvore[i] = arvore[i], arvore[0]
        heap_tamanho -= 1
        max_heapify(arvore, heap_tamanho, 0)


Lista = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]
print(f'Lista: \033[33m{Lista}\033[m\n')  # antes de ordenar
heapsort(Lista)
print(f'Lista final: \033[33m{Lista}\033[m')  # depois de ordenar
