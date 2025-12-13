# A função deve retornar um valor inteiro, o maior número entre a e b.
def maior5(a,b,c,d,e):
    biggest_num = a 
    if biggest_num < b:
        biggest_num = b
    #print(biggest_num)
    if biggest_num < c:
        biggest_num = c
    #print(biggest_num)
    if biggest_num < d:
        biggest_num = d
    #print(biggest_num)
    if biggest_num < e:
        biggest_num = e
    #print(biggest_num)
    return biggest_num
#a, b, c, d, e = map(int, input().split())
#biggest_num = maior5(a, b, c, d, e)
#print(biggest_num)