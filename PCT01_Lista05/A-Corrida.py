#A entrada consiste de duas linhas; cada linha descreve uma das charretes que lidera a corrida. A descrição de uma charrete consiste de três inteiros N (1 ≤ N ≤ 99), D (0 ≤ D ≤ 1000) e V (0 ≤ V ≤ 50) indicando, 
# respectivamente, o número da charrete, a sua distância à linha de chegada em metros, e a sua velocidade, em quilômetros por hora. Os números das duas charretes são distintos.
n, d, v = map(int, input().split())
n2, d2, v2 = map(int, input().split())
#Imprima uma única linha, contendo um único número inteiro, indicando o número da charrete que seria vencedora, conforme descrito acima.
Tempo1 = (18 * d) / (5 * v)
Tempo2 = (18 * d2) / (5 * v2)
if Tempo1 < Tempo2:
    print(n)
else:
    print(n2)