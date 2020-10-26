###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Filtros de Imagens
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################


'''
Função que recebe uma imagem e imprime essa imagem no formato PGM
'''
def imprime_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))

'''
Função que retorna a mediana de uma lista. Se o tamanho da lista
for par, a função retorna a parte inteira da média entre os elementos
centrais
'''
def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        #retorna a parte inteira da média entre os elementos centrais
        return (lista_ordenada[elemento_central-1] + lista_ordenada[elemento_central]) // 2

''' 
Função que recebe a matriz que representa a imagem original e
retorna a imagem resultante da aplicação do filtro negativo 
'''
def filtro_negativo(imagem):

    # For aninhado percorrendo cada elemento da matriz
    for i in range(len(imagem)):
        for j in range(len(imagem[i])):
            imagem[i][j] = 255 - imagem[i][j]

    return imagem

'''
Função que recebe a matriz que representa a imagem original e 
retorna a imagem resultante da aplicação do filtro da mediana
'''
def filtro_mediana(imagem):

    # Inicializando a matriz (imagem) de retorno com apenas zeros
    imagem_filtrada = []
    for i in range(len(imagem)):
        linha = [0] * len(imagem[i])
        imagem_filtrada.append(linha)

    # For aninhado percorrendo cada elemento da matriz
    for i in range(len(imagem)):
        for j in range(len(imagem[i])):
            mascara = []
            #print("---------")
            #print(f"i: {i}, j: {j}")

            # For aninhado percorrendo os elementos ao redor de cada elemento da matriz
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    # If aninhado para verificar se estamos nos limites permitidos pela matriz
                    if (x >= 0 and x < len(imagem)):
                        if (y >= 0 and y < len(imagem[i])):
                            # Preenchemos a lista com os (possiveis) elementos ao redor do elemento atual 
                            mascara.append(imagem[x][y])
            
            # Chamamos a funcao mediana para calcular a mediana do elemento atual
            mdn = mediana(mascara)
            #print(mdn)

            # Substituimos o pixel pelo valor da mediana
            imagem_filtrada[i][j] = mdn       

    return imagem_filtrada

'''
Função que recebe três parâmetros: 

imagem: matriz que representa a imagem original
M: matriz núcleo
D: divisor

Essa função retorna a imagem resultante da aplicação de um filtro 
que usa convolução
'''
def convolucao(imagem, M, D):
    # Inicializando a matriz (imagem) de retorno com apenas zeros
    imagem_filtrada = [] 

    for i in range(len(imagem)):
        linha = [0] * len(imagem[i])
        imagem_filtrada.append(linha)

    # For aninhado percorrendo cada elemento da matriz
    for i in range(len(imagem)):
        for j in range(len(imagem[i])):
            if (i == 0 or i == (len(imagem) - 1)): # Caso seja a primeira ou ultima linha faça nada
                continue
            elif (j == 0 or j == (len(imagem[i]) - 1)): # Caso seja a primeira coluna ou ultima coluna faça nada
                continue
            else: # Caso seja qualquer elemento diferente das bordas

                # Calculo dos parametros l1, l2 e l3 para cada elemento
                a, b, c = M[0][0], M[0][1], M[0][2]
                d, e, f = M[1][0], M[1][1], M[1][2]
                g, h, ii = M[2][0], M[2][1], M[2][2]

                # print(f"id atual: i: {i}, j: {j}")
                # print(imagem[i - 1][j - 1], imagem[i - 1][j], imagem[i - 1][j + 1])
                # print(imagem[i][j - 1], imagem[i][j], imagem[i][j + 1])
                # print(imagem[i + 1][j - 1], imagem[i + 1][j], imagem[i + 1][j + 1])

                l1 = a*(imagem[i - 1][j - 1]) + b*(imagem[i - 1][j]) + c*(imagem[i - 1][j + 1])
                l2 = d*(imagem[i][j - 1]) + e*(imagem[i][j]) + f*(imagem[i][j + 1])
                l3 = g*(imagem[i + 1][j - 1]) + h*(imagem[i + 1][j]) + ii*(imagem[i + 1][j + 1])
                #print(l1, l2, l3)

                # Calculo do novo pixel
                newpixel = (l1 + l2 + l3) // D
                #print(newpixel)
                # Verificando se o novo pixel está no intervalo [0, 255]
                if (newpixel < 0):
                    newpixel = 0
                elif (newpixel > 255):
                    newpixel = 255

                imagem_filtrada[i][j] = newpixel

    # Removendo as bordas da matriz
    imagem_filtrada.pop(0)
    imagem_filtrada.pop((len(imagem_filtrada) - 1))

    for i in range(len(imagem_filtrada)):
        for j in range(len(imagem_filtrada[i])):
            if (j == 0 or j == (len(imagem_filtrada[i]) - 1)):
                imagem_filtrada[i].pop(j)
                    
    return imagem_filtrada

# Leitura da entrada

filtro = input()
_ = input() # P2 (linha a ser ignorada)

m, n = [int(x) for x in input().split()]

_ = input() # 255 - linha a ser ignorada

imagem = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)

# Aplica o filtro

if filtro == "negativo":
    imagem = filtro_negativo(imagem)
elif filtro == "mediana":
    imagem = filtro_mediana(imagem)
elif filtro == "edge-detect":
    M = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    D = 1
    imagem = convolucao(imagem, M, D)
elif filtro == "blur":
    M = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    D = 9
    imagem = convolucao(imagem, M, D)
elif filtro == "sharpen":
    M = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    D = 1
    imagem = convolucao(imagem, M, D)

# Imprime a imagem gerada

imprime_imagem(imagem)
