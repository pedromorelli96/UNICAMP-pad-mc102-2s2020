######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
######################################################################

# Leitura de dados
n1 = int(input())
n3 = int(input())
n4 = int(input())
n6 = int(input())
n2 = 0
n5 = 0

# Impressão dos quatro números fornecidos como entrada

print("Primeiro número:", "{:02}".format(n1))
print("Terceiro número:", "{:02}".format(n3))
print("Quarto número:", "{:02}".format(n4))
print("Sexto número:", "{:02}".format(n6))

# Processamento e impressão da lista de possíveis apostas

print("Lista de possíveis apostas:")
for n2 in range(n1+1, n3, 2):
    for n5 in range(n4+1, n6, 2):
        if (((n1 + n2 + n3 + n4 + n5 + n6) % 7) != 0):
            if (((n1 + n2 + n3 + n4 + n5 + n6) % 13) != 0):
                # print(f"{n1:02} - {n2:02} - {n3:02} - {n4:02} - {n5:02} - {n6:02}")
                print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))


