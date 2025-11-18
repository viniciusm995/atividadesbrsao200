'''4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.'''

from datetime import datetime

nascimento = input("Digite a data de nascimento: \n")

try:
    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    atual = datetime.today()

    dias_vivo = (atual - data_nascimento).days

    print(f"Você tem {dias_vivo} dias de vida atualmente.")

except ValueError:
    print("Digite uma data valida, no formato DD/MM/AAAA")