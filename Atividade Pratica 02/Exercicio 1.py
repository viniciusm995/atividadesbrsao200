'''1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''


valor_reais = 100
taxa_dolar = 5.20
taxa_euro = 6.15

dolar_convertido = valor_reais / taxa_dolar
euro_convertido = valor_reais / taxa_euro

print(f"Valor em reais: R${valor_reais:.2f}")
print(f"Cotação Dolar: R${taxa_dolar:.2f}")
print(f"Cotação Euro: R${taxa_euro:.2f}")
print("Valores após taxa de cambio:")
print(f"Dólar: {dolar_convertido:.2f}")
print(f"Euro: {euro_convertido:.2f}")