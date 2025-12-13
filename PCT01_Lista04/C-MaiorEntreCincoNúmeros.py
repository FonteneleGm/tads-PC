#A entrada é composta de 3 números inteiros a, b, c, d e e ( - 10000 ≤ a, b, c, d, e ≤ 10000), cada número em uma linha.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
#A saída deve conter uma única linha com um número inteiro, o maior dos 5 números lidos.
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d
if e > maior:
    maior = e
print(maior)