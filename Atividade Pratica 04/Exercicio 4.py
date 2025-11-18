'''4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.'''


par = 0
impar = 0


while True:
    entrada = input("Digite um número inteiro ou 'fim': \n")

    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print("Esse valor é par.")
            par += 1

        else:
            print("Esse número é ímpar.")
            impar += 1

    except ValueError:
        print("Digite apenas números inteiros ou 'fim'. ")

print("Resultado:")
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")