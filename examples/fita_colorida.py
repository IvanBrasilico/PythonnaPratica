"""
Roberto tem um conjunto de lápis com 10 tons diferentes de uma mesma cor, numerados de 0 a 9.
Numa fita quadriculada, alguns quadrados foram coloridos inicialmente com o tom 0.
Roberto precisa determinar, para cada quadrado Q não colorido, qual é a distância dele
para o quadrado mais próximo de tom 0. A distância entre dois quadrados é definida com
o número mínimo de movimentos para a esquerda, ou para a direita,
 para ir de um quadrado para o outro.
O quadrado Q, então, deve ser colorido com o tom cuja numeração corresponde à distância determinada.
Se a distância for maior ou igual a 9, o quadrado deve ser colorido com o tom 9.
Seu programa deve colorir e imprimir a fita quadriculada dada na entrada.

Entrada
A primeira linha da entrada contém apenas um inteiro N, indicando o número de quadrados da fita.
A segunda linha contém N números inteiros: "-1" se o quadrado não está colorido, e "0" se está colorido com o tom 0.
Saída
Seu programa deve escrever na saída a fita totalmente colorida, de acordo com a regra definida acima.
Restrições
3 ≤ N ≤ 10000;
Sempre existe pelo menos um "0" inicialmente na fita.
"""

n = 8
fita = '-1 -1 0 -1 -1 -1 0 -1'.split()

print(fita)
zeros = []
for ind, dig in enumerate(fita):
    if dig == '0':
        zeros.append(ind)

ind_atual = 0
distancias = []
for ind_zero in zeros:
    distancias.append(ind_zero - ind_atual)
    ind_atual = ind_zero
print(distancias)

nova_lista = []
cor_atual = distancias[0] + 1
for ind in range(0, zeros[0]):
    ind_atual += 1
    cor_atual -= 1
    nova_lista.append(cor_atual)
    print(nova_lista)

zeros.pop(0)
distancias.pop(0)

for ind_zero, distancia in zip(zeros, distancias):
    ind_atual = 0
    cor_atual = -1
    for ind in range(0, (distancia // 2) + 1):
        ind_atual += 1
        cor_atual += 1
        nova_lista.append(cor_atual)
        print('loop 1', nova_lista)

    for ind in range(ind_atual, distancia):
        cor_atual -= 1
        nova_lista.append(cor_atual)
        print('loop 2', nova_lista)

print(nova_lista)

cor_atual = 0
for ind in range(zeros[len(zeros) - 1], len(fita)):
    nova_lista.append(cor_atual)
    cor_atual += 1
    print('loop 3', nova_lista)
