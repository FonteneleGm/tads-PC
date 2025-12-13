#A única linha da entrada contém um único inteiro N (0 ≤ N ≤ 103), indicando o consumo de água da residência, em m3.
n = int(input())
#Seu programa deve imprimir uma única linha, contendo o valor da conta de água daquela residência
total = 7  
if n <= 10:
    pass  
elif n <= 30:
    total += (n - 10) * 1
elif n <= 100:
    total += 20 * 1 + (n - 30) * 2
else:
    total += 20 * 1 + 70 * 2 + (n - 100) * 5
print(total)
