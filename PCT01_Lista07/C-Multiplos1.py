#Escreva um programa que leia dois números inteiros a e b e mostre todos os múltiplos de a menores ou iguais a b.
# Tentativa em recursividade, mas pelo menos resolveu para a lógica
#def mul_entre_dois(a, b):
#    n = 1
#    if a or b == 0:
#        return 0
#    elif (a * n) > b:
#        return mults
#    elif (a * n) <= b:
#        mults.append(a)
#        return 1 + mul_entre_dois(a, b)
#Uma única linha com 2 números inteiros a e b (1 ≤ a ≤ b ≤ 106) separados por um espaço.
a, b = map(int, input().split())
n = 1
mults = []
#Uma única linha com os múltiplos de a, separados por espaço.
for i in range(a,b+1): # Mais 1 para não terminar quando chegar no "b" em si, e sim depois que verificar o "b".
    if (a * n) > b:
        break
    mult = (a * n)
    mults.append(mult)
    n = n + 1
print(*mults) # * é printar como se estivesse um alinhado do outro separadamente.