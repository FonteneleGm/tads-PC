#No planeta Alpha vive a criatura Blobs, que come precisamente (metade) de seu suprimento de comida disponível todos os dias. 
#Escreva um programa que leia a capacidade inicial de suprimento de comida C, em Kg,
#e calcule quantos dias passarão antes que Blobs coma todo esse suprimento até restar um quilo ou menos.

#A primeira linha de entrada contem um único inteiro N (1 ≤ N ≤ 1000), indicando o número de casos de teste. 
n = int(input())
#As N linhas seguintes contém um valor de ponto flutuante C (1 ≤ C ≤ 1000) correspondente à quantidade de comida disponível para Blobs.
for i in range(n):
    c = float(input())
    days = 0
    # A partir daqui está errado. (♪ I'm Crucified Crucified like my savior ♪)
    while c >= 0:               # (♪ Saintlike behavior, a lifetime I prayed ♪...)
        c /= 2
        days = days + 1
        if c <= 0:
            print(f"{days} Dias")
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢰⣷⣶⢀⣤⠀⠀⠀
#⠀⠀⠤⢄⣤⢤⡤⢤⠤⢤⡤⠤⠤⢤⠤⢤⡤⠤⢾⣿⡇⢸⣿⡯⣼⣿⠀⠀⢀
#⠀⠀⢀⣞⡞⣸⣧⣾⠀⠘⠀⠀⠀⠀⡃⠀⢹⠀⠈⣿⡇⠻⠿⡇⡝⠁⠀⢀⢼
#⢠⠀⡾⡼⠀⠈⠁⡅⢀⠃⣂⡠⠔⣚⣓⠀⠀⠤⢤⣿⣷⣾⣿⡿⠇⠀⢀⡾⣹
#⢸⢸⣷⠃⠀⠀⢀⠇⣼⢊⡷⣶⣾⣿⢫⠗⠄⣀⠂⠟⣿⣟⠓⠃⠀⠀⢻⣦⢸
#⡏⢀⣝⣧⠀⣶⡜⣰⡟⣿⢀⣹⠿⠃⠀⠀⠀⢱⢜⠎⠘⠿⠇⠀⠀⠀⠀⠉⢻
#⡇⢸⣿⣿⡀⡟⣼⣉⠃⠘⣁⣥⣀⡀⠀⠀⠀⢸⡈⡄⠀⠀⠀⠀⠀⠀⠀⢠⣾
#⠗⠀⣧⠹⢅⣾⡵⠋⠀⠀⠀⠉⠙⠀⠀⠀⠀⠀⢷⠘⠀⠀⠀⠀⠀⠀⠀⠀⢹
#⠀⢸⢔⣶⣿⣿⡥⠶⠶⠦⡀⠀⠀⠀⠀⠀⠀⠀⠈⢣⢣⠀⠀⠀⠀⠀⠀⠈⣿
#⠀⠀⠣⠽⢿⡉⠀⠀⢀⣀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⠂⠀⠀⠀⠀⠀⠀⣿
#⠀⠀⠀⠀⠀⢇⢀⠀⠀⠀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡌⠄⠀⠀⠀⠀⠀⠇
#⠀⠀⠀⠀⠀⠘⡌⠙⡗⡚⠈⠁⣀⣀⠤⠤⠆⠀⠀⠀⠀⢸⠈⠑⢄⠀⠀⠀⢰
#⠀⠀⠀⠀⠀⠀⠐⣯⣉⣀⡴⠉⠀⠀⠀⣠⠎⠀⠀⠀⠀⡆⠀⠀⠀⠁⣢⡀⣸
#⠀⠀⠀⢀⣤⡄⣴⣬⠻⣮⠀⢀⡴⠖⠚⠋⠀⠀⠀⠀⠀⡿⢄⡀⠠⢔⣨⣿⣿
#⠀⣴⣧⠘⣿⣿⣿⣿⠀⠈⢇⠺⣶⣤⠀⠀⠀⠀⠀⠀⣀⣈⣲⣶⣺⣯⣿⡿⢻
#⡀⢹⣿⡄⠿⠿⠟⠉⠀⠀⠀⢢⠿⠁⠀⢀⡠⣴⣶⣿⣿⣿⣿⣿⣟⣟⡴⣠⢹
#⠀⠈⣿⣷⣤⣶⣾⣿⡷⠀⣶⣦⢆⠀⡴⣿⣿⣿⣯⣿⣿⣷⡇⠀⠀⣰⣣⢃⣾
#⠀ ⠘⣿⣟⠛⠉⠁⣤⣆⠹⠿⢘⣓⡚⠛⠚⠒⠛⠛⠛⢻⣶⣶⣶⡿⢡⣾⣿
#⠠⠤⠀⣹⣿⡄⠀⠀⠘⣿⣶⣾⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠑⢿⣽⣶⣿⠟⢹
#⠀⠀⠀  ⠉⠁⠀⠒⠛⠻⠯⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡀⠀⢸
#⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠒⠂⠤⠄⠀⢀⡀⠀⠈⣦⣘
#⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠉⠛            