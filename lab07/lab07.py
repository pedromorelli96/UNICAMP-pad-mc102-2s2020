###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Nota de MC102
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
###################################################

# Leitura de dados

n = int(input())

notas = []
for i in range(n):
    notas.append(float(input()))

pesos = []
for i in range(n):
    pesos.append(int(input()))


# Cálculo da média ponderada dos laboratórios
media_preliminar = 0
sum_pesos = 0

for i in range(n):
    media_preliminar += notas[i]*pesos[i]
    sum_pesos += pesos[i]

media_labs = media_preliminar/sum_pesos

print("Media laboratorios:", format(media_labs, ".1f").replace(".", ","))

# Verificação da situação do aluno

if (media_labs >= 5):
    # Caso o aluno tenha sido aprovado por nota
    print("Situacao: Aprovado por nota")
    nota_final = media_labs
elif (media_labs < 2.5):
    # Caso o aluno tenha sido reprovado por nota
    print("Situacao: Reprovado por nota")
    nota_final = media_labs
else:
    # Cálculo da nota do exame, caso o aluno tenha ido para o exame

    # Leitura dos dados referentes ao exame
    m = int(input())

    labs_exame = []
    for i in range(m):
        labs_exame.append(int(input()))

    notas_exame = []
    for i in range(m):
        notas_exame.append(float(input()))
    
    # Cálculo da média ponderada dos laboratórios pós-exame
    media_parcial_exame = 0
    sum_pesos_exame = 0
    
    for i in range(m):
        media_parcial_exame += notas_exame[i]*pesos[labs_exame[i] - 1]
        sum_pesos_exame += pesos[labs_exame[i] - 1]

    media_parcial_exame /= sum_pesos_exame

    media_exame = (media_parcial_exame + media_labs)/2


    if (media_exame >= 5):
        # Caso o aluno tenha sido aprovado no exame
        print("Situacao: Aprovado no exame")
        nota_final = 5
    else:
        # Caso o aluno tenha sido repravado no exame
        print("Situacao: Reprovado no exame")
        nota_final = media_exame


# Saída de dados

print("Nota final:", format(nota_final, ".1f").replace(".", ","))
