###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################

# Leitura de dados
l = int(input())

linhas = []

for i in range(l):
    linhas.append(input())

n = int(input())

palavras = []

for i in range(n):
    palavras.append(input())

# Processamento do texto
pontuacoes = ".,:;!?"

for p in palavras:
    ocorrencia = 0
    similares = 0
    for l in linhas:
        cada_palavra = l.split()
        for c in cada_palavra:
            # Primeiro, remover as pontuacoes
            for char in c:
                if (char in pontuacoes):
                    c = c.replace(char, "")
            # Agora, verificar se é ocorrencia ou similar
            if (c.lower() == p.lower()):
                ocorrencia += 1
            elif (p.lower() in c.lower()):
                similares += 1

    # Saída de dados
    print("Palavra buscada:", p)
    print("Ocorrencia:", ocorrencia)
    print("Palavras similares:", similares)




