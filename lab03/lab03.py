######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Bruto x Líquido
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
######################################################################

# Leitura de dados

salario_bruto = float(input())

# Desconto de INSS

if (salario_bruto <= 1045.00):
    INSS = salario_bruto * (7.5/100)
elif (salario_bruto <= 2089.60):
    INSS = salario_bruto * (9/100)
elif (salario_bruto <= 3134.40):
    INSS = salario_bruto * (12/100)
elif (salario_bruto <= 6101.06):
    INSS = salario_bruto * (14/100)
else:
    INSS = 6101.06 * (14/100)

salario_menos_inss = salario_bruto - INSS

# Desconto de IR

if (salario_menos_inss <= 1903.98):
    IR = 0
elif (salario_menos_inss <= 2826.65):
    IR = (salario_menos_inss * (7.5/100)) - 142.80
elif (salario_menos_inss <= 3751.05):
    IR = (salario_menos_inss * (15/100)) - 354.80
elif (salario_menos_inss <= 4664.68):
    IR = (salario_menos_inss * (22.5/100)) - 636.13
else:
    IR = (salario_menos_inss * (27.5/100)) - 869.36

salario_liquido = salario_menos_inss - IR

# Saída de dados

print("Bruto: R$", format(salario_bruto, ".2f").replace(".", ","))
print("INSS: R$", format(INSS, ".2f").replace(".", ","))
print("IR: R$", format(IR, ".2f").replace(".", ","))
print("Liquido: R$", format(salario_liquido, ".2f").replace(".", ","))
