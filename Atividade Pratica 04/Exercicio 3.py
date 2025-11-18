'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''



while True:

    senha = input("Digite uma senha ou 'sair' para encerrar: \n")

    if senha.lower() == "sair":
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("A senha deve ter 8 caracteres.")
        continue

    numero = any(char.isdigit() for char in senha)

    if not numero:
        print("A senha deve conter pelo menos 1 número.")
        continue

    print("A senha é forte.")
    break

