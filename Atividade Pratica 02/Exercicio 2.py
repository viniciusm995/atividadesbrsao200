'''2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.'''

nome_produto = "Camiseta"
preco = 50
desconto = 0.2

valor_desconto = preco * desconto
preco_final = preco - valor_desconto

print(f"Nome do produto: {nome_produto}")
print(f"Preço Original: R${preco:.2f}")
print("Desconto aplicado de 20%")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Preço final: R${preco_final:.2f}")