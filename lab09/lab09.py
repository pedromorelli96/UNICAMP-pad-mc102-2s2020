#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Tabela da Copa do Mundo de Futebol
# Nome: Pedro Rodrigo Ramos Morelli
# RA: 204737
#####################################################

# Leitura da lista de seleções

selecoes = []
dic = {}
for i in range(16):
  selecao = input()
  selecoes.append(selecao)
  dic[selecao] = {"partidas": 0, "vitorias": 0, "derrotas": 0, "penaltis": 0,
                  "normal": 0, "marcados": 0, "sofridos": 0}

# Leitura das partidas e processamento dos dados

parenteses = "()"

for i in range(16):
  jogo = input().split()

  # Caso em que o jogo acabou em tempo normal
  if (len(jogo) == 5):

    if (jogo[1] > jogo[3]): # Time A venceu Time B
      # Time vencedor
      dic[jogo[0]]["partidas"] += 1
      dic[jogo[0]]["vitorias"] += 1
      dic[jogo[0]]["normal"] += 1
      dic[jogo[0]]["marcados"] += int(jogo[1])
      dic[jogo[0]]["sofridos"] += int(jogo[3])
      # Time perdedor
      dic[jogo[4]]["partidas"] += 1
      dic[jogo[4]]["derrotas"] += 1
      dic[jogo[4]]["normal"] += 1
      dic[jogo[4]]["marcados"] += int(jogo[3])
      dic[jogo[4]]["sofridos"] += int(jogo[1])

    else: # Time B venceu Time A
      # Time vencedor
      dic[jogo[4]]["partidas"] += 1
      dic[jogo[4]]["vitorias"] += 1
      dic[jogo[4]]["normal"] += 1
      dic[jogo[4]]["marcados"] += int(jogo[3])
      dic[jogo[4]]["sofridos"] += int(jogo[1])
      # Time perdedor
      dic[jogo[0]]["partidas"] += 1
      dic[jogo[0]]["derrotas"] += 1
      dic[jogo[0]]["normal"] += 1
      dic[jogo[0]]["marcados"] += int(jogo[1])
      dic[jogo[0]]["sofridos"] += int(jogo[3])

  else: # Caso dos penaltis
    
    # Removendo os parenteses dos resultados dos penaltis
    for char in jogo[4]:
      if char in parenteses:
        jogo[4] = jogo[4].replace(char, "")

    for char in jogo[6]:
      if char in parenteses:
        jogo[6] = jogo[6].replace(char, "")

    if (jogo[4] > jogo[6]): # Time A venceu Time B
      # Time vencedor
      dic[jogo[0]]["partidas"] += 1
      dic[jogo[0]]["vitorias"] += 1
      dic[jogo[0]]["penaltis"] += 1
      dic[jogo[0]]["marcados"] += int(jogo[1])
      dic[jogo[0]]["sofridos"] += int(jogo[3])
      # Time perdedor
      dic[jogo[7]]["partidas"] += 1
      dic[jogo[7]]["derrotas"] += 1
      dic[jogo[7]]["penaltis"] += 1
      dic[jogo[7]]["marcados"] += int(jogo[3])
      dic[jogo[7]]["sofridos"] += int(jogo[1])
    
    else: # Time B venceu Time A
      # Time vencedor
      dic[jogo[7]]["partidas"] += 1
      dic[jogo[7]]["vitorias"] += 1
      dic[jogo[7]]["penaltis"] += 1
      dic[jogo[7]]["marcados"] += int(jogo[3])
      dic[jogo[7]]["sofridos"] += int(jogo[1])
      # Time perdedor
      dic[jogo[0]]["partidas"] += 1
      dic[jogo[0]]["derrotas"] += 1
      dic[jogo[0]]["penaltis"] += 1
      dic[jogo[0]]["marcados"] += int(jogo[1])
      dic[jogo[0]]["sofridos"] += int(jogo[3])


for selecao in selecoes:
  if (dic[selecao]["derrotas"] == 0):
    campeao = selecao

# Saída de dados

for selecao in selecoes:
  print("-" * 50)
  print("Pais:", selecao)
  print("Partidas:", dic[selecao]["partidas"])
  print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
  print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
  print("Vitorias:", dic[selecao]["vitorias"])
  print("Derrotas:", dic[selecao]["derrotas"])
  print("Gols marcados:", dic[selecao]["marcados"])
  print("Gols sofridos:", dic[selecao]["sofridos"])
  
print("-" * 50)
print("Pais campeao:", campeao)
print("-" * 50)
