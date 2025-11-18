'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''



def preco_final(valor, desconto):
    valor_desconto = valor * (desconto / 100)
    valor_final = valor - valor_desconto
    return valor_desconto, valor_final


try:
    valor = float(input("Digite o valor do produto: \n"))
    desconto = float(input("Digite o percentual de desconto: \n"))

    valor_desconto, valor_final = preco_final(valor, desconto)

    print(f"O preço inicial do produto é: R${valor:.2f}")
    print(f"O valor do desconto é: R${valor_desconto:.2f}")
    print(f"O preço final do produto é: R${valor_final:.2f}")

except ValueError:
    print("Digite apenas valores válidos.")