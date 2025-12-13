#Escreva um programa que leia 2 números inteiros e informe se o maior é múltiplo do menor.

# A entrada é composta de dois números inteiros a eb (1 ≤ a, b ≤ 109), cada um em uma linha.
a = int(input())
b = int(input())
# A saída deve conter uma única linha com o texto "Multiplos" caso o maior seja múltiplo do menor ou "Nao multiplos" caso contrário. Observe que não há acentos no texto.
menor = min(a, b)
maior = max(a, b)
if maior % menor == 0:
    print("Multiplos")
else:
    print("Nao multiplos")
