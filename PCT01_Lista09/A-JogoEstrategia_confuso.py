#Um jogo de estratégia, com J jogadores, é jogado em volta de uma mesa. O primeiro a jogar é o jogador 1, o segundo a jogar é o jogador 2 e assim por diante. 
#Uma vez completada uma rodada, novamente o jogador 1 faz sua jogada e a ordem dos jogadores se repete novamente. 
#A cada jogada, um jogador garante uma certa quantidade de Pontos de Vitória. A pontuação de cada jogador consiste na soma dos Pontos de Vitória de cada uma das suas jogadas.

#Dado o número de jogadores, o número de rodadas e uma lista representando os Pontos de Vitória na ordem em que foram obtidos, você deve determinar qual é o jogador vencedor. 
#Caso mais de um jogador obtenha a pontuação máxima, o jogador com pontuação máxima que tiver jogado por último é o vencedor.

#A entrada consiste de duas linhas. A primeira linha contém dois inteiros J e R, *
j, r = map(int, input().split()) #*o número de jogadores e de rodadas respectivamente (1 ≤ J, R ≤ 500). 
#A segunda linha contém J × R inteiros, *
points = list(map(int, input().split())) #*correspondentes aos Pontos de Vitória em cada uma das jogadas feitas, na ordem em que aconteceram. 
#Os Pontos de Vitória obtidos em cada jogada serão sempre inteiros entre 0 e 100, inclusive.
#Seu programa deve produzir uma única linha, contendo o inteiro correspondente ao jogador vencedor.
total = [0] * j
indice = 0
for rodada in range(r):
    for jogador in range(j):
        total[jogador] = total[jogador] + points[indice]
        indice = indice + 1
# Para definir o vencedor. 
vencedor = 0 
for i in range(j):
    if total[i]>=total[vencedor]:
        vencedor = i
 
print(vencedor+1) # Por conta do ínicio ser no índice "0", não existe jogador "0", então "vencedor+1".