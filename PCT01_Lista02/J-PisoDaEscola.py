l = int(input()) # A primeira linha da entrada contém um inteiro L (1 ≤ L ≤ 100) indicando a largura da sala.
c = int(input()) # A segunda linha contém um inteiro C (1 ≤ C ≤ 100) representando o comprimento da sala.
     
FirstType = (l * c) + (l - 1) * (c - 1)
SecondType = 2 * ((l - 1) + (c - 1))
     
print(FirstType)
print(SecondType)