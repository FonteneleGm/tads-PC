#Escreva um programa que leia N números inteiros e calcule a média dos números lidos. 
#Depois o programa deve contar quantos números estão acima da média e quantos estação abaixo da média. 

#A entrada é composta de 2 (duas) linhas, a primeira linha contém um inteiro N (1 ≤ N ≤ 106), a quantidade de números a serem lidos. 
n = int(input())
#A segunda contém N números inteiros Ai (0 ≤ Ai ≤ 109), separados por espaço.
Ai = list(map(int, input().split()))
#Seu programa deve imprimir deve imprimir 3 (três) linhas, *
 
average_divider = len(Ai)
#print(average_divider)
average = sum(Ai) / average_divider
nums_lta = []
nums_hta = []
for i in range(len(Ai)):
    #current_index = Ai[1]
    #print(current_index)
    if Ai[i] < average:
        nums_lta.append(Ai[i])
    if Ai[i] > average:
        nums_hta.append(Ai[i])
    if Ai[i] == average:
        nums_hta.append(Ai[i])
    #current_index = current_index+1

# * onde a primeira linha contém um a média dos números lidos, com 1 (uma) casa decimal.    
print(f"{average:.1f}")
# A segunda linha contém a quantidade de números abaixo da média
#print(*nums_lta) Mostra os índices da lista menores que (average) sem estar no formato de lista.
print(len(nums_lta))
# e a terceira linha a quantidade de números igual à média ou acima da média.
#print(*nums_hta) Mostra os índices da lista maiores ou iguais a (average) sem estar no formato de lista.
print(len(nums_hta))