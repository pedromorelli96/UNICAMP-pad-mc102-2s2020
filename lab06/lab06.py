######################################################################
# MC102 - Algoritmos e Programação de Computadores                                                                              
# Laboratório 6 - De Volta para o Passado                                  
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737                                             
######################################################################

# Leitura de dados
n = int(input()) # número de dias

precos_acoes = [] # preço por dia
for i in range(n): # de 0 até (n - 1)
    precos_acoes.append(float(input()))

k = int(input()) # número máximo de dias permitido entre a compra e venda de uma ação

q = float(input()) # quantidade de dinheiro levado na viagem


# Escolha da melhor variação de valores da ação

dia_compra = 0
dia_venda = 0
valor_compra = 0
valor_venda = 0
qtde_acoes = 0
lucro = 0 # importante inicializar lucro como zero

for i in range(n):
    for j in range(i, i+k+1): # (i+k+1) pois range sempre vai até o limite-1
        if (j <= n-1):
            acoes_possiveis = int(q // precos_acoes[i]) # quantas ações posso comprar naquele dia

            diferenca = precos_acoes[j] - precos_acoes[i] # qual o lucro por ação entre os dias observados

            lucro_preliminar = acoes_possiveis*diferenca # qual o lucro total preliminar neste caso
            
            if (lucro_preliminar > lucro):
                lucro = lucro_preliminar
                dia_compra = i + 1
                dia_venda = j + 1
                

if (lucro == 0): # caso em que o primeiro dia tem o maior preço de ações
    dia_compra = 1
    dia_venda = 1
    valor_compra = precos_acoes[0]
    valor_venda = precos_acoes[0]
    qtde_acoes = int(q // valor_compra)
    lucro = 0
else:
    valor_compra = precos_acoes[dia_compra-1]
    valor_venda = precos_acoes[dia_venda-1]
    qtde_acoes = int(q // valor_compra)
    lucro = qtde_acoes*(valor_venda - valor_compra)



# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))