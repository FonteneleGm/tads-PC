#Escreva um programa que leia N números inteiros e calcule a média dos números lidos. 
#Depois o programa deve mostrar quantos números estão acima da média e quais são, também deve mostrar quantos estação abaixo da média e quais são. ]

#A entrada é composta de 2 (duas) linhas, a primeira linha contém um inteiro N (1 ≤ N ≤ 106), a quantidade de números a serem lidos. 
n_q = int(input())
#A segunda contém N números inteiros Ai (0 ≤ Ai ≤ 109), separados por espaço.
Ai = list(map(int, input().split()))
#Seu programa deve imprimir deve imprimir 3 (três) linhas, 
average = sum(Ai) / n_q
nums_ba = []
nums_aorntta = []
for i in range(len(Ai)):
    if Ai[i] < average:
        nums_ba.append(Ai[i])
    if Ai[i] >= average:
        nums_aorntta.append(Ai[i])
    #else:
    #    nums_aorntta.append(Ai[i-1])
nums_ba.insert(0, len(nums_ba)) # Insira o "len(nums_ba)" no indice 0 da lista "nums_ba"
nums_aorntta.insert(0, len(nums_aorntta))
#onde a primeira linha contém um a média dos números lidos, com 1 (uma) casa decimal. 
print(f"{average:.1f}")
#A segunda linha contém a quantidade de números abaixo da média e a lista dos números, na ordem em que foram lidos, separados por espaço. 
print(*nums_ba)
#Por fim, na terceira e última linha, a quantidade de números igual à média ou acima da média e os números, também separados por espaço. 
print(*nums_aorntta)