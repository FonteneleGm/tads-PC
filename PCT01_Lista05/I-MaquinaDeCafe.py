#A entrada consiste em 3 números, A1 , A2 , A3 (0 ≤ A1, A2, A3 ≤ 1000), um por linha, onde Ai representa o número de pessoas que trabalham no i-ésimo andar.
a1 = int(input())
a2 = int(input())
a3 = int(input())
#Seu programa deve imprimir uma única linha, contendo o número total de minutos a serem gastos com o melhor posicionamento possível da máquina.
cost_1stfloor = (a2 * 2) + (a3 * 4)
cost_2ndfloor = (a1 * 2) + (a3 * 2)
cost_3rdfloor = (a1 * 4) + (a2 * 2)
lowest_cost = cost_1stfloor
if cost_2ndfloor < lowest_cost:
    lowest_cost = cost_2ndfloor
if cost_3rdfloor < lowest_cost:
    lowest_cost = cost_3rdfloor
print(lowest_cost)