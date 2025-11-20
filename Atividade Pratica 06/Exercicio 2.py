'''Crie um programa que  acesse a API Random User Generator para buscar um usuário fictício aleatório. 
exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha."'''



import requests


try:
    link = "https://randomuser.me/ap/"

    resposta = requests.get(link)
    dados = resposta.json()

    usuario = dados['results'][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("Dados do Usuário")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")

except Exception as erro:
    print(f"Erro ao acessar a API: {erro}")