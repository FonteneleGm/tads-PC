#No planeta Alpha vive a criatura Blobs, que come precisamente (metade) de seu suprimento de comida disponível todos os dias. 
#Escreva um programa que leia a capacidade inicial de suprimento de comida C, em Kg,
#e calcule quantos dias passarão antes que Blobs coma todo esse suprimento até restar um quilo ou menos.

#A primeira linha de entrada contem um único inteiro N (1 ≤ N ≤ 1000), indicando o número de casos de teste. 
n = int(input())
#As N linhas seguintes contém um valor de ponto flutuante C (1 ≤ C ≤ 1000) correspondente à quantidade de comida disponível para Blobs.
for i in range(n):
    c = float(input())
    days = 0
    #while c >= 0: Se for assim vai chegar muito próximo de 0, mas nunca irá parar.
    #while c >= 1: Se for igual a "1", se começar no "1" já era.
    while c > 1:
        c = (c / 2)
        #if c < 0: Não é necessário
        days = days + 1       
    print(f"{days} dias") # Estava dentro do "while", com isso ia ter um efeito similar ao "Maid in Heaven"
        