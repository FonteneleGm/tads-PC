#Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, retorne o menor número par maior do que X.

# Uma linha contendo um número x (0 < x < 107).
x = int(input())
# Uma linha contendo a resposta do problema.
if (x%2==0):
 print(x + 2)
else:
  print(x + 1)
 