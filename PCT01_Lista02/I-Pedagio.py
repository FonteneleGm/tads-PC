l, d = map(int, input().split()) # A primeira linha da entrada contém dois inteiros L e D (1 ≤ L, D ≤ 104), indicando o comprimento da estrada e a distância entre pedágios, respectivamente.
k, p = map(int, input().split()) # A segunda linha contém dois inteiros K e P (1 ≤ K, P ≤ 104 ), indicando o custo por quilômetro percorrido e o valor de cada pedágio.
# O primeiro pedágio está localizado no quilômetro D da estrada (ou seja, a distância do início da estrada para o primeiro pedágio é D quilômetros).
Cost_Per_Km = l * k
Num_of_Tolls = l // d
TollCost = Num_of_Tolls * p
TotalCost = Cost_Per_Km + TollCost
print(TotalCost)