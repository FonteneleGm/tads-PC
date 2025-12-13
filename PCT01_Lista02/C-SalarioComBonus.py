WorkersName = input() #A primeira linha contém o nome do vendedor, formada apenas por letras maiúsculas e minúsculas, sem acentos e sem espaços.
S = float(input())  #A segunda linha contém um real S, o salário base do vendedor (0.01 ≤ S ≤ 5000.00) 
V = float(input()) #e a terceira linha contém um número real V (0.00 ≤ 50000.00), o total de vendas do vendedor no mês. 
Comission = V * 0.15
SalaryToPay = S + Comission
print(WorkersName)
print("R$ ""{:.2f}".format(SalaryToPay))