###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Palavras 3.0
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################

lpos = [-1, -1, -1, 0, 0, 1, 1, 1]
cpos = [-1, 0, 1, -1, 1, -1, 0, 1]

def rec_busca(matriz, linha, coluna, palavra, index, answer, posicoes):

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    # Se estourarmos o indice ou se o elemento atual não for
    # igual ao caracter procurado na palavra
    palavra_size = len(palavra) - 1
    if (index > palavra_size or matriz[linha][coluna] != palavra[index]):
        return 

    # Adiciona a posição atual a resposta
    coord = "(" + str(linha + 1) + ", " + str(coluna + 1) + ")"
    answer.append(coord)

    # Se estivermos no ultimo caracter, formamos a palavra buscada
    if (index == palavra_size):
        #print(answer)
        posicoes.append(answer[0])
        return

    # Para os demais casos, chamamos rec_busca recursivamente
    # olhando os elementos ao redor, nas oito possibilidades
    for i in range(8):
        # Verificamos se os novos indices a serem procurados são possíveis
        if (linha + lpos[i] >= 0 and linha + lpos[i] < num_linhas):         # vertical
            if (coluna + cpos[i] >= 0 and coluna + cpos[i] < num_colunas):  # horizontal
                rec_busca(matriz, linha + lpos[i], coluna + cpos[i], palavra, index + 1, answer, posicoes)

    return


"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada em todas as direções (norte, sul, leste, oeste,
nordeste, sudeste, noroeste e sudoeste) a partir da posição inicial.

Caso a palavra seja encontrada a partir da posição inicial a função
deve retornar o valor True. Caso contrário, a função de retornar o
valor False.
"""
def busca_palavra(matriz, linha, coluna, palavra):
    posicoes = [] 
    # Primeiro caracter da palavra na matriz encontrado
    if (matriz[linha][coluna] == palavra[0]):
        rec_busca(matriz, linha, coluna, palavra, 0, [], posicoes)
    return posicoes


# Leitura da matriz

matriz = []
linha = input() # Le a primeira linha do input = primeira linha da matriz

while(linha.isdigit() == False): # Enquanto não foi lido N
  matriz.append(linha.split())   # Preenchemos as demais linhas da matriz
  linha = input()                # E continuamos a leitura das linhas

num_linhas = len(matriz)
num_colunas = len(matriz[0])

# Leitura das palavras

palavras = []

for _ in range(int(linha)):
  palavras.append(input())


# Processamento da busca na matriz e impressão, por palavra,
# das posições iniciais (linha e coluna)
    
res = {}
   
for palavra in sorted(palavras):
    res[palavra] = []
    for i in range(num_linhas):
        for j in range(num_colunas):
            posicoes = busca_palavra(matriz, i, j, palavra)
            if (posicoes):
                res[palavra].append(posicoes[0])

print(40 * "-")
print("Lista de Palavras")
print(40 * "-")

for palavra in res:
    print("Palavra:", palavra)
    if (res[palavra]):
        print("Posicoes: ", end = '')
        print(*res[palavra])
    else:
        print("Posicoes:")
    print(40 * "-")
