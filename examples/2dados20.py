from random import random
from collections import Counter


resultados = list()
counter = Counter()
counter_rodada = Counter()
for s in range(5):
  for i in range(2000):
    acum = 0
    for turn in range(3):
      dado1 = int(random() * 20 + 1)
      dado2 = int(random() * 20 + 1)
      rodada = dado1 + dado2
      counter_rodada[rodada] +=1
      acum += rodada

    resultados.append(acum)
    counter[acum] +=1

result_rodadas = counter_rodada.most_common()
print(result_rodadas)
print(counter.most_common(20))

resultados = [item[0] for item in result_rodadas]
qtdes = [item[1] for item in result_rodadas]

import matplotlib.pyplot as plt


plt.bar(resultados, qtdes)
plt.show('hist.png')
