'''Crie um programa que gera uma senha aleatória com o
módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de
caracteres dessa senha aleatória.'''


import random
import string

while True:
    try:
        
        tamanho = int(input("Digite o tamanho da senha que deseja gerar: \n"))

        if tamanho <= 0:
            print("Digite um tamanho válido.")
            continue

        caracteres = string.ascii_letters + string.digits + string.punctuation

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        print(f"Senha gerada: {senha}")
        break

    except ValueError:
        print("Digite um número válido.")