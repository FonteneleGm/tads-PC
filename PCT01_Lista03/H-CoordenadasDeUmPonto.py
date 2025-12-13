# Escreva um programa que leia 2 valores reais x e y, que devem representar as coordenadas de um ponto em um plano cartesiano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

# A entrada contém uma única linha, com as coordenadas x e y ( - 109 ≤ x, y ≤ 109) do ponto.
x, y = map(float, input().split())
# Se o ponto estiver na origem, escreva a mensagem "Origem".
if x == 0.0 and y == 0.0:
    print("Origem")
# Se o ponto estiver sobre um dos eixos escreva "Eixo X" ou "Eixo Y", conforme for a situação.
elif x == 0.0:
    print("Eixo Y")
elif y == 0.0:
    print("Eixo X")
#A saída deve apresentar o quadrante em que o ponto se encontra: 'Q1', 'Q2', 'Q3' ou 'Q4'.
elif x > 0.0 and y > 0.0:
    print("Q1")
elif x < 0.0 and y > 0.0:
    print("Q2") 
elif x < 0.0 and y < 0.0:
    print("Q3")          
elif x > 0.0 and y < 0.0:
    print("Q4") 