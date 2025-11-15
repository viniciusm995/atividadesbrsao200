'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''


temperatura = float(input("Digite uma temperatura: \n"))

temperatura_original = int(input("Escolha entre as opções qual a temperatura você deseja converter: \n 1 - Celsius \n 2 - Fahrenheit \n 3 - Kelvin \n Escolha: "))

temperatura_convetida = int(input("Escolha entre as opções para qual temperatura você deseja converter: \n 1 - Celsius \n 2 - Fahrenheit \n 3 - Kelvin \n Escolha: "))

if temperatura_original == 1 and temperatura_convetida == 1:
    print(f"A temperatura {temperatura} graus Celsius equivale a {temperatura} graus Celsius.")

elif temperatura_original == 1 and temperatura_convetida == 2:
    nova_temperatura = (temperatura * 9/5) + 32
    print(f"A temperatura {temperatura} graus Celsius equivale a {nova_temperatura} graus Fahrenheit.")

elif temperatura_original == 1 and temperatura_convetida == 3:
    nova_temperatura = temperatura + 273.15
    print(f"A temperatura {temperatura} graus Celsius equivale a {nova_temperatura} graus Kelvin.")

elif temperatura_original == 2 and temperatura_convetida == 1:
    nova_temperatura = (temperatura - 32) * 5/9
    print(f"A temperatura {temperatura} graus Fahrenheit equivale a {nova_temperatura} graus Celsius.")

elif temperatura_original == 2 and temperatura_convetida == 2:
    print(f"A temperatura {temperatura} graus Fahrenheit equivale a {temperatura} graus Fahrenheit.")

elif temperatura_original == 2 and temperatura_convetida == 3:
    nova_temperatura = (temperatura - 32) * 5/9 + 273.15
    print(f"A temperatura {temperatura} graus Fahrenheit equivale a {nova_temperatura} graus Kelvin.")

elif temperatura_original == 3 and temperatura_convetida == 1:
    nova_temperatura = temperatura - 273.15
    print(f"A temperatura {temperatura} graus Kelvin equivale a {nova_temperatura} graus Celsius.")

elif temperatura_original == 3 and temperatura_convetida == 2:
    nova_temperatura = (temperatura - 273.15) * 9/5 + 32
    print(f"A temperatura {temperatura} graus Kelvin equivale a {nova_temperatura} graus Fahrenheit.")

elif temperatura_original == 3 and temperatura_convetida == 3:
    print(f"A temperatura {temperatura} graus Kelvin equivale a {temperatura} graus Kelvin.")

else:
    print("Você não escolheu opções válidas!")