# Escreva um programa que leia 2 (dois) números inteiros a e b e mostre o maior dos 2.

a = int(input()) # A entrada é composta por duas linhas. A primeira linha contém apenas um inteiro a (1 ≤ a ≤ 109)
b = int(input()) # e a segunda um inteiro b (1 ≤ b ≤ 109).
# Seu programa deve mostrar uma única linha contendo o valor do maior inteiro.
if (a < b):
  print(b)
else: 
  print(a)