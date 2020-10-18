###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################


# TRÊS SEÇÕES PARA CADA FUNÇÃO
# (1) - Percorrer os caracteres da palavra buscada, condicionando ao limite da linha ou da coluna 
# (2) - Comparar os caracteres da palavra buscada com os caracteres da matriz, sejam maiusculos, minusculos ou '*'
# (3) - Se a palavra for encontrada, modificar cada caracter (com auxiliar) para maisculo


# """
# Esta função recebe como parâmetro uma matriz, uma posição inicial na
# matriz determinada pelos parâmetros linha e coluna e uma palavra que
# deve ser buscada na horizontal (da direita para esquerda) a partir da
# posição inicial.  Caso a palavra seja encontrada a partir da posição
# inicial a função deve transformar todas as letras da palavra em
# maiúsculas e retornar o valor True. Caso contrário, a função deve
# retornar o valor False.
# """

def horizontal(matriz, linha, coluna, palavra):
  sum_acertos = 0 # Contador de caracteres corretos

  for i in range(len(palavra)): # Percorremos o tamanho da palavra buscada
    if (coluna + i < len(matriz[linha])): # Como estamos na horizontal, não podemos extrapolar o tamanho da linha = matriz[linha]
      # Se o caracter na linha for igual (ou coringa '*') ao caracter na palavra, somamos aos acertos
      # Precisamos comparar o caracter da palavra com ocorrencias minusculas e maiusculas pois cada função pode modificar a matriz
      if (matriz[linha][coluna + i] == palavra[i] or matriz[linha][coluna + i] == palavra[i].upper()): 
        sum_acertos += 1
      elif (matriz[linha][coluna + i] == '*'):
        sum_acertos += 1
  
  if (sum_acertos == len(palavra)): # Se encontramos a palavra
    for i in range(len(palavra)):
      maisculo = matriz[linha][coluna + i].upper() # Criamos caracteres auxiliares para torná-los maiúsculos e substituimos o caracter original
      matriz[linha][coluna + i] = maisculo     
    return True
  else:
    return False


# """
# Esta função recebe como parâmetro uma matriz, uma posição inicial na
# matriz determinada pelos parâmetros linha e coluna e uma palavra que
# deve ser buscada na vertical (de cima para baixo) a partir da posição
# inicial.  Caso a palavra seja encontrada a partir da posição inicial a
# função deve transformar todas as letras da palavra em maiúsculas e
# retornar o valor True. Caso contrário, a função deve retornar o valor
# False.
# """
def vertical(matriz, linha, coluna, palavra):
  sum_acertos = 0

  for i in range(len(palavra)):
    if (linha + i < len(matriz)): # Aqui, a diferença pra horizontal se da no limite do tamanho da coluna = len(matriz) = numero de linhas
      # Precisamos comparar o caracter da palavra com ocorrencias minusculas e maiusculas pois cada função pode modificar a matriz
      if (matriz[linha + i][coluna] == palavra[i] or matriz[linha + i][coluna] == palavra[i].upper()):
        sum_acertos += 1
      elif (matriz[linha + i][coluna] == '*'):
        sum_acertos += 1
  
  if (sum_acertos == len(palavra)):
    for i in range(len(palavra)):
      maisculo = matriz[linha + i][coluna].upper()
      matriz[linha + i][coluna] = maisculo     
    return True
  else:
    return False


# """
# Esta função recebe como parâmetro uma matriz, uma posição inicial na
# matriz determinada pelos parâmetros linha e coluna e uma palavra que
# deve ser buscada na diagonal (no sentido inferior direito) a partir da
# posição inicial.  Caso a palavra seja encontrada a partir da posição
# inicial a função deve transformar todas as letras da palavra em
# maiúsculas e retornar o valor True. Caso contrário, a função deve
# retornar o valor False.
# """
def diagonal1(matriz, linha, coluna, palavra):
  sum_acertos = 0

  for i in range(len(palavra)):
    # Precisamos observar dois limites aqui:
    # Horizontal => coluna + i < len(matriz[linha])
    # Vertical (de baixo para cima, portanto o 'teto' é zero) => len(matriz) - i >= 0
    if ((coluna + i < len(matriz[linha])) and (len(matriz) - i >= 0)): 
      # Precisamos comparar o caracter da palavra com ocorrencias minusculas e maiusculas pois cada função pode modificar a matriz
      if (matriz[linha - i][coluna + i] == palavra[i] or matriz[linha - i][coluna + i] == palavra[i].upper()):
        sum_acertos += 1
      elif (matriz[linha - i][coluna + i] == '*'):
        sum_acertos += 1

  if (sum_acertos == len(palavra)):
    for i in range(len(palavra)):
      maisculo = matriz[linha - i][coluna + i].upper()
      matriz[linha - i][coluna + i] = maisculo     
    return True
  else:
    return False

# """
# Esta função recebe como parâmetro uma matriz, uma posição inicial
# na matriz determinada pelos parâmetros linha e coluna e uma palavra
# que deve ser buscada na diagonal (sentido superior direito) a partir
# da posição inicial.  Caso a palavra seja encontrada a partir da
# posição inicial a função deve transformar todas as letras da palavra
# em maiúsculas e retornar o valor True. Caso contrário, a função deve
# retornar o valor False.

# """
def diagonal2(matriz, linha, coluna, palavra):
  sum_acertos = 0

  for i in range(len(palavra)):
    # Precisamos observar dois limites aqui:
    # Horizontal => coluna + i < len(matriz[linha])
    # Vertical (de cima para baixo, portanto o 'piso' é o numero de linhas) => linha + i < len(matriz)
    if ((coluna + i < len(matriz[linha])) and (linha + i < len(matriz))):
      # Precisamos comparar o caracter da palavra com ocorrencias minusculas e maiusculas pois cada função pode modificar a matriz
      if (matriz[linha + i][coluna + i] == palavra[i] or matriz[linha + i][coluna + i] == palavra[i].upper()):
        sum_acertos += 1
      elif (matriz[linha + i][coluna + i] == '*'):
        sum_acertos += 1

  if (sum_acertos == len(palavra)):
    for i in range(len(palavra)):
      maisculo = matriz[linha + i][coluna + i].upper()
      matriz[linha + i][coluna + i] = maisculo     
    return True
  else:
    return False



# Leitura da matriz

matriz = []
linha = input() # Le a primeira linha do input = primeira linha da matriz

# Dica: use linha.isdigit(), linha.split() e matriz.append()
# para processar a entrada e armazenar a matriz de caracteres

while(linha.isdigit() == False): # Enquanto não foi lido N
  matriz.append(linha.split())   # Preenchemos as demais linhas da matriz
  linha = input()                # E continuamos a leitura das linhas

# Leitura e processamento das palavras

palavras = {} # Dicionario para associar cada palavra buscada com seu numero de ocorrencias

for i in range(int(linha)):
  palavras[input()] = 0     # Leitura da palavra e iniciando um contador de ocorrencias no dicionario


# Processamento
for palavra in palavras:  # Para cada palavra na lista a ser buscada
  for linha in range(len(matriz)): # Cada linha                           // len(matriz) = numero de linhas
    for coluna in range(len(matriz[linha])): # Cada coluna em cada linha //  len(matriz[linha]) = numero de caracteres por linha
      # Chamada das funções
      if (horizontal(matriz, linha, coluna, palavra)):
        palavras[palavra] += 1
      if (vertical(matriz, linha, coluna, palavra)):
        palavras[palavra] += 1
      if (diagonal1(matriz, linha, coluna, palavra)):
        palavras[palavra] += 1
      if (diagonal2(matriz, linha, coluna, palavra)):
        palavras[palavra] += 1


print("-" * 40)
print("Lista de Palavras")
print("-" * 40)

for palavra in palavras:
  ocorrencias = palavras[palavra]
  print("Palavra:", palavra)
  print("Ocorrencias:", ocorrencias)
  print("-" * 40)

# Impressão da matriz

for linha in matriz:
  print(" ".join(linha))