'''3 - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado,
 caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.'''


import requests

while True:

    cep = input("Digite o CEP que deseja procurar: \n")

    link = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resultado = requests.get(link)
        dados = resultado.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            continue

        logradouro = dados.get("logradouro")
        bairro = dados.get("bairro")
        cidade = dados.get("localidade")
        estado = dados.get("uf")

        print("\n Informações do CEP:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}\n")

    except ValueError:
        print("Digite um CEP válido.")



    '''except Exception as erro:
        print(f"Erro: {erro}\n")'''

    



