#A entrada é composta de uma única linha, com um valor inteiro n (1 ≤ n ≤ 106).
n = int(input())
#O programa deve mostra uma linha com o valor do somatório com 4 casas decimais.
soma = 0 # Variável tem ser declarada antes da função para ela não ser substituida pelos conteúdos da função.
for i in range(1,n+1): # O "range" é de 1 até o número mais 1, porque quando chega no final do "range" ele para, por isso tem de ser "+1".
    soma += 1 / i #Em Python, += é um operador de atribuição composto que adiciona o valor à direita ao valor armazenado na variável à esquerda e atribui o resultado de volta à variável.
print(f"{soma:.4f}") # Formatação com f para exibir casas décimais
# Tem de ser f abrindo aspas com colchetes dentro delas e dentro deles a variável mais :.-qtd de casas-f.
