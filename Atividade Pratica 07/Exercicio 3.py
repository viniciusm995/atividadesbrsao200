'''3 - 

Crie um programa que leia um arquivo CSV informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.

'''

import csv

def ler_arquivo_csv(arquivo_csv):
    try:
        with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            leitor = csv.reader(file)
            
            for linha in leitor:
                print(linha)
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

arquivo = input("Digite o nome do arquivo CSV (ex: dados.csv): ")
ler_arquivo_csv(arquivo)
