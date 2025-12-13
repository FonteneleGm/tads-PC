# A entrada é composta por três linhas, cada linha contendo um número inteiro N (5 ≤ N ≤ 100), a idade de uma das irmãs.
age1 = int(input())
age2 = int(input())
age3 = int(input())
# Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila.
if (age1 >= age2 or age1 >= age3) and (age1 <= age2 or age1 <= age3):
    print(age1)
elif (age2 >= age1 or age2 >= age3) and (age2 <= age1 or age2 <= age3):
    print(age2)
elif (age3 >= age1 or age3 >= age2) and (age3 <= age1 or age3 <= age2):
    print(age3)
