WorkersName = input() #A entrada é composta de 3 linhas. A primeira contém o nome do funcionário, sem espaços, com, no máximo 20 letras.
H = float(input()) #A segunda linha contém um inteiro que representa o total de horas trabalhadas H (1 ≤ H ≤ 160)
V = float(input()) #A terceira linha contém um valor real V (0.01 ≤ V ≤ 500.00) com o valor a ser pago por hora de trabalho. 
SalaryToPay = H * V
print(WorkersName)
print("R$ ""{:.2f}".format(SalaryToPay))