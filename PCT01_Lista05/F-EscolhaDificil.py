#A primeira linha contem três inteiros Ca, Ba e Pa (0 ≤ Ca, Ba, Pa ≤ 100), representando respectivamente o número de refeições disponíveis de frango, bife e massa.
Ca, Ba, Pa = map(int, input().split())
#A segunda linha contem três inteiros Cr, Br e Pr (0 ≤ Cr, Br, Pr ≤ 100), indicando respectivamente o número de refeições requisitadas de frango, bife e massa respectivamente.
Cr, Br, Pr = map(int, input().split())
#Imprima uma única linha com um inteiro representando o número de passageiros que seguramente não receberão sua escolha de refeição.
if Ca < Cr:
    SemFrango = Cr - Ca
if Ca >= Cr:
    SemFrango = 0
if Ba < Br:
    SemBife = Br - Ba
if Ba >= Br:
    SemBife = 0
if Pa < Pr:
    SemMassa = Pr - Pa    
if Pa >= Pr:
    SemMassa = 0
print(SemFrango + SemBife + SemMassa)
