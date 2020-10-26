###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Tabela de Vendas
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################

# O algoritmo do Insertion Sort abaixo foi modificado para que
# a comparação por chaves aconteça numa pseudo-lista, de forma que
# fixamos a coluna e percorremos as linhas. 
# A chave a ser comparada a cada iteração é sempre um elemento unico,
# todavia, na hora da inserção da chave, transpomos toda sua respectiva linha.
def insertionSort(lista, coluna, n):
        for i in range(1, n): 
                chave = lista[i][coluna] # Elemento da 'lista' a ser usado como referência para as comparações
                linha = lista[i] # Linha completa atrelada ao elemento que está sendo comparado
                
                j = i - 1
                while j >= 0 and chave < lista[j][coluna]: # Compara-se apenas o elemento chave
                        lista[j + 1] = lista[j] # Mas modifica-se toda a respectiva linha
                        j -= 1
                lista[j + 1] = linha # Insere toda a respectiva linha do elemento no final do laço


# Leitura de dados

n = int(input())

# Leitura do cabeçalho separado dos dados
cabecalho = [x for x in input().split(',')]

dados = []
for i in range(n):
        linha = [x for x in input().split(',')]
        dados.append(linha)

# Conversao dos numeros para inteiros
for i in range(n):
        for j in range(len(dados[i])):
                if (j != 0):
                        dados[i][j] = int(dados[i][j])
                

prioridade = [x for x in input().split()]

# Ordenação dos dados

for p in reversed(prioridade): # É importante realizar os ordenamentos do menos prioritário pro mais prioritário
        if (p == "Produto"):
                insertionSort(dados, 0, n)
        elif (p == "Setembro"):
                insertionSort(dados, 1, n)
        elif (p == "Outubro"):
                insertionSort(dados, 2, n)
        elif (p == "Novembro"):
                insertionSort(dados, 3, n)

# Saída dos dados
print('{:15s}'.format(cabecalho[0]), ''.join('{:>10}'.format(item) for item in cabecalho[1:]))
for linha in dados:
        print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))
