# Escreva um programa que leia 3 números inteiros e mostre o maior.

# A entrada é composta de 3 números inteiros a, b e c ( - 10000 ≤ a, b, c ≤ 10000), cada número em uma linha.
a = int(input())
b = int(input())
c = int(input())
# A saída deve conter uma única linha com um número inteiro, o maior dos 3 números lidos.
if (a>=b and a>=c):
 print(a)
else:
 if (b>=a and b>=c):
  print(b)
 else:
    if (c>=a and c>=b):
     print(c)