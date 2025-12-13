#DO SEMESTRE PASSADO

#Dado um número inteiro n, encontre o menor número primo maior do que n. 

#A entrada é composta de uma única linha, contendo um número inteiro n (1 ≤ n ≤ 106).

#Seu programa deve mostrar um número inteiro p, que é o menor número primo maior do que n.
def is_prime(n):
    if n==1: 
        return False
    if n==2:
        return True
    d = 3
    while d < n-1:
        if n%d == 0:
            return False
        d = d+1
    return True

n = int(input())
x = n+1
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x = x+1
        