###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - De salto em salto
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################

lpos = [-1, 0, 1, 0]
cpos = [0, 1, 0, -1]

def rec_caminho(tabuleiro, a, b, c, d, old_pos, possibilidades):

	# A condição de parada no caso de caminho errado é voltar no mesmo caminho
	# Por isso criamos a lista old_pos que guarda os pontos já percorridos
	pos = str(a) + str(b)
	if (pos in old_pos):
		return
	else:
		old_pos.append(pos)

	#print(f"[{tabuleiro[a][b]}]: ({a}, {b})")

	# Se chegamos no final
	if (a == c and b == d):
		possibilidades.append(True)
		return

	num_linhas = len(tabuleiro)
	num_colunas = len(tabuleiro[0])

	salto = tabuleiro[a][b]

	# Se não estamo no final, e a posição tem salto 0, é impossivel continuar
	if (salto == 0):
		return 

	# Testamos as quatro direções, vezes o tamanho do salto, verificando se é possível
	for i in range(4):
		if (a + lpos[i]*salto >= 0 and a + lpos[i]*salto < num_linhas):		 # vertical
			if (b + cpos[i]*salto >= 0 and b + cpos[i]*salto < num_colunas): # horizontal
				rec_caminho(tabuleiro, a + lpos[i]*salto, b + cpos[i]*salto, c, d, old_pos, possibilidades)

	return

'''
Dado um tabuleiro e duas posições (a,b) e (c,d), verifica se é
possível deslocar uma peça da posição (a,b) até a posição (c,d).

Em caso positivo, sua função deve retornar True e, em caso negativo,
False.
'''
def existe_caminho(tabuleiro, a, b, c, d):
	possibilidades = []
	rec_caminho(tabuleiro, a, b, c, d, [], possibilidades)
	if possibilidades:
		return True
	else:
		return False


# Leitura de dados

n, m = [int(i) for i in input().split()]
tabuleiro = []
for _ in range(n):
	tabuleiro.append([int(i) for i in input().split()])
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]

# Verifica se existe caminho entre as posições dadas

caminho1 = existe_caminho(tabuleiro, a, b, c, d)
caminho2 = existe_caminho(tabuleiro, c, d, a, b)

if caminho1 == True:
	caminho_1 = "existe caminho"
else:
	caminho_1 = "nao existe caminho"

if caminho2 == True:
	caminho_2 = "existe caminho"
else:
	caminho_2 = "nao existe caminho"

# Impressão do resultado

print("({},{}) -> ({},{}):".format(a,b,c,d), caminho_1)
print("({},{}) -> ({},{}):".format(c,d,a,b), caminho_2)
