#A primeira linha da entrada contém um inteiro A. A segunda linha da entrada contém um inteiro B. A terceira linha da entrada contém um inteiro C. 
# Os três inteiros representam as posições atuais das traseiras dos carros A, B e C, respectivamente, onde 0 ≤ A < B < C ≤ 500.
a = int(input())
b = int(input())
c = int(input())
#Seu programa deve imprimir uma linha contendo um inteiro: 1 se o carro B precisa acelerar; −1 se precisa desacelerar; ou 0 se precisa manter a velocidade atual.
if (b - a) < (c - b):
    print('1')
if (b - a) > (c - b):
    print('-1')
if (b - a) == (c - b):
    print('0')