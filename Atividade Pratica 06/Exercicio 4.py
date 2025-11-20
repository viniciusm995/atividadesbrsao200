'''4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, 
mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, 
retorne uma mensagem de erro.  '''


import requests

while True:
    moeda = input("Digite o código da moeda (ex: USD, EUR, BTC) ou 'sair' para encerrar: ").upper()

    if moeda == "SAIR":
        break

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        
        if resposta.status_code != 200:
            print("Erro ao consultar API. Tente novamente.")
            continue

        dados = resposta.json()

        chave = moeda + "BRL"

        if chave not in dados:
            print("Moeda não encontrada ou código inválido.")
            continue

        info = dados[chave]

        print("\n COTAÇÃO ATUAL")
        print(f"Moeda: {info['code']} -> {info['codein']}")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Valor máximo do dia: R$ {info['high']}")
        print(f"Valor mínimo do dia: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}\n")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}\n")
