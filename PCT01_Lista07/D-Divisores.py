#Escreva um programa que leia um número inteiro n e mostre os divisores de n, incluindo ele mesmo.

#A entrada é composta de uma única linha com um inteiro n (1 ≤ n ≤ 106)
n = int(input())
#Seu programa deve mostrar, em uma única linha, todos os divisores de n, separados por espaços.
divider = 1
dividers = []
for i in range(1,n+1):
    #division = n / divider 
    if n % divider == 0:
        dividers.append(divider)
    #if (division - 1) > division and division < (division + 1):
    #    break
    #if isinstance(division, float): # Isso é aqui é caso literalmente fosse especificado [int(), float()...], não valores inteiros ou não.
    #    break
    #if (division).is_integer:
    #    break
    #dividers.append(divider)
    divider = divider + 1
print(*dividers)

