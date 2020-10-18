######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Chegada na Estação
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
######################################################################

# Leitura de dados

x = int(input())
t = int(input())
v_1 = float(input())
v_2 = float(input())

# Cálculo dos tempos de viagem

tempo_t1 = x/v_1 # em horas
tempo_t2 = (x/v_2) + (t/60) # em horas

# Impressão da resposta

if (tempo_t1 < tempo_t2):
    print("True")
else:
    print("False")