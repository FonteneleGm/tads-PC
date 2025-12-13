# A entrada consiste de uma linha contendo os valores dos três créditos A, B e C (1 ≤ A, B, C ≤ 1000).
a, b, c = map(int, (input().split()))
# Seu programa deve imprimir uma linha contendo o caracter "S" se é possível viajar e voltar para o presente, ou "N" caso contrário.
if a == b or a == c or b == c or a + b == c or a + c == b or b + c == a:
    print("S")
else:
    print("N")









