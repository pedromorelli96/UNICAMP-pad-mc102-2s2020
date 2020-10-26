###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Palavras 3.0
# Nome: 
# RA: 
###################################################

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

# Leitura da matriz

matriz = []



# Leitura das palavras

palavras = []



# Processamento da busca na matriz e impressão, por palavra,
# das posições iniciais (linha e coluna)

print(40 * "-")
print("Lista de Palavras")
print(40 * "-")


print("Palavra:", palavra)
print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())
print(40 * "-")
