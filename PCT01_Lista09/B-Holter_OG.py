#Professor Edu sentiu-se mal no último final de semana e precisou ir ao hospital. 
#Durante o atendimento foi observado que ele apresentou um quadro de arritmia cardíaca e foi encaminhado para um médico cardiologista. 
#Um dos exames solicitados pelo médico utiliza um monitor Holter, equipamento que monitora o coração durante um determinado período, em geral, 24 horas.

#No exame realizado por Edu, foram registrados os batimentos cardíacos a cada 30 minutos. 
#E, como ele é muito ansioso, decidiu verificar os registros dos seus batimentos e anotar algumas informações para a conversa a ser realizada com seu cardiologista na próxima consulta médica.

#Edu decidiu verificar basicamente duas informações: a quantidade média de batimentos cardíacos no exame realizado e a quantidade de medições com batimentos acima ou abaixo da média obtida considerando uma diferença de 10% entre cada valor medido e a média.

#A primeira linha da entrada contém um inteiro N (2 ≤ N ≤ 48) com o número de medições realizadas pelo equipamento. 
#numbers = list(map(int, input().split()))
hr_measures_num = int(input()) # Número de medições.
measure_nums = [] # Números das medições.
for nums_input in range(hr_measures_num):
    z = int(input())
    measure_nums.append(z) 
 #As N linhas seguintes possuem valores inteiros B (50 ≤ B ≤ 150) referentes às medições dos batimentos cardíacos.    
beats = measure_nums
#A saída deve conter dois valores inteiros:
average_beat = sum(beats) // len(beats)
count = 0
for beat in beats:
    #if beat > (average_beat * 1.1)//100 or beat < (average_beat * 0.9)//100:
    if beat > (average_beat * 110)//100 or beat < (average_beat * 90)//100:
        count += 1 # Mesma coisa que count = count + 1 
#*na primeira linha, o batimento médio obtido a partir das medições realizadas, *     
print(average_beat)
#*  e na segunda linha, a quantidade de medições acima ou abaixo deste valor médio considerando uma diferença de 10% entre os valores medidos e a média.     
print(count)