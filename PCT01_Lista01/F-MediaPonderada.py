grade1, grade2 = map(float, input().split())
weight1, weight2 = map(float, input().split())
weighted_mean = (grade1*weight1 + grade2*weight2)/(weight1+weight2) # // Divisão Inteira
print(int(weighted_mean))
#Posso converter para inteiro apenas no resultado "Na hora do 'print'".
#print("{:.5f}".format(weighted_mean))
