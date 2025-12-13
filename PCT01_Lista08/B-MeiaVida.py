#DO SEMESTRE PASSADO

#Um determinado material radioativo perde metade de sua massa a cada s segundos. 
#Escreva um programa que leia o tempo s de perda de massa e a massa inicial mi, em gramas, de um material. 
#O programa deve então calcular em quanto tempo a massa do material fica menor do que 0, 5 grama. 
#O programa deve mostrar a massa final, com 3 casas decimais em uma linha e o tempo gasto para o material chegar a essa massa. 
#O tempo deve ser mostrado na forma D dias HH:MM:SS.

#A entrada é composta de 1 linha contendo 2 (dois) números inteiros s (1 ≤ s ≤ 109), o tempo, em segundos, que a massa do material cai pela metadee mi, a massa inicial do material radioativo.
s, mi = map(int, input().split())
#Seu programa deve mostrar uma única linha, com o tempo gasto em forma de horas, minutos, segundos e milissegundos: D dias HH:MM:SS. 
b = 0
c = s
while mi >= 0.5:
    s = s+b
    b = c
    a = mi/2
    mi = a
     
d = s // 86400
h = (s // 3600)%24
m = (s // 60)%60
seg = s % 60
     
print("{} dias {:02}:{:02}:{:02}".format (d, h, m, seg))