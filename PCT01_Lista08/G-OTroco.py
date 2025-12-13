#O pai de Joãozinho lhe pediu que fosse à venda comprar um determinado ingrediente e lhe deu as seguintes instruções:

#1. Não me importo com qual marca você vai escolher, contanto que compre o máximo possível.
#2. Não volte de mãos vazias (compre pelo menos um produto).
#3. Não me traga produtos de marcas diferentes.
#4. Se não violar nenhuma das restrições anteriores o troco é seu.
#Joãozinho não é muito bom em matemática e pediu sua ajuda para escolher a marca que maximizaria seu troco de acordo com as restrições impostas. 
#Você não gosta de pessoas preguiçosas e prometeu a Joãozinho que faria um programa para resolver apenas uma parte do problema: 
#encontrar o valor máximo (sem dizer qual marca ele deve escolher para obter tal troco).

#A primeira linha contém um inteiro T (1 ≤ T ≤ 2000), o número de casos de teste.
t = int(input())
#Cada caso de teste é composto por 2 linhas. 
for i in range(t):
#A primeira linha contém os inteiros D (10 ≤ D ≤ 500) e N (2 ≤ N ≤ 300), indicando a quantia que Joãozinho levou ao mercado 
#e a quantidade de marcas diferentes disponíveis (assuma que o estoque da loja é suficiente para vender qualquer quantidade de qualquer produto), respectivamente.
    d, n = map(int, input().split())
#A segunda linha contém N números de ponto flutuante pi, representando o preço da unidade fabricada pela marca mi.
    nPi = list(map(float, input().split()))
    biggestChange = 0
#Assuma que não haverá nenhum preço com mais de 2 dígitos após o ponto decimal.
    for i in range(n):
        if nPi[i] <= d:
            if (d % nPi[i] > biggestChange):
                biggestChange = d % nPi[i]
    print(f"{biggestChange:.2f}")
#Para cada caso de teste imprima uma única linha contendo um valor de ponto flutuante com 2 dígitos após o ponto decimal: o maior troco que Joãozinho poderá obter.

