# A entrada consiste de uma única linha, contendo 8 números inteiros N1, N2, N3, N4, N5, N6, N7 e N8, indicando os valores lidos pelo dispositivo (Ni é 0, 1 ou 9 para 1 ≤ i ≤ 8).
n1, n2, n3, n4, n5, n6, n7, n8 = map(int, (input().split()))
#Imprima uma única linha contendo a letra maiúscula 'S' caso todos os bits sejam lidos com sucesso; caso contrário imprima uma única linha contendo a letra maiúscula 'F', correspondendo a uma falha.
if n1 == 9 or n2 == 9 or n3 == 9 or n4 == 9 or n5 == 9 or n6 == 9 or n7 == 9 or n8 == 9:
    print("F")
else:
    print("S")