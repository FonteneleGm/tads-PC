V = int(input()) # A primeira linha contém o valor do item V (1 ≤ V ≤ 105).
Q = int(input()) # A segunda linha contém a quantidade de itens comprado Q (1 ≤ Q ≤ 103).
T = int(input()) # A terceira linha contém o valor total pago T (1 ≤ T ≤ 108).
ToPay = V * Q
Change = T - ToPay
print(f"A pagar: {ToPay}")
print(f"Troco  : {Change}")
