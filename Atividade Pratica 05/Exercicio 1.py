'''Enunciado: Crie uma função que calcule a gorjeta a ser deixada em um
restaurante, baseada no valor total da conta e na porcentagem de gorjeta
desejada.

Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros:

valor_conta (float): O valor total da conta

porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna:

float: O valor da gorjeta calculada'''


def valor_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

try:
    conta = float(input("Digite o valor da conta: \n"))
    porcentagem = float(input("Digite o percentual da gorjeta: \n"))

    if conta < 0 or porcentagem < 0:
        print("Os valores não podem ser negativos")
    
    else:
        valor = valor_gorjeta(conta, porcentagem)
        print(f"O valor da gorjeta é: R${valor:.2f}")

except ValueError:
    print("Digite apenas números.")
    exit()

