#Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

#Código	Produto	Preço
#1	Cachorro-quente	R$ 4,00
#2	X-salada	R$ 4,50
#3	X-Bacon	R$ 5,00
#4	Torrada simples	R$ 2,00
#5	Refrigerante	R$ 1,50

# A entrada contém dois valores inteiros c (1 ≤ c ≤ 5) e q (1 ≤ q ≤ 100), correspondentes ao código e à quantidade de um item conforme tabela acima.
c, Quantity = map(int, input().split())
# A saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
if c == 1:
    preço = 4
elif c == 2:
    preço = 4.50
elif c == 3:
    preço = 5
elif c == 4:
    preço = 2
elif c == 5:
    preço = 1.50
TotalToPay = (preço * Quantity)
print(f"Total: R$ {TotalToPay:.2f}")