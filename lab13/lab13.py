###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Tabela de Vendas
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################

# Leitura de dados




# Ordenação dos dados



# Saída dos dados
for linha in dados:
        print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))
