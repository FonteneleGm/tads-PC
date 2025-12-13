# Essa Peguei no Grupo da Sala
# A entrada consiste de uma única linha contendo quatro inteiros A1, A2, A3, A4, indicando a área de casa uma das zonas.
a1, a2, a3, a4 = map(int, input().split())
#Imprima uma única linha contendo um único caractere: 'S' se Bloggs pode preservar seu projeto e 'N' caso contrário.
if (a1 * a2 == a3 * a4) or (a1 * a3 == a2 * a4) or (a1 * a4 == a2 * a3):
    print("S")
else:
    print("N")
