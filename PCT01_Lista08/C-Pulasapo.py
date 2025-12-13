#Em cada fase do jogo do Pula Sapo você deve conduzir seu anfíbio através de uma sequência de canos de alturas diferentes até chegar a salvo no cano mais à direita. Entretanto, o sapo só consegue sobreviver se a diferença de altura entre canos consecutivos for de, no máximo, a altura do pulo do sapo. 
#Caso a altura do cano seguinte seja muito alta, o sapo bate no cano e cai. 
#Se a altura do cano seguinte for muito baixa, o sapo não aguenta a queda. 
#O sapo sempre começa em cima do cano mais à esquerda.
#Neste jogo, a distância entre os canos é irrelevante, ou seja, o sapo sempre consegue alcançar o próximo cano com um pulo.

#Imagem_Da_C.png

#Você deve escrever um programa que, dadas as alturas dos canos e a altura do pulo do sapo, mostra se a fase do jogo pode ser vencida ou não.

#A entrada é dada em duas linhas. A primeira tem dois inteiros positivos P e N, a altura do pulo do sapo e o número de canos (1 ≤ P ≤ 5 e 2 ≤ N ≤ 100). 
p, n = map(int, input().split())
#A segunda linha tem N inteiros positivos que indicam as alturas dos canos ordenados da esquerda para a direita. 
Heights = list(map(int, input().split()))
#Não há altura maior do que 10.
HeLost = False
#A saída é dada em uma única linha. Se o sapo pode chegar no cano mais à direita, escreva "YOU WIN". 
#Se o sapo não consegue, escreva "GAME OVER".
for i in range (1, n):
    if (abs(Heights[i] - Heights[i-1]) > p):
        print("GAME OVER")
        HeLost = True
        break
if HeLost == False:
    print("YOU WIN")