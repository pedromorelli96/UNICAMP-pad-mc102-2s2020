######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome: Pedro Rodrigo Ramos Morelli 
# RA: 204737
######################################################################

# Leitura do hp dos lutadores
ryu = int(input())
ken = int(input())

# Leitura da sequência de golpes
golpes_ryu = 0
golpes_ken = 0

while (ryu > 0 and ken > 0):
    golpe = int(input())
    if (golpe > 0):
        golpes_ryu += 1
        print(f"RYU APLICOU UM GOLPE: {golpe}")
        ken -= golpe
        if (ken < 0):
            ken = 0
        print(f"HP RYU = {ryu}")
        print(f"HP KEN = {ken}")
    else:
        golpes_ken += 1
        print(f"KEN APLICOU UM GOLPE: {abs(golpe)}")
        ryu -= abs(golpe)
        if (ryu < 0):
            ryu = 0
        print(f"HP RYU = {ryu}")
        print(f"HP KEN = {ken}")
    


# Impressão do vencedor e do número de golpes aplicados
if (ryu == 0):
    print("LUTADOR VENCEDOR: KEN")
    print(f"GOLPES RYU = {golpes_ryu}")
    print(f"GOLPES KEN = {golpes_ken}")
else:
    print("LUTADOR VENCEDOR: RYU")
    print(f"GOLPES RYU = {golpes_ryu}")
    print(f"GOLPES KEN = {golpes_ken}")