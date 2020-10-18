###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################

# REGRAS:
# (1) - Peça sempre na posição mais alta e mais a esquerda possivel
# (2) - Peça não pode sofrer rotação


# """
# Esta função recebe seis parâmetros:
# - tabuleiro: a configuração inicial do tabuleiro;
# - altura_tabuleiro: o valor da altura do tabuleiro;
# - largura_tabuleiro: o valor da largura do tabuleiro;
# - peca: a configuração da peça a ser inserida;
# - altura_peca: o valor da altura da peça a ser inserida;
# - largura_peca: o valor da largura da peça a ser inserida.

# A função deve retornar a configuração atualizada do tabuleiro 
# e o status do jogo ("O jogo deve continuar" ou "Fim de jogo")
# """
def verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                  peca, altura_peca, largura_peca):
	
	# Caso não seja possível inserir a peça no tabuleiro,
	# devemos retornar o tabuleiro como foi lido e o status de fim de jogo
	status_do_jogo = "Fim de jogo"

	# Primeiro 'for' aninhado percorre todos os elementos do tabuleiro
	for linha in range(altura_tabuleiro):
		for coluna in range(largura_tabuleiro):
			# Definindo se a peça já foi posicionada contando o número de acertos
			sum_acertos = 0

			# Segundo 'for' aninhado percorre todos os elementos da peça
			for peca_linha in range(altura_peca):
				for peca_coluna in range(largura_peca):

					# Checando limite vertical
					if (linha + peca_linha < altura_tabuleiro):
						# Checando limite horizontal
						if (coluna + peca_coluna < largura_tabuleiro):

							# Checando compatibilidade dos caracteres
							if (peca[peca_linha][peca_coluna] == '.'):
								if (tabuleiro[linha + peca_linha][coluna + peca_coluna] == '*'):
									sum_acertos += 1
							elif (peca[peca_linha][peca_coluna] == '#'):
								if (tabuleiro[linha + peca_linha][coluna + peca_coluna] == '.'):
									sum_acertos += 1

			# Se foi possível encaixar a peça, substituimos no tabuleiro
			if (sum_acertos == altura_peca*largura_peca): 
				for peca_linha in range(altura_peca):
					for peca_coluna in range(largura_peca):
						if (tabuleiro[linha + peca_linha][coluna + peca_coluna] != '*'):
							tabuleiro[linha + peca_linha][coluna + peca_coluna] = '#'

				# E modificamos o status do jogo
				status_do_jogo = "O jogo deve continuar"

				# E retornamos para finalizar (pois começamos do alto e da esquerda, temos a posição ideal)
				return tabuleiro, status_do_jogo

	return tabuleiro, status_do_jogo



# Leitura de dados
 
altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]

# Leitura do tabuleiro

# Dica: use a função list() para transformar uma string numa lista de caracteres

tabuleiro = []
for _ in range(altura_tabuleiro): # o caracter '_' indica que o índice não é relevante/utilizado
	tabuleiro.append(list(input()))

altura_peca, largura_peca = [int(x) for x in input().split()]
                           
# Leitura da peça

# Dica: use a função list() para transformar uma string numa lista de caracteres
peca = []
for _ in range(altura_peca):
	peca.append(list(input()))


# Impressão da configuração atualizada do tabuleiro

tabuleiro, status_do_jogo = verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                                          peca, altura_peca, largura_peca)

for linha in tabuleiro:
	print("".join(linha))


# Impressão do status do jogo
print(status_do_jogo)
