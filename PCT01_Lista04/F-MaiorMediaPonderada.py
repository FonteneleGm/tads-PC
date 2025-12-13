# A primeira linha contém dois números inteiros a11 e a21 (0 ≤ a11, a21 ≤ 108), que são as notas da avaliação 1 para as etapas 1 e 2, respectivamente. 
grade_11, grade21 = map(int, input().split())
# A segunda linha possui dois inteiros a12 e a22 (0 ≤ a12, a22 ≤ 108), que são as notas da avaliação 2 pas etapas 1 e 2, respectivamente.
grade_12, grade22 = map(int, input().split())
# A terceira linha contém 2 (dois) números inteiros p1 e p2 (1 ≤ p1, p2 ≤ 103), os pesos das etapas 1 e 2, respectivamente.
p1, p2 = map(int, input().split())
#Seu programa deve mostrar uma única linha com um número inteiro a informando qual avaliação Eduzinho vai pedir ao professor Faísca para usar. 
# Todos os cálculos devem ser feitos utilizando valores inteiros, desprezando-se as casas decimais.
mean_1 = ((grade_11 * p1) + (grade21 * p2)) // (p1 + p2)
mean_2 = ((grade_12 * p1) + (grade22 * p2)) // (p1 + p2)
if mean_1 >= mean_2:
    print("1")
else:
    print("2")